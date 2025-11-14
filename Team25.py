import random

def play_round(my_history, their_history, my_score, their_score):
    "Strategy with printed output + randomness."

    high_count = 0

    print("Analyzing opponent history:", their_history)

    
    for num in their_history:
        print("Checking number:", num)
        if num > 50:
            print(" → This number is high!")
            high_count += 1

    print("Total high numbers:", high_count)

  
    random_choice_if_high = random.choice(['b', 'c'])
    random_choice_if_low = random.choice(['b', 'c'])

  
    if high_count > len(their_history) / 2:
        print("More than half were high → Random choice:", random_choice_if_high)
        return random_choice_if_high
    else:
        print("Half or fewer were high → Random choice:", random_choice_if_low)
        return random_choice_if_low

my_history = []
their_history = [10, 60, 20, 5]  
my_score = 0
their_score = 0

result = play_round(my_history, their_history, my_score, their_score)

print("Opponent history:", their_history)
print("My decision:", result)
