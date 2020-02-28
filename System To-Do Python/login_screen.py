"""
 ============================================================================
 Name         : System To-Do Python
 Author       : Ramon Soares Mendes Meneses Leite
 Version      : 0.49
 E-mail:      : ramnsores1000@gmail.com
 University   : Universidade Federal de Goiás - Catalão GO
 Objective    : Just for fun
 ============================================================================
"""
 
import os
import re
import shelve
import sys
from color import font


def is_valid_email(email):
    if len(email) > 7:
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) is not None:
            return True
    return False


def type_validation(msg):
    while True:
        try:
            v_int = int(input(msg))
            return v_int
        except (ValueError, TypeError):
            print(' # ERRO! Tipo inválido!')
        except KeyboardInterrupt:
            sys.exit()


class Login:

    def __init__(self):
        self.db = shelve.open("login/login.db")
        self.logged = None
        self.start()

    def start(self):

        print(font('azul1') + "=" * 40)
        print("||               To-Do                ||")
        print("=" * 40 + font('reset'))
        print(font('amarelo') + "=" * 40)
        start_menu = ["1- Entrar", "2- Cadastrar Novo Usuário", "3- Ver Usuários Cadastrados", "4- Excluir Usuário",
                      "5- Sair"]
        for i in start_menu:
            print(f"| {i: <36} |")
        print("=" * 40)

        while True:
            choice = type_validation(font('vermelho') + '\n > ')
            if 0 < choice <= 5:
                break
            else:
                print(' # Opção inválida!')

        if choice == 1:
            self.log_into_account()
        elif choice == 2:
            self.register_user()
        elif choice == 3:
            self.view_registered()
        elif choice == 4:
            self.del_user()
        elif choice == 5:
            print(font('magenta') + '\n >>> Te vejo em breve! Adios! <<<\n')
            sys.exit()

    def log_into_account(self):

        while True:
            print(font('amarelo') + "+=" * 20 + '+')
            print(' > Entrar <                              ')
            print("+=" * 20 + '+')
            login_user = str(input('> Usuário: '))
            login_pass = str(input('> Senha: '))
            print("+=" * 20 + '+')

            if login_user not in self.db:
                print(font('vermelho') + "\n # Usuário inválido! Tente novamente...")
            else:
                if login_pass == self.db[login_user]['Senha']:
                    self.logged = login_user
                    print(font('reset'))
                    break
                    # ('AQUI COMEÇA OUTRO MODULO')
                else:
                    print(font('vermelho') + '\n # Senha inválida! Tente novamente...')

    def register_user(self):

        while True:
            print(font('amarelo') + "+=" * 20 + '+')
            print(' > Cadastro <                            ')
            print("+=" * 20 + '+')
            user = str(input(' > Usuário: '))
            name = str(input(' > Nome: '))
            email = str(input(' > Email: '))
            pswd = str(input(' > Senha: '))
            print("+=" * 20 + '+')

            if len(user) == 0 or len(name) == 0 or len(email) == 0 or len(pswd) == 0:
                print(font('vermelho') + '\n # Erro! Nenhum dos campos pode ser nulo!\n')
            elif user in self.db:
                print(font('vermelho') + '\n # Usuário já existente!\n')
            elif is_valid_email(email) is False:
                print(font('vermelho') + '\n # Email inválido!\n')
            else:
                self.db[user] = {'Nome': name, 'Email': email, 'Senha': pswd}
                print(font('magenta') + '\n >>> Usuário criado com sucesso! <<<\n')
                break
        self.start()

    def view_registered(self):
        print(font('amarelo') + "+=" * 20 + '+')
        print(' > Usuário Cadastrados <                      ')
        print("+=" * 20 + '+')
        if len(self.db) == 0:
            print(" # Não há usuários cadastrados!")
        else:
            for i in self.db:
                print(i)
        print("+=" * 20 + '+')
        self.start()

    def del_user(self):
        print(font('amarelo') + "+=" * 20 + '+')
        print('| > Excluir Usuário <                   |')
        print("+=" * 20 + '+')
        print("| 1- Excluir                            |")
        print("| 2- Voltar ao menu anterior            |")
        print("+=" * 20 + '+')

        while True:
            choice = type_validation(font('vermelho') + '\n > ')
            if 0 < choice <= 2:
                break
            else:
                print(' # Opção inválida!')
        if choice == 1:
            if len(self.db) == 0:
                print("\n # Não há usuários cadastrados!\n")
                self.start()
            else:
                print(font("amarelo") + "+=" * 20 + '+')
                for i in self.db:
                    print(i)
                print("+=" * 20 + '+')
                delete_user = str(input(" > Digite um usuário para deletar: "))
                del_status = False
                for i in self.db:
                    if i == delete_user:
                        del_status = True
                        break
                if del_status is True:
                    try:
                        del(self.db[i])
                        if os.path.exists('users/' + i + '.csv'):
                            os.remove('users/' + i + '.csv')
                        print(font("magenta") + "\n  >>> Usuário excluído com sucesso! <<<\n")
                        self.del_user()
                    except:
                        print(font("vermelho") + "\n # Não foi possível excluir o usuário!\n")
                        self.del_user()
                else:
                    print(font("vermelho") + "\n # Usuário não existente!\n")
                    self.del_user()
        elif choice == 2:
            self.start()


# main

if os.path.isdir('./login'):
    pass
else:
    os.makedirs('./login')

root = Login()
logged = root.logged

from to_do import System

System(logged)
