word = 'color'
words = ["green", "red", "blue"]

print("word:", word)
print("length of word:", len(word))
print("how many 'o' in this word:", word.count("o"))

print("uppercase:", word.upper())

print("lowercase:", word.lower())

print()
print(" ".join([word1.capitalize() for word1 in words]))
print()

print("find string as resualt give index:", word.find("r"))

print(word.split("l"))

print("revers:", word[::-1])