# T1053.005 - Scheduled Task

## What I Learned From This Attack

This attack helped me understand different attack vectors from a visibility and stealth perspective, and especially how attackers think when trying to stay hidden and make their attack more Obfuscated.

### Stealth Ranking (Based on This Exercise)

| Tool / Binary     | Stealth Level | Reason                                                                                   | Detection Notes                                      |
|-------------------|---------------|------------------------------------------------------------------------------------------|------------------------------------------------------|
| **schtasks.exe**  | Very Low      | Rarely used by normal users in interactive sessions<br>Creates obvious scheduled task artifacts | Easy to spot with basic process creation logging   `Event ID 1`|
| **powershell.exe**| High          | Used extremely frequently in Windows environments<br>Almost every admin task involves PowerShell | Blends in perfectly with legitimate activity       |
| **wmi.exe** (or **wmic.exe** / **wmiprvse.exe**) | Very High     | WMI is used constantly by the system and applications<br>Generates massive log noise<br>Requires special WMI tracing to see malicious activity<br>Has full access to hardware, processes, and API | Extremely hard to detect without enabling WMI operational logs (and even then — very noisy) |

## WMI Logs
`Note: To capture WMI persistence (EIDs 19, 20, 21), you must explicitly enable these events in your Sysmon configuration. `
- Event ID 19 — WmiEventFilter (filter creation)
- Event ID 20 — WmiEventConsumer (consumer creation)
- Event ID 21 — WmiEventConsumerToFilter (binding creation)

### Key Takeaway
Attackers don’t always choose the most powerful tool — they choose the one that looks the most normal in the environment. The quieter the tool is in everyday use, the longer they can stay undetected.

##  What is this Attack
Adversaries may abuse the Windows Task Scheduler to perform task scheduling for initial execution or persistence. Scheduled tasks can be used to execute programs at system startup or on a scheduled basis for persistence.

##  Why Attackers Use This
- **Persistence**: Ensure their malware runs every time the computer starts or at specific times.
- **Privilege Escalation**: Some tasks run as SYSTEM.
- **Execution**: Run code in the background without user interaction.


##  Telemetry & Detection
We will focus on **Sysmon** telemetry to detect this.

### Key Events
- **Event ID 1 (Process Creation)**: Look for `schtasks.exe` with `/create` arguments.
- **Event ID 11 (File Create)**: New files created in `C:\Windows\System32\Tasks`.
- **Event ID 12/13 (Registry Event)**: Changes to `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree`.

##  Mitigation
- Restrict who can create scheduled tasks.
- Monitor for unexpected task creation.
