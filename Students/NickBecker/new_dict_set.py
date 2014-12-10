food_prefs = {"name": u"Cris",
              u"city": u"Seattle",
              u"cake": u"lemon",
              u"fruit": u"pomegranate",
              u"salad": u"chop",
              u"pasta": u"lasagna"}

print "{name} is from {city}, and he likes {cake}, {fruit}, {salad}, and {pasta}".format(**food_prefs)

#Add in keys from values!

bin_list = [x for x in range(16)]

hex_list = [chr(x) for x in range(16)]

hex_dict = {bin_num: hex_num for bin_num, hex_num in zip(bin_list, hex_list)}

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

sets = set(range(21))

#Add in final set!
