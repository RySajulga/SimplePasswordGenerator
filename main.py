import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRST"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},.;:/\!?+-_*&^%$#@"

# Change to disable/enable parts of the password generator
upper, lower, nums, syms = True, True, True, True

all = " "

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 20
amount = 10



for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)