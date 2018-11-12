#Constants
DE_ANZA_BURGER = 5.25
BACON_CHEESE = 5.75
MUSHROOM_SWISS = 5.95
WESTERN_BURGER = 5.95
DON_CALI_BURGER = 5.95
TAX = 1.09


def main():
    displayMenu()
    takeOrder()
    studentOrStaff()


def displayMenu():
    print("De Anza Burger: $5.25. Enter 1.")
    print("Bacon Cheese: $5.75. Enter 2.")
    print("Mushroom Swiss: $5.25. Enter 3.")
    print("Western Burger: $5.25. Enter 4.")
    print("Don Cali Burger: $5.25. Enter 5.")


def takeOrder():
    quantity1 = 0
    quantity2 = 0
    quantity3 = 0
    quantity4 = 0
    quantity5 = 0
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    while(True):

        order = int(input("Which burger would you like? "))

        if(order == 0):
            print("Thanks!")
            break
        elif(order > 5 or order < 0):
            print("Please Select a valid option")
            break

        quantity = int(input("How many would you like? "))

        if order == 1:
            total1 = quantity * DE_ANZA_BURGER
            quantity1 += 1
            quantity1 = quantity1 * quantity
            continue
        elif order == 2:
            total2 = quantity * BACON_CHEESE
            quantity2 += 1
            quantity2 = quantity2 * quantity
            continue
        elif order == 3:
            total3 = quantity * MUSHROOM_SWISS
            quantity3 += 1
            quantity3 = quantity3 * quantity
            continue
        elif order == 4:
            total4 = quantity * WESTERN_BURGER
            quantity4 += 1
            quantity4 = quantity4 * quantity
            continue
        elif order == 5:
            total5 = quantity * DON_CALI_BURGER
            quantity5 += 1
            quantity5 = quantity5 * quantity
            continue


    print(quantity1, quantity2, quantity3, quantity4, quantity5)
    print(total1, total2, total3, total4, total5)
    grandTotal = total1 + total2 + total3 + total4 + total5
    return (grandTotal)


def studentOrStaff():
    studentOrStaff = input("Are you a student or staff??: ")
    if studentOrStaff == "staff":
        tax = TAX
    elif studentOrStaff == "student":
        tax = 1
    print(tax)
    return (tax)


main()






