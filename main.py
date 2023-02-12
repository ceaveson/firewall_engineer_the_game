from games import smallest_ip_range

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

Press enter to start
""")

input()

number_of_questions = 10
score = 0

while number_of_questions > 0:
    answer = 'c'
    accepted_answers = ['a','b']
    question = smallest_ip_range()
    print('Give least amount of IP addresses access')
    print(f'a: {question[0]}')
    print(f'b: {question[1]}')
    while answer not in accepted_answers:
        answer = input('Answer either \'a\' or \'b\':')
    if answer == question[2]:
        score += 1
    number_of_questions -= 1

if score ==10:
    print(f"You scored {score} out of 10!")
elif score in range(6,9):
    print(f"You scored {score} out of 10, not too bad...")
elif score < 6:
    print(f"You scored {score} out of 10... Your P45 is waiting for you")