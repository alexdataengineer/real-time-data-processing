import requests
import time
import json
import os
from dotenv import load_dotenv
from azure.eventhub import EventHubProducerClient, EventData

# Carregar variáveis de ambiente
load_dotenv()

# Configurações do Event Hub
CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STRING")
EVENTHUB_NAME = os.getenv("EVENT_HUB_NAME")

# URLs das APIs do Citi Bike
STATION_INFO_URL = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"
STATION_STATUS_URL = os.getenv("CITIBIKE_API_URL", "https://gbfs.citibikenyc.com/gbfs/en/station_status.json")

# Frequência de envio (em segundos)
INTERVAL = 30

def fetch_citibike_data():
    info_resp = requests.get(STATION_INFO_URL)
    status_resp = requests.get(STATION_STATUS_URL)
    info = info_resp.json()["data"]["stations"]
    status = status_resp.json()["data"]["stations"]
    # Indexar status por station_id
    status_map = {s["station_id"]: s for s in status}
    # Unir info + status
    merged = []
    for station in info:
        sid = station["station_id"]
        station_data = {**station, **status_map.get(sid, {})}
        merged.append(station_data)
    return merged

def send_to_eventhub(stations):
    producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR, eventhub_name=EVENTHUB_NAME)
    with producer:
        for station in stations:
            event_json = json.dumps(station)
            event_data = EventData(event_json)
            try:
                producer.send_batch([event_data])
            except Exception as e:
                print(f"Erro ao enviar estação {station.get('station_id')}: {e}")
    print(f"Enviadas {len(stations)} estações para o Event Hub (uma por vez).")

def main():
    while True:
        print("Buscando dados do Citi Bike...")
        stations = fetch_citibike_data()
        print(f"Enviando {len(stations)} estações para o Event Hub...")
        send_to_eventhub(stations)
        print(f"Aguardando {INTERVAL} segundos...")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main() 