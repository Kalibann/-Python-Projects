# Bibliotecas utilizadas:

import csv
import keyboard
import os
import sys
import pandas as pd
from datetime import datetime
from random import randint


# Validador de inteiros:
def itype_validation(msg):
    while True:
        try:
            v_int = int(input(msg))
            return v_int
        except (ValueError, TypeError):
            print(' # ERRO! Tipo inválido!')
        except KeyboardInterrupt:
            sys.exit()


class System:

    def __init__(self, logged_user):
        self.user = logged_user
        self.daily_check()

    def daily_check(self):
        print(f' >>> Bem-vindo {self.user}! <<<\n')
        try:
            with open('users/' + self.user + '.csv', 'r') as test:
                test.read()
        except:
            if os.path.isdir('./users'):
                pass
            else:
                os.makedirs('./users')

            with open('users/' + self.user + '.csv', 'w') as test:
                test.write('Cod,Tarefa,Data,Importancia,Conclusao,Atraso\n')

        data_user = pd.read_csv('users/' + self.user + '.csv', encoding='ISO-8859-1')
        temp = data_user

        dat = '01/01/2000'
        dat = datetime.strptime(dat, '%d/%m/%Y').date()
        dat = dat.today()

        aux = temp['Data'].values
        for j in range(len(aux)):
            aux[j] = aux[j].replace('-', '/')
            aux[j] = datetime.strptime(aux[j], '%Y/%m/%d').date()
            if aux[j] < dat:
                temp.iloc[j, 5] = 1

        temp.to_csv('users/' + self.user + '.csv', index=False, encoding='ISO-8859-1')
        self.main_menu()

    # Funções do programa:

    def main_menu(self):
        data_user = pd.read_csv('users/' + self.user + '.csv', encoding='ISO-8859-1')
        opt = ('1 - Ver tarefas', '2 - Cadastrar tarefa', '3 - Tarefas concluídas', '4 - Excluir tarefa',
               '5 - Sair do programa')
        print('~~' * 20)
        print(' * Menu Principal                      *')
        print('~~' * 20)
        for i in opt:
            print(f'* {i: <36} *')
        print('~~' * 20)
        while True:
            choice = itype_validation('\n > ')
            if 0 < choice <= 5:
                break
            else:
                print(' # Opção inválida!')

        if choice == 1:
            self.view_tasks(data_user)

        elif choice == 2:
            self.register_task(data_user)

        elif choice == 3:
            self.completed_tasks(data_user)

        elif choice == 4:
            self.delete_task(data_user)

        elif choice == 5:
            print('\n >>> Te vejo em breve! Adios! <<<\n')
            sys.exit()

    def view_tasks(self, data_user):
        print('~' * 47)
        print('--------------------')
        print('* Mais importantes:')
        print('--------------------')
        temp = data_user[(data_user['Conclusao'] == 0)]
        temp0 = temp[(temp['Importancia'] == 5)]
        if len(temp0.index) != 0:
            print(temp0.drop(['Conclusao', 'Atraso'], axis=1))
        else:
            print('\n # Não há registros!\n')

        print('---------------------')
        print('* Tarefas atrasadas:')
        print('---------------------')
        temp1 = temp[temp['Atraso'] == 1]
        if len(temp1.index) != 0:
            print(temp1.drop(['Conclusao', 'Atraso'], axis=1))
        else:
            print('\n # Não há registros!\n')

        print('-------------------')
        print('* Tarefas de hoje:')
        print('-------------------')
        # Isso é só uma inicialização
        dat = '01/01/1900'
        dat = datetime.strptime(dat, '%d/%m/%Y').date()
        dat = dat.today()
        temp2 = temp[temp['Data'] == str(dat)]
        if len(temp2.index) != 0:
            print(temp2.drop(['Conclusao', 'Atraso'], axis=1))
        else:
            print('\n # Não há registros!\n')
        print('~' * 47 + '\n')

        menu_tasks = ('1- Ver todas as tarefas', '2- Marcar tarefa como concluída', '3- Voltar ao menu anterior')
        print('~' * 47)
        print(' > Menu <                                     *')
        print('~' * 47)

        for i in menu_tasks:
            print(f'* {i: <43} *')
        print('~' * 47, end='')
        while True:
            choice = itype_validation('\n > ')
            if 0 < choice <= 3:
                break
            else:
                print(' # Opção inválida!')

        if choice == 1:
            print('-' * 48)
            if len(temp.index) != 0:
                print(temp.drop(['Conclusao', 'Atraso'], axis=1))
            else:
                print('\n # Não há registros!\n')
            print('-' * 48)
            print(' > Pressione enter para continuar...')
            keyboard.wait('enter')
            self.main_menu()

        elif choice == 2:
            temp = data_user
            codf = str(input('\n * Digite o código da tarefa para marcá-la como concluída: '))
            if codf not in str(temp['Cod']):
                print(' # Registro de tarefa inválido!')
                self.main_menu()
            else:
                for i in range(len(temp.index)):
                    if str(temp.iloc[i, 0]) == codf:
                        temp.iloc[i, 4] = 1
                        temp.iloc[i, 5] = 0
                        print('\n' + '-' * 33)
                        print('\n * Tarefa marcada como concluída!')
                        print('\n' + '-' * 33)

                try:
                    temp.to_csv('users/' + self.user + '.csv', index=False, encoding='ISO-8859-1')
                except:
                    print(' # Erro ao limpar tarefas concluídas!')
                    self.main_menu()

        elif choice == 3:
            self.main_menu()

    def register_task(self, data_user):
        while True:
            cod = randint(0, 1000)
            if cod not in data_user['Cod']:
                break

        print('~' * 50)
        task = str(input(' * Nome da tarefa: '))
        while True:
            try:
                str_date = str(input(' * Digite a data para a tarefa: '))
                dat = datetime.strptime(str_date, '%d/%m/%Y').date()
                break
            except:
                print(' # Data inválida!')

        while True:
            rate = itype_validation(' * Importância (1-5): ')
            if 0 < rate <= 5:
                break
            else:
                print(' # Entrada inválida!')

        if dat < dat.today():
            z = [cod, task, dat, rate, 0, 1]
        else:
            z = [cod, task, dat, rate, 0, 0]
        print('~' * 50)

        try:
            with open('users/' + self.user + '.csv', 'a', newline='') as reg:
                reg_writer = csv.writer(reg, delimiter=',')
                reg_writer.writerow(z)
        except:
            print(' # Erro de gravação! Tente novamente...\n')
            self.register_task(data_user)

        print(29 * '-' + '\n * Tarefa gravada com sucesso!\n' + 29 * '-' + '\n')
        self.main_menu()

    def completed_tasks(self, data_user):
        temp = data_user[data_user['Conclusao'] == 1]
        print('-' * 41)
        if len(temp.index) == 0:
            print(' # Você não possui tarefas concluídas!')
        else:
            print(temp.drop(['Conclusao', 'Atraso'], axis=1))
        print('-' * 41 + '\n')
        print('~' * 47)
        print(' > Menu <                                     *')
        print('~' * 47)
        aux = ['1- Limpar tarefas concluídas               *', '2- Voltar ao menu anterior                 *']

        for i in aux:
            print(' * ' + i)
        print('~' * 47)
        while True:
            choice = itype_validation('\n > ')
            if 0 < choice <= 2:
                break
            else:
                print(' # Opção inválida!')

        if choice == 1:
            temp = data_user[data_user['Conclusao'] == 0]
            try:
                temp.to_csv('users/' + self.user + '.csv', index=False, encoding='ISO-8859-1')
                print(' * Operação concluída com sucesso!')
                self.main_menu()
            except:
                print(' # Erro ao limpar tarefas concluídas!')
                self.completed_tasks(data_user)

        elif choice == 2:
            self.main_menu()

    def delete_task(self, data_user):
        exclusion_menu = ['1- Selecionar tarefa para exclusão', '2- Excluir todas tarefas atrasadas',
                    '3- Voltar ao menu anterior']
        print('\n' + '.' * 41)
        print(' > Menu <                               *')
        print('.' * 41)
        for i in exclusion_menu:
            print(' * ' + i)
        print('.' * 41)
        while True:
            choice = itype_validation('\n > ')
            if 0 < choice <= 3:
                break
            else:
                print(' # Opção inválida!')

        if choice == 1:
            temp = data_user
            print('\n' + '-' * 41)
            print(temp.drop(['Conclusao', 'Atraso'], axis=1))
            print('-' * 41)
            cod = str(input('\n * Digite o código da tarefa: '))
            if cod not in str(temp['Cod']):
                print('\n # Registro de tarefa não encontrado!')
                self.delete_task(data_user)
            else:
                for i in range(len(temp['Cod'])):
                    if str(temp.iloc[i, 0]) == cod:
                        temp = temp.drop(i, axis=0)
                        try:
                            temp.to_csv('users/' + self.user + '.csv', index=False, encoding='ISO-8859-1')
                            print("\n >>> Tarefa(s) excluídas com sucesso! <<<\n")
                            self.main_menu()
                        except:
                            print('\n # Erro ao deletar tarefas concluídas!')
                            self.delete_task(data_user)

        elif choice == 2:
            temp = data_user[data_user['Atraso'] == 1]
            if len(temp.index) == 0:
                print('\n # Não existem tarefas atrasadas!')
                self.delete_task(data_user)
            else:
                temp = data_user.drop(temp.index)
                try:
                    temp.to_csv('users/' + self.user + '.csv', index=False, encoding='ISO-8859-1')
                    print("\n >>> Tarefa(s) excluídas com sucesso! <<<\n")
                    self.main_menu()
                except:
                    print('\n # Erro ao deletar tarefas concluídas!\n')
                    self.delete_task(data_user)
        elif choice == 3:
            self.main_menu()


# main
