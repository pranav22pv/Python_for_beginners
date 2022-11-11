import random

class Dice:
    def roll():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        tuple = (dice1,dice2)             # There's another method to return tuple
        print(tuple)


    roll()


# or

class Dices:
    def rolls(self):
        dices1 = random.randint(1,6)
        dices2 = random.randint(1,6)
        return dices1,dices2    # python interpreter takes it as tuple when u don't give it in () brackets



dice = Dices()
print(dice.rolls())