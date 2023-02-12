from random import randint, choice

def smallest_ip_range():
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
    return [f"{first_three_octects}.0/{prefix_len}", f"{first_three_octects}.[0-{ip_range_amount}]", answer]


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
        a = randint(1, len(service_ports))
        if a not in possible_answers:
            possible_answers.append(a)
    possible_answers_list = []
    for item in possible_answers:
        possible_answers_list.append(service_ports[item-1]['port'])
    answer = service_ports[choice(possible_answers)-1]
    return {'possbile_answers' : possible_answers, 'answer' : answer}


print(match_port_and_service())

# for p in a:
#     print(f"""
#     {p['port']}
#     {p['protocol']}
#     {p['name']}
#     {p['description']}
#     """)