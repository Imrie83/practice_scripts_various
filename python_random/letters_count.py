import sys

file_name = sys.argv[1]
count = 0
with open(file_name) as f:
    text = f.read()

    for letter in text:
        if letter.isupper():
            count += 1

print(count)
