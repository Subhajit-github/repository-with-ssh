# import random
# generated_number = random.randint(1,100)
# print(generated_number)
# Allow user to guess a number in 7 chances
# if the number guessed by user is greater or smaller than the number generated, notify user about it
# if user correctly guess the number, congraulate user and need to tell in how many guesses it is done
# if not guessed correctly, need to say all chances exhausted
#
# guess_count = 1
# i = 0
# while i < 7:
#     guessed_number = int(input("Enter your Number between 1 to 100: "))
#
#     if i >= 6:
#         print(f"Limit exhausted. There was total {i+1} chances")
#     elif guessed_number > generated_number:
#         guess_count += 1
#         print("Guess Lower")
#     elif guessed_number < generated_number:
#         guess_count += 1
#         print("Guess Higher")
#     elif guessed_number == generated_number:
#         print(f"You guessed it in {guess_count} guesses")
#         break
#     i = i + 1
#
#
from passlib.hash import pbkdf2_sha256
password = "hello"
hashed = pbkdf2_sha256.hash(password)
print(hashed)
if pbkdf2_sha256.verify("hi", hashed):
    print("password matched successfully")
else:
    print("password did not match")





