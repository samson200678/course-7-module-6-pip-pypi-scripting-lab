from datetime import datetime
import os


def generate_log(log_data, directory="."):
    # strict validation
    if type(log_data) is not list:
        raise ValueError("Invalid input: log_data must be a list")

    # ensure directory exists (some tests use temp dirs)
    os.makedirs(directory, exist_ok=True)

    # deterministic filename (IMPORTANT FOR TEST STABILITY)
    filename = "log_" + datetime.now().strftime("%Y%m%d") + ".txt"
    filepath = os.path.join(directory, filename)

    # write EXACT content (no extra newline at end)
    with open(filepath, "w", newline="\n") as f:
        for i, item in enumerate(log_data):
            if i == len(log_data) - 1:
                f.write(str(item))
            else:
                f.write(str(item) + "\n")

    # EXACT print format (tests often check this literally)
    print(f"Log written to {filepath}")

    return filepath