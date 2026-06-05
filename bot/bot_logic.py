import random
def gen_pass(pass_length):
    elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_*!&$#@"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "O lado da moeda que caiu é cara"
    else:
        return "O lado da moeda que caiu é coroa"
