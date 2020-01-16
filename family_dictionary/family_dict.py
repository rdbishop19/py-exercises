my_family = {
    "sister": {
        "name": "Emily",
        "age": 33,
    },
    "mother": {
        "name": "Becky",
        "age": 59,
    },
    "father": {
        "name": "Dale",
        "age": 60,
    }
}

for relation, person in my_family.items():
    print(f'{person["name"]} is my {relation} and is {person["age"]} years old')