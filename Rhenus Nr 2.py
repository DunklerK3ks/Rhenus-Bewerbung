#Made By Tim Mathis // DunklerKeks
while True:
    num1 = input("Gib die erste Zahl ein: ") #  Die Erste Zahl Imput
    oper = input("Welche Rechenoperation soll durchgeführt werden? (+,-,/.,*): ") # Welcher Rechen Operator genommen werden solö
    num2 = input("Gib die zweite Zahl ein: ") # Die Weitern Inputs
    num3 = input("Gib die dritte Zahl ein: ") # Die Weitern Inputs

    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
      # Die Rechnungen
    if (oper == "+"):
        print("Deine Rechnung:", num1, " + ", num2 , " + ", num3) 
        print("Ergebnis:", num1 + num2 + num3)

    elif (oper == "-"):
        print("Deine Rechnung:", num1, " - ", num2 , "-", num3)
        print("Ergebnis:", num1 - num2 - num3)

    elif (oper == "/"):
        print("Deine Rechnung:", num1, " / ", num2 ," / ", num3)
        print("Ergebnis:", num1 / num2 / num3)

    elif (oper == "*"):
        print("Deine Rechnung:", num1, " * ", num2 ,"*", num3)
        print("Dein Ergebnis:", num1 * num2 * num3)
    else:
        print("Deine Eingaben sind nicht gültig")
1