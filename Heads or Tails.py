import random

test_seed = int(input('Create a seed number: '))
random.seed(test_seed)

random_side = random.randint(0, 1)

if random_side == 1:
    print('Heads')
elif random_side == 0:
    print('Tails')
else:
    print('Error!')