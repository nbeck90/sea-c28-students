new_dict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print new_dict

del new_dict["cake"]
print new_dict

new_dict.update({"fruit": "Mango"})

for keys in new_dict.keys():
    print keys

for values in new_dict.values():
    print values

print "cake" in new_dict

print "Mango" in new_dict.values()

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

hex1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

hex_dict = dict(zip(numbers, hex1))

print hex_dict

new_dict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

for key in new_dict:
    new_dict[key] = new_dict[key].count("a")

print new_dict

s2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
s3 = {3, 6, 9, 12, 15, 18}
s4 = {4, 8, 12, 16, 20}

print s2
print s3
print s4

print s3.issubset(s2)
print s4.issubset(s2)

pyset = {"P", "Y", "T", "H", "O", "N"}

pyset.update({"I"})

print pyset

fro_set = frozenset(("M", "A", "R", "A", "T", "H", "O", "N"))

print fro_set.union(pyset)

print fro_set.intersection(pyset)
