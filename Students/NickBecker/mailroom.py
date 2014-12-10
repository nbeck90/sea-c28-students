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
    for names in Donors:
        print names, Donors[names], sum(Donors[names])

    print '\n\nDonor\t\t\t\tAmount\t\tNumber of Donations\t\tAverage Donation'
    print '-----\t\t\t\t------\t\t-------------------\t\t----------------'

    sorting = list()
    for name in Donors:
        sorting.append(name)

    for donor_name in sorted(sorting, key=lambda individual: sum(Donors[individual]), reverse=True):
        print donor_name,
        if len(donor_name) < 10:
            print "\t\t\t",
        else:
            print "\t\t",
        print sum(Donors[donor_name]),
        print "\t\t\t",
        if len(Donors[donor_name]) > 0:
            print len(Donors[donor_name]),
            print "\t\t\t",
            print sum(Donors[donor_name]) / len(Donors[donor_name])
        else:
            print "0\t\tNA"
    print "\n\n\n\n"
    print "Send a Thank You"
    print "Create a Report"
    print "Quit"


def new_donor(name):
    """Create a new donor and input a value, or add a value to an existing donor"""
    donations = []
    total = 0
    while total >= 0:
        new_donation = safe_input("Please enter a donation or type -1 to move back: ")
        if new_donation.lower() == "quit":
            main_menu()
        else:
            pass
        try:
            total = int(new_donation)
            if total > 0:
                donations.append(total)
        except ValueError:
                print "Please input a number"
                total = 0
        if name not in Donors:
            Donors[name] = donations
            total = -1
        else:
            Donors[name] = donations + Donors[name]
            total = -1
    letter = safe_input("Would you like to print this letter?: ")
    if letter.lower() == "yes":
        print thank_you(name, Donors[name])
    elif letter.lower() == "quit":
        main_menu()
    else:
        pass


def list_donors():
    """List all current donors and their donation amounts"""
    for key in Donors:
        print key, Donors[key]


def main_menu():
    """Main hub for moving between writing a thank you or creating a report"""
    print "Send a Thank You"
    print "Create a Report"
    print "Quit"
    while True:
        main_menu = safe_input("Choose an option from above: ")
        if main_menu.lower() == "quit":
            break
        elif main_menu.lower() == "create a report":
            create()
        elif main_menu.lower() == "send a thank you":
            ThankYou = True
            while ThankYou:
                print "List Donors"
                print "Enter a Donor Name"
                print "Return to Main Menu"
                thanks_choice = safe_input("Please choose from above: ")
                if thanks_choice.lower() == "list donors":
                    list_donors()
                elif thanks_choice.lower() == "quit":
                    print "Send a Thank You"
                    print "Create a Report"
                    print "Quit"
                    ThankYou = False
                elif thanks_choice.lower() == "return to main menu":
                    ThankYou = False
                    print "Send a Thank You"
                    print "Create a Report"
                    print "Quit"
                else:
                    new_donor(thanks_choice)
        else:
            print "Please reselect"

if __name__ == "__main__":
    main_menu()
