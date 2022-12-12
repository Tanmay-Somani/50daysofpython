def your_vat():
    try:
        price = int(input("Enter the price of the item"))
        VAT = float(input("Enter the VAT of the product"))
        perc = (price*VAT/100)
        total = price+(perc)
        return total
    except ValueError:
        print("Invalid entry please enter again")
        your_vat()


print(your_vat())
