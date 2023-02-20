from games import smallest_ip_range, match_port_and_service
import os
from random import choice

games = [smallest_ip_range, match_port_and_service]
os.system('clear')
print("""
█▀▀ █ █▀█ █▀▀ █░█░█ ▄▀█ █░░ █░░  
█▀░ █ █▀▄ ██▄ ▀▄▀▄▀ █▀█ █▄▄ █▄▄  

 █▀▀ █▄░█ █▀▀ █ █▄░█ █▀▀ █▀▀ █▀█  
 ██▄ █░▀█ █▄█ █ █░▀█ ██▄ ██▄ █▀▄ 

 ▀█▀ █░█ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀ █
 ░█░ █▀█ ██▄   █▄█ █▀█ █░▀░█ ██▄ ▄

There are 10 requests in the ticket queue.

They must all be completed before the big PEN test.

Go Go Go!

Press "enter" to start
""")

input()
os.system('clear')

number_of_questions = 10
score = 0

while number_of_questions > 0:
    answer = choice(games)()
    if answer == True:
        score += 1
    number_of_questions -= 1
    os.system('clear')

if score ==10:
    print(f"You scored {score} out of 10!")
elif score in range(6,9):
    print(f"You scored {score} out of 10, not too bad...")
elif score < 6:
    print(f"You scored {score} out of 10... Your P45 is waiting for you")