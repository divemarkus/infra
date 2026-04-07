
# 🧠 Why pfSense Uses ZFS (Not UFS anymore)

Historically:

* pfSense used **UFS**
* Starting ~2.5+, **ZFS became the default**

👉 Reason:

```text
Reliability + atomic upgrades + recovery
```

This is less about performance and more about **not bricking your firewall during upgrades or crashes**.

---

# ⚙️ ZFS Features (Relevant to pfSense)

## 1. Copy-on-Write (CoW)

ZFS never overwrites data in place.

Instead:

```text
Old block → kept
New block → written elsewhere
Metadata → updated last
```

### Why pfSense cares:

* Prevents corruption during:

  * power loss
  * crashes
  * failed upgrades

👉 This is HUGE for firewalls.

---

## 2. Boot Environments (🔥 Most Important Feature)

This is the **#1 reason Netgate moved to ZFS**.

### What it is:

Each upgrade creates a snapshot of the system:

```text
BE1: pfSense 2.7.0
BE2: pfSense 2.7.1
BE3: pfSense 2.7.2
```

You can:

* Boot into previous versions
* Rollback instantly

### In pfSense:

```bash
bectl list
bectl activate <BE>
```

### Why this matters:

```text
Upgrade breaks firewall → reboot → select old version → you're back
```

👉 No reinstall. No recovery drama.

---

## 3. Snapshots

ZFS supports instant snapshots:

```bash
zfs snapshot zroot/ROOT/default@before-change
```

### pfSense usage:

* Boot environments are built on snapshots
* Manual recovery possible if needed

---

## 4. Data Integrity (Checksums)

Every block has a checksum.

On read:

```text
If checksum fails → data is invalid
```

If redundancy exists (mirror):

* ZFS auto-heals

### Why pfSense cares:

* Protects:

  * config files
  * system binaries
  * logs

👉 Silent corruption = prevented

---

## 5. Atomic Transactions

All writes are transactional:

```text
All or nothing commit
```

### Impact:

* No partial writes
* No half-updated system

---

## 6. Compression (Used, but not critical)

ZFS supports:

```text
lz4 compression (default)
```

pfSense benefits:

* Smaller footprint
* Faster reads in many cases

---

## 7. ARC Cache (RAM-based)

ZFS uses RAM aggressively:

* Cache reads
* Improve performance

👉 On small boxes:

* Can be tuned
* pfSense doesn’t rely heavily on it

---

# 🚫 What pfSense DOES NOT really use from ZFS

Let’s be precise:

| Feature             | Used? | Why                         |
| ------------------- | ----- | --------------------------- |
| RAID-Z              | ❌     | Most installs = single disk |
| Deduplication       | ❌     | Too memory heavy            |
| Large-scale pooling | ❌     | Not a storage appliance     |
| Dataset complexity  | ❌     | Mostly simple layout        |

👉 pfSense uses ZFS **as a reliability layer**, not a storage platform.

---

# 🔐 Lock-Down & Security Layers (Important Section)

ZFS is **not a security tool by itself** — but it enables stronger system integrity.

Let’s break the layers:

---

## 1. Read-Only Root (Conceptual, not strict)

pfSense behaves like an appliance:

* System files rarely change
* Most configs stored separately

ZFS helps by:

* Preventing corruption
* Enabling rollback if tampered

---

## 2. Boot Environment Isolation

Each BE is:

* Immutable snapshot
* Independent boot target

👉 If compromised:

```text
Switch BE → revert system state
```

---

## 3. Upgrade Safety (Atomic OS Replacement)

When pfSense upgrades:

* New BE is created
* Old one untouched

👉 No in-place overwrite → safer

---

## 4. Filesystem Integrity Validation

ZFS ensures:

```text
If data != checksum → reject
```

This protects against:

* disk errors
* bit rot
* silent corruption

---

## 5. Limited Write Surface

pfSense design:

* Logs → `/var`
* Config → `/conf/config.xml`
* System → mostly static

ZFS enforces structure, but pfSense limits write locations.

---

## 6. No Native Encryption (by default in pfSense)

ZFS supports encryption, BUT:

* pfSense installer does **not enable it by default**
* Reason:

  * boot complexity
  * recovery issues

👉 You *can* enable manually, but not typical

---

## 7. No SELinux/AppArmor Equivalent

FreeBSD (pfSense base):

* Uses:

  * permissions
  * jails (not heavily used in pfSense)
* NOT:

  * SELinux
  * AppArmor

👉 ZFS is NOT enforcing execution policies

---

# 🧠 Real Security Model of pfSense (Important Insight)

ZFS is **not the primary security layer**.

pfSense security comes from:

```text
1. Network isolation (firewall rules)
2. Limited exposed services
3. Appliance model (not general-purpose OS)
4. Config-driven system
5. ZFS = integrity + recovery
```

---

# ⚠️ What ZFS DOES NOT Protect You From

Be very clear here:

ZFS does NOT stop:

* ❌ Remote exploits
* ❌ Misconfigured firewall rules
* ❌ Credential compromise
* ❌ WebGUI vulnerabilities

It only helps you:

```text
Recover + maintain integrity
```

---

# 🔥 Why This Matters 

ZFS gives you:

✅ Safe upgrades
✅ Instant rollback
✅ Crash resistance
✅ Config integrity

---

# 🧠 Final Takeaway

```text
ZFS in pfSense ≠ storage feature
ZFS in pfSense = reliability + rollback safety net
```

---

