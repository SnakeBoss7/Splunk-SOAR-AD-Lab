Invoke-AtomicTest T1003.001 -ShowDetails
Invoke-AtomicTest T1003.001
```

Focus on:
- Process creation (EventID 1)
- File creation (EventID 11)
- Registry changes (EventID 12/13)
- Network connections (EventID 3)

### **Phase 2: Add Attacker Machine (Optional but Impressive)**

**Why add it:**
- Demonstrates **network-based detection** (not just host-based)
- Shows understanding of **lateral movement**
- Captures **attacker infrastructure** IOCs

**What to attack from Kali:**
1. **Port scanning** (Nmap) → Detect with Sysmon EventID 3
2. **SMB enumeration** → Detect failed auth attempts
3. **RDP brute force** → Windows Security logs
4. **Payload delivery** → Suspicious downloads
5. **C2 simulation** (Metasploit) → Outbound connections

**Network detection you'll capture:**
```
Attacker IP: 192.168.1.50 (Kali)
Victim IP: 192.168.1.100 (Windows)

Splunk will show:
- Source/Destination IPs
- Ports used
- Connection patterns
- Protocol anomalies
# Run the atomic test
Invoke-AtomicTest T1003.001
```

**3. Detection Engineering:**
- Write Splunk search query
- Create alert with proper threshold
- Test with multiple variations
- Document false positive scenarios

**4. Analysis & Documentation:**
- Screenshot the alert firing
- Show the raw logs
- Explain what each field means
- Create incident timeline
- Write detection logic explanation

**5. Visualization:**
- Add to dashboard
- Create relevant charts
- Map to MITRE ATT&CK framework

**6. Response Playbook:**
- Document how to investigate this alert
- List remediation steps
- Provide hunting queries

---

## 📊 What Your Final Project Should Include:

### **Documentation Structure:**
```
├── README.md (Project overview)
├── Lab-Setup/
│   ├── Architecture-Diagram.png
│   ├── Sysmon-Config.xml
│   └── Setup-Instructions.md
├── Detections/
│   ├── T1003.001-LSASS-Dumping/
│   │   ├── Attack-Execution.md
│   │   ├── Splunk-Search.spl
│   │   ├── Alert-Configuration.md
│   │   ├── Screenshots/
│   │   └── Incident-Report.md
│   ├── T1059.001-PowerShell/
│   └── [6 more attacks...]
├── Dashboards/
│   ├── SOC-Overview.xml
│   └── Dashboard-Screenshots/
├── Sigma-Rules/
│   └── converted-rules.yml
└── Lessons-Learned.md
```