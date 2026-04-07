
---

# 🔎 Advanced osquery Threat Hunting Queries

These queries focus on **persistence, privilege escalation, suspicious processes, and attacker techniques**.

---

# 1️⃣ Auto-Starting Services (Persistence)

```sql
SELECT
  name AS service_name,
  path AS service_path,
  start_type,
  status
FROM services
WHERE start_type = 'AUTO_START'
ORDER BY name;
```

Detects services that **automatically start on boot**, a common persistence method.

---

# 2️⃣ Scheduled Tasks (Persistence & Recon)

```sql
SELECT
  name AS task_name,
  path AS task_path,
  action AS task_action,
  enabled,
  datetime(last_run_time, 'unixepoch', 'localtime') AS last_run_time,
  datetime(next_run_time, 'unixepoch', 'localtime') AS next_run_time
FROM scheduled_tasks
WHERE enabled = 1
ORDER BY next_run_time DESC;
```

Attackers often use **scheduled tasks for persistence or delayed execution**.

---

# 3️⃣ Registry Autoruns (HKLM & HKCU)

```sql
SELECT
  CASE
    WHEN path LIKE 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run%' THEN 'HKLM'
    WHEN path LIKE 'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run%' THEN 'HKCU'
    ELSE 'Other'
  END AS hive,
  path AS registry_key,
  name AS value_name,
  type AS value_type,
  data AS value_data
FROM registry
WHERE path LIKE 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run%'
   OR path LIKE 'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run%'
ORDER BY registry_key;
```

Detects **startup persistence through registry run keys**.

---

# 4️⃣ Local Administrator Accounts (Privilege Audit)

```sql
SELECT
  u.username,
  u.description,
  u.directory AS home_directory
FROM users u
JOIN user_groups ug ON ug.uid = u.uid
JOIN groups g ON g.gid = ug.gid
WHERE g.groupname = 'Administrators'
ORDER BY u.username;
```

Shows **all users with local administrator privileges**.

---

# 5️⃣ WMI Event Filters (Hidden Execution Triggers)

```sql
SELECT
  name AS filter_name,
  query AS wql_query
FROM wmi_event_filters
ORDER BY name;
```

Attackers often use **WMI event subscriptions for stealth persistence**.

---

# 6️⃣ Orphan Processes (Suspicious Parent)

```sql
SELECT
  pid,
  name AS process_name,
  path AS process_path,
  parent AS parent_pid,
  datetime(start_time, 'unixepoch', 'localtime') AS start_time
FROM processes
WHERE parent = 0
ORDER BY start_time DESC;
```

Processes with **parent PID = 0** may indicate suspicious execution.

---

# 7️⃣ Listening Network Ports

```sql
SELECT
  lp.pid,
  p.name AS process_name,
  lp.protocol,
  lp.address,
  lp.port
FROM listening_ports lp
JOIN processes p ON p.pid = lp.pid
WHERE lp.address NOT IN ('127.0.0.1', '::1')
ORDER BY lp.port;
```

Detects **processes listening on network interfaces**.

---

# 8️⃣ Non-Microsoft Signed Modules (Possible DLL Hijack)

```sql
SELECT
  pm.name AS module_name,
  pm.path AS module_path,
  pm.pid,
  pm.signed,
  pm.signed_by
FROM pe_modules pm
WHERE pm.signed_by NOT LIKE '%Microsoft%'
ORDER BY pm.pid, pm.name;
```

Useful for detecting:

* **DLL hijacking**
* **malicious module injection**

---

# 9️⃣ Recent Sysmon Process Creations

```sql
SELECT
  datetime(time_generated/1000, 'unixepoch', 'localtime') AS event_time,
  json_extract(event_data, '$.Image') AS process_path,
  json_extract(event_data, '$.CommandLine') AS cmdline,
  json_extract(event_data, '$.User') AS user
FROM windows_eventlog
WHERE channel = 'Microsoft-Windows-Sysmon/Operational'
AND eventid = 1
ORDER BY event_time DESC
LIMIT 20;
```

Requires **Sysmon installed**.

Shows **recent process executions with command lines**.

---

# 🔟 Loaded Kernel Drivers

```sql
SELECT
  name AS driver_name,
  path AS driver_path,
  signed
FROM drivers
WHERE signed = 0
ORDER BY name;
```

Unsigned drivers may indicate:

* rootkits
* malicious kernel modules
* privilege escalation attempts

---

# 1️⃣1️⃣ Recent PowerShell Script Blocks

```sql
SELECT
  datetime(time_generated/1000, 'unixepoch', 'localtime') AS exec_time,
  json_extract(event_data, '$.ScriptBlockText') AS ps_script
FROM windows_eventlog
WHERE channel = 'Microsoft-Windows-PowerShell/Operational'
AND eventid IN (4103,4104)
ORDER BY exec_time DESC
LIMIT 20;
```

Detects **PowerShell script execution**, useful for detecting:

* fileless malware
* encoded commands
* attacker scripts

---

# 1️⃣2️⃣ Recently Modified System32 Files

```sql
SELECT
  path AS file_path,
  datetime(mtime, 'unixepoch', 'localtime') AS modified_time,
  mode,
  size
FROM file
WHERE path LIKE 'C:\\Windows\\System32\\%'
ORDER BY mtime DESC
LIMIT 20;
```

Detects **unexpected modifications to critical system files**.

---

# 1️⃣3️⃣ Recently Logged-In Users

```sql
SELECT
  user,
  host,
  datetime(time, 'unixepoch', 'localtime') AS login_time
FROM logged_in_users
ORDER BY login_time DESC
LIMIT 10;
```

Useful during **incident response to see recent interactive logins**.

---

