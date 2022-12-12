#!/usr/bin/env python3
# Created by: Minab Berhane
# Created on: Dec. 12, 2022
# This program asks the user for their address
# then re-prints it in proper format.


# properly formats an address following the Canadian post standard
def format_address(name, question, street_num, street_name, city,
                   province, postal_code, apt_num=None):
    # format strings and sets them as uppercase
    can_post_address = name.upper() + "\n" + street_num + " " \
                       + street_name.upper() + "\n" + city.upper() \
                       + " " + province.upper() + " " + postal_code.upper()

    # adds apt number if user lives in an apartment
    if question == "y":
        can_post_address = name.upper() + "\n" + apt_num \
                           + "-" + street_num + " " + street_name.upper() \
                           + "\n" + city.upper() + " " + province.upper() \
                           + " " + postal_code.upper()
        return can_post_address
    # copies the format to the main function
    return can_post_address


# gets input from user and displays the address
def main():
    apt_num_user = None

    # display opening message
    print("This program creates an address to a Canadian mailing address!")
    print("")

    # gets input from the user
    full_user = input("Enter your full name: ")
    question_user = input("Do you live in an apartment? (y/n): ")

    # check if user lives in an apartment
    if question_user == "y":
        apt_num_user = input("Enter your apartment number: ")

    # gets input from the user
    street_num_user = input("Enter your street number: ")
    street_name_user = input("Enter your street name and "
                             "type (Main St., Flower Cres., etc.): ")
    city_user = input("Enter your city: ")
    province_user = input("Enter your province (as an abbreviation "
                          "i.e ON, AB, etc.): ")
    postal_user = input("Enter your postal code (i.e A1B 2C3): ")

    # assigns varaible to function that formats the address
    if apt_num_user is not None:
        user_address = format_address(full_user, question_user,
                                      street_num_user, street_name_user,
                                      city_user, province_user,
                                      postal_user, apt_num_user)
    else:
        user_address = format_address(full_user, question_user,
                                      street_num_user, street_name_user,
                                      city_user, province_user,
                                      postal_user)
    print("")
    print("Your Canadian mailing address is:\n")
    print(user_address)


if __name__ == "__main__":
    main()