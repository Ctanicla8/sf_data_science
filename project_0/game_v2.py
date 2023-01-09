"""Game: guess the number.
The computer guesses and guesses the numbers.
"""

import numpy as np

def random_predict(number:int=1)->int:
    """The computer randomly guesses a number.

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return (count)

def score_game(random_predict)->int:
    """For how many attempts on average out of 1000 approaches does our algorithm guess the number.

    Args:
        random_predict ([type]): Guessing function.

    Returns:
        int: Average attempts.
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Your algorithm guesses the number in {score} attempts on average.')
    return(score)

#RUN
if __name__ == '__main__':
    score_game(random_predict)