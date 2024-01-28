data = (4, 24, 7, 4, True, "hi", 5.6)

print("'lenght':", len(data))

print("'4':", data.count(4))

lst = []
for el in data:
    lst.append(el)
print(lst)

new_data = "Hello World"
new_tuple = tuple(new_data)
print("new_tuple:", new_tuple)