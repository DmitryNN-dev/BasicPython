data = input("ВВедите текст: ")

file = open("work_with_file/text.txt", 'w')

# file = open("work_with_file/text.txt", 'a')  # сохраняет (не перезаписывает при перезапуске)

file.write("Hello")
file.write("!!!!\n")

file.write(data)

file.close()