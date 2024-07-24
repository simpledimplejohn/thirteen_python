array1 = [1,2,3,4,5,6]

count_array = [11,13,9,10]

print("basic for loop")
for i in array:
    print(i, array[i])

# this will give you the indicies of the array
print("enumerate over indicies")
for index, value in enumerate(array):
    print(index, value)


for i in count_array:
    print("level 1, i =",i)
    for j in range(i):
        print("level 2, j =",j,"i =",i)