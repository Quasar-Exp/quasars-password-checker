import string
import os

while True:
    password = input("Enter the password : ")
    score = 0

    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])

    characters = [upper_case, lower_case, special, digits]

    length = len(password)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    rockyou_path = os.path.join(script_dir, "rockyou.txt")

    with open(rockyou_path, 'r', encoding='latin-1', errors='ignore') as f:
        rockyou = f.read().splitlines()

        common_path = os.path.join(script_dir, "common.txt")

        with open(common_path, 'r', encoding='latin-1', errors='ignore') as f:
            common = f.read().splitlines()

        if password in rockyou or password in common:
            print("Password is in a common password list. Score: 0")
            continue

    if length > 7:
        score += 1

        if length > 12:
            score += 1

            if length > 16:
                score += 1

                if length > 20:
                    score += 1
    print(f"Password length is {str(length)}, adding {str(score)} points!")

    if sum(characters) > 1:
        score += 1
        if sum(characters) > 2:
            score += 1
            if sum(characters) > 3:
                score += 1
    print(f"Characters used: {str(sum(characters))}, different character types, adding {str(sum(characters) - 1)} points!")

    if score < 4:
        print(f"Bad password, restart completely. Score: {str(score)} / 7")
    elif score == 4:
        print(f"Needs improvement. Score: {str(score)} / 7")

    elif score > 4 and score < 7:
        print(f"Now this is a good password, but could use some work. Score: {str(score)} / 7")

    elif score > 6 and score < 9:
        print(f"Oh wow look, now you have a strong password! Score: {str(score)} / 7")

    print("Final Score:", score)

    again = input("Another Chance To Redeem Yourself? (yes/no): ").strip().lower()
    if again != "yes":
        print("Exiting program.")
        break
