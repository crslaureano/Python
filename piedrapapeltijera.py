import random
import os
import time
import sys

# Marcadores de juegos
option_menu = ['s', 'q', 'r', 'p', 't']

def menu(opt):
    menus = {
        'menu' : 'Iniciar: [s] | Quit: [q]',
        'menu_game' : 'Pierdra: [r] | Papel: [p] | Tijera: [t] | Quit: [q]'
    }
    print(f"+{menus[opt]:^55}+")

def control_select():
    get_option = input("> ").lower().strip()
    while True:
        if get_option in option_menu:
            return get_option
            break
        else:
            os.system('clear')
            get_option = input('> Ingrese un valor correcto : ')

def register():
    os.system("clear")
    user_name = input("> Your Name: ")
    print("Succel full user creater... ")
    return user_name.lower().strip()

def game():
    ganadas = 0
    empates = 0
    perdidas = 0

    user = register()
    time.sleep(.75)
    os.system('clear')
    while True:
        menu('menu')
        option_m = control_select()
        if option_m in option_menu:
            while True:
                if option_m == 's':
                    os.system('clear')
                    while True:
                        os.system('clear')
                        print(f"+{'':-^55}+")
                        menu('menu_game')
                        print(f"+{'':-^55}+")
                        # print(f"+{user:>10} -> {ganadas:>10} {empates:>10} {perdidas:>10}+")
                        print(f"+{f'{user} -> Ganadas:{ganadas} / Empates:{empates} / Perdidas:{perdidas}':^55}+")
                        print(f"+{'':-^55}+")
                        option_user = control_select()
                        option_computer = random.choice(['r', 'p', 't'])
                        # print(f"User: {option_user} Computer: {option_computer}")
                        print(f"Coputer: {option_computer}")
                        if option_user == option_computer:
                            print('Empate')
                            empates += 1
                        elif option_user == 'r':
                            if option_computer == 't':
                                print("Ganaste!!!")
                                ganadas += 1
                            else:
                                print("Perdiste :(")
                                perdidas += 1
                        elif option_user == 'p':
                            if option_computer == 'r':
                                print("Ganaste!!!")
                                ganadas += 1
                            else:
                                print("Perdiste :(")
                                perdidas +=1
                        elif option_user == 't':
                            if option_computer == 'p':
                                print("Ganaste!!!")
                                ganadas += 1
                            else:
                                print("Perdiste :(")
                                perdidas += 1
                        elif option_user == 'q':
                            os.system('clear')
                            print(ganadas, empates, perdidas)
                            sys.exit()
                        else:
                            menu("menu_game")
                            print("> Ingrese un valor correcto...")
                            option_user == control_select()
                        time.sleep(1.25)
                if option_m == 'q':
                    sys.exit()
        else:
            option_m = control_select()

if __name__ == "__main__":
    game()
