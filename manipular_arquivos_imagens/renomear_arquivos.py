import os
import shutil
from time import sleep
from salvar_ajustar.salvar_ajustar import escolher_arquivo, gerar_dataframe, escolher_pasta


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
    """move files renaming them. YOU SHOULD CREATE A BACKUP FILE"""
    from time import sleep

    def to_str(array: list) -> list:
        """convert all element's list to str"""
        array = [str(value) for value in array]
        return array

    folder_from = escolher_pasta()
    folder_to = escolher_pasta()
    planilha_mapa = gerar_dataframe(escolher_arquivo())
    files_in_folder = os.listdir(folder_from)
    nome_from = to_str(planilha_mapa['old'].tolist())
    nome_to = to_str(planilha_mapa['new'].tolist())

    try:
        for index, file in enumerate(nome_from):
            if file in files_in_folder:
                correcao = nome_to[index]
                print(f"Substituindo {file} por {correcao}")
                os.rename(folder_from + '\\' + f'{file}', folder_to + '\\' + f'{correcao}')
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

def renomearImagensComNomePasta():
    folderPath = r'C:\Users\Victor\Desktop\Imagens Bosch P3 (17) Movido 01'
    for folderName in os.listdir(folderPath):
        c = 2
        for item in os.listdir(folderPath + "\\" + folderName):
            primeiro = False
            if item == '01.jpg' or item == '001.jpg':
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


renomear_varios_arquivos()

# será interessante tratar a extensão dos arquivos... por exemplo se houver diferentes extensões em uma pasta
