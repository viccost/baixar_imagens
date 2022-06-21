import os
import shutil
from time import sleep


def see_files():
    """Apenas lista os arquivos na pasta"""
    import glob
    folderPath = r'C:\Users\Ferimport\Desktop\Para jogar no servidor'
    # todos os tipos de arquivo
    fileType = r"\*"
    files = glob.glob(folderPath + fileType)
    print(os.listdir(folderPath))
    #  max_file = max(files, key=os.path.getctime) >>> exemplo de ordem, pegando o arquivo mais atual nesse caso


def renomear_varios_arquivos():  # substituindo os nomes errados por novos corretos
    """Movimenta os arquivos contidos em uma pasta e em uma lista qualquer para outra pasta com nomes corrigidos"""
    from time import sleep
    folderPath = r'C:\Users\Ferimport\Desktop\1'
    folderPathDestino = r'C:\Users\Ferimport\Desktop\2'
    arquivosNaPasta = os.listdir(folderPath)
    # OLD example:                                                    · list comprehension
    # arquivosNaPasta = [nome.replace(f'{extensaoImagem}', '') for nome in arquivosNaPasta]
    arquivosParaSeremCorrigidos = []
    # com o auxilio do dir > list.csv teremos todos os arquivos na pasta. É necessário fornecer as correções
    # através de um dicionário, ou outra estrutura.
    dictCorrecoes = {}
    try:
        for arquivoParaCorrecao in arquivosParaSeremCorrigidos:
            if str(arquivoParaCorrecao) in arquivosNaPasta:
                correcao = dictCorrecoes[arquivoParaCorrecao]
                print(f"Substituindo {arquivoParaCorrecao} por {correcao}")
                os.rename(folderPath + '\\' + f'{arquivoParaCorrecao}', folderPathDestino + '\\' + f'{correcao}')
                sleep(2)
    except FileNotFoundError as e:
        print(f'033[31mArquivo não encontrado:033[m {e}')


def renomear_varios_arquivos_subpastas():
    """Faça backup de seus arquivos antes de usar!"""
    # exemplo com subpastas, não pode haver outras pastas senão aquelas que deseja renomear. Além disso, deve conter
    # apenas pastas, e não arquivos.

    folderPath = r'C:\Users\Ferimport\Desktop\jj'
    for folderName in os.listdir(folderPath):  # identificando todas as pastas no PATH
        fileNumber = 1
        for fileName in os.listdir(folderPath + "\\" + folderName):
            os.rename(folderPath + '\\' + folderName + '\\' + fileName,
                      folderPath + '\\' + folderName + '\\' + f'{fileName}.jpg')
            print(f"Arquivo [{fileNumber}] renomeado!")
            fileNumber += 1


def excluirPng():
    folderPath = r'C:\Users\Victor\Desktop\Imagens'
    for folderName in os.listdir(folderPath):
        for item in os.listdir(folderPath + "\\" + folderName):
            if item.endswith(".png"):
                os.remove(os.path.join(folderPath, folderName, item))
                print(f'Arquivo {os.path.basename(item)} removido')


def moverLocal():
    folderPath = r'C:\Users\Victor\Desktop\Imagens Bosch P3 (17)'
    folderPath_2 = r'C:\Users\Victor\Desktop\Imagens Bosch P2 (17) Movido'
    for folderURL in os.listdir(folderPath):
        for folder in os.listdir(folderPath + "\\" + folderURL):
            pastaCriada = folderPath_2 + '\\' + folderURL
            os.makedirs(pastaCriada)
            sleep(0.8)
            for item in os.listdir(folderPath + "\\" + folderURL + "\\" + folder):
                shutil.move(folderPath + '\\' + folderURL + '\\' + folder + '\\' + item,
                            pastaCriada + '\\' + item)
                print(f"Arquivo [{item}] movido!")


def renomearImagensComNomePasta():
    folderPath = r'C:\Users\Victor\Desktop\Imagens Bosch P3 (17) Movido 01'
    for folderName in os.listdir(folderPath):
        c = 2
        for item in os.listdir(folderPath + "\\" + folderName):
            primeiro = False
            if item == '01.jpg' or item =='001.jpg':
                primeiro = True
                c1 = 1
                photoNumber = f'00{c1}'
                os.rename(folderPath + '\\' + folderName + '\\' + item,
                          folderPath + '\\' + folderName + '\\' + f'{photoNumber}.jpg')
            if c < 10:
                photoNumber = f'00{c}'
            else:
                photoNumber = f'0{c}'
            if not primeiro:
                os.rename(folderPath + '\\' + folderName + '\\' + item,
                          folderPath + '\\' + folderName + '\\' + f'{photoNumber}.jpg')
                c += 1

        print(f"Arquivo [{item}] renomeado!")
        c += 1


renomearImagensComNomePasta()

# será interessante tratar a extensão dos arquivos... por exemplo se houver diferentes extensões em uma pasta
