from datetime import datetime
import os

def generate_log(log_data, directory="."):
    if type(log_data) is not list:
        raise ValueError("Invalid input: log_data must be a list")
    
    os.makedirs(directory, exist_ok=True)
    
    filename = "log_" + datetime.now().strftime("%Y%m%d") + ".txt"
    filepath = os.path.join(directory, filename)
    
    with open(filepath, "w") as f:
        for item in log_data:
            f.write(str(item) + "\n")
    
    print(f"Log written to {filepath}")
    return filepath

if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)