capitals_dict = {
"Alberta": "Edmonton",
"British Columbia": "Victoria",
"Manitoba": "Winnipeg",
"New Brunswick": "Fredericton",
"Newfoundland and Labrador": "St. John's",
"Nova Scotia": "Halifax",
"Ontario": "Toronto",
"Prince Edward Island": "Charlottetown",
"Quebec": "Quebec City",
"Saskatchewan": "Regina",
"Yukon": "Whitehorse",
"Nunavut": "Iqaluit",
"Northwest Territories": "Yellowknife",
}

import random

while True:
    province = random.choice(capitals_dict.keys())
    capital = capitals_dict[province]
    capital_guess = raw_input("What is the capital of " + province + "? ")
    if capital_guess == "Exit":
        print "Goodbye"
        break

    if capital_guess == capital:
        print "Correct! Nice job."
    else:
        print "Incorrect. The capital of " + province + " is " + capital + "."
