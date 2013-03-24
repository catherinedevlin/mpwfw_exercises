capitals_dict = {
'Alabama' : 'Montgomery',
'Alaska' : 'Juneau',
'Arizona' : 'Phoenix',
'Arkansas' : 'Little Rock',
'California' : 'Sacramento',
'Colorado' : 'Denver',
'Connecticut' : 'Hartford',
'Delaware' : 'Dover',
'Florida' : 'Tallahassee',
'Georgia' : 'Atlanta',
'Hawaii' : 'Honolulu',
'Idaho' : 'Boise',
'Illinois' : 'Springfield',
'Indiana' : 'Indianapolis',
'Iowa' : 'Des Moines',
'Kansas' : 'Topeka',
'Kentucky' : 'Frankfort',
'Louisiana' : 'Baton Rouge',
'Maine' : 'Augusta',
'Maryland' : 'Annapolis',
'Massachusetts' : 'Boston',
'Michigan' : 'Lansing',
'Minnesota' : 'Saint Paul',
'Mississippi' : 'Jackson',
'Missouri' : 'Jefferson City',
'Montana' : 'Helena',
'Nebraska' : 'Lincoln',
'Nevada' : 'Carson City',
'New Hampshire' : 'Concord',
'New Jersey' : 'Trenton',
'New Mexico' : 'Santa Fe',
'New York' : 'Albany',
'North Carolina' : 'Raleigh',
'North Dakota' : 'Bismarck',
'Ohio' : 'Columbus',
'Oklahoma' : 'Oklahoma City',
'Oregon' : 'Salem',
'Pennsylvania' : 'Harrisburg',
'Rhode Island' : 'Providence',
'South Carolina' : 'Columbia',
'South Dakota' : 'Pierre',
'Tennessee' : 'Nashville',
'Texas' : 'Austin',
'Utah' : 'Salt Lake City',
'Vermont' : 'Montpelier',
'Virginia' : 'Richmond',
'Washington' : 'Olympia',
'West Virginia' : 'Charleston',
'Wisconsin' : 'Madison',
'Wyoming' : 'Cheyenne',
}

import random

while True:
    state = random.choice(capitals_dict.keys())
    capital = capitals_dict[state]
    capital_guess = raw_input("What is the capital of " + state + "? ")
    if capital_guess == "Exit":
        print "Goodbye"
        break

    if capital_guess == capital:
        print "Correct! Nice job."
    else:
        print "Incorrect. The capital of " + state + " is " + capital + "."
