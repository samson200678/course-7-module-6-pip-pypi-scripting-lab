"""
generate_log.py
---------------
Step 2: Demonstrates file writing using Python scripting.
Writes a session activity log to a timestamped .txt file.
"""

from datetime import datetime


def generate_log(log_entries: list[str], output_dir: str = ".") -> str:
    """Write log entries to a timestamped file and return the filename."""
    filename = f"{output_dir}/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    header = f"=== Activity Log | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n"

    with open(filename, "w") as file:
        file.write(header)
        for i, entry in enumerate(log_entries, start=1):
            timestamp = datetime.now().strftime("%H:%M:%S")
            file.write(f"[{timestamp}] [{i:>3}] {entry}\n")
        file.write(f"\nTotal entries: {len(log_entries)}\n")

    return filename


if __name__ == "__main__":
    log_data = [
        "User logged in",
        "User updated profile",
        "Dashboard viewed",
        "Report exported",
        "User logged out",
    ]

    output_file = generate_log(log_data)
    print(f"Log written to {output_file}")