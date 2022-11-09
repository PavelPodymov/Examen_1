# array = ["hello", "2", "world", ":-)"]  # ["2", ":-)"]
array = ["1234", "1567", "-2", "computer science"]    # ["-2"]
# array = ["Russia", "Denmark", "Kazan"]  # []

new_array = [i for i in array if len(i) <= 3]
print(new_array)


