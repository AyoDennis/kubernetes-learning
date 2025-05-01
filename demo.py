import time
import os


name1 = os.environ.get("FIRST_NAME")

name2 = os.environ.get("LAST_NAME")

name3 = os.environ.get("MIDDLE_NAME")

print(f"I am {name1} {name2} {name3}")

time.sleep(20000)
