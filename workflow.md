# The Architecture Diagram

## Trigger (Splunk):
- **Input**: Sysmon detects `mimikatz.exe`.
- **Splunk**: The SPL search finds this event.
- **Action**: Splunk triggers a "Custom Alert Action" (or a simple Webhook).

## The Bridge (Webhook/Script):
- Splunk sends the raw event data (JSON) to your Python Script.

## The Brain (Your Python SOAR):

### Step A (Parsing):
- Python receives the JSON. It extracts the **File Hash**, **Source IP**, and **User**.

### Step B (Enrichment):
- Python sends the **Hash** to the VirusTotal API.
- Python sends the **IP** to the AbuseIPDB API.

### Step C (The AI Analyst):
- Python constructs a prompt: 
  ```
  "I have an incident with Hash X (VT Score: 50/60) and IP Y. Analyze this attack vector, map to MITRE, and suggest remediation."
  ```
- Sends this to OpenAI API (GPT-4o-mini) or Groq (Llama3).

## The Output (Response):
- The LLM sends back the analysis.
- Your Python script formats this into a pretty message.
- Sends it to a **Slack Webhook** or **Telegram Bot**.

