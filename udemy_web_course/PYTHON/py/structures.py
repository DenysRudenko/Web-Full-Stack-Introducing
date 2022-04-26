number_list = [32, 21, 48, 34.56]
print(number_list)

some_list = [12, 35.334, 'hello']
print(some_list)
print(len(some_list))
print(some_list[1])

another_list = some_list[:2]
print(another_list)

some_list[2] = "hi"
print(some_list)

new_list = some_list + another_list
print(new_list)

#---> Adding items

#new_list[5] = "new item"
new_list.append("new item")
print(new_list)

new_list.insert(0, "start")
print(new_list)

#---> Removing items

new_list.pop()
print(new_list)

#---> Sorting items

number_list = [54, 12, 3, -455]
letter_list = ['s', 't', 'a', 'r']

number_list.sort()
letter_list.sort()

print(number_list)
print(letter_list)