from pandas import DataFrame
from typing import List


class SpreadSheetImagesMap:
    """A planilha só precisa ter duas colunas, sku e url"""
    def __init__(self, spreadsheet_map: DataFrame):
        self._COLUMN_NAME_KEY = "sku"
        self._COLUMN_NAME_URL = 'url'
        self._records = spreadsheet_map.to_dict(orient="records")

    @property
    def records(self) -> List:
        """:return return data as list of dicts"""
        return self._records


