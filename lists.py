food = ["apple", "coconut", "banana"]
food.append(True)
food.extend(['string', 12])

print(food)
print("coconut" not in food)
food.remove("apple")
print("apple" in food)

