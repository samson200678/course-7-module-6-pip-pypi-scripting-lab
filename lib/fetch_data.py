from datetime import datetime

log_data = [
    "User logged in",
    "User updated profile",
    "Report exported"
]

filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

with open(filename, "w") as file:
    for entry in log_data:
        file.write(entry + "\n")

print(f"Log written to {filename}")