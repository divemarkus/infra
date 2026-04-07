
# 🧠 Firewall Internals — Kernel, Dataplane & Packet Processing Architecture

> *“You don’t really understand a firewall until you understand how a packet moves through it.”*

---

## 1. 🎯 Scope

This comparison focuses ONLY on:

1. **System foundation**

   * OS / kernel
   * Architecture design philosophy

2. **Dataplane / packet flow**

   * How packets are processed
   * Flow vs packet-based engines

---

## 2. 🧱 System Foundations (Kernel & OS)

---

### 🧬 Core Architecture Comparison

| Platform    | Base OS / Kernel       | Architecture Type                  | Design Philosophy       |
| ----------- | ---------------------- | ---------------------------------- | ----------------------- |
| Cisco ASA   | Custom OS (LINA)       | Monolithic                         | Firewall-first (legacy) |
| Cisco FTD   | Linux + Snort          | Hybrid                             | Bolt-on NGFW            |
| Fortinet    | FortiOS (custom)       | Custom OS + ASIC                   | Hardware-accelerated    |
| Juniper SRX | JUNOS (FreeBSD-based)  | Modular                            | Routing-first           |
| Palo Alto   | Custom Linux-based     | Modular (control/data plane split) | App-aware NGFW          |
| MikroTik    | RouterOS (Linux-based) | Monolithic                         | Network-first           |
| pfSense     | FreeBSD + pf           | Modular                            | Open-source firewall    |
| Sophos      | Linux-based (SFOS)     | Unified                            | UTM-style               |
| OpenWrt     | Linux                  | Modular                            | Embedded networking     |
| OPNsense    | Hardened FreeBSD       | Modular                            | Security-focused OSS    |

---

### 🧠 Key Observations

* **FreeBSD lineage (pfSense, Juniper, OPNsense):**

  * Strong networking stack
  * Predictable behavior

* **Linux-based systems (Palo Alto, Sophos, OpenWrt):**

  * Flexible, extensible
  * Easier integration with modern systems

* **Custom OS (Fortinet, Cisco ASA):**

  * Optimized for performance
  * Less transparent

---

## 3. ⚙️ Dataplane & Packet Processing Models

---

### 🔬 Processing Engine Comparison

| Platform    | Processing Model     | Flow vs Packet | Acceleration     |
| ----------- | -------------------- | -------------- | ---------------- |
| Cisco ASA   | Flow-based           | Flow           | Limited          |
| Cisco FTD   | Snort + flow         | Hybrid         | Limited          |
| Fortinet    | Flow-based + ASIC    | Flow           | ✅ ASIC (NP/SPU)  |
| Juniper SRX | Flow-based           | Flow           | ✅ SPC/NPC        |
| Palo Alto   | Single-pass parallel | Flow           | ⚠️ Partial       |
| MikroTik    | FastPath / FastTrack | Hybrid         | ⚠️ CPU optimized |
| pfSense     | pf (stateful filter) | Flow           | ❌                |
| Sophos      | DPI engine           | Flow           | ⚠️               |
| OpenWrt     | netfilter/nftables   | Packet/Flow    | ❌                |
| OPNsense    | pf + netmap          | Flow           | ❌                |

---

## 4. 🔄 Packet Flow Architecture (How Traffic Moves)

---

### 🥇 Palo Alto — Single-Pass Architecture

```text
Packet → App-ID → Policy → Threat Inspection → Forward
```

* One-pass processing
* No repeated lookups
* Efficient for deep inspection

---

### 🥇 Juniper SRX — Flow Engine

```text
Packet → Session Lookup → Policy → NAT → Forward
```

* Session created on first packet
* Subsequent packets bypass heavy checks

---

### 🥇 Fortinet — ASIC Offload Model

```text
Packet → CPU (session setup) → ASIC (fast path)
```

* First packet handled by CPU
* Subsequent traffic offloaded to ASIC

---

### 🧪 pfSense / Open Source — pf Engine

```text
Packet → Rule match → State table → Forward
```

* Highly deterministic
* No hardware acceleration

---

### 🧪 MikroTik — FastTrack

```text
Packet → Connection tracking → FastTrack → Bypass firewall
```

* Fast but:

  * Skips inspection
  * Tradeoff between speed vs visibility

---

## 5. 🧠 Control Plane vs Data Plane Separation

| Platform    | Separation Model | Notes                              |
| ----------- | ---------------- | ---------------------------------- |
| Palo Alto   | Strong           | Dedicated planes                   |
| Juniper SRX | Strong           | Routing engine vs forwarding plane |
| Fortinet    | Strong           | CPU vs ASIC                        |
| Cisco       | Mixed            | Depends on platform                |
| MikroTik    | Weak             | Shared resources                   |
| pfSense     | Weak             | Single system                      |
| Sophos      | Moderate         | Unified OS                         |
| OpenWrt     | Weak             | Embedded                           |
| OPNsense    | Weak             | Similar to pfSense                 |

---

## 6. 🏆 Best Architectural Designs

---

### 🥇 Most Elegant Dataplane

| Rank | Platform    | Why                    |
| ---- | ----------- | ---------------------- |
| 🥇   | Palo Alto   | Single-pass efficiency |
| 🥈   | Juniper SRX | Clean flow engine      |
| 🥉   | Fortinet    | ASIC acceleration      |

---

### 🥇 Best Kernel / System Design

| Rank | Platform           | Why                       |
| ---- | ------------------ | ------------------------- |
| 🥇   | Juniper SRX        | FreeBSD + modular JUNOS   |
| 🥈   | pfSense / OPNsense | pf + FreeBSD              |
| 🥉   | Palo Alto          | Modern Linux + separation |

---

### 🥇 Best Performance Architecture

| Rank | Platform  | Why                  |
| ---- | --------- | -------------------- |
| 🥇   | Fortinet  | ASIC dominance       |
| 🥈   | Juniper   | Hardware forwarding  |
| 🥉   | Palo Alto | Optimized inspection |

---

## 7. ⚠️ Architectural Tradeoffs

| Design Choice          | Tradeoff                         |
| ---------------------- | -------------------------------- |
| ASIC acceleration      | Less flexibility                 |
| Single-pass inspection | Complex implementation           |
| Flow-based engines     | Less granular per-packet control |
| CPU-based systems      | Performance limits               |

---

## 8. 🧭 Key Insights

---

### 🧠 Two Major Design Philosophies

| Philosophy     | Platforms           |
| -------------- | ------------------- |
| Network-first  | Juniper, MikroTik   |
| Security-first | Palo Alto, Fortinet |

---

### ⚡ Performance vs Visibility

| Platform    | Tradeoff                  |
| ----------- | ------------------------- |
| Fortinet    | Speed via ASIC            |
| Palo Alto   | Visibility via inspection |
| Juniper     | Balance                   |
| Open-source | Control over speed        |

---

## 🧭 Final Takeaways

* **Best engineered system overall:**
  → Juniper SRX (clean separation, proven OS)

* **Best inspection pipeline:**
  → Palo Alto (single-pass architecture)

* **Best raw throughput design:**
  → Fortinet (ASIC acceleration)

---

## 📌 Closing Thought

> *Every firewall processes packets — but how it does it determines everything from performance to security to predictability.*

---

