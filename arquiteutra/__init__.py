from utilidade import cor


def linha(tam=42):
    return '_' * tam


#---------------------------------------------------------------------------------------


# cabecalho
def cabecalho(txt):
    print(f'{cor.verde}{linha()}')
    print(f'{cor.preto}{txt.center(42)}')
    print(f'{cor.verde}{linha()}')


#---------------------------------------------------------------------------------------


# Tratamento de erro
def verificarErro(msg):

    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cor.vermelho}ERRO: por favor, digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print(f'{cor.vermelho}USUARIO preferiu nao digitar esse numero.')
            return 0
        else:
            return n



#---------------------------------------------------------------------------------------


# menu opcao
def menu(lista):
    """

    :param lista: lista de menu de opcoes gerada
    :return: retorno final de looping de opc caso queira continuar
    """
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{cor.amarelo}{c}º ⇒ {cor.azul}{item}')
        c += 1
    print(cor.verde, linha())
    opc = verificarErro(f'{cor.branco}Sua Opcao:')
    return opc
