
---

# 🔎 Practical Security Hunting Queries

These queries are useful for **security analysts, blue teams, and incident responders** to detect suspicious activity on endpoints.

---

## 1️⃣ Find Suspicious Listening Ports

Detect processes listening on network ports that are **not localhost**.

```sql
SELECT
  p.pid,
  p.name AS process_name,
  lp.protocol,
  lp.address,
  lp.port
FROM listening_ports lp
JOIN processes p ON p.pid = lp.pid
WHERE lp.address NOT IN ('127.0.0.1', '::1')
ORDER BY lp.port;
```

**Why it matters**

Attackers often open **backdoor ports** to maintain persistence.

---

## 2️⃣ Detect Processes Running from Temp Directories

```sql
SELECT
  pid,
  name,
  path
FROM processes
WHERE path LIKE '%Temp%'
   OR path LIKE '%AppData%';
```

**Why it matters**

Malware commonly runs from:

* `%TEMP%`
* `%APPDATA%`
* `%LOCALAPPDATA%`

---

## 3️⃣ Find Suspicious Parent-Child Process Relationships

```sql
SELECT
  child.pid,
  child.name AS child_process,
  parent.name AS parent_process
FROM processes child
JOIN processes parent
ON child.parent = parent.pid
WHERE parent.name = 'winword.exe'
   OR parent.name = 'excel.exe';
```

**Why it matters**

Office spawning processes like:

* `powershell.exe`
* `cmd.exe`
* `wscript.exe`

is often **malicious macro behavior**.

---

## 4️⃣ Detect Running PowerShell Instances

```sql
SELECT
  pid,
  name,
  path,
  cmdline
FROM processes
WHERE name LIKE '%powershell%';
```

**Why it matters**

PowerShell is frequently abused for:

* fileless malware
* lateral movement
* data exfiltration

---

## 5️⃣ Check Startup Persistence Mechanisms

```sql
SELECT
  name,
  path,
  source
FROM startup_items;
```

**Why it matters**

Attackers commonly add persistence through:

* registry run keys
* startup folders
* scheduled tasks

---

## 6️⃣ Identify Recently Created Users

```sql
SELECT
  username,
  uid,
  directory
FROM users;
```

**Why it matters**

Unauthorized accounts can indicate:

* compromised systems
* persistence mechanisms
* privilege escalation

---

## 7️⃣ Detect Suspicious Network Connections

```sql
SELECT
  p.pid,
  p.name,
  n.remote_address,
  n.remote_port
FROM process_open_sockets n
JOIN processes p ON p.pid = n.pid
WHERE n.remote_address NOT LIKE '192.168.%'
AND n.remote_address NOT LIKE '10.%'
AND n.remote_address NOT LIKE '172.%';
```

**Why it matters**

Shows processes communicating with **external IP addresses**.

---

## 8️⃣ Find Unsigned Executables

```sql
SELECT
  path,
  signed,
  publisher
FROM authenticode
WHERE signed = 0;
```

**Why it matters**

Unsigned binaries may indicate:

* malware
* suspicious tools
* unauthorized software

---

## 9️⃣ Detect Scheduled Tasks (Persistence)

```sql
SELECT
  name,
  action,
  path
FROM scheduled_tasks;
```

**Why it matters**

Malware frequently schedules tasks to:

* run payloads periodically
* execute on system startup

---

## 🔟 Check Loaded Kernel Drivers

```sql
SELECT
  name,
  path,
  status
FROM drivers;
```

**Why it matters**

Malicious drivers are used for:

* rootkits
* privilege escalation
* stealth persistence

---

# 💡 Pro Tip

Combine `osquery` with:

* **SIEM platforms**
* **FleetDM**
* **Elastic**
* **Splunk**

to run these queries across **thousands of endpoints simultaneously**.

Example:

```bash
osqueryi "SELECT name, pid FROM processes WHERE name LIKE '%powershell%';"
```

---

# 🛡️ Security Use Cases

`osquery` is commonly used for:

* Threat hunting
* Incident response
* Compliance auditing
* Endpoint visibility
* Digital forensics

---

# 📚 Useful Query Packs

You can explore **community hunting queries here**:

* [https://github.com/osquery/osquery/tree/master/packs](https://github.com/osquery/osquery/tree/master/packs)
* [https://github.com/osquery/osquery/tree/master/tools](https://github.com/osquery/osquery/tree/master/tools)

---


