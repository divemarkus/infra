
---

# 🧠 Option 1: Fleet + Elastic Stack

This is the **most realistic SOC-style setup**.

**Components**

* **osquery** → endpoint data
* **FleetDM** → central management
* **Elasticsearch** → data storage
* **Kibana** → dashboards
* **Filebeat** → log pipeline

### Architecture

```
    Server
      │
      │ osquery
      ▼
   FleetDM
      │
      ▼
   Filebeat
      │
      ▼
 Elasticsearch
      │
      ▼
    Kibana
```

### Why this is great

You get:

* centralized **query management**
* **live queries**
* endpoint **security dashboards**
* **alerting**

---

## Example docker homelab stack

```yaml
version: "3"

services:

  fleet:
    image: fleetdm/fleet
    ports:
      - "8080:8080"

  elasticsearch:
    image: elasticsearch:8.12.0
    environment:
      - discovery.type=single-node
    ports:
      - "9200:9200"

  kibana:
    image: kibana:8.12.0
    ports:
      - "5601:5601"
```

Then install **osquery on endpoints**:

```
winget install osquery.osquery
```

Point it to Fleet.

---

# 🧠 Option 2: Wazuh

The easiest **SIEM + osquery** setup.

Use:

* **Wazuh**
* **osquery**

Wazuh **already supports osquery integration**.

### Architecture

```
Endpoint
   │
   │ osquery
   ▼
Wazuh Agent
   │
   ▼
Wazuh Manager
   │
   ▼
Wazuh Dashboard
```

### Advantages

* built-in alerts
* vulnerability detection
* MITRE ATT&CK mapping
* dashboards ready immediately

---

### Quick docker install

```bash
docker run -d \
--name wazuh \
-p 5601:5601 \
-p 1514:1514 \
-p 1515:1515 \
wazuh/wazuh
```

Then enable **osquery module** in the agent.

---

# 🧠 Option 3 (Lightweight): osquery → Loki → Grafana

This is the **lightest stack**.

Components:

* **osquery**
* **Grafana Loki**
* **Grafana**

### Architecture

```
osquery
   │
   ▼
Promtail
   │
   ▼
Loki
   │
   ▼
Grafana
```

Great for:

* dashboards
* timeline analysis
* lightweight setups

---

# 🔎 Example osquery log pipeline

Configure **osquery.conf**

```json
{
  "options": {
    "logger_plugin": "filesystem",
    "logger_path": "C:\\Program Files\\osquery\\log",
    "schedule_splay_percent": 10
  }
}
```

Logs will appear:

```
C:\Program Files\osquery\log\
```

Ship them to your SIEM.

Example **Filebeat config**

```yaml
filebeat.inputs:
- type: log
  paths:
    - "C:/Program Files/osquery/log/osqueryd.results.log"

output.elasticsearch:
  hosts: ["http://192.168.1.50:9200"]
```

---

# 🧠 Example Detection in SIEM

Query example in **Kibana**:

Detect suspicious PowerShell:

```
process_name: powershell.exe AND
cmdline: *EncodedCommand*
```

Detect network listeners:

```
event.module: osquery AND
listening_ports.port: *
```

---

# 🏠 Architecture Design Ideas

If you want something that **looks like a real SOC environment**:

```
Endpoints
   │
   ▼
osquery
   │
   ▼
FleetDM
   │
   ▼
Elastic Stack
   │
   ▼
Kibana Dashboards
```

This teaches:

* endpoint telemetry
* detection engineering
* SIEM operations
* threat hunting

---

# 🔥 Homelab Ideas

- Using Prometheus as its lighter
- Prometheus node-exporter
- Grafana
- Stay tuned

---


