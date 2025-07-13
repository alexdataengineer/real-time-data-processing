import os
from dotenv import load_dotenv
from azure.eventhub import EventHubProducerClient, EventData

# Carregar variáveis de ambiente
load_dotenv()

CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STRING")
EVENTHUB_NAME = os.getenv("EVENT_HUB_NAME")

def main():
    producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR, eventhub_name=EVENTHUB_NAME)
    with producer:
        event_data_batch = producer.create_batch()
        event_data_batch.add(EventData('{"station_id": "test", "name": "Teste", "num_bikes_available": 5, "lat": 40.7, "lon": -74.0}'))
        producer.send_batch(event_data_batch)
    print("Evento de teste enviado!")

if __name__ == "__main__":
    main() 