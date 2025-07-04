import functions
import os

from Program.functions import generate_pass

while True:
    user_imp = input('Gerador de Senhas! \n\n[0] SAIR \n[1] GERAR SENHA \nOption: ')

    try:
        user_imp = int(user_imp)
        if user_imp == 0:
            print('é  isso')
            break
        elif user_imp == 1:
            try:

                letters_qtd = int(input('Quantos caracteres (letras maiúsculas e minúsculas): '))
                numbers_qtd = int(input('Quantos números: '))
                characters_qtd = int(input('Quantos caracteres (letras maiúsculas e minúsculas): '))
                gen_pass = generate_pass(numbers_qtd, letters_qtd, characters_qtd)

                print(f'Nova senha sugerida: {gen_pass}\n\n')

            except ValueError:
                print('\nOpção inválida \n')
    except ValueError:
        print('\nOpção inválida \n')
        os.system('clear')

