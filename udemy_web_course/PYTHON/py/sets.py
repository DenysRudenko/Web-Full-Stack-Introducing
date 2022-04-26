from cgitb import text


rainbow_colors = {'red', 'orange', 'yellow', 'blue', 'indigo', 'violet'}

print(rainbow_colors)
print(type(rainbow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 43, 56]
text_tuple = ('abrakadabra')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(777)
set_from_tuple.add("Hello")

print(set_from_list)
print(set_from_tuple)

set_from_list.pop
set_from_tuple.remove
