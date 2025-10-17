import os
import re

def get_next_version(model_dir="model"):
    """
    Find the next available model version automatically.
    Looks for subfolders like v1/, v2/, etc.
    Each folder contains its model file (e.g., model/v1/model_v1.pkl)
    """
    os.makedirs(model_dir, exist_ok=True)  # Ensure base folder exists

    # List all subfolders inside the model directory
    subdirs = [d for d in os.listdir(model_dir) if os.path.isdir(os.path.join(model_dir, d))]
    versions = []

    for d in subdirs:
        match = re.match(r"v(\d+)$", d)  # Match folder names like v1, v2, v10
        if match:
            versions.append(int(match.group(1)))

    # Determine next version number
    next_version = max(versions) + 1 if versions else 1

    # Create the new version folder (optional)
    new_version_dir = os.path.join(model_dir, f"v{next_version}")
    os.makedirs(new_version_dir, exist_ok=True)

    return next_version