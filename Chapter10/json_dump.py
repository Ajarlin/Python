import json

numbers = [0,1,1,2,3,5,8]
filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)


with open(filename) as f:
    numbers = json.load(f)

print(numbers)
