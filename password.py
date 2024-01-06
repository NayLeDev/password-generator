import random
import string

def calculate_score(password):
    score = 0
    score += len([c for c in password if c.isalpha()]) * 10
    score += len([c for c in password if c in "!#%"]) * 20
    score -= abs(8 - len(password)) * 5
    return min(max(score, 0), 100)

choice = input("Do you want to include a word in your password? (yes/no) ")
if choice.lower() == "yes":
    word = input("Enter the word to include: ")
else:
    word = ""

characters = string.ascii_letters + string.digits + "!#%"

password = list(word + "".join(random.choices(characters, k=8-len(word))))
random.shuffle(password)

password = "".join(password)
print("Your password is: " + password)

score = calculate_score(password)
print("Your password security score is: " + str(score) + "%")

