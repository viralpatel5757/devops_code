with open("file1.txt") as data1:
    F1_list = data1.readlines()

with open("file2.txt") as data2:
    F2_list = data2.readlines()

result = [int(n) for n in F1_list if n in F2_list]


print(result)