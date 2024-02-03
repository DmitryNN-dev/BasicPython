file = open("work_with_file/text.txt", 'r')  # для чтения

# print(file.read())
# print(file.read(9))

for line in file:
    print(line, end="")

file.close()