from random import randint


def smallest_ip_range():
    prefix_len = randint(24, 30)
    ip_prefix_amount = 2 ** (32 - prefix_len)
    ip_range_amount = 0
    while (
        ip_prefix_amount == ip_range_amount
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
