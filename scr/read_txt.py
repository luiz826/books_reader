import os
import sys

file_path = os.path.join("data", "Artificial-Intelligence-A-Modern-Approach-_4th-Edition_.txt")

txt = open(file_path, encoding='utf8') 

for _ in range(10):
    print(txt.readline().strip())

# itterate for all the txt



