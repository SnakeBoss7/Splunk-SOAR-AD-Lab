🎯 Recommended Attack Scenarios
1. T1003.001 - LSASS Memory Dumping ✅ (You already have this)
Why: Classic credential access technique
Detection Focus: Process access to lsass.exe, suspicious tool execution
powershellInvoke-AtomicTest T1003.001
2. T1059.001 - PowerShell Execution
Why: Most common initial access/execution vector
Detection Focus: Encoded commands, download cradles, suspicious parent processes
powershellInvoke-AtomicTest T1059.001
Sysmon Events: EventID 1 (Process Creation with CommandLine), EventID 3 (Network)
3. T1053.005 - Scheduled Task Creation
Why: Persistence mechanism
Detection Focus: schtasks.exe execution, suspicious task names/paths
powershellInvoke-AtomicTest T1053.005
Sysmon Events: EventID 1, Windows Security EventID 4698
4. T1547.001 - Registry Run Keys
Why: Common persistence technique
Detection Focus: Registry modifications in Run/RunOnce keys
powershellInvoke-AtomicTest T1547.001
Sysmon Events: EventID 12/13 (Registry modifications)
5. T1055 - Process Injection
Why: Defense evasion and privilege escalation
Detection Focus: Remote thread creation, suspicious memory operations
powershellInvoke-AtomicTest T1055
Sysmon Events: EventID 8 (CreateRemoteThread), EventID 10 (Process Access)
6. T1082 - System Information Discovery
Why: Reconnaissance/Discovery phase
Detection Focus: systeminfo, whoami, net commands in rapid succession
powershellInvoke-AtomicTest T1082
Sysmon Events: EventID 1 (Process chains)
7. T1070.001 - Clear Windows Event Logs
Why: Defense evasion - covering tracks
Detection Focus: wevtutil.exe usage, EventLog service stops
powershellInvoke-AtomicTest T1070.001
Sysmon Events: EventID 1, Windows Security EventID 1102 (log cleared)
8. T1021.001 - Remote Desktop Protocol (RDP)
Why: Lateral movement technique
Detection Focus: Unusual RDP connections, failed login attempts
powershell# From Kali attacker machine
xfreerdp /v:192.168.1.100 /u:testuser /p:wrongpassword
Sysmon Events: EventID 3 (Network), Windows Security EventID 4625 (failed logon)

# Attack Scenarios by MITRE ATT&CK Tactic Coverage

The following Mermaid quadrant chart visualizes MITRE ATT&CK techniques across two dimensions:

- **X-axis**: Priority (Low → High)
- **Y-axis**: Tactic progression (Initial Access → Lateral Movement)
- **Quadrants**:
  1. High Priority - Early Stage
  2. High Priority - Late Stage
  3. Low Priority - Early Stage
  4. Low Priority - Late Stage

## Technique Mapping

| Tactic              | Technique                     | Priority | Quadrant Placement                  |
|---------------------|-------------------------------|----------|-------------------------------------|
| **Initial Access**  | T1059.001 (PowerShell)        | HIGH     | High Priority - Early Stage         |
| **Execution**       | T1053.005 (Scheduled Task)    | HIGH     | High Priority - Early Stage         |
| **Persistence**     | T1547.001 (Registry Run Keys) | MEDIUM   | Medium Priority - Early Stage       |
| **Privilege Escalation** | T1055 (Process Injection) | HIGH     | High Priority - Mid Stage           |
| **Defense Evasion** | T1070.001 (Clear Logs)        | MEDIUM   | Medium Priority - Mid Stage         |
| **Credential Access** | T1003.001 (LSASS Dump)     | HIGH     | High Priority - Mid-Late Stage      |
| **Discovery**       | T1082 (System Info)           | LOW      | Low Priority - Mid Stage            |
| **Lateral Movement**| T1021.001 (RDP)               | MEDIUM   | Medium Priority - Late Stage        |

> **Key Insight**: High-priority techniques cluster in early-to-mid kill chain stages (Initial Access → Privilege Escalation), indicating critical focus areas for detection and prevention.
🔥 Bonus: Network-Based Attacks (If Adding Kali)
If you add the attacker machine, include these:
9. Port Scanning (Reconnaissance)
bash# From Kali
nmap -sS -p 1-1000 192.168.1.100
Detection: Multiple connection attempts, Sysmon EventID 3
10. SMB Enumeration
bash# From Kali
enum4linux 192.168.1.100
```
**Detection:** Multiple SMB connections, failed auth attempts

---

## 📋 Execution Order Recommendation

**Start with these 5 (Core SOC Detection Scenarios):**
1. T1059.001 - PowerShell (execution)
2. T1003.001 - LSASS Dump (credential access)
3. T1053.005 - Scheduled Task (persistence)
4. T1547.001 - Registry Run Keys (persistence)
5. T1070.001 - Clear Logs (defense evasion)

**Then add these for completeness:**
6. T1055 - Process Injection (advanced)
7. T1082 - System Discovery (basic)
8. T1021.001 - RDP from Kali (network-based)

---

## 🎯 Why These Specific Attacks?

✅ **Coverage across kill chain** - Initial access → Persistence → Credential access → Defense evasion  
✅ **Real-world relevance** - These are top techniques used in ransomware/APT attacks  
✅ **Rich telemetry** - Each generates multiple Sysmon event types  
✅ **Detection variety** - Process-based, registry-based, network-based, and behavioral  
✅ **Splunk-friendly** - Easy to query and create visualizations  

---

## 💡 Pro Tips for Your Project

1. **Document each attack's "normal vs malicious" behavior**
   - Example: PowerShell is normal, but `powershell -enc` with network activity is suspicious

2. **Create detection tiers:**
   - **Tier 1:** High-confidence detections (few false positives)
   - **Tier 2:** Medium confidence (needs context)
   - **Tier 3:** Low confidence (hunting queries)

3. **Build a "detection story"** for each:
```
   Attack → Telemetry Generated → Detection Logic → Alert → Triage Steps → Remediation

Test your detections with benign activity to tune false positives

Would you like me to create a detailed execution guide for any specific attack, or help you write the Splunk detection queries for these techniques?