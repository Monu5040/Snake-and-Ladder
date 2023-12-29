import random
class Dice :
    def __init__(self,dice_count) :
        self.dice_count = dice_count

    def roll_dice(self) :
        dice_value = 0
        for _ in range(self.dice_count) :
            dice_value = dice_value + random.randint(1,6)
        return dice_value
