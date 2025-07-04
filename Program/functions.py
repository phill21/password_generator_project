import random
import string

def char_generate_pass(param1):
    # Utilizar esse caso queira remover acentos e caracteres complexos
    # char_pass = random.sample(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '.', '?', '+'], k=param1)

    char_pass = random.choices(string.punctuation, k=param1)
    return ''.join(char_pass)

def num_generate_pass(param2):
    num_pass = random.choices(string.digits, k=param2)
    return ''.join(num_pass)

def alpha_generate_pass(param3):
    alpha_pass = random.choices(string.ascii_letters, k=param3)
    return ''.join(alpha_pass)

def generate_pass(qtd_num, qtd_alpha, qtd_char):
    united_param = ''.join(num_generate_pass(qtd_num) + alpha_generate_pass(qtd_alpha) + char_generate_pass(qtd_char))
    united_param = list(united_param.strip())
    random.shuffle(united_param)
    new_pass = ''.join(united_param)
    return new_pass



