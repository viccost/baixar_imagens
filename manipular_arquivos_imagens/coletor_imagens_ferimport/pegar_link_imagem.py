from bs4 import BeautifulSoup
from requests import request
from typing import Union


class ColetorDeImagensFerimport:
    """Download the main product's image from a list of urls and skus, also is possible download directly with
    image's link"""

    def __init__(self, sku, url_imagem):
        self.sku = sku
        self.url = url_imagem

    def colect_getting_image_link_first(self) -> int:
        """it collects getting link from site before downloading"""
        url_imagem = self._get_link_imagem()
        if url_imagem != 0:
            status = self._download_image(url_imagem)
            return 200
        else:
            return 0

    def colect_download_directly(self) -> int:
        """it collects downloading directly, so you have already the image link"""
        status = self._download_image(self.url)
        return status

    def _get_link_imagem(self) -> Union[str, int]:
        """:return 0 if there's no content and 200 if everything is ok"""
        raw_html = request("GET",
                           f"{self.url}").content
        object_html = BeautifulSoup(raw_html, features="lxml")
        url_image = object_html.find("img",
                                     class_="vtex-store-components-3-x-productImageTag "
                                            "vtex-store-components-3-x-productImageTag--main")
        if not url_image:
            return 0
        else:
            src_image = url_image['src']
        return src_image

    def _download_image(self, url_imagem: str) -> int:
        """download images using vtex exportation spreadsheet
        :return 0 if there's no content and 200 if everything is ok"""
        img = request("GET", url_imagem).content
        if img:
            nome = f"{self.sku}"
            with open(f'baixar/{nome}.webp', 'wb') as handler:
                handler.write(img)
            return 200
        else:
            return 0
