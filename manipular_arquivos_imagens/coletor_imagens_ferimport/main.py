from pegar_link_imagem import ColetorDeImagensFerimport
from spreadsheet_map import SpreadSheetImagesMap
from salvar_ajustar.salvar_ajustar import escolher_arquivo, gerar_dataframe, salvar_arquivo_planilha
from time import sleep
from pandas import DataFrame

print('É necessário uma planilha com as colunas (sku, url)')
spreadsheet_map = SpreadSheetImagesMap(gerar_dataframe(escolher_arquivo()))
records_to_colect = spreadsheet_map.records

progress = 0
size = len(records_to_colect)
for record in records_to_colect:
    progress += 1
    print(f"{progress} de {size}...")
    sleep(1.0)
    coletor = ColetorDeImagensFerimport(record['sku'], record['url'])
    statuscode = coletor.colect_getting_image_link_first()
    if statuscode == 200:
        status = "Sim"
    else:
        status = "Não"
    record['baixou'] = status

spreadsheet_map = DataFrame(records_to_colect)
salvar_arquivo_planilha(spreadsheet_map, "TESTE", "xlsx")






