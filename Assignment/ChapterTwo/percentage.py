principal = input("Enter the principal: ")

principal = float(principal)

rate = input("Enter the rate: ")

rate = float(rate)

duration = input("Enter the duration: ")

duration = int(duration)

print("Monthly payment", principal * (rate * (1 + rate) ** duration) / ((1 + rate) ** duration - 1))
