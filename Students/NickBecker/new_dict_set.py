food_prefs = {"name": u"Cris",
              u"city": u"Seattle",
              u"cake": u"lemon",
              u"fruit": u"pomegranate",
              u"salad": u"chop",
              u"pasta": u"lasagna"}

print "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta".format(**food_prefs)

#Add in keys from values!

hex_list = dict((num, hex(num)) for num in range(16))

print hex_list

hex_dict = {item: hex(item) for item in range(16)}

print hex_dict

food_new = dict(food_prefs)

for key in food_new:
    food_new[key] = food_new[key].count("a")

print food_new

s2 = {nums for nums in range(21) if nums % 2 == 0}

print s2

s3 = {nums for nums in range(21) if nums % 3 == 0}

print s3

s4 = {nums for nums in range(21) if nums % 4 == 0}

print s4


def int_mod(new_mod=4):
    new_list = []
    for items in range(1, new_mod):
        new_list.append({nums for nums in range(21) if nums % items == 0})
    return new_list


print int_mod(5)
