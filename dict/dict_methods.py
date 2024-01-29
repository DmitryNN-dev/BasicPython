dct = {"a": 1, "b": 5}

print("a:", dct["a"])
print("b:", dct["b"])

print()

new_dict = dict(language="RU", name="Russia" )
print(new_dict)
print("name:", new_dict["name"])

print()

for key in new_dict:
    print("keys:", key)

print()

print("items:", new_dict.items())

print()

for key, value in new_dict.items():
    print(key, " - ", value)

print()

print("language:", new_dict.get("language"))

print()

print("before:", new_dict)
new_dict.pop("name")
print("after:", new_dict)

print()

print("before:", dct)
dct.popitem()  # delete last key and his value
print("after:", dct)

# 
print()

print("keys:", dct.keys())

print()

print("keys and value:", dct.items())

print()
# 

dct.update({"new_key": "new_value"})
print("add new key and value:", dct)
dct.update({"new_key": "update_value"})
print("update value for key:", dct)