# Citi Bike NYC Real-Time Data Pipeline & Dashboard

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp env.example .env
   ```
   Then edit `.env` with your Azure Event Hub credentials:
   ```
   EVENT_HUB_CONNECTION_STRING=your_connection_string_here
   EVENT_HUB_NAME=your_event_hub_name
   CONSUMER_GROUP=your_consumer_group
   ```

3. **Run the ingestion script:**
   ```bash
   python citibike_ingest/ingest_citibike_to_eventhub.py
   ```

4. **Start the dashboard:**
   ```bash
   streamlit run dashboard.py
   ```

## Architecture

```mermaid
graph TD
    A[Citi Bike NYC API] --> B[Python Ingestion Script]
    B --> C[Azure Event Hub]
    C --> D[Streamlit Dashboard]
    C --> E[Other Consumers (optional)]
    C --> F[Azure Monitoring & Metrics]
    
    subgraph "Data Sources"
        A1[Station Information API]
        A2[Station Status API]
    end
    
    subgraph "Data Processing"
        B1[Data Fetching]
        B2[JSON Processing]
        B3[Event Batching]
    end
    
    subgraph "Streaming Platform"
        C1[Event Hub Partitions]
        C2[Consumer Groups]
        C3[Message Routing]
    end
    
    subgraph "Visualization"
        D1[Real-time Charts]
        D2[Interactive Maps]
        D3[Auto-refresh Dashboard]
    end
    
    subgraph "Monitoring"
        F1[Throughput Metrics]
        F2[Error Tracking]
        F3[Performance Analytics]
    end
```

### **System Components:**

#### **1. Data Sources**
- **Citi Bike NYC API:** Real-time station data endpoints
- **Station Information API:** Static station metadata (location, capacity)
- **Station Status API:** Dynamic status (available bikes, docks)

#### **2. Data Ingestion Layer**
- **Python Ingestion Script:** Fetches data every 30 seconds
- **JSON Processing:** Transforms API responses into event format
- **Event Batching:** Groups multiple stations into efficient batches
- **Error Handling:** Retry logic for transient failures

#### **3. Streaming Platform (Azure Event Hub)**
- **Event Hub Partitions:** Enables parallel processing and high throughput
- **Consumer Groups:** Allows multiple consumers to read independently
- **Message Routing:** Distributes events across partitions
- **Scalability:** Handles thousands of events per second

#### **4. Visualization Layer**
- **Streamlit Dashboard:** Web-based real-time interface
- **Real-time Charts:** Live updates of station availability
- **Interactive Maps:** Geographic visualization of stations
- **Auto-refresh:** Updates every 5 seconds automatically

#### **5. Monitoring & Analytics**
- **Azure Metrics:** Tracks incoming/outgoing messages and bytes
- **Error Tracking:** Monitors failed requests and server errors
- **Performance Analytics:** Throughput and latency monitoring

### **Data Flow:**

```
Citi Bike NYC API → Python Script → Azure Event Hub → Streamlit Dashboard
     ↓                    ↓              ↓                    ↓
Station Data      →   JSON Events  →  Partitions    →  Real-time Viz
     ↓                    ↓              ↓                    ↓
30s intervals     →   Batch Send   →  Consumer Groups →  Auto-refresh
```

### **Technical Specifications:**

- **Latency:** < 1 second for visualization
- **Throughput:** Supports thousands of events per second
- **Scalability:** Event Hub partitions for horizontal scaling
- **Reliability:** Retry logic and comprehensive error handling
- **Security:** Environment variables for credential management
- **Data Format:** JSON with station metadata and status

---

## 1. Overview

This project implements a real-time data ingestion and visualization pipeline for Citi Bike NYC station data. It continuously ingests live station information and status, streams the data through Azure Event Hub, and visualizes it in real time using a custom Streamlit dashboard. The solution enables instant monitoring and analysis of bike station availability and operational KPIs.

- **Ingestion:** Collects Citi Bike NYC station data in real time.
- **Streaming:** Uses Azure Event Hub to distribute messages efficiently.
- **Visualization:** Displays live data and analytics via a Streamlit dashboard.

---

## 2. Developer Information

- **Author:** Alexsander Silveira
- **Role:** Project creator and main developer

---

## 3. Benefits for the Business

- **Real-time monitoring:** Enables instant visibility into operational KPIs.
- **Faster decision-making:** Supports agile responses to events and anomalies.
- **Reduced downtime:** Early detection of issues helps minimize service interruptions.
- **Improved customer experience:** Ensures better resource allocation and station availability.
- **Enhanced resource allocation:** Data-driven insights for optimal bike and dock distribution.

---

## 4. Return on Investment (ROI)

- **Agile operations:** Real-time visibility allows for immediate action, reducing delays.
- **Lower operational costs:** Early detection and response reduce manual interventions and downtime.
- **Higher user satisfaction:** Customers benefit from more reliable and available services.

---

## 5. Technical Stack

- **Azure Event Hub:** Scalable, partitioned event streaming platform for ingesting and distributing messages.
- **Python:** Used for data ingestion, processing, and dashboard backend.
- **Streamlit:** Interactive, real-time dashboard for data visualization.
- **JSON:** Standard format for message payloads.
- **Event Hub Partitions:** Used to scale throughput and parallelize message processing.
- **Message Structure:** Each message is a JSON object representing a bike station’s status and metadata.

---

## 6. Complexity and Challenges

- **Message Handling:** Ensuring reliable delivery, deduplication, and ordering.
- **Scaling Partitions:** Balancing throughput and consumer parallelism.
- **Fast Data Visualization:** Keeping the dashboard responsive with high-frequency updates.
- **Volume Management:** 
  - Use batch writes to Event Hub when possible.
  - Implement buffering and retry logic for transient failures.
  - Monitor and tune partition count for optimal performance.

---

## 7. When and Why to Use Streaming

- **Use Cases:**
  - Vehicle and asset tracking
  - Delivery and logistics updates
  - IoT sensor data
  - Financial transactions
  - Any scenario where near real-time decision-making is critical

- **Why Streaming?**
  - Use streaming when the freshness of data directly impacts business value, such as in operations, customer experience, or risk management.

---

## 8. Metrics and Monitoring

- **Azure Metrics Used:**
  - **Incoming/Outgoing Messages:** Track message flow and detect bottlenecks.
  - **Incoming/Outgoing Bytes:** Monitor data volume and throughput.
  - **Successful vs Failed Requests:** Ensure reliability and identify issues.
  - **Server Errors & Throttled Requests:** Detect and respond to system health problems.

- **How Metrics Are Used:**
  - To ensure system health, optimize throughput, and proactively address issues before they impact users.

---

## 9. Screenshots (Recommended)

- Add screenshots of:
  - Terminal logs showing event ingestion and processing
  - The Streamlit dashboard with live data
  - Azure Event Hub metrics and charts
  - Any error or alert visualizations

---

> **Developed by Alexsander Silveira**  
> For questions or contributions, please open an issue or pull request on GitHub. 