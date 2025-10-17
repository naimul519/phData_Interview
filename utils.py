import os
import re

def find_latest_model_version(model_dir: str = "./model") -> int:
    """Scans the model directory to find the latest version number."""
    if not os.path.exists(model_dir):
        return 0  # Or raise an error if no model dir exists
    
    # Find all subdirectories matching the pattern 'v' followed by digits (e.g., v1, v2)
    version_dirs = [d for d in os.listdir(model_dir) if os.path.isdir(os.path.join(model_dir, d)) and re.match(r'^v\d+$', d)]
    
    if not version_dirs:
        return 0 # No versioned models found

    # Extract the numbers and find the max
    versions = [int(d[1:]) for d in version_dirs]
    return max(versions)

def get_next_version(model_dir: str = "model") -> int:
    """Finds the latest version and returns the next version number."""
    if not os.path.exists(model_dir):
        return 1 # Start with version 1 if the directory doesn't exist
    
    version_dirs = [d for d in os.listdir(model_dir) if d.startswith('v')]
    if not version_dirs:
        return 1 # Start with version 1 if no version subdirectories exist
    
    latest_version = max([int(d[1:]) for d in version_dirs])
    return latest_version + 1