def your_vat():
    try:
        price = int(input("Enter the price of the item"))
        VAT = float(input("Enter the VAT of the product"))
        total = price+(price * VAT/100)
        return total
    except ValueError:
        print("invalid entry please enter again")
        your_vat()


print(your_vat())
