if __name__ == "__main__":

    # Part one of list_lab: adding to lists and choosing answers
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]

    print fruits

    input_fruit1 = raw_input("Choose a fruit to add to the list: ")

    fruits.append(input_fruit1)

    print "You now have these fruits"

    print fruits

    while True:
        fruit_query = raw_input("Pick a number of one of your fruits: ")
        if fruit_query.isdigit() is False:
            print "Please enter an integer"
        elif int(fruit_query) == 0:
            print "You have more than 0 fruits, enter a number!"
        elif int(fruit_query) > len(fruits):
            print "Your number is too high!"
        else:
            print fruit_query
            print fruits[int(fruit_query) - 1]
            break

    print fruits

    input_fruit2 = raw_input("Choose another fruit to add to the list: ")

    fruits2 = [input_fruit2]
    fruits += fruits2
    print fruits

    input_fruit3 = raw_input("Choose a third fruit!: ")

    fruits.insert(0, input_fruit3)
    print fruits

    print "Displaying fruits that start with 'P'"

    for item in fruits:
        if item[0] == "P":
            print item
        elif item[0] == "p":
            print item
        else:
            pass

    # Part 2 of list_lab: deleting items from lists

    print fruits

    print "Deleting the last fruit"

    fruits.pop()

    print fruits

    fruit_del = raw_input("Pick a fruit to get rid of: ")

    for items in fruits:
        if items == fruit_del:
            fruits.remove(fruit_del)
        else:
            pass

    print fruits

    #Part 3 of list_lab (Do you like?: yes or no)

    print fruits

    new_fruits = []

    for items in fruits:
        while True:
            fruit_answer = raw_input("Do you like %s?: " % (items))
            if fruit_answer.lower() == "yes":
                new_fruits.append(items)
                print "Great!"
                pass
                break
            elif fruit_answer.lower() == "no":
                print "That's a shame"
                break
            else:
                print "Please answer yes or no"
        fruits = new_fruits

    print fruits

    #Part 4 of list_lab: copying lists, reversing letters, deleting

    fruits_copy = list(fruits)

    def rev_list(mylist):
        new_list = []
        for items in mylist:
            items = items[::-1]
            new_list.append(items)
        print new_list

    print rev_list(fruits_copy)
    print fruits

    fruits.pop()
    print fruits
    print rev_list(fruits_copy)
