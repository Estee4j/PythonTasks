total = 0
while True:
    number = int(input("Enter a number: "))
    total += number 
    if number <= 0:
        print(f"total is {total}")
        break
