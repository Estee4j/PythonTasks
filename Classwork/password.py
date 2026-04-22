#  take your input
# the password variation must be strong.
# must be 8-16 lines long
# could have characters if you chose to add
# pasword should display very weak if the length is short, should display weak if it comprises of just numbers that are too common, should display strong if you mix it with characters and letters, and should display very strong if it is over 16 length long mixed with characters, symbols and numbers..



password =(input ("users password: "))

password_length = len(password)


if (password_length < 8):
    print("very weak password")
elif (password_length == 8):
    print("weak password")
elif (password_length > 8 and password_length < 16):
    print("strong password")
elif (password_length > 16):
    print("very strong password")
