nums = []

reruns = int(input("HI!Give me how many item you need to the list: "))

print("OK, start")

try:
    for el in range(reruns):
        W_type = input("Type: (floating/integer/string) ")

        if W_type == "integer":
            num = int(input("Your int num: "))
            nums.append(num)

        elif W_type == "floating":
            num = float(input("Your float num: "))
            nums.append(num)

        elif W_type == "string":
            num = input("Your string: ")
            nums.append(num)

except ValueError:

    print()
    print("The type doesn't match:")


finally:
    print(nums)