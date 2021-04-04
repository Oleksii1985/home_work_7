from collections import Counter

# Task 1
dict_ = {"name": "Oleksii", "surname": "Voitiuk", "age": 36, "gender": "male", "phone": "0967618604"}
print("dict_:", dict_)
print("id dict_:", id(dict_))
first = list(dict_.items())[0]
second = list(dict_.items())[1]
last = list(dict_.items())[-1]
dict_[first[0]], dict_[last[0]] = last[1], first[1]
print("dict_:", dict_)
print("id dict_:", id(dict_))
dict_.pop(second[0])
print(dict_)
print(id(dict_))
dict_["new_key"] = "new_value"
print(dict_)
print(id(dict_))

# Task 2
student = {"name": "Emma", "class": 9, "marks": 75}
print(student.get("marks"))

# Task 3,4
p = {"name": "Mike", "salary": 8000}
print(p.get("age"))
# Answer: None

# Task 5
sample = {"1": ["a", "b"], "2": ["c", "d"]}
print(sample["2"][1])

# Task 6
list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
list_2 = ["Киев", "Токио", "Минск"]
list_ = []
for elem in list_1:
    if "Киев" in elem or "Токио" in elem or "Минск" in elem:
        list_.append(elem)
new_list = [element for item in list_ for element in item.split("-")]
dict_ = dict(zip(new_list[::2], new_list[1::2]))
print(dict_)

# Task 7
choice_method = input("Please enter your choice encrypt or decrypt ('e'/'d'): ")
keys = {
    'a': "!", 'b': "z", 'c': "y", 'd': "x", 'e': "w", 'f': "v",
    'g': "u", 'h': "t", 'i': "s", 'j': "r", 'k': "q", 'l': "p",
    'm': "o", 'n': "-", 'o': "n", 'p': "m", 'q': "l", 'r': "k",
    's': "j", 't': "i", 'u': "1", 'v': "2", 'w': "3", 'x': "4",
    'y': "5", 'z': "6", ' ': "7"
}
if choice_method == "e":
    message = input("Please enter a message for encrypt: ")
    cipher_text = []
    message = list(message)
    for symbol in message:
        for key in keys:
            if key == symbol:
                cipher_text.append(keys[key])
    print(cipher_text)
elif choice_method == "d":
    message = input("Please enter code for decrypt: ")
    normal_text = []
    reverse_keys = {value: key for key, value in keys.items()}
    message = list(message)
    for symbol in message:
        for key in reverse_keys:
            if key == symbol:
                normal_text.append(reverse_keys[key])
    print(normal_text)
else:
    print("You put incorrect value!")

# Task 8
dict_ = {key: key ** 3 for key in range(1, 11)}
print(dict_)

# Task 9
check_string = "gfalkglakgjklgkahjk"
result = Counter(check_string)
print("result is: ", result)
