from games import smallest_ip_range, match_port_and_service
import os
from random import choice

games = [smallest_ip_range, match_port_and_service]
question_list = ['[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]','[10]']

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
    print('Requests remaining in the ticket queue')
    print(*question_list)
    print()
    question_list.pop()
    answer = choice(games)()
    if answer == True:
        score += 1
    number_of_questions -= 1
    os.system('clear')

if score == 10:
    print(f"""
            .=.,
            ;c =\ 
          __|  _/
        .'-'-._/-'-._
       /..   ____    \ 
      /' _  [<_->] )  \     You scored {score}
     (  / \--\_>/-/'._ )    out of 10!
      \-;_/\__;__/ _/ _/
       '._)|==o==\(_\/
        /  /-._.--\  \ 
       // /   /|   \ \ \ 
      / | |   | \;  |  \ \ 
     / /  | :/   \: \   \_\ 
    /  |  /.'|   /: |    \ \ 
    |  |  |--| . |--|     \_\ 
    / _/   \ | : | /___--._) \ 
   |_(---'-| >-'-| |       '-'
       /_/     \_\ 
""")
elif score in range(6,10):
    print(f"""
         __
 _(\    |@@|               
(__/\__ \--/ __            
   \___|----|  |   __     You scored {score} 
       \ \/ /\ )_ / _\    out of 10,
       /\__/\ \__O (__    not too bad...
      (--/\--)    \__/
      _)(  )(_
     `---''---`
""")
elif score < 6:
    print(f"""
        _______
        |.-----.|        
        ||x . x||        You scored {score} out
        ||_.-._||        of 10. Your P45 is 
        `--)-(--`        waiting for you...
       __[=== o]___
      |:::::::::::|
       `-=========-`()
""")