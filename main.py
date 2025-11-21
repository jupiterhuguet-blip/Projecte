#Bucle principal del programa
while True:
    def menu():
        # Importem l'arxiu de jocs
        import jocs
        print("MINI ARCADE")
        print("Pedra,Paper,Tisora 1")
        print("Endivinar el numero 2")
        print("Sortir S")
        # Triem el joc
        choice = input("Tria el joc (1 o 2) o sortir amb (S): ")
        if choice == '1':
            jocs.janken()
        elif choice == '2':
            jocs.nana()
        elif choise == 'S' or choice == 's':
            print("Gracies per jugar")
            break

# Per comprovar si estem en el fitxer principal
    if __name__ == "__main__":
        menu()