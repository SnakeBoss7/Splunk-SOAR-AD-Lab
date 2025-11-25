### 1. Create the App Structure

```text
/opt/splunk/etc/apps/your_app_name/
├── bin/
│   └── your_script.py          # Your Python script
├── default/
│   ├── alert_actions.conf      # Alert action definition
│   └── app.conf                # App metadata
├── metadata/
│   └── default.meta            # Permissions
└── README/
    └── alert_actions.conf.spec # (optional) Documentation
```

### 2. Configure alert_actions.conf

Template:
```ini
[your_alert_name]
is_custom = 1
label = Your Alert Display Name
description = What your alert does
icon_path = icon.png
payload_format = json
param.your_parameter = default_value
```

My `alert_actions.conf`:
```ini
[soar_response]
is_custom = 1
label = SOAR Auto-Response
description = Enriches incidents with threat intelligence and AI and Create a Ticket on Jira
icon_path = alert_icon.png
payload_format = json
param.script = soar_response.py
```

### 3. Python Script for Debugging

File: `/opt/splunk/etc/apps/soar_mini/bin/soar_response.py`

```python
import sys
from datetime import datetime

# Debug logging
def log_debug(msg):
    try:
        with open("/tmp/soar_debug.log", "a") as f:
            f.write(f"[{datetime.now()}] {msg}\n")
        sys.stderr.write(f"SOAR: {msg}\n")
    except:
        pass

log_debug("=== Script Started ===")
log_debug(f"Arguments: {sys.argv}")
```

### 4. Debugging

To view the debug log:
```bash
sudo tail -f /tmp/soar_debug.log
```
