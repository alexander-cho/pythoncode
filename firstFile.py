#Constants
DE_ANZA_BURGER = 5.25
BACON_CHEESE = 5.75
MUSHROOM_SWISS = 5.95
WESTERN_BURGER = 5.95
DON_CALI_BURGER = 5.95
TAX = 1.09
QUANTITY1 = 0
QUANTITY2 = 0
QUANTITY3 = 0
QUANTITY4 = 0
QUANTITY5 = 0
TOTAL1 = 0
TOTAL2 = 0
TOTAL3 = 0
TOTAL4 = 0
TOTAL5 = 0


def main():
    displayMenu()
    orderTotal = takeOrder()
    taxRate = studentOrStaff()
    orderTotalAfterTax = (calculateTotalAfter(orderTotal, taxRate))


def displayMenu():
    print("De Anza Burger: $5.25. Enter 1.")
    print("Bacon Cheese: $5.75. Enter 2.")
    print("Mushroom Swiss: $5.25. Enter 3.")
    print("Western Burger: $5.25. Enter 4.")
    print("Don Cali Burger: $5.25. Enter 5.")


def takeOrder():
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
            TOTAL1 = quantity * DE_ANZA_BURGER
            QUANTITY1 += 1
            quantity_ = QUANTITY1
            QUANTITY1 = QUANTITY1 * quantity
            continue
        elif order == 2:
            TOTAL2 = quantity * BACON_CHEESE
            QUANTITY2 += 1
            QUANTITY2 = QUANTITY2 * quantity
            continue
        elif order == 3:
            TOTAL3 = quantity * MUSHROOM_SWISS
            QUANTITY3 += 1
            QUANTITY3 = QUANTITY3 * quantity
            continue
        elif order == 4:
            TOTAL4 = quantity * WESTERN_BURGER
            QUANTITY4 += 1
            QUANTITY4 = QUANTITY4 * quantity
            continue
        elif order == 5:
            TOTAL5 = quantity * DON_CALI_BURGER
            QUANTITY5 += 1
            QUANTITY5 = QUANTITY5 * quantity
            continue


    print(QUANTITY1, QUANTITY2, QUANTITY3, QUANTITY4, QUANTITY5)
    print(TOTAL1, TOTAL2, TOTAL3, TOTAL4, TOTAL5)
    grandTotal = TOTAL1 + TOTAL2 + TOTAL3 + TOTAL4 + TOTAL5
    print(grandTotal)

    return (grandTotal)


def calculateTotalAfter(totalAmount, taxRate):
    return(totalAmount * taxRate)


def studentOrStaff():

    studentOrStaff = input("Are you a student or staff??: ")
    if studentOrStaff == "staff":
        tax = TAX
    elif studentOrStaff == "student":
        tax = 1

    return (tax)


main()






