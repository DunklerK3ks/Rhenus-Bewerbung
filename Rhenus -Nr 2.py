# Made by Tim Mathis // DunklerK3ks
while True:
    num1 = input("Gib die erste Zahl ein: ") #  Die Erste Zahl Imput
    oper = input("Welche Rechenoperation soll durchgeführt werden? (+,-,/.,*): ") # Welcher Rechen Operator genommen werden solö
    num2 = input("Gib die zweite Zahl ein: ") # Die Weitern Inputs
    num3 = input("Gib die dritte Zahl ein: ") # Die Weitern Inputs

    num1 = int(num1) # Die eingaben werden in Zahlen Umgewandelt
    num2 = int(num2) # Die eingaben werden in Zahlen Umgewandelt
    num3 = int(num3)#  Die eingaben werden in Zahlen Umgewandelt
  
  
  # Die Rechnungen
    if (oper == "+"): # Hier wird der Rechen Operator festglegt
        print("Deine Rechnung:", num1, " + ", num2 , " + ", num3)# Hier wird deine Rechnung gezeigt
        print("Ergebnis:", num1 + num2 + num3) # Das Ergebniss  mit Rechung

    elif (oper == "-"):# Hier wird der Rechen Operator festglegt
        print("Deine Rechnung:", num1, " - ", num2 , "-", num3)# Hier wird deine Rechnung gezeigt
        print("Ergebnis:", num1 - num2 - num3)# Das Ergebniss  mit Rechung

    elif (oper == "/"):# Hier wird der Rechen Operator festglegt
        if num2 == 0 or num3 == 0: # Wenn es Null ist kann man es nich rechen das wird hier festgelegt
           print("Division durch null ist nicht möglich") # Die ausgabe das ma nes nicht ausrechen kann
        else:
           print("Deine Rechnung:", num1, " / ", num2 ," / ", num3)#Hier wird deine Rechnung gezeigt
           print("Ergebnis:", num1 / num2 / num3)# Hier sieht man die Lösung

    elif (oper == "*"):# Hier wird der Rechen Operator festglegt
        print("Deine Rechnung:", num1, " * ", num2 ,"*", num3) #Hier wird deine Rechnung gezeigt
        print("Dein Ergebnis:", num1 * num2 * num3)# Hier sieht man die Lösung
    else:
        print("Deine Eingaben sind nicht gültig") # Wenn man Buchstaben eingibt
