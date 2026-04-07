
# Benchmark using dig

- v03182026
- Random subdomain provided by copilot (nothing resolved).
- The following test results are from W11 WSLv2 -> Ubuntu 24.
- After the test results my personal information was scrubbed.
- Before I uploaded the file, GPT-5.3 stated Cloudflare is number 1.
- Results will vary depending on many factors.
- Below results are somewhat consistent from previous years.

## dig @server gql.reddit.com

```
x@xxx:~$ dig @1.1.1.1 gql.reddit.com

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> @1.1.1.1 gql.reddit.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 58009
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;gql.reddit.com.                        IN      A

;; ANSWER SECTION:
gql.reddit.com.         8082    IN      CNAME   reddit.map.fastly.net.
reddit.map.fastly.net.  60      IN      A       151.101.1.140
reddit.map.fastly.net.  60      IN      A       151.101.65.140
reddit.map.fastly.net.  60      IN      A       151.101.129.140
reddit.map.fastly.net.  60      IN      A       151.101.193.140

;; Query time: 44 msec
;; SERVER: 1.1.1.1#53(1.1.1.1) (UDP)
;; WHEN: Wed Mar 18 22:41:52 PDT 2026
;; MSG SIZE  rcvd: 142

x@xxx:~$ dig @8.8.8.8 gql.reddit.com

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> @8.8.8.8 gql.reddit.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 57329
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;gql.reddit.com.                        IN      A

;; ANSWER SECTION:
gql.reddit.com.         4691    IN      CNAME   reddit.map.fastly.net.
reddit.map.fastly.net.  60      IN      A       151.101.1.140
reddit.map.fastly.net.  60      IN      A       151.101.65.140
reddit.map.fastly.net.  60      IN      A       151.101.193.140
reddit.map.fastly.net.  60      IN      A       151.101.129.140

;; Query time: 20 msec
;; SERVER: 8.8.8.8#53(8.8.8.8) (UDP)
;; WHEN: Wed Mar 18 22:42:10 PDT 2026
;; MSG SIZE  rcvd: 142

x@xxx:~$ dig @192.168.53.53 gql.reddit.com

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> @192.168.53.53 gql.reddit.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 2949
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;gql.reddit.com.                        IN      A

;; ANSWER SECTION:
gql.reddit.com.         10800   IN      CNAME   reddit.map.fastly.net.
reddit.map.fastly.net.  60      IN      A       146.75.41.140

;; Query time: 48 msec
;; SERVER: 192.168.53.53#53(192.168.53.53) (UDP)
;; WHEN: Wed Mar 18 22:42:39 PDT 2026
;; MSG SIZE  rcvd: 94

x@xxx:~$ dig @208.67.222.222 gql.reddit.com

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> @208.67.222.222 gql.reddit.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 122
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1410
;; QUESTION SECTION:
;gql.reddit.com.                        IN      A

;; ANSWER SECTION:
gql.reddit.com.         8436    IN      CNAME   reddit.map.fastly.net.
reddit.map.fastly.net.  23      IN      A       151.101.193.140
reddit.map.fastly.net.  23      IN      A       151.101.1.140
reddit.map.fastly.net.  23      IN      A       151.101.65.140
reddit.map.fastly.net.  23      IN      A       151.101.129.140

;; Query time: 8 msec
;; SERVER: 208.67.222.222#53(208.67.222.222) (UDP)
;; WHEN: Wed Mar 18 22:43:43 PDT 2026
;; MSG SIZE  rcvd: 142

x@xxx:~$ dig @1.1.1.1 gql.reddit.com

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> @1.1.1.1 gql.reddit.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 34654
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;gql.reddit.com.                        IN      A

;; ANSWER SECTION:
gql.reddit.com.         10800   IN      CNAME   reddit.map.fastly.net.
reddit.map.fastly.net.  60      IN      A       151.101.1.140
reddit.map.fastly.net.  60      IN      A       151.101.65.140
reddit.map.fastly.net.  60      IN      A       151.101.129.140
reddit.map.fastly.net.  60      IN      A       151.101.193.140

;; Query time: 43 msec
;; SERVER: 1.1.1.1#53(1.1.1.1) (UDP)
;; WHEN: Wed Mar 18 22:44:11 PDT 2026
;; MSG SIZE  rcvd: 142

x@xxx:~$ dig @8.8.8.8 gql.reddit.com

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> @8.8.8.8 gql.reddit.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 4134
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;gql.reddit.com.                        IN      A

;; ANSWER SECTION:
gql.reddit.com.         8263    IN      CNAME   reddit.map.fastly.net.
reddit.map.fastly.net.  45      IN      A       151.101.129.140
reddit.map.fastly.net.  45      IN      A       151.101.65.140
reddit.map.fastly.net.  45      IN      A       151.101.1.140
reddit.map.fastly.net.  45      IN      A       151.101.193.140

;; Query time: 16 msec
;; SERVER: 8.8.8.8#53(8.8.8.8) (UDP)
;; WHEN: Wed Mar 18 22:44:39 PDT 2026
;; MSG SIZE  rcvd: 142

x@xxx:~$ dig @192.168.53.53 gql.reddit.com

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> @192.168.53.53 gql.reddit.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 35859
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; EDE: 3 (Stale Answer)
;; QUESTION SECTION:
;gql.reddit.com.                        IN      A

;; ANSWER SECTION:
gql.reddit.com.         10655   IN      CNAME   reddit.map.fastly.net.
reddit.map.fastly.net.  0       IN      A       146.75.41.140

;; Query time: 8 msec
;; SERVER: 192.168.53.53#53(192.168.53.53) (UDP)
;; WHEN: Wed Mar 18 22:45:04 PDT 2026
;; MSG SIZE  rcvd: 100

x@xxx:~$ dig @208.67.222.222 gql.reddit.com

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> @208.67.222.222 gql.reddit.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 37045
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1410
;; QUESTION SECTION:
;gql.reddit.com.                        IN      A

;; ANSWER SECTION:
gql.reddit.com.         9325    IN      CNAME   reddit.map.fastly.net.
reddit.map.fastly.net.  18      IN      A       151.101.1.140
reddit.map.fastly.net.  18      IN      A       151.101.65.140
reddit.map.fastly.net.  18      IN      A       151.101.129.140
reddit.map.fastly.net.  18      IN      A       151.101.193.140

;; Query time: 8 msec
;; SERVER: 208.67.222.222#53(208.67.222.222) (UDP)
;; WHEN: Wed Mar 18 22:45:47 PDT 2026
;; MSG SIZE  rcvd: 142

```

