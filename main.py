#main.py
from Canoe import Canoe
from tabulate import tabulate
import random
import csv
import datetime
import tabulate


#define roulette wheel
wheel = [
    Canoe(number=0, color='GREEN'),
    Canoe(number=28, color='BLACK'),
    Canoe(number=9, color='RED'),
    Canoe(number=26, color='BLACK'),
    Canoe(number=30, color='RED'),
    Canoe(number=11, color='BLACK'),
    Canoe(number=7, color='RED'),
    Canoe(number=20, color='BLACK'),
    Canoe(number=32, color='RED'),
    Canoe(number=17, color='BLACK'),
    Canoe(number=5, color='RED'),
    Canoe(number=22, color='BLACK'),
    Canoe(number=34, color='RED'),
    Canoe(number=15, color='BLACK'),
    Canoe(number=3, color='RED'),
    Canoe(number=24, color='BLACK'),
    Canoe(number=36, color='RED'),
    Canoe(number=13, color='BLACK'),
    Canoe(number=1, color='RED'),
    Canoe(number=00, color='GREEN'),
    Canoe(number=27, color='RED'),
    Canoe(number=10, color='BLACK'),
    Canoe(number=25, color='RED'),
    Canoe(number=29, color='BLACK'),
    Canoe(number=12, color='RED'),
    Canoe(number=8, color='BLACK'),
    Canoe(number=19, color='RED'),
    Canoe(number=31, color='BLACK'),
    Canoe(number=18, color='RED'),
    Canoe(number=6, color='BLACK'),
    Canoe(number=21, color='RED'),
    Canoe(number=33, color='BLACK'),
    Canoe(number=16, color='RED'),
    Canoe(number=4, color='BLACK'),
    Canoe(number=23, color='RED'),
    Canoe(number=35, color='BLACK'),
    Canoe(number=14, color='RED'),
    Canoe(number=2, color='BLACK'),
    ]

def spin():
    #generate random outcome of spin
    spin_number = random.randint(0, 37)

    #print results
    if 0 <= spin_number < len(wheel):
        selected_canoe = wheel[spin_number]
        if (selected_canoe.number % 2) == 0:
            if (selected_canoe.number == 0 or selected_canoe.number == 00):
                print(f"The Winning Number is: {selected_canoe.number}, \033[32m{selected_canoe.color}\033[0m.")
                with open('spin_log.csv', 'a', newline='') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(["n/a", selected_canoe.number, selected_canoe.color, "EVEN", datetime.datetime.now()])
            else:
                if (selected_canoe.color == 'red'):
                    print(f"The Winning Number is: {selected_canoe.number}, \033[0;31m{selected_canoe.color}. EVEN.")
                    with open('spin_log.csv', 'a', newline='') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(["n/a", selected_canoe.number, selected_canoe.color, "EVEN", datetime.datetime.now()])
                else:
                    print(f"The Winning Number is: {selected_canoe.number}, \033[0;30m{selected_canoe.color}\033[0m. EVEN.")
                    with open('spin_log.csv', 'a', newline='') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(["n/a", selected_canoe.number, selected_canoe.color, "EVEN", datetime.datetime.now()])
        else:
                if (selected_canoe.color == 'red'):
                    print(f"The Winning Number is: {selected_canoe.number}, \033[0;31m{selected_canoe.color}\033[0m. ODD.")
                    with open('spin_log.csv', 'a', newline='') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(["n/a", selected_canoe.number, selected_canoe.color, "ODD", datetime.datetime.now()])
                else:
                    print(f"The Winning Number is: {selected_canoe.number}, \033[0;30m{selected_canoe.color}\033[0m. ODD.")
                    with open('spin_log.csv', 'a', newline='') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow(["n/a", selected_canoe.number, selected_canoe.color, "ODD", datetime.datetime.now()])
    else:
        print(f"Index {spin_number} is out of range.")

