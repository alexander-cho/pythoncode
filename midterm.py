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
    print(round(0, 2))


def displayMenu():
    print("De Anza Burger: $5.25. Enter 1.")
    print("Bacon Cheese: $5.75. Enter 2.")
    print("Mushroom Swiss: $5.25. Enter 3.")
    print("Western Burger: $5.25. Enter 4.")
    print("Don Cali Burger: $5.25. Enter 5.")


def takeOrder():

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

    userInputFlag = True
    while(userInputFlag):

        order = int(input("Which burger would you like? "))
        if(order == 0):
            print("")
            print("Thanks!")
            userInputFlag = False
        elif(order > 5 or order < 0):
            print("")
            print("Please Select a valid option")
            userInputFlag = False

        if(userInputFlag == True):
            quantity = int(input("How many would you like? "))
            if(order == 1):
                TOTAL1 = quantity * DE_ANZA_BURGER
                QUANTITY1 += 1
                quantity_ = QUANTITY1
                QUANTITY1 = QUANTITY1 * quantity
                continue
            elif(order == 2):
                TOTAL2 = quantity * BACON_CHEESE
                QUANTITY2 += 1
                QUANTITY2 = QUANTITY2 * quantity
                continue
            elif(order == 3):
                TOTAL3 = quantity * MUSHROOM_SWISS
                QUANTITY3 += 1
                QUANTITY3 = QUANTITY3 * quantity
                continue
            elif(order == 4):
                TOTAL4 = quantity * WESTERN_BURGER
                QUANTITY4 += 1
                QUANTITY4 = QUANTITY4 * quantity
                continue
            elif(order == 5):
                TOTAL5 = quantity * DON_CALI_BURGER
                QUANTITY5 += 1
                QUANTITY5 = QUANTITY5 * quantity
                continue

    totalBeforeTax = TOTAL1 + TOTAL2 + TOTAL3 + TOTAL4 + TOTAL5
    taxRate = studentOrStaff()
    totalAfterTax = calculateTotalAfter(totalBeforeTax, taxRate)
    printBill(QUANTITY1, TOTAL1, QUANTITY2, TOTAL2, QUANTITY3, TOTAL3, QUANTITY4, TOTAL4, QUANTITY5, TOTAL5, totalBeforeTax, taxRate, totalAfterTax)


def calculateTotalAfter(totalAmount, taxRate):
    return(totalAmount * taxRate)


def studentOrStaff():
    studentOrStaff = input("Are you a student or staff??: ")
    if studentOrStaff == "staff":
        tax = TAX
    elif studentOrStaff == "student":
        tax = 1
    print("")
    return (tax)


def printBill(q1,p1,q2,p2,q3,p3,q4,p4,q5,p5,totalBeforeTax,Tax,totalAfterTax):
    print("You Ordered: ")
    p1 = "%.2f" % p1
    print(str(q1) + " DeAnza Burger," + " $" + str(p1))
    p2 = "%.2f" % p2
    print(str(q2) + " Bacon Cheese," +  " $" + str(p2))
    p3 = "%.2f" % p3
    print(str(q3) + " Mushroom Swiss," + " $" + str(p3))
    p4 = "%.2f" % p4
    print(str(q4) + " Western Burger," + " $" + str(p4))
    p5 = "%.2f" % p5
    print(str(q5) + " Don Cali," + " $" + str(p5))
    print("")
    print("Cost Breakdown: ")
    totalBeforeTax = "%.2f" % totalBeforeTax
    print("Total Before Tax: " + "$" + str(totalBeforeTax))
    if(Tax == 1):
        print("Tax Rate: " + "No Tax")
    else:
        print("Tax Rate: " + str(Tax) + "%")
    totalAfterTax = "%.2f" % totalAfterTax
    print("Total After Tax: " + "$" + str(totalAfterTax))

main()