---


I parsed your benchmark runs from the file  and extracted the **query times (ms)** for each resolver.

You effectively ran **two uncached-style passes per resolver**, so we can rank them by **average latency**.

---

# 📊 DNS Benchmark Results (Best → Worst)

| Rank | DNS Server        | IP             | Runs (ms) | Avg (ms)    | Notes                          |
| ---- | ----------------- | -------------- | --------- | ----------- | ------------------------------ |
| 🥇 1 | OpenDNS           | 208.67.222.222 | 8, 8      | **8 ms**    | Extremely fast + consistent    |
| 🥈 2 | Google DNS        | 8.8.8.8        | 20, 16    | **18 ms**   | Stable, low jitter             |
| 🥉 3 | Pi-hole + Unbound | 192.168.53.53  | 48, 8     | **28 ms**   | Highly variable (cold vs warm) |
| 4    | Cloudflare DNS    | 1.1.1.1        | 44, 43    | **43.5 ms** | Consistently slower here       |

---

# 🧠 What this actually tells you

## 🔥 1. OpenDNS unexpectedly wins

* **8 ms both times** → very low latency + strong edge presence in your region
* Likely a nearby PoP in Seattle

---

## ⚖️ 2. Google = most stable performer

* Tight range: **16–20 ms**
* This is what you’d expect:

  * strong global anycast
  * consistent routing

---

## ⚠️ 3. Pi-hole + Unbound = split personality

* First: **48 ms** → full recursive resolution (cold)
* Second: **8 ms** → cache hit or stale serve

Also key detail from your data:

```
EDE: 3 (Stale Answer)
```

That means:

* Unbound served **expired cache** instead of resolving fresh
* That’s why you got **8 ms**

👉 Translation:

* Your resolver is **fast when warm**
* But **slow when doing real recursion**

---

## 🧊 4. Cloudflare underperforming (for your location)

* ~43–44 ms consistently
* That’s unusual (Cloudflare is usually fastest)

This suggests:

* suboptimal routing from your ISP
* or WSL networking path overhead
* or hitting a less optimal Cloudflare PoP

---

# ⚡ Key Insight (this is the real takeaway)

You actually measured **three different DNS behaviors**:

| Behavior                     | Winner                      |
| ---------------------------- | --------------------------- |
| Raw latency (edge proximity) | OpenDNS                     |
| Consistency                  | Google                      |
| Cached performance           | Pi-hole                     |
| Cold recursive resolution    | Public DNS (Google/OpenDNS) |

---

# 🧠 What I would do in your setup

Given your style (systems + performance-oriented):

## ✅ Optimal architecture

* **Primary:** Pi-hole + Unbound (your local resolver)
* **Fallback / upstream tuning:** consider forwarding to:

  * OpenDNS (based on your results)
  * or Google

---

## 🔧 But fix this first (important)

Your Unbound config is likely:

* doing full recursion every time (good)
* but not aggressively caching or prefetching

### You want:

```conf
prefetch: yes
serve-expired: yes
cache-min-ttl: 300
cache-max-ttl: 86400
```

This turns your Pi-hole into:

* low-latency like OpenDNS
* but local + private

---

## The following "Hypothesis" was updated by me:
- After `dig-ging` with GPT-5.3 that OpenDNS is clear winner.
- Other hosted ML/AI models would also assume Cloudflare is the fastest.
- Figuring out how infrastructure is laid-out.
- More testing is required like proximity.
- Why it's a hypothesis, not a theory.
- Below is not entirely GPT-5.3.

---

### ✅ Hypothesis
- For a person obssessed about DNS, this needs `dig-ging` into.

* Large DNS providers **do deploy infrastructure close to ISPs**
* They often sit in:

  * IXPs (Internet Exchanges)
  * carrier-neutral data centers
* Physical proximity **does matter**
* DNS performance is driven by **anycast PoP placement + peering relationships**, inside ISP facilities.

---

<sup>
...code & cloud matters less, when infrastructure wins
</sup>