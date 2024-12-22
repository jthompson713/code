import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']

results = random.choices(symbols, k=3)

def check_jackpot(results):
    return results[0] == symbols[3] and results[1] == symbols[3] and results[2] == symbols[3]

def play_again():
    return input("Want to try your luck again? (y/n): ").lower().startswith('y')

def play():
    results = random.choices(symbols, k=3)
    print(results[0], '|', results[1], '|', results[2])
    return results

playing = True
while playing:
    current_spin = play()
    if check_jackpot(current_spin):
        print('🎰 JACKPOT! Congratulations, you won! 🎰')
        playing = play_again()
    else:
        playing = play_again()

print('Thanks for playing! Come back soon! 👋')