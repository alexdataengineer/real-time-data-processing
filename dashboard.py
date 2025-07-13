import streamlit as st
import pandas as pd
import json
from azure.eventhub import EventHubConsumerClient
import threading
from streamlit_autorefresh import st_autorefresh
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Event Hub settings
CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STRING")
EVENTHUB_NAME = os.getenv("EVENT_HUB_NAME")
CONSUMER_GROUP = os.getenv("CONSUMER_GROUP", "$Default")  # Using the default consumer group

# Global buffer for received data
data_buffer = []

# Save each event to a file for debug
BUFFER_FILE = "event_buffer.jsonl"

def on_event(partition_context, event):
    try:
        data = json.loads(event.body_as_str())
        data_buffer.append(data)
        # Save to file for debug
        with open(BUFFER_FILE, "a") as f:
            f.write(json.dumps(data) + "\n")
        # Limit buffer size
        if len(data_buffer) > 1000:
            del data_buffer[:len(data_buffer)-1000]
    except Exception as e:
        print("[ERROR] Failed to process message:", e)
    partition_context.update_checkpoint(event)

def start_eventhub_consumer():
    try:
        print("[DEBUG] Connecting to Event Hub...")
        client = EventHubConsumerClient.from_connection_string(
            CONNECTION_STR,
            consumer_group=CONSUMER_GROUP,
            eventhub_name=EVENTHUB_NAME,
        )
        with client:
            print("[DEBUG] Connection established. Waiting for events...")
            client.receive(
                on_event=on_event,
                starting_position="@latest",  # Only new events
            )
    except Exception as e:
        print("[ERROR] Failed to connect to Event Hub:", e)

# Start the consumer in a separate thread (only once)
if 'consumer_started' not in st.session_state:
    threading.Thread(target=start_eventhub_consumer, daemon=True).start()
    st.session_state['consumer_started'] = True

st.set_page_config(page_title="Citi Bike NYC - Real-Time Dashboard", layout="wide")
st.title("🚴 Citi Bike NYC - Real-Time Dashboard")

# Add autorefresh every 5 seconds
st_autorefresh(interval=5000, key="datarefresh")

# DEBUG: Show buffer size
st.write(f"[DEBUG] Buffer size in memory: {len(data_buffer)}")

# Try to read from memory buffer
if data_buffer:
    st.write("[DEBUG] Reading from memory buffer!")
    df = pd.DataFrame(data_buffer)
    st.write(f"Total records received: {len(df)}")
    st.dataframe(df.tail(20))
    # Example: Top stations with most bikes available
    if 'num_bikes_available' in df.columns and 'name' in df.columns:
        top = df.groupby('name')['num_bikes_available'].max().sort_values(ascending=False).head(10)
        st.subheader("Top 10 stations with most bikes available")
        st.bar_chart(top)
    lat_col = None
    lon_col = None
    for c in df.columns:
        if c in ['lat', 'latitude']:
            lat_col = c
        if c in ['lon', 'longitude']:
            lon_col = c
    if lat_col and lon_col:
        st.subheader("Map of stations (latest data)")
        st.map(df[[lat_col, lon_col]].dropna().tail(100))
else:
    # Try to read from file as fallback
    if os.path.exists(BUFFER_FILE):
        try:
            st.write("[DEBUG] Reading from event_buffer.jsonl file!")
            df = pd.read_json(BUFFER_FILE, lines=True)
            st.write(f"Total records received (file): {len(df)}")
            st.dataframe(df.tail(20))
            # Repeat visualizations for file DataFrame
            if 'num_bikes_available' in df.columns and 'name' in df.columns:
                top = df.groupby('name')['num_bikes_available'].max().sort_values(ascending=False).head(10)
                st.subheader("Top 10 stations with most bikes available")
                st.bar_chart(top)
            lat_col = None
            lon_col = None
            for c in df.columns:
                if c in ['lat', 'latitude']:
                    lat_col = c
                if c in ['lon', 'longitude']:
                    lon_col = c
            if lat_col and lon_col:
                st.subheader("Map of stations (latest data)")
                st.map(df[[lat_col, lon_col]].dropna().tail(100))
        except Exception as e:
            st.write(f"[ERROR] Failed to read file: {e}")
    else:
        st.write("Waiting for data from Event Hub...") 