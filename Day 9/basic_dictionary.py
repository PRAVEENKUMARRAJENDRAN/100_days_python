
my_dict = dict()

my_dict["name"] = "praveen"
my_dict["age"] = 25
my_dict["profession"] = "Data Engineer"
my_dict["high_degree"] = "Phd in Data Management"

print(my_dict)

for index, (key, value )in enumerate(my_dict.items()):
    if key == "name":
        print(f"Hi! I'm {value}")
    elif key == "age":
        print(f"I'm {value} years old.")
    elif key == "profession":
        print(f"I'm a {value}.")
    else:
        print(f"I have done {value}.")
