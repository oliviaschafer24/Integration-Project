"""
A program that calculates and provides information about
the game 'Stardew Valley'

Sources: https://www.stardewvalleywiki.com/Stardew_Valley_Wiki
"""

__author__ = "Olivia Schafer"


def main():  # main function definition
    """
Defines the main function that introduces the user to the the program
    """
    print("Hello, user!",
          end=' ')
    # end=' ' allows the next print statement to be on the same line
    # with a space in between
    print("Welcome to", "Stardew Valley Stats and Info! ",
          sep='... ')  # sep=' ' puts a ... where the first comma is
    input("Press 'Enter' to get started. ")


if __name__ == "__main__":
    main()

# Counters

total_skips = 0
total_readthroughs = 0
invalid_skip_inputs = 0

# Player Options (Customization)

print(
    "\n~Player Creation Customization~\n")  # \n starts the print
# statement on the next line

read_customization = True
skip_customization = None

while read_customization is True:
    # while loop to repeat the prompt if the user input is invalid
    try:
        skip_customization = float(input(
            "Skip the Player Creation Customization section? "
            "(Enter 1 to read through, or enter any other number to skip): "))
        read_customization = False
    except:
        print("Your input was invalid. Please try again.\n")
        invalid_skip_inputs += 1  # shortcut operator to add to a total count


# Base Customization

def customization():
    """
Defines the customization function definition that shows all of the game's
start-up customization options, along with the total number of combinations
     """

    print("\n// Base Customization")

    genders = 1 + 1  # add (+) 1 (boy) and 1 (girl) to get 2
    skin_tones = 24
    hairstyles = 73
    shirts = 112
    pants = 24 % 5  # use modulus (%) to find 24 divided by
    # 5 has a remainder of 4
    accessories = 20
    animals = 6

    print("\nNumber of genders: ",
          format(genders, '21d'))  # format 'd' aligns numbers to the right
    print("Number of skin tones: ", format(skin_tones, '18d'))
    print("Number of hairstyles: ", format(hairstyles, '18d'))
    print("Number of shirts: ", format(shirts, '22d'))
    print("Number of pants: ", format(pants, '23d'))
    print("Number of accessories: ", format(accessories, '17d'))
    print("Number of animals (3 dogs and 3 cats): ", animals)

    base_cc_options = genders * skin_tones * hairstyles * shirts * pants * \
        accessories * animals  # multiply (*) #
    # of base customizations to find the total
    print("\nThe total number of base player customization options is",
          base_cc_options, end='.')

    input("\n\nPress 'Enter' to continue. ")

    # Color Customization

    print("\n// Color Customization")

    print("\nHue Options: ", format(int(10000 / 100),
                                    '26d'))
    # divide( /) 10000 by 100 to get 100
    print("Saturation Options: ",
          format(10001 // 100, '19d'))  # divide and round down (//) to get 100
    print("Value/Brightness Options:",
          format(150 - 50, '14d'))  # subtract (-) 50 from 150 to get 100

    color_options = 100  # includes hue, saturation, and brightness
    color_vals_total = color_options ** 3  # exponent of 100 to the power of 3
    # (**)(100 color values for three categories: hue, saturation,
    # and brightness)
    print("\nNumber of eye color options:  ", format(color_vals_total, '9d'))

    hair_color_cc_options = hairstyles * color_vals_total
    print("Number of hair color options:  ", hair_color_cc_options)

    pants_color_cc_options = pants * color_vals_total
    print("Number of pants color options:  ", pants_color_cc_options)

    all_color_total = color_vals_total * hair_color_cc_options * \
        pants_color_cc_options
    print("\nThe number of color options is", all_color_total,
          end='.')  # 'color_val_total' also represents eye color options
    # since there aren't any base eye options

    input("\n\nPress 'Enter' to continue. ")

    # Total Customization

    print("\n// Total Customization Options")

    customization_total = all_color_total * base_cc_options
    print("\n" + ">" * 3,
          "The total number of player customization options is",
          customization_total,
          end='.' + "\n")  # string operators (+ and *) attaches (adds) '\n'
    # to '>' which is repeated (multiplied) 3 times


if skip_customization == 1:  # standard conditional structures -
    # if-else, relational operator (==)
    customization()
    total_readthroughs += 1
else:
    total_skips += 1
    print("\nPlayer Customization section skipped.")

input("\nPress 'Enter' to continue. ")

# Farm Options

print("\n~Farm Options~\n")

read_farm_options = True
skip_farm_options = None

while read_farm_options is True:  # while loop to repeat the prompt if the
    # user input is invalid
    try:
        skip_farm_options = float(input(
            "Skip the Farm Options section? "
            "(Enter 1 to read through, or enter any other number to skip): "))
        print(" ")
        read_farm_options = False
    except:
        print("Your input was invalid. Please try again.\n")
        invalid_skip_inputs += 1

standard_farm_info = "Standard Farm: Original farm map, favors farming skill."
forest_farm_info = "Forest Farm: Woody farm map, favors foraging skill."
hilltop_farm_info = "Hilltop Farm: Rocky farm map, favors mining skill."
riverland_farm_info = "Riverland Farm: Water-filled farm map, " \
                      "favors fishing skill."
wilderness_farm_info = "Wilderness Farm: Monster-filled (at night) " \
                       "farm map, favors combat skill."
four_corners_farm_info = "Four Corners Farm: Split farm map, " \
                         "intended for multiplayer."
beach_farm_info = "Beach Farm: Sandy farm map for veteran players, " \
                  "favors foraging and fishing skills."


def farm_options():
    """
Defines the farm options function which explains the different farms
available in the game
    """

    read_farm_list = True

    farms_list = ['End', 'Standard Farm', 'Forest Farm', 'Hilltop Farm',
                  'Riverland Farm', 'Wilderness Farm', 'Four Corners Farm',
                  'Beach Farm']
    for num in range(
            len(farms_list)):  # for x in range to loop a sequence
        # of the length of items in farms_list
        print(num, "-", farms_list[num])

    while read_farm_list is True:
        try:
            which_farm = float(input(
                "Which farm map would you like to know more about? "
                "(Enter the number corresponding to each farm; ex: 4): "))
            if which_farm > 7 or which_farm < 0:  # 'or' and 'and'
                # are boolean operators, > and < are relational operators
                print("Invalid number. Please try again.\n")
            elif 0 < which_farm < 8:
                farm_number = which_farm  # passing argument
                # from which_farm to farm_number
                if farm_number == 1:
                    print("\n" + standard_farm_info + "\n")
                elif farm_number == 2:
                    print("\n" + forest_farm_info + "\n")
                elif farm_number == 3:
                    print("\n" + hilltop_farm_info + "\n")
                elif farm_number == 4:
                    print("\n" + riverland_farm_info + "\n")
                elif farm_number == 5:
                    print("\n" + wilderness_farm_info + "\n")
                elif farm_number == 6:
                    print("\n" + four_corners_farm_info + "\n")
                elif farm_number == 7:
                    print("\n" + beach_farm_info + "\n")
                else:
                    print("Invalid number. Please try again.\n")
            else:
                read_farm_list = False
        except:
            print("\n Your input was invalid. Please try again.")


if skip_farm_options == 1:  # standard conditional structures -
    # if-else, relational operator (==)
    farm_options()
    total_readthroughs += 1
else:
    total_skips += 1
    print("Farm Options section skipped.")

# '!=' relational operator
if total_skips != 0:
    print("You've skipped at least one section")

# 'not' Boolean operator
count = 0
if total_skips is not count:
    print("You've skipped at least one section")