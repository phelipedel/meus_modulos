from utilidade import cor


#---------------------------------------------------------------------------------------


def linha(tam=42):
    return '_' * tam


#---------------------------------------------------------------------------------------



# cabecalho
def cabecalho(txt):
    print(f'{cor.verde}{linha()}')
    print(f'{cor.preto}{txt.center(42)}')
    print(f'{cor.verde}{linha()}')


#---------------------------------------------------------------------------------------



def arqivoExiste(nome):
    """

    :param nome: nome do arquivo gerado
    :return: se existe ou nao
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


#---------------------------------------------------------------------------------------



def criarArquivo(nome):
    """

    :param nome: gerar o arquivo
    :return: verificar se ocorreu algum erro, caso nao retorn confirmacao positiva
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'{cor.vermelho}Houve um ERRO na criacao do arquivo!!')
    else:
        print(f'{cor.ciano}Arquivo {nome} criado com sucesso')


#---------------------------------------------------------------------------------------



#leitura de arquivo
def lerarquivo(nome):
    try:
        a = open(nome, 'rt')

    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('Dados do arquivo ')
        for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{cor.azul}{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


#---------------------------------------------------------------------------------------



#cadastro de dados
def cadastrar(arq, nome='Desconhecido', idade=0):
    """

    :param arq: arquivo gerado
    :param nome: nome da pessoa que sera adificonada, OBS: MODELO A SER REAJUSTADO PARA TEXTO SQL
    :param idade: idade da pessoa adicionada
    :return: retorno de verificao de esse dado ja existe ou nao, ser adptado para confirmacao de tabela sql existe ou nao
    """
    try:
        a = open(arq, 'at')
    except:
        print(f'{cor.vermelho}Houve um ERRO na abertura do arquivo {arq}')
    else:
        try:
            a.write(f'{nome.capitalize()};{idade}\n')
        except:
            print(f'{cor.vermelho}Dados ja existente ')
        else:
            print(f'{cor.amarelo}Novo registro de {nome.capitalize()} adicionado.')
            a.close()