import random
def roll_2():
    six=[1,2,3,4,5,6]
    die1 = random.choice(six)
    die2 = random.choice(six)
    total = die1 + die2
    print 'Clickety clack!/n',die1, '+', die2, '=', total