def stats():
    userInput = input(display_stats_controls())
    while userInput != 'back' :
        if userInput == 'all':
            with open('spin_log.csv', 'r') as csv_file:
                stats_output = csv.reader(csv_file, delimiter=',')
                for row in stats_output:
                    print(row)
        if userInput == 'avg':
            with open('spin_log.csv', 'r') as csv_file:
                stats_output = csv.reader(csv_file, delimiter=',') 
                total_rows = 0
                green_count = 0
                red_count = 0
                black_count = 0
                odd_count = 0
                even_count = 0
                for row in stats_output:
                    total_rows += 1
                    if (row[2] == 'GREEN'):
                        green_count += 1
                    if (row[2] == 'RED'):
                        red_count += 1
                    if (row[2] == 'BLACK'):
                        black_count += 1
                    if (row[3] == 'ODD'):
                        odd_count += 1
                    if (row[3] == 'EVEN'):
                        even_count += 1
                green_avg = round(green_count/total_rows * 100, 2)
                red_avg = round(red_count/total_rows * 100, 2)
                black_avg = round(black_count/total_rows * 100, 2)
                odd_avg = round(odd_count/total_rows * 100, 2)
                even_avg = round(even_count/total_rows * 100, 2)
                print(tabulate.tabulate([['Total Spins', total_rows, '-'],
                                        ['GREEN', green_count, f"{green_avg}%"],
                                        ['RED', red_count, f"{red_avg}%"],
                                        ['BLACK', black_count, f"{black_avg}%"],
                                        ['ODD', odd_count, f"{odd_avg}%"],
                                        ['EVEN', even_count, f"{even_avg}%"]
                                        ], 
                                        headers=['stat', 'count', 'average'],
                                        tablefmt="outline"))

                    
        userInput = input("Enter 'averages' or 'all', or 'back' to exit stats\n")
    
def intro():
    print(r"""
     ________  ___    ___ _________  ___  ___  ________  ________                       
    |\   __  \|\  \  /  /|\___   ___\\  \|\  \|\   __  \|\   ___  \                    
    \ \  \|\  \ \  \/  / ||___ \  \_\ \  \\\  \ \  \|\  \ \  \\ \  \                     
     \ \   ____\ \    / /     \ \  \ \ \   __  \ \  \\\  \ \  \\ \  \                   
      \ \  \___|\/   / /       \ \  \ \ \  \ \  \ \  \\\  \ \  \\ \  \                
       \ \__\ __/   / /         \ \__\ \ \__\ \__\ \_______\ \__\\ \__\               
        \|__||\___ / /           \|__|  \|__|\|__|\|_______|\|__| \|__|                
             \|____|/                                                                     
                                                                                          
                                                                                          
     ________  ________  ___  ___  ___       _______  _________  _________  _______     
    |\   __  \|\   __  \|\  \|\  \|\  \     |\  ___ \|\___   ___\\___   ___\\  ___ \     
    \ \  \|\  \ \  \|\  \ \  \\\  \ \  \    \ \   __/\|___ \  \_\|___ \  \_\ \   __/|     
     \ \   _  _\ \  \\\  \ \  \\\  \ \  \    \ \  \_|/__  \ \  \     \ \  \ \ \  \_|/__  
      \ \  \\  \\ \  \\\  \ \  \\\  \ \  \____\ \  \_|\ \  \ \  \     \ \  \ \ \  \_|\ \ 
       \ \__\\ _\\ \_______\ \_______\ \_______\ \_______\  \ \__\     \ \__\ \ \_______\ 
        \|__|\|__|\|_______|\|_______|\|_______|\|_______|   \|__|      \|__|  \|_______|""")

def display_controls():
    print(tabulate.tabulate([['BET', 'b'],
                        ['SPIN', 's'],
                        ['EXIT', 'e'],
                        ['Stats', 'stats']],
                        headers=['Action', 'Command'],
                        tablefmt="outline"))

def display_stats_controls():
    print(tabulate.tabulate([['Averages', 'avg'],
                        ['Display all results', 'all'],
                        ['Go back', 'back']],
                        headers=['Action', 'Command'],
                        tablefmt="outline"))
    
#start game
intro()
userInput = input(display_controls())
while userInput != 'e' :
    if userInput == 's':
        spin()
    if userInput == 'b':
        print(f'enter bet prompt\n')
    if userInput == 'stats':
        stats()
    userInput = input("Enter 'b' to BET or 's' to SPIN\n")
