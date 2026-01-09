#Bucle principal del programa
import jocs
while True:
        # Importem l'arxiu de jocs
        print("MINI ARCADE")
        print("Pedra,Paper,Tisora 1")
        print("Endivinar el numero 2")
        print("Cara o Creu 3")
        print("Tres en ratlla 4")
        print("Sortir S")
        # Triem el joc
        choice = input("Tria el joc (1 o 2 o 3 o 4) o sortir amb (S): ")
        if choice == '1':
            jocs.janken()
            jocs.nana()
            
        elif choice == '3':
            jocs.coinflip()
        
        elif choice == '4':
            jocs.tresenratlla()
            
        elif choice == 'S' or choice == 's':
            print("Gracies per jugar")
            break
        else:
            print("Opcio no valida, torna-ho a intentar")
        
