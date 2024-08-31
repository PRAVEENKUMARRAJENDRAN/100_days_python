from random import randint

dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1,6)
if dice_num < len(dice_images):
    print(dice_images[dice_num])