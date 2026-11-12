import random

number = random.randint(1, 100)
points = 200
attempts = 0

print("¡Welcome to the guess the number game!")

while True:
    answer = int(input("Guess the number (1-100): "))
    attempts += 1
    points -= 10

    if answer < number:
        print("¡¡You Failed!! The number is higher ↑")
    elif answer > number:
        print("¡¡You Failed!! The number is lower ↓")
    else:
        print("¡¡CORRECT!! 🎉")
        print(f"Total attempts: {attempts}")
        print(f"Your final score is: {points}")
        break  # Breacks the cycle and ends the game

    print(f"Current attempts: {attempts} | Current score: {points}\n")
