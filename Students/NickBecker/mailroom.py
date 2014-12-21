#!/usr/bin/env python

from safe_input import safe_input

Donors = {
    "Alan Grant": [100, 500],
    "Dennis Nedry": [10, 50, 5],
    "John Hammond": [10000],
    "Ian Malcolm": [300, 600],
    "Ellie Sattler": [450, 50]
}


def thank_you(name, amount):
    """Print a thank you note including the donations from a given donor"""
    print ""
    print "Dear %s," % (name)
    print "Thank you so much for your generous donation!"
    print ""
    print "We will put the amounts of "
    print amount
    print "to excellent use."
    print ""
    print "We look forward to your generosity in the future"
    print ""


def create():
    """Create a report based on amounts given by each donor"""
    print "\n"
    for name in Donors:
        print name, (Donors[name]), sum(Donors[name])
    print "\n"

    title = [u"{:20}".format(u"Name")]
    title.append(u"{:12}".format(u"Total"))
    title.append(u"{:14}{:12}".format(u"Donations", u"Average"))
    print u" ".join(title)

    sorting = list()
    for name in Donors:
        sorting.append(name)

    for donor_name in sorted(sorting, key=lambda individual: sum(Donors[individual]), reverse=True):
        print "{: <20}".format(donor_name),
        print "{: <16}".format(sum(Donors[donor_name])),
        print "{: <9}".format(len(Donors[donor_name])),
        print "{: <11}".format(sum(Donors[donor_name]) / len(Donors[donor_name]))
    print "\n\n\n\n"
    print "Send a Thank You (S)"
    print "Create a Report (C)"
    print "Quit (Q)"


def new_donation(name):
    """Create a new donor and input a value, or add a value to an existing donor"""
    donations = []
    total = 0
    while total >= 0:
        new_donation = safe_input("Please enter a donation or type B to move back: ")
        if new_donation.lower() == "quit":
            main_menu()
        elif new_donation.lower() == "b":
            total = -1
        try:
            total = int(new_donation)
            if total > 0:
                donations.append(total)
        except:
            total = 0
        if name not in Donors:
            Donors[name] = donations
            total = -1
        elif new_donation.lower() == "b":
            total = -1
        else:
            Donors[name] = donations + Donors[name]
            total = -1
    letter = safe_input("Would you like to print this letter? (Y/N): ")
    if letter.lower() == "y":
        print thank_you(name, Donors[name])
    elif letter.lower() == "quit":
        main_menu()


def list_donors():
    """List all current donors and their donation amounts"""
    for key in Donors:
        print key, Donors[key]
    print "\n"


def main_menu():
    """Main hub for moving between writing a thank you or creating a report"""
    print "Send a Thank You (S)"
    print "Create a Report (C)"
    print "Quit (Q)"
    while True:
        main_menu = safe_input("Choose an option from above: ")
        if main_menu.lower() == "q":
            break
        elif main_menu.lower() == "c":
            create()
        elif main_menu.lower() == "s":
            while True:
                print "List Donors (L)"
                print "Enter a Donor Name"
                print "Return to Main Menu (R)"
                thanks_choice = safe_input("Please choose from above: ")
                if thanks_choice.lower() == "l":
                    list_donors()
                elif thanks_choice.lower() == "q":
                    print "Send a Thank You (S)"
                    print "Create a Report (C)"
                    print "Quit (Q)"
                    break
                elif thanks_choice.lower() == "r":
                    print "Send a Thank You (S)"
                    print "Create a Report (C)"
                    print "Quit (Q)"
                    break
                else:
                    new_donation(thanks_choice)
        else:
            print "Please reselect"

if __name__ == "__main__":
    main_menu()
