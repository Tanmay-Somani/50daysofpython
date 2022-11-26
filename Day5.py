def my_discount():
    price = int(input("Enter the price of the product: "))
    discount = int(input("Enter the user discount"))
    price_a_d = price-(price*(discount/100))
    return price_a_d


print(my_discount())
