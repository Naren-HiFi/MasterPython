first_name = input("Enter your first name: \n")
last_name = input("Enter your last name: \n")
def format_name(first_name,last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide the valid inputs."
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"The full name of the user is {formatted_first_name} {formatted_last_name}"

formatted_string = format_name(first_name,last_name)
print(formatted_string)