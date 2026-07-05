Excellent. Given your background, I'll treat this as an enterprise campus design scaled for residential use rather than a consumer network.

A 5,000 sq ft (465 sq m) main house plus an 800 sq ft pool house, 12–15 users, staff, dual ISPs, and an all-Fortinet stack is a very reasonable deployment.

## First Design Goals

Before selecting hardware, I'd like to establish the design philosophy.

### 1. Availability

How far do you want to go?

**Option A - Simple**

* Single FortiGate
* Single FortiSwitch stack
* Several FortiAPs

**Option B - Business-Class**

* HA FortiGate (A/P)
* Redundant FortiSwitch uplinks
* UPS everywhere
* Dual ISP SD-WAN

**Option C - "Money is secondary"**

* HA FortiGate
* Dual FortiSwitch core/distribution
* LACP everywhere
* Fiber backbone
* UPS + generator integration
* Management VLAN
* Out-of-band management

Personally I'd build Option B. It gives nearly enterprise reliability without becoming ridiculous.

---

# 2. ISP Details

You mentioned

* Converge
* PLDT

Questions:

Are both

* Static IP?
* PPPoE?
* DHCP?
* CGNAT?

Upload/download?

Example

```
PLDT
400/400

Converge
400/400
```

---

# 3. Existing Cabling

Very important.

Do you have

* CAT6
* CAT6A
* Fiber
* Combination

How many cable runs approximately? Or very minimal cabling?

Example

```
Living Room x6

Office x8

Bedrooms x2 each

TV x2

Ceiling APs x5

Outdoor cameras x8

Pool House x4
```

---

# 4. Central Rack

Where will everything terminate?

I'm hoping something like

```
Fiber ONTs

Patch panels

24U rack

UPS

Modem / Router

NVR / Server

Home Assistant
```

---

# 5. WiFi

Do you want

Enterprise roaming

or

Maximum throughput?

They aren't always identical.

I'd tune toward

* 802.11k
* 802.11v
* 802.11r
* Client steering
* Band steering
* Manual channel planning

rather than simply blasting maximum power.

---

# 6. Cameras

How many?

Examples

* Hikvision
* Uniview
* Dahua
* Ubiquiti
* ONVIF

Separate PoE VLAN?

---

# 7. Smart Home

Approximately how many IoT devices?

Examples

* Shelly
* Tuya
* Matter
* Zigbee
* Hue
* Home Assistant
* Alexa
* Google
* Apple HomeKit

Could easily exceed 150 devices.

---

# 8. Servers

Anything local?

Examples

* NAS Appliances / Synology
* AI server
* Plex / Jellyfin
* Home Assistant

---

# 9. Security Philosophy

Would you like segmentation similar to an enterprise?

For example:

```
Users

Staff

Guests

IoT

Pool House

Printers / Media / Servers

Management / Infrastructure

Voice

Work Devices

Security System / Cameras
```

This is how I'd build it.

---

# 10. VPN

Remote access?

SSL VPN?

IPsec?

Site-to-site?

---

# 11. WiFi SSIDs

I generally avoid having too many.

Example

```
Home

Guest

IoT

Staff

```

Everything else can be assigned via dynamic VLANs or wired ports.

---

# 12. PoE Budget

Do you expect:

* PTZ cameras?
* Outdoor APs?
* Intercoms?
* Door access?
* VoIP phones?

These determine whether we need 370 W, 740 W, or higher PoE capacity.

---

# 13. Future Expansion

Any plans for:

* EV chargers
* Solar
* Battery storage
* Smart gate
* Elevator
* CCTV expansion
* Additional guest house

---

# 14. Internet Policy

Would you like to leverage SD-WAN features on the FortiGate?

For example:

* Active/active load balancing across PLDT and Converge
* SLA-based path selection (latency, jitter, packet loss)
* Automatic failover within seconds
* Policy-based steering (e.g., video conferencing always prefers the lower-latency ISP, while downloads can use either link)

---

# 15. Management Philosophy

Since you're already experienced with Fortinet, I'd recommend treating the home like a small enterprise:

* Infrastructure management VLAN
* Dedicated management IPs for all switches and APs
* LLDP enabled
* SNMPv3 and Syslog to a monitoring platform
* Automated configuration backups
* Role-based admin accounts instead of a shared admin login
* Consistent interface descriptions and naming conventions

---

## My Initial Hardware Recommendation

Without sizing every detail yet, my starting point would be:

