import functions
import os

while True:
    user_imp = input('Gerador de Senhas! \n\n[0] SAIR \n[1] GERAR SENHA \n[2] CONSULTAR SENHA GERADA \nOption: ')

    try:
        user_imp = int(user_imp)
        if user_imp == 0:
            print('é  isso')
            break
        elif user_imp == 1:
            ...
        elif user_imp == 2:
            ...
    except ValueError:
        print('\nOpção inválida \n')
        os.system('clear')

