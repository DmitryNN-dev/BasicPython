numbers = [5, 7, 10]

numbers.append(100)
print("add to the end of the list:", numbers)

numbers.insert(1, 17)
print("add new number by index:", numbers)

numbers.extend([9, 11, 4])
print("add to the end:", numbers)

numbers.sort()
print("sorted:", numbers)

numbers.reverse()
print("reverse:", numbers)

numbers.pop()  # deleting by index (by default the last item)
print("delet last item", numbers)
numbers.pop(2)
print("delet '11':", numbers)

numbers.remove(9)  #remove item if it was found
print("remove '9':", numbers)

# numbers.clear()  #clear the numbers list
# print("clear list:", numbers)
print()

count1 = numbers.count(100)  # it can help count item
print("count item '100' in this list:", count1)
numbers.append(100)
print("add item to the list", numbers)
print("count item '100' in this list:", numbers.count(100))
print()

print("how many item of the list?:", len(numbers))