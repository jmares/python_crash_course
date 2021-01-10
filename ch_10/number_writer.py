import json

numbers = [2, 3, 4, 5, 6, 7, 11, 13]

filename = "numbers.json"
with open(filename, 'w') as f:
    json.dump(numbers, f)