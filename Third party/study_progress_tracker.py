from tqdm import tqdm
import time

# Change this value to make the progress faster or slower
delay = 0.2

for i in tqdm(range(20), desc="Study progress"):
    time.sleep(delay)

print("All 20 study tasks completed!")