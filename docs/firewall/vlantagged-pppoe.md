
# 🧵 VLAN-Tagged PPPoE Support — Firewall Compatibility Matrix 

> *“CenturyLink Fiber (legacy / Lumen) commonly requires PPPoE over VLAN (typically VLAN 201). Not all firewalls were designed for this edge use case.”*

---

## 🧠 Background

Typical CenturyLink Fiber requirements:

* **PPPoE authentication**
* **802.1Q VLAN tagging (commonly VLAN 201)**
* WAN interface must support:

  * VLAN subinterface (tagged)
  * PPPoE client bound to that VLAN

---

## ✅ Fully Supported (Native + Reliable)

| Firewall                   | Support Level | Notes                                                                 |
| -------------------------- | ------------- | --------------------------------------------------------------------- |
| **pfSense**                | ✅ Full        | VLAN → PPPoE binding is straightforward                               |
| **OPNsense**               | ✅ Full        | Same architecture as pfSense                                          |
| **VyOS**                   | ✅ Full        | Native CLI support                                                    |
| **Fortinet (FortiGate)**   | ✅ Full        | VLAN subinterface + PPPoE                                             |
| **RouterOS (MikroTik)**    | ✅ Full        | Very common deployment                                                |
| **OpenWrt**                | ✅ Full        | Popular for CenturyLink bypass                                        |
| **Juniper Networks (SRX)** | ✅ Full        | Fully supported via logical interfaces (e.g., `ge-0/0/0.201` + PPPoE) |

---

## ⚠️ Supported but Less Common / Clunky

| Firewall                  | Support Level | Notes                                                       |
| ------------------------- | ------------- | ----------------------------------------------------------- |
| **Cisco ASA**             | ⚠️ Partial    | PPPoE + VLAN possible, not elegant                          |
| **Cisco Firepower (FTD)** | ⚠️ Limited    | Rare use case, not well integrated                          |
| **Sophos Firewall**       | ⚠️ Partial    | PPPoE works; VLAN binding inconsistent depending on version |
| **DD-WRT**                | ⚠️ Partial    | Firmware/device dependent                                   |
| **FreshTomato**           | ⚠️ Limited    | Hardware-dependent, not always reliable                     |

---

## ❌ Historically Problematic → Now Supported

| Firewall                        | Status | Notes                     |
| ------------------------------- | ------ | ------------------------- |
| **Palo Alto Networks (PAN-OS)** | ❌ → ✅  | See version details below |

---

## 🔥 Palo Alto Networks — VLAN PPPoE Support (Version Detail)

### 📌 Historical State

* PAN-OS **≤ 9.x**

  * ❌ No support for PPPoE on VLAN-tagged subinterfaces
  * Required external modem/router workaround

---

### ⚠️ Transitional

| Version          | Status                    |
| ---------------- | ------------------------- |
| PAN-OS 10.0–10.1 | ⚠️ Partial / inconsistent |

---

### ✅ Modern Support

| Version          | Status      |
| ---------------- | ----------- |
| **PAN-OS 10.2+** | ✅ Supported |

---

### ⚙️ Implementation Notes

* PPPoE can now be bound to:

  * Layer 3 interfaces
  * VLAN-tagged subinterfaces
* Still:

  * Not a common enterprise design
  * Less intuitive than routing-first platforms

---

## 🧪 Real-World Reliability Ranking (ISP Use Case)

> *Based on practical deployments (not just feature availability)*

| Rank | Platform            | Why                                      |
| ---- | ------------------- | ---------------------------------------- |
| 🥇   | MikroTik (RouterOS) | Extremely reliable, ISP-grade behavior   |
| 🥈   | pfSense / OPNsense  | Clean and simple                         |
| 🥉   | Juniper SRX         | Very solid, but requires JUNOS knowledge |
| 4    | OpenWrt             | Lightweight, widely used                 |
| 5    | FortiGate           | Works well, enterprise-grade             |
| 6    | VyOS                | Powerful but CLI-heavy                   |
| 7    | Palo Alto (10.2+)   | Functional, not ideal                    |
| 8    | Cisco / Sophos      | Not designed for this edge case          |

---

## 🧭 Key Takeaways

* VLAN-tagged PPPoE is best supported by:

  * **Routing-first platforms (Juniper, MikroTik, VyOS)**
  * **Open-source firewalls (pfSense, OpenWrt)**

---

### 🧠 Architectural Insight

| Platform Type                   | Behavior                    |
| ------------------------------- | --------------------------- |
| Routing-centric (SRX, MikroTik) | ✅ Native + clean            |
| Open-source (pfSense, OpenWrt)  | ✅ Flexible + easy           |
| NGFW (PAN, Cisco, Sophos)       | ⚠️ Often secondary use case |

---

## 📌 Closing Thought

> *If a firewall handles VLAN-tagged PPPoE cleanly, it usually means it was built with real routing use cases in mind — not just policy enforcement.*

---
