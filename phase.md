```markdown
CORRECTED Plan (Your Plan Fixed):
Phase 1: T1003.001 (Week 1-2)

✅ Learn: rundll32, lsass, minidump internals
✅ Test: 4-5 methods (comsvcs, procdump, PowerShell, .NET, Dumpert)
✅ Create:

config-v1.xml (basic detection)
T1003-Playbook.md
T1003-Analysis.md
Splunk queries


✅ Test: Alerts fire? Dashboard shows events?
✅ Tune: Fix false positives → config-v1.1.xml


Phase 2: T1059.001 (Week 3)

✅ Learn: PowerShell execution, obfuscation
✅ Test: 3 methods
✅ Update config-v1.1.xml → config-v2.xml

Keep T1003 rules
ADD T1059 rules
ADD NetworkConnect for PowerShell


✅ Update Splunk queries
✅ Test: Both T1003 AND T1059 still detected?


Phase 3: T1053.005 (Week 4)

✅ Learn: Scheduled task persistence
✅ Test: 2 methods
✅ Update config-v2.xml → config-v3.xml

Keep T1003 + T1059 rules
ADD T1053 rules
ADD RegistryEvent monitoring


✅ Final tuning


Phase 4: Final Documentation (Week 5)

✅ Create master dashboard (all 3 attacks)
✅ Write Config-Evolution.md (why v1→v2→v3)
✅ Test all 3 attacks still work
✅ Record demo video


File Structure (CORRECTED):
├── T1003.001/
│   ├── Attack-Analysis.md
│   ├── Playbook.md
│   ├── config-v1.xml (T1003 only)
│   ├── config-v1.1.xml (T1003 tuned)
│   └── Splunk-Queries/
│
├── T1059.001/
│   ├── Attack-Analysis.md
│   ├── Playbook.md
│   ├── config-v2.xml (T1003 + T1059) ← EVOLVED, not separate
│   └── Splunk-Queries/
│
├── T1053.005/
│   ├── Attack-Analysis.md
│   ├── Playbook.md
│   ├── config-v3.xml (ALL 3 attacks) ← FINAL VERSION
│   └── Splunk-Queries/
│
└── Final-Config/
    ├── sysmon-production.xml (config-v3 renamed)
    ├── Config-Evolution.md (v1→v2→v3 explained)
    └── Detection-Coverage-Matrix.xlsx

Summary - Your Plan Fixed:
What You SaidStatusFixLearn 1003.001 deeply✅ CORRECTNoneTest 4-5 methods✅ CORRECTNoneCreate playbook/analysis✅ CORRECTNoneTest Splunk "reports"⚠️ WRONG TERMTest ALERTS, not reportsSeparate XML per attack❌ WRONGBuild ONE XML incrementallyMerge at end❌ WRONGEVOLVE config, don't merge
```