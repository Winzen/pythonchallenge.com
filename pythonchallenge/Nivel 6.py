import re
import zipfile


def get_order_extract():

    """RETORNA lista com a ordem correta para extração dos comentarios zips"""

    txts_list = []
    inicio = "90052"
    while inicio:

        txt = open(rf"channel\{inicio}.txt", "r").read()
        txts_list.append(inicio)
        n = re.findall("(\d.*)", txt, re.UNICODE)

        inicio = n[0] if len(n) > 0 else False
    return txts_list


def extract_comments_zip(lista_order):

    """Apartir da lista da ordem de txt. Retorna comentarios zips"""

    li = []
    zp = zipfile.ZipFile(r"channel.zip", mode="r")
    for files in lista_order:

        letra = re.findall("b'(\S)'", str(zp.getinfo(f"{files}.txt").comment), re.UNICODE)

        li.append(letra) if letra else ""

    zp.close()
    return li


def pega_unicos(lista):

    """De uma lista retorna uma string com os elementos unicos"""
    sinais_list = []
    for linhas in lista:
        for sinal in linhas:
            sinais_list.append(sinal) if sinal not in sinais_list else None
    unicos = "".join(sinais_list)
    print(unicos)
    return unicos


if __name__ == '__main__':
    order = get_order_extract()
    extract = extract_comments_zip(order)
    unics = pega_unicos(extract)
