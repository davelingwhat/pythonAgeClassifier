"""This is my first demo project, taken from Chapter 3, Problem 3 in the 'starting out with Python' textbook.
The following program asks for the user to input their age and returns a message stating whether they are an
infant, a child, a teenager, or an adult.

Author: David Whatcott"""

min_infant_age = 0
min_child_age = 1
min_teenager_age = 13
min_adult_age = 20


def classification(age):
    "This function takes the user's age input and assigns that age to one of the four age groups."
    if age < min_child_age:
        return "an infant"
    elif age < min_teenager_age:
        return "a child"
    elif age < min_adult_age:
        return "a teenager"
    else:
        return "an adult"


def main():
    age = int(input("What is your current age in years? "))
    age_group = classification(age)

    while age < 0:
        print("This is not a valid age.")
        age = int(input("What is your current age in years? "))
    print(f"You are currently {age_group}.")


if __name__ == '__main__':
    main()