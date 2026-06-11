from datetime import datetime
import os


def generate_log(log_data, directory="."):

    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")


    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    filepath = os.path.join(directory, filename)

 
    with open(filepath, "w") as file:
        for item in log_data:
            file.write(f"{item}\n")

 
    print(f"Log written to {filename}")

    return filepath