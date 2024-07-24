import numpy as np
import sounddevice as sd
import time
import os

# [in_count,in_hold,out_count,out_hold]
count_array = [13,13,13,13]

sequence = [3,2,1,10,9,8,7,6,5,4,3,2,1]
fsequence = [1,2,3,4,5,6,7,8,9,10,1,2,3]

count_object = [{1:13},{2:10},{3:9},{4:10}]

cycle_object = ["in","out","in","out"]
 
os.system(f"say start")

num_cycles = 1

for h in range(num_cycles):
    print("cycle =",num_cycles + 1)

    for i in range(4):
        os.system(f"say {cycle_object[i]}")
        print("cycle object is",cycle_object[i])
        start_time = time.time()

        number = i + 1
        
        print("level is:",number, "index is:",i)

        print("count for this level",count_object[i][number])
        current_count = count_object[i][number]

        for i in range(current_count):
            print("index:",i,"sequence array:",sequence[i])
            counting = i + 1
            if counting > 10:
                counting = fsequence[i]
            print("counting:",counting)
            os.system(f"say {counting}")
            next_time = start_time +1
            while time.time() < next_time:
                pass
            start_time = next_time

