Excellent. Given your background, I'll treat this as an enterprise campus design scaled for residential use rather than a consumer network.

A 4,000 sq ft main house plus an 800 sq ft pool house, 12–15 users, staff, dual ISPs, and an all-Fortinet stack is a very reasonable deployment.

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
1000/1000

Converge
600/600
```

---

# 3. Existing Cabling

Very important.

Do you have

* CAT6
* CAT6A
* Fiber
* Combination

How many cable runs approximately?

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

Kids

Parents

IoT

Cameras

Pool House

Printers

Media

Servers

Management

Infrastructure

VPN

Voice

Gaming

Work Devices

Security System
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
| Security Gateway | FortiGate 90G (or HA pair of 90Gs)                                   | Strong performance for dual-gigabit Internet, full UTM features, SD-WAN, and room for growth. |
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
