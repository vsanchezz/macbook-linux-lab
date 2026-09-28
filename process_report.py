from pathlib import Path
import os

status_file = Path("/proc/self/status")
fields = {}

for line in status_file.read_text().splitlines():
    if ":" in line:
        name, value = line.split(":", 1)
        fields[name] = value.strip()

print(f"Directorio de trabajo: {Path.cwd()}")
print(f"PID según Python: {os.getpid()}")

for name in ("Name", "Pid", "PPid", "Uid", "VmRSS"):
    print(f"{name}: {fields.get(name, 'no disponible')}")