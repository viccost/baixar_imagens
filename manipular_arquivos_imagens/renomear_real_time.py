import glob
import os
from time import sleep
import requests
from salvar_ajustar.salvar_ajustar import gerar_dataframe, escolher_arquivo

# pasta que o script deve trackear
folderPath = r'C:\Users\Victor\Downloads\1'
# pasta que o script deve destinar o arquivo renomeado
folderDestino = r'C:\Users\Victor\Downloads\2'


def aguardarDownload(novoNomeArquivo):
    sleep(0.5)
    contador = 0
    # mapeia quantos arquivos há na pasta antes do download, apenas arquivos, não pastas
    numArquivosPath_ = len([f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))])

    # aguardando iniciar download, identificando através da contagem de arquivos
    while True:
        contador += 1
        sleep(1)
        numAttArquivosPath = len([f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))])
        if numAttArquivosPath != numArquivosPath_:
            print(f'Novo elemento encontrado. Renomeando')
            break

    def renomearImagem():
        sleep(2)
        tipoArquivo = r'\*'
        arquivos = glob.glob(folderPath + tipoArquivo)
        ultimoArquivo = max(arquivos, key=os.path.getctime)
        os.rename(rf'{ultimoArquivo}',
                  fr'C:\Users\Victor\Desktop\Imagens\{novoNomeArquivo}.webpg')  # como ignorar a extensão
        print('{}Renomeado.{}'.format("\033[32m", "\033[m"))
    return renomearImagem()


if __name__ == "__main__":
    file = gerar_dataframe(escolher_arquivo())
    file = file.to_dict(orient='records')

    progress = 1
    for detail in file:
        print(f'Processing... {progress}')
        img = requests.get(detail['url']).content
        nome = detail['name']
        with open(f'{nome}.webp', 'wb') as handler:
            handler.write(img)
