"""Module used to download images from internet and also rename its
"""

import requests
from salvar_ajustar.salvar_ajustar import gerar_dataframe, escolher_arquivo


if __name__ == "__main__":
    file = gerar_dataframe(escolher_arquivo())
    file = file.to_dict(orient='records')

    progress = 0
    for detail in file:
        progress += 1
        print(f'Processing... {progress}')
        img = requests.get(detail['url']).content
        nome = detail['name']
        with open(f'{nome}.png', 'wb') as handler:
            handler.write(img)
