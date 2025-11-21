import robot
# Joc de Pedra, Paper, Tisora
def janken():
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
    print("Joc de endevinar el numero")
    print("He triat un numero entre l'1 i el 100")
    # Generem el numero aleatori
    import random
    random_number = random.randint(1, 100)
    # El cos principal del joc
    while True:
        try:
            player = int(input("Intenta endevinar el numero: ").strip())
        except ValueError:
            print("Introdueix un numero entre 1 i 100.")
            continue
# Comprovem la resposta del jugador
        if player < random_number:
            print("El numero es mes gran")
        elif player > random_number:
            print("El numero es mes petit")
        else:
            print("Ben fet has adivinat el numero.")
            break