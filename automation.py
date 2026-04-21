import os
import time

print("Starting pipeline...")

os.system("python scripts/fetch_data.py")
time.sleep(2)

os.system("python scripts/process_data.py")

print("Pipeline completed successfully!")