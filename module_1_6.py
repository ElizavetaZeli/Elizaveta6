my_dict = {"Elizaveta": 2003, "Roman": 2000, "Ivan": 1972 }
print(my_dict)
print(my_dict.get("Elizaveta"))
print(my_dict.get("Tihon", "Нет такого ключа"))
my_dict["Olga"] = 1979
my_dict["Molly"] = 2009
a = my_dict.pop("Roman")
print(a)
print(my_dict)
my_set = {1, 2, 3, "peach", 3, "coconut"}
print(my_set)
my_set.add(4)
my_set.add("apple")
my_set.discard(1)
print(my_set)