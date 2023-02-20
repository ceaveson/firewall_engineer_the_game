from random import randint, choice

def smallest_ip_range():
    answer = 'c'
    accepted_answers = ['a','b']
    prefix_len = randint(24, 30)
    ip_prefix_amount = 2 ** (32 - prefix_len)
    ip_range_amount = 0
    while (
        ip_prefix_amount-1 == ip_range_amount
        or ip_range_amount < 1
        or ip_range_amount > 255
    ):
        ip_range_amount = randint(ip_prefix_amount - 10, ip_prefix_amount + 10)
    if ip_prefix_amount < ip_range_amount:
        answer = "a"
    else:
        answer = "b"
    first_three_octects = f"{randint(1,254)}.{randint(1,254)}.{randint(1,254)}"
    question = [f"{first_three_octects}.0/{prefix_len}", f"{first_three_octects}.[0-{ip_range_amount}]", answer]

    print('Give least amount of IP addresses access')
    print(f'a: {question[0]}')
    print(f'b: {question[1]}')
    answer = input('Answer either \'a\' or \'b\':')
    if answer == question[2]:
        return True


def match_port_and_service():
    service_ports = []
    with open('popular_ports.txt') as f:
        ports_list = f.readlines()
    for port in ports_list:
        port_dict = {}
        port_dict['port'] = port.split('\t')[0].strip()
        port_dict['name'] = port.split('\t')[1].strip()
        port_dict['protocol'] = port.split('\t')[2].strip()
        port_dict['description'] = port.split('\t')[3].strip()
        service_ports.append(port_dict)
    possible_answers = []
    while len(possible_answers) < 4:
        i = randint(1, len(service_ports))
        if i not in possible_answers:
            possible_answers.append(i)
    possible_answers_list = []
    for item in possible_answers:
        possible_answers_list.append(service_ports[item-1]['port'])
    answer = service_ports[choice(possible_answers)-1]
    print(f"Which of the following service ports does {answer['name']} use:\n")
    answers_map = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3}
    user_choice = input(f"Possible Answers: a. {possible_answers_list[0]}, b. {possible_answers_list[1]}, c. {possible_answers_list[2]} d. {possible_answers_list[3]}\nYour answer:")
    if possible_answers_list[answers_map[user_choice]] == answer['port']:
        return True