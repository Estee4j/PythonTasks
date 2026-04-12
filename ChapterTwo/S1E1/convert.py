seconds = input("enter your seconds: ")

seconds = int (seconds)

hour = seconds // 3600

minutes = (seconds // 3600) % 60

seconds = seconds % 60

print("the time is", hour, "hours", minutes, "minutes", seconds, "seconds")
