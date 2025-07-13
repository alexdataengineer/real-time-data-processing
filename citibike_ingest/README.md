# Citi Bike NYC → Azure Event Hub

Este projeto consome dados em tempo real das APIs públicas do Citi Bike NYC e envia para um Azure Event Hub.

## Como funciona
- Busca dados das APIs:
  - https://gbfs.citibikenyc.com/gbfs/en/station_information.json
  - https://gbfs.citibikenyc.com/gbfs/en/station_status.json
- Envia cada estação como mensagem JSON para o Event Hub.

## Como rodar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure a connection string do Event Hub no script.
3. Execute:
   ```bash
   python ingest_citibike_to_eventhub.py
   ```

## Próximos passos
- Configurar Stream Analytics para consumir do Event Hub e gravar no SQL Server.
- Criar tabela no SQL Server para receber os dados. 