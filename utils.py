import os
import re

def get_next_version(model_dir="model"):
    """
    Find the next available model version automatically.
    Looks for existing files named model_v{N}.pkl
    """
    os.makedirs(model_dir, exist_ok=True)  # Ensure folder exists

    # List all files matching model_v*.pkl
    files = os.listdir(model_dir)
    versions = []

    for f in files:
        match = re.match(r"model_v(\d+)\.pkl", f)
        if match:
            versions.append(int(match.group(1)))

    # Next version is max + 1, or 1 if no files exist
    next_version = max(versions) + 1 if versions else 1
    return next_version