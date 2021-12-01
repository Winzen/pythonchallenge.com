charada = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw
#rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""
resultado = "map"

def decodificador(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    corret = ''
    for letra in text:
        if letra in abc:
            local = abc.find(letra)
            correta_letra = abc[local+2] if local+2 < 26 else abc[local+2-26]
            corret += correta_letra
        else:
            corret += letra
    return corret

if __name__ == '__main__':
    print(decodificador(charada))
    print(decodificador(resultado))

#Respota: ocr


