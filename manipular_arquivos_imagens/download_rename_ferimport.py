"""Module used to download ferimport's images from internet and also rename it, THE LINKS MUST BE IN A SPREADSHEET """

import requests
from salvar_ajustar.salvar_ajustar import gerar_dataframe, escolher_arquivo
from pandas import DataFrame
from typing import Set


def dowload_images(exportation: DataFrame, list_skus: Set) -> None:
    """download images using vtex exportation spreadsheet, configure the output name. Downloads all sku's image."""
    COLUMN_NAME_KEY = "_SkuId"
    COLUMN_TRANSPOSE = 'URL Imagem'
    for sku in list_skus:
        sku_mask = (exportation[COLUMN_NAME_KEY] == sku)
        df = exportation[sku_mask]
        progress = 0
        for url_imagem in df[COLUMN_TRANSPOSE]:
            progress += 1
            print(f'Processing... {progress}')
            img = requests.get(url_imagem).content
            nome = f"{sku}-0{progress}"
            with open(f'baixar/{nome}.webp', 'wb') as handler:
                handler.write(img)


if __name__ == "__main__":
    data = gerar_dataframe(escolher_arquivo())
    list_sku = set(data['_SkuId'].to_list())
    dowload_images(data, list_sku)
