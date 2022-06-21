import os.path
import shutil
import glob
import requests
from PIL import Image

folderImagens = r'C:\Users\Victor\Desktop\1'
folderDestino = r'C:\Users\Victor\Desktop\2'
imagensNaoEncontradas = []


def baixarImagem(nome, url):
    imagemUrl = url
    imagemData = requests.get(imagemUrl).content
    with open(folderImagens + fr'\{nome}.png', 'wb') as handler:
        handler.write(imagemData)


def redimensionarImagem(nome):
    image_path = folderImagens + fr'\{nome}'
    try:
        image = Image.open(image_path, 'r')
        image_size = image.size
        width = image_size[0]
        height = image_size[1]
        if width != height:
            bigside = width if width > height else height
            background = Image.new('RGB', (bigside, bigside), (255, 255, 255, 255))
            offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2), 0)))
            background.paste(image, offset)
            background.save(folderDestino + fr'\{nome}')  # verificar se precisa do .jpg
            print("{}Imagem tratata!{}".format("\033[32m", "\033[m"))
        else:
            print("{}A imagem já está 1:1!{}".format("\033[33m", "\033[m"))
            shutil.copyfile(folderImagens + fr'\{nome}',
                            folderDestino + fr'\{nome}')
    except FileNotFoundError:
        print("{1}{0} não encontrado{2}".format(nome, '\033[31m', '\033[m'))
        imagensNaoEncontradas.append(nome)


c = 1
for file in glob.glob(fr'{folderImagens}\*.jpg'):
    redimensionarImagem(os.path.basename(file))
    print(c)
    c += 1
