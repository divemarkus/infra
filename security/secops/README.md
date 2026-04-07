Below is a **production-ready `docker-compose.yml`** tailored to your setup:

* ✅ Full Wazuh SIEM stack
* ✅ Prometheus + Grafana
* ✅ Redis buffer (lightweight, stable)
* ✅ AI integration service (hooks into your existing Ollama/OpenWebUI)
* ✅ Ready for Kali ingestion workflows

No Ollama/OpenWebUI containers included (assumed external).

---

# 🧱 Directory Structure (IMPORTANT)

Before deploying:

```bash
mkdir -p secops-stack/{wazuh,config,prometheus,grafana,ai}
cd secops-stack
```

---

# 🚀 [docker-compose.yml](docker-compose.yml)


---

# ⚙️ Prometheus Config

`./config/prometheus.yml`
[prometheus.yml](./config/prometheus.yml)

---

# 🧠 AI Analyzer (Minimal Working API)

`./ai/main.py`
[main.py](./ai/main.py)

---

# 🛰️ Log Agents (Host + Kali)

## On Ubuntu host:

Install Wazuh agent

```bash
curl -sO https://packages.wazuh.com/4.x/wazuh-agent.sh
sudo bash wazuh-agent.sh -a 192.168.18.X
```

---

## On Kali (Ingestion Workflows)

### Option 1 — Native Agent (BEST)

Install Wazuh agent same way.

### Option 2 — Push Scan Results

```bash
nmap -oX scan.xml 192.168.18.0/24
```

Send to pipeline:

```bash
curl -X POST http://<ubuntu-ip>:8000/analyze \
  -H "Content-Type: application/json" \
  -d @scan.xml
```

---

# 🔁 Data Flow (Final)

```
Kali Scan → Wazuh Agent → Wazuh Manager
         → Indexer → Dashboard

Alerts → Redis → AI Analyzer → Ollama
       → Enriched Alerts → Grafana
```

---

# 🚀 Bring It Up

```bash
[+] up 16/16
 ✔ Network secops-stack_monitoring_net Created                                                                                                  0.0s
 ✔ Network secops-stack_siem_net       Created                                                                                                  0.0s
 ✔ Network secops-stack_ai_net         Created                                                                                                  0.0s
 ✔ Volume secops-stack_opensearch_data Created                                                                                                  0.0s
 ✔ Volume secops-stack_wazuh_data      Created                                                                                                  0.0s
 ✔ Volume secops-stack_grafana_data    Created                                                                                                  0.0s
 ✔ Volume secops-stack_prometheus_data Created                                                                                                  0.0s
 ✔ Container redis                     Started                                                                                                  0.7s
 ✔ Container cadvisor                  Started                                                                                                  0.9s
 ✔ Container wazuh.indexer             Started                                                                                                  0.6s
 ✔ Container wazuh.manager             Started                                                                                                  0.8s
 ✔ Container grafana                   Started                                                                                                  0.9s
 ✔ Container prometheus                Started                                                                                                  0.8s
 ✔ Container node-exporter             Started                                                                                                  0.7s
 ✔ Container wazuh.dashboard           Started                                                                                                  0.7s
 ✔ Container ai-analyzer               Started                                                                                                  0.8s
```

Check:

* Wazuh → [http://localhost:5601](http://localhost:5601)
* Grafana → [http://localhost:3002](http://localhost:3000)
* Prometheus → [http://localhost:9090](http://localhost:9090)

---


| Service         | Port       |
| --------------- | ---------- |
| Wazuh Dashboard | 5601       |
| Prometheus      | 9090       |
| Grafana         | ✅ **3002** |
| cadvisor        | ✅ **8081** |
| OpenWebUI       | 8080       |
| Flowise         | 3000–3001  |
| AI Analyzer     | 8000       |