| Layer            | Recommendation                                                       | Why                                                                                           |
| ---------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Security Gateway | [FortiGate 50G](https://www.amazon.com/Fortinet-FortiGate-50G-Firewall-Offices-Ethernet/dp/B0F3K3YTJ5?th=1) (or HA pair of 50Gs)                                   | Strong performance for dual-gigabit Internet, full UTM features, SD-WAN, and room for growth. |
| Core Switching   | FortiSwitch 248E-FPOE or 248F-FPOE                                   | 48 PoE ports provide ample capacity for APs, cameras, and wired devices.                      |
| Edge Switching   | Optional FortiSwitch 124F-PoE in the pool house                      | Reduces long copper runs and provides local PoE.                                              |
| Wireless         | 4–6 FortiAPs (indoor) plus 1 outdoor-rated FortiAP for the pool area | Supports seamless roaming and good coverage across both buildings.                            |
| Power            | Two UPS units (network rack and pool house)                          | Maintains connectivity during short outages and protects equipment.                           |

---

My goal is to design this as a **reference-grade residential Fortinet deployment**, not merely "gear that works." We'll focus on a scalable, maintainable architecture with clean VLAN segmentation, SD-WAN, Wi-Fi RF planning, security policies, monitoring, and automation—essentially what you'd expect in a small enterprise, adapted to a high-end home environment.

Once you answer the questions above, I'll produce:

1. A full physical topology diagram.
2. A logical VLAN and IP addressing plan.
3. FortiLink architecture.
4. Wi-Fi RF placement and channel plan.
5. SD-WAN and firewall policy design.
6. Security hardening checklist.
7. Equipment sizing with justification.
8. Rack layout, patch panel organization, and cable labeling scheme.
9. A phased implementation and migration plan.

---

# Additional details

Here is a breakdown of what that string of specifications means, piece by piece:

### 1. Tri-Band

The router or device broadcasts on three separate wireless frequency bands to reduce network congestion and handle more traffic:

* **2.4 GHz:** Slower speeds but longer range and better wall penetration.
* **5 GHz:** Faster speeds with moderate range.
* **6 GHz:** Extremely fast speeds and virtually no interference, though with shorter range.

### 2. Wi-Fi 7 & IEEE 802.11be

**Wi-Fi 7** is the commercial name for the **802.11be** wireless standard. It is the latest generation of Wi-Fi technology, designed for ultra-low latency and massive throughput using features like 320 MHz channel widths and Multi-Link Operation (MLO), which lets devices connect to multiple bands simultaneously.

### 3. IEEE 802.11a/b/g/n/ac/ax/be

This lists backwards compatibility. The device supports every major Wi-Fi generation that came before it:

* **b/a/g:** Wi-Fi 1, 2, and 3 (Legacy protocols).
* **n:** Wi-Fi 4 (Introduced 2.4/5 GHz dual-band).
* **ac:** Wi-Fi 5 (High-speed 5 GHz).
* **ax:** Wi-Fi 6 / 6E (Introduced the 6 GHz band and better efficiency).
* **be:** Wi-Fi 7 (The current standard).

### 4. Letters /e/h/i/j/k/r/v

These lowercase letters represent specific amendment protocols that handle background network management, security, and roaming:

* **e:** Quality of Service (QoS) management to prioritize traffic like gaming or video calls.
* **h:** Spectrum and power management to prevent interference with radar systems.
* **i:** Enhanced security protocols (the foundation for WPA2/WPA3).
* **j:** Japanese wireless frequency adaptations.
* **k:** Radio resource measurement, helping devices find the best available access point.
* **r:** Fast Roaming (FT), allowing seamless transition from one access point to another without dropping connection.
* **v:** Network management, allowing the router to guide devices to the most optimal band or access point.

### 5. 9.32 Gbit/s

This is the **maximum theoretical bandwidth** across all combined bands, representing a top speed of 9.32 Gigabits per second. Real-world speeds will be lower due to distance, physical obstacles, and overhead, but it indicates massive capacity for data-heavy tasks like local network transfers and high-speed internet connections.

---

# Wifi Recommendation

If your goal is to reduce the AP count from six to four, I think this is the sweet spot:

3 × FortiAP 431G
1 × FortiAP U231G

This could work well if the main house has a relatively open floor plan and no large RF barriers.

However, if the home has thick concrete walls, multiple wings, or two concrete floors, I'd instead choose:

4 × FortiAP 431G
1 × FortiAP U231G

That gives you excellent coverage while still reducing the number of indoor APs compared with the 231G design.