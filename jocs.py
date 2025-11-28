import robot
# Joc de Pedra, Paper, Tisora
def janken():
    print("")
    print("")
    print("Nem a jugar a Pedra, Paper, Tisora")
    print("Per jugar al que guanye 3 (1)")
    print("Per jugar al millor de 5 rondes (2)")
    # Aqui triem les rondes
    choice = input("Tria 1 o 2: ")    
    if choice == "1":
        rounds_to_win = 3
        rounds = None  
    elif choice == "2":
        rounds_to_win = None 
        rounds = 5
    else:
        print("No val esta opció, jugarem al millor de 3 rondes")
        rounds_to_win = 3
        rounds = None  
    player_score = 0
    robot_score = 0 
    current_round = 0 
    # El cos principal del joc
    while True:
        r = robot.robot()
        jugador = input("Tria pedra, paper o tisora: ")
        eleccio_robot = r.playing()
        print(f"El robot ha triat: {eleccio_robot}")
        if jugador == eleccio_robot:
            print("Empate")
            if choice == "2":
                current_round += 1
        elif (jugador == "pedra" and eleccio_robot == "tisora") or \
             (jugador == "paper" and eleccio_robot == "pedra") or \
             (jugador == "tisora" and eleccio_robot == "paper"):
            print("Has guanyat")
            player_score += 1
            current_round += 1
        else:
            print("Ha guanyat el robot")
            robot_score += 1
            current_round += 1
            #Per comprovar si estem en la opccio 1 o 2
        if rounds_to_win and player_score == rounds_to_win:
            print("Has guanyat la partida")
            break
        if rounds_to_win and robot_score == rounds_to_win:
            print("El robot ha guanyat la partida")
            break
        if rounds and current_round >= rounds:
            if player_score > robot_score:
                print("Has guanyat la partida")
            elif robot_score > player_score:
                print("El robot ha guanyat la partida")
            else:
                print("La partida ha acabat en empat")
            break
# Joc d'endevinar el numero
def nana():
    print("")
    print("")
    print("Joc de endevinar el numero")
    print("He triat un numero entre l'1 i el 100")
    # Generem el numero aleatori
    import random
    random_number = random.randint(1, 100)
    # El cos principal del joc
    while True:
        try:
            player = int(input("Intenta endevinar el numero: ").strip())
            if player < random_number:
                print("El numero es mes gran")
            elif player > random_number:
                print("El numero es mes petit")
            else:
                print("Ben fet has adivinat el numero.")
                break
        except ValueError:            
            print("Introdueix un numero entre 1 i 100.")
def coinflip():
    print("")
    print("")
    print("Joc de Cara o Creu")
    import robot2
    r = robot2.robot()
    jugador = input("Tria cara o creu: ")
    eleccio_robot = r.playing()
    print(f"la moneda ha caigut en: {eleccio_robot}")
    if jugador == eleccio_robot:
        print("Has guanyat")
        print("")
        print("")
    else:
        print("Has perdut")
        print("")
        print("")
    if jugador != "cara" and jugador != "creu":
        print("Opcio no valida, torna-ho a intentar")
        print("")
        print("")
import robot
import robot3
import random
from time import sleep
def tresenratlla():
    print("")
    print("")
    print("Joc de Tres en Ratlla")
    import robot
    r = robot3.robot()
    
    while True:
        try:
            sleep(1)
            fila_robot, columna_robot = r.playing()
            print(f"El robot ha triat la posicio: fila {fila_robot}, columna {columna_robot}")
            print("")
            r.mostrar_tauler()
            print("")
            sleep(1)
            columna_jugador = int(input("Posicio fila (0, 1 o 2): "))
            fila_jugador = int(input("Posicio columna (0, 1 o 2): "))
            
            if columna_jugador < 0 or columna_jugador > 2 or fila_jugador < 0 or fila_jugador > 2:
                print("Posicio no valida. Intenta de nou.")
                continue
            
            if r.game[fila_jugador][columna_jugador] != "-":
                print("Aquesta posicio ja esta ocupada. Intenta de nou.")
                continue
        
            r.game[fila_jugador][columna_jugador] = "o"
            print("")
            r.mostrar_tauler()
            print("")
            
            
        except ValueError:
            print("Introdueix numeros valids (0, 1 o 2).")
    
