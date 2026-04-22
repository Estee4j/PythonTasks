## collect the users input
 # if a customer purchases 1,00 to 10,000 worth of item, print the price after discount for 5%
 ##if a customer purchases 10,000 to 50,000 worth of item, print the price after discount for 10%
 #if a customer purchases an item worth over 50,000, print the price after discount for 20%.
## print the result of all of the above and show.




customer = input("total spending in store")
customer = float(customer)
if customer <= 10000:
    discount = customer * 0.05
    print("Discount: ", discount)

elif customer <= 50000:
    discount = customer * 0.10
    print("Discount: ", discount)

elif customer >= 5000:
    discount = customer * 0.20
    print("Discount: ", discount)
