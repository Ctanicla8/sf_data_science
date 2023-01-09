"""Game: guess the number"""

import numpy as np

number = np.random.randint(1, 101)
count = 0
while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100.'))
    if predict_number > number:
        print('The number must be less!')
    elif predict_number < number:
        print('The number must be greater!')
    else:
        print(f"You guessed the number! This number is {number}, for {count} attempts.")
        break