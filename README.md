# Citi Bike NYC Real-Time Data Pipeline & Dashboard


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
- 
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/75baacf3-4ccf-461a-b5d5-c8efa60d85c2" />

### **Data Flow:**

```
Citi Bike NYC API → Python Script → Azure Event Hub → Streamlit Dashboard
     ↓                    ↓              ↓                    ↓
Station Data      →   JSON Events  →  Partitions    →  Real-time Viz
     ↓                    ↓              ↓                    ↓
30s intervals     →   Batch Send   →  Consumer Groups →  Auto-refresh
```
Metric	Current Value
Incoming Requests	57.35k
Successful Requests	49.17k
Incoming Messages	13.42k
Outgoing Messages	43.03k
Incoming Bytes	12.16 MB
Outgoing Bytes	40.96 MB
Server Errors / Throttling	0

### **Technical Specifications:**

- **Latency:** < 1 second for visualization
- **Throughput:** Supports thousands of events per second
- **Scalability:** Event Hub partitions for horizontal scaling
- **Reliability:** Retry logic and comprehensive error handling
- **Security:** Environment variables for credential management
- **Data Format:** JSON with station metadata and status

---
<img width="2048" height="873" alt="image" src="https://github.com/user-attachments/assets/f5460afd-9f06-44c7-b7f4-f805f5f37c85" />


## 1. Overview

This project implements a real-time data ingestion and visualization pipeline for Citi Bike NYC station data. It continuously ingests live station information and status, streams the data through Azure Event Hub, and visualizes it in real time using a custom Streamlit dashboard. The solution enables instant monitoring and analysis of bike station availability and operational KPIs.

- **Ingestion:** Collects Citi Bike NYC station data in real time.
- **Streaming:** Uses Azure Event Hub to distribute messages efficiently.
- **Visualization:** Displays live data and analytics via a Streamlit dashboard.

---
<img width="1984" height="1348" alt="image" src="https://github.com/user-attachments/assets/af1506d8-550c-4a97-a69f-a9fa46632f66" />

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
<img width="2048" height="938" alt="image" src="https://github.com/user-attachments/assets/c82690e7-4786-46ee-918c-0b108cbc4693" />
<img width="2048" height="678" alt="image" src="https://github.com/user-attachments/assets/e44c00f4-bfd2-45f8-a485-90c587682774" />
<img width="2048" height="881" alt="image" src="https://github.com/user-attachments/assets/2f49618a-a589-444c-88b5-2bbc44c04d25" />

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
