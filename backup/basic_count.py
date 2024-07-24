# Basic thirteen count
import os

# [in_count,in_hold,out_count,out_hold]
count_array = [13,13,13,13]



os.system(f"say starting")
for i in count_array:
    print()
    print("level 1, i =",i)
    for j in range(i):
        number = j + 1
        os.system(f"say {number}")
        print("level 2, j =",j,"i =",i)