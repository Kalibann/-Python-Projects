def font(cor):
    # 1 = claro; 2 = escuro; NULL = normal

    preto = '\033[1;30m'
    vermelho = '\033[1;31m'
    verde = '\033[1;32m'
    amarelo = '\033[1;33m'
    azul = '\033[1;34m'
    magenta = '\033[1;35m'
    ciano = '\033[1;36m'
    cinza1 = '\033[1;37m'
    cinza2 = '\033[1;90m'
    vermelho1 = '\033[1;91m'
    verde1 = '\033[1;92m'
    amarelo1 = '\033[1;93m'
    azul1 = '\033[1;94m'
    magenta1 = '\033[1;95m'
    ciano1 = '\033[1;96m'
    branco = '\033[1;97m'
    negrito = '\033[;1m'
    inverte = '\033[;7m'
    reset = '\033[0;0m'
    listacor = preto, vermelho, verde, amarelo, azul, magenta, ciano, cinza1, cinza2, vermelho1, verde1, amarelo1, azul1, magenta1, ciano1, branco, negrito, inverte, reset
    listacorstr = 'preto', 'vermelho', 'verde', 'amarelo', 'azul', 'magenta', 'ciano', 'cinza1', 'cinza2', 'vermelho1', 'verde1', 'amarelo1', 'azul1', 'magenta1', 'ciano1', 'branco', 'negrito', 'inverte', 'reset'
    tam = len(listacor)
    i = 0
    j = 0
    while i < tam:
        if cor == listacorstr[i]:
            j = 1
            return listacor[i]
        else:
            j = 0
        i += 1
    if j == 1:
        return reset
