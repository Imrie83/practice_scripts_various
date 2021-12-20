my_string = "taco cat"
my_string_2 = "kajak"
my_string_3 = "taco, cat."
my_string_4 = "?kajak!"


# palindrom recursive
def palindrom_1(str):
    if len(str) <= 1:
        return True
    elif str[0] != str[-1]:
        return False
    else:
        return palindrom_1(str[1:-1])


print(palindrom_1(my_string))
print(palindrom_1(my_string_2))


# ignore capital letters and spaces
def palindrom_2(string):
    string = string.lower().replace(" ", "")
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True


print(palindrom_2(my_string))
print(palindrom_2(my_string_2))


# ignore punctuation
def palindrom_3(stri):
    punctuation = [".", ",", "!", "?"]
    for punk in punctuation:
        stri = stri.replace(punk, "")
    if len(stri) <= 1:
        return True
    elif stri[0] != stri[-1]:
        return False
    else:
        return palindrom_3(stri[1:-1])


print(palindrom_3(my_string_3))
print(palindrom_3(my_string_4))
