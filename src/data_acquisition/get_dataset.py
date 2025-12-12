import os
import shutil
import sys

import kagglehub

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "..", "app"))

from logger import get_logger

log = get_logger(__name__)

log.info("Started data acquisition module")

# Download latest version
try:
    log.info("Downloading dataset...")
    cache_path = kagglehub.dataset_download("raduoprea/traffic-signs")
except Exception as e:
    log.error(f"Error downloading dataset: {e}")
    print(f"Error downloading dataset: {e}")

print("Path to dataset files:", cache_path)

log.info(f"Copying dataset from {cache_path}...")
print("Copying to dataset folder from cache...")

try:
    shutil.copytree(
        cache_path + "/V2 - Traffic Signs/train", "data/raw", dirs_exist_ok=True
    )
    shutil.copytree(
        cache_path + "/V2 - Traffic Signs/valid",
        "data/validation",
        dirs_exist_ok=True,
    )
    print("Done copying dataset.")
    log.info("Data copied succesfully.")
except Exception as e:
    print(f"Error copying dataset: {e}")
    log.error(f"Error copying dataset: {e}")

print("Cleaning up...")
log.info("Cleaning up unnecessary files...")

shutil.rmtree(cache_path)

print("Done")
log.info("Data acquisition module finished")
