
---

# Osquery

**osquery** is an open-source tool originally developed at Facebook that exposes an operating system as a **relational database**, allowing users to query OS data like running processes, kernel modules, users, services, installed applications, and network connections using **SQL**.

It serves as a powerful framework for:

* 🔎 **Security visibility**
* 🛡 **Endpoint detection**
* 📋 **Compliance monitoring**
* 🚨 **Incident response**
* 🖥 **System inventory**

Instead of using multiple platform-specific commands, **osquery provides a unified interface across operating systems**.

Supported platforms:

* Windows
* macOS
* Linux

---

## How Osquery Works

Osquery converts system information into **tables**, similar to a SQL database.

For example:

| Table             | Description             |
| ----------------- | ----------------------- |
| `processes`       | Running processes       |
| `listening_ports` | Open ports              |
| `programs`        | Installed applications  |
| `users`           | Local user accounts     |
| `services`        | Running system services |
| `startup_items`   | Startup programs        |

You simply run SQL queries like:

```sql
SELECT * FROM processes;
```

This makes osquery extremely powerful for **security analysts and system administrators** who are already familiar with SQL.

---

# Basics

### Install osquery (Windows)

Open **Command Prompt as Administrator**.

```powershell
winget install osquery.osquery -e
```

---

### Start the interactive shell

```powershell
osqueryi
```

If the command is not found:

```powershell
cd "C:\Program Files\osquery"
osqueryi
```

---

### osquery Interactive Prompt

Once launched, you will see:

```
osquery>
```

This means the SQL shell is ready.

---

### Example Query

Paste a query and press **Enter**.

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

This query shows:

* Running processes
* Listening network ports
* External network bindings

Very useful during **network investigations**.

---

# Queries

Below are some useful example queries.

---

## 1. Get version of an application

```powershell
PS C:\Users\me> osqueryi "SELECT name, version FROM programs WHERE name LIKE '%TIDAL%';"
```

Example output:

```
+-------+---------+
| name  | version |
+-------+---------+
| TIDAL | 2.40.0  |
+-------+---------+
```

---

## 2. List running processes

```sql
SELECT pid, name, path FROM processes;
```

Useful for identifying:

* suspicious binaries
* malware
* unknown background services

---

## 3. Show open network connections

```sql
SELECT pid, address, port FROM listening_ports;
```

This helps identify:

* exposed services
* unexpected network listeners
* malware command & control ports

---

## 4. List system users

```sql
SELECT username, uid, gid, directory FROM users;
```

Useful for:

* auditing accounts
* checking privilege levels
* detecting unauthorized users

---

## 5. Find startup programs

```sql
SELECT name, path FROM startup_items;
```

Great for detecting:

* persistence mechanisms
* malicious startup scripts

---

# Commonly Used Tables

| Table             | Purpose                |
| ----------------- | ---------------------- |
| `processes`       | Running processes      |
| `listening_ports` | Open ports             |
| `programs`        | Installed applications |
| `services`        | System services        |
| `users`           | Local users            |
| `groups`          | Local groups           |
| `scheduled_tasks` | Scheduled jobs         |
| `startup_items`   | Startup programs       |

Full table list:

[https://osquery.io/schema/](https://osquery.io/schema/)

---

# Use Cases

## Security Monitoring

Osquery allows security teams to detect:

* malware processes
* unauthorized ports
* suspicious startup items
* unknown user accounts

---

## Incident Response

During an incident, investigators can quickly gather system data:

```sql
SELECT * FROM processes;
SELECT * FROM listening_ports;
SELECT * FROM logged_in_users;
```

---

## Compliance

Organizations use osquery to ensure:

* required software is installed
* security settings are correct
* unauthorized applications are not present

---

# Tips

### Run single queries from PowerShell

```powershell
osqueryi "SELECT * FROM processes LIMIT 5;"
```

---

### View table schema

```sql
.schema processes
```

---

### List all tables

```sql
.tables
```

---

# About

* Official GitHub
  [https://github.com/osquery/osquery](https://github.com/osquery/osquery)

* Official Website
  [https://osquery.io/](https://osquery.io/)

* Schema Documentation
  [https://osquery.io/schema/](https://osquery.io/schema/)

---

# Summary

Osquery turns an operating system into a **queryable database**, making it an incredibly powerful tool for:

* security monitoring
* endpoint management
* system auditing
* incident response

If you know **SQL**, you already know how to use **osquery**.

---
