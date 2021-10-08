import random

test_seed = int(input('Create a seed number: '))
random.seed(test_seed)

nameAsCSV = input("Give me everybody's names, seperated by coma. ")
names = nameAsCSV.split(', ')

# Get the total number of items in list.
# num_item = len(names)

# Generate random number between 0 and the last index.
# random_choice = random.randint(0, num_item-1)
# person_who_will_pay = names[random_choice]

person_who_will_pay = random.choice(names)

print(person_who_will_pay + " is going to buy the meal today!")
