
my_dict = dict()

my_dict["name"] = "praveen"
my_dict["age"] = 25
my_dict["profession"] = "Data Engineer"
my_dict["high_degree"] = "phd"

print(my_dict)

for index, (key, value )in enumerate(my_dict.items()):
    print(key, value)