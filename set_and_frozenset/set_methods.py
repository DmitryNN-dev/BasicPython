data = set("hello")
print("set:", data, "\n")

data = {5, 15, 9, 10, 7}
print("before:", data)

# new element 
print("after:")
data.add(32)
data.update([24,"32", True, 74, 18])
print("result:", data)

# delete element
data.remove("32")
data.pop()
# data.clear()
data.discard(3)  # Удалит элемент 3 из множества, если он там присутствует
print(data, "\n")