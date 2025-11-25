
import requests, base64
import json

invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
stream = False


headers = {
  "Authorization": "Bearer <api>",
  "Accept": "text/event-stream" if stream else "application/json"
}
user_prompt ={
  "AlertData": {
    "AlertName": {
      "ExtractedValue": "PowerShell Encoded Command Detected",
      "ContextualClue": "High Suspicion Trigger"
    },
    "User": {
      "ExtractedValue": "NT AUTHORITY\\SYSTEM",
      "ContextualClue": "KEY CLUE: High privilege, but a system account."
    },
    "Hostname": {
      "ExtractedValue": "WIN-SERVER-004",
      "ContextualClue": "Log Source (Server context)"
    },
    "ParentProcessName": {
      "ExtractedValue": "msiexec.exe",
      "ContextualClue": "KEY CLUE: MSI Installer."
    },
    "Image": {
      "ExtractedValue": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
      "ContextualClue": "Standard Windows path."
    },
    "CommandLine": {
      "ExtractedValue": "powershell.exe -NoP -Enc VABlAHMAdABpAG4AZwAgAFMAeQBzAHQAZQBtACAAVwBjAGwAZQAgAFMAZABrAC4ALgA=",
      "ContextualClue": "Looks malicious (Encoded Command)."
    },
    "FileHash_SHA256": {
      "ExtractedValue": "B1C6A9EE3C...",
      "ContextualClue": "Standard Hash for powershell.exe."
    },
    "SourceIP": {
      "ExtractedValue": "N/A",
      "ContextualClue": "Local Execution."
    },
    "VTScore": {
      "ExtractedValue": "0/70",
      "ContextualClue": "KEY CLUE: Benign."
    }
  }
}


system_prompt = r"""
**SYSTEM INSTRUCTION:** You are a Tier 3 Cyber Security Incident Handler. Your task is to perform an initial analysis of a high-severity alert. Analyze the provided log data and enrichment findings. Your output must be strictly structured using the requested sections.

---
**INCIDENT DATA:**
**ALERT NAME:** Suspicious Credential Harvesting Tool Execution
**HOSTNAME:** WIN-DESKTOP-54321
**USER:** CORP\analyst_temp
**PROCESS NAME:** mimi.exe (Executed from Downloads folder)
**COMMAND LINE:** C:\Users\analyst_temp\Downloads\mimi.exe "sekurlsa::logonpasswords full" exit
**FILE HASH (SHA256):** A94A8FE5CCB19BA61C4C0873D391E987982FC03A1672323D47721A58AE981B68
**SOURCE IP:** 192.168.10.201
**ENRICHMENT: VIRUSTOTAL SCORE:** 58/70 (Malicious)

---
**ANALYSIS TASKS:**
1.  **Attack Analysis:** Provide a brief summary of the attack, identifying the tool and its function.
2.  **MITRE ATT&CK Mapping:** Map the activity to the most relevant Tactics and Techniques, including the Technique ID (T-ID).
3.  **Severity Score & Rationale:** Assign a final severity score (Critical, High, Medium, Low) and justify it.
4.  **Recommended Response (3 Steps):** Suggest the immediate containment and investigation actions for a SOC analyst.

Collect Sysmon Event ID 1, 7, 11, and 13 for process ancestry and image loads.
Review Security Logs 4624 and 4672 for privileged logons before/after execution.
Check for credential theft persistence via scheduled tasks, Run keys, WMI subscriptions.
Acquire memory snapshot to confirm credential theft (Volatility plugins: lsadump, mimikatz).

"""


payload = {
  "model": "meta/llama-4-maverick-17b-128e-instruct",
  "messages": [{"role":"system","content":system_prompt+"think"},{"role":"user","content":json.dumps(user_prompt)}],
  "max_tokens": 512,
  "temperature": 1.00,
  "top_p": 1.00,
  "frequency_penalty": 0.00,
  "presence_penalty": 0.00,
  "stream": stream
}

response = requests.post(invoke_url, headers=headers, json=payload)

if stream:
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
else:
    print(response.json())
