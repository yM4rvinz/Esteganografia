from textwrap import wrap
from PIL import Image
from PIL import ImageColor
from math import sqrt
import vigenere
import numpy

def decode():
    img = Image.open("encoded.png")
    pixels = img.load()
    width, height = img.size
    lista = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            lista.append(f"{r:02x}{g:02x}{b:02x}")
    lista = "".join(lista)
    lista = vigenere.decode(lista, senha, "0123456789abcdef")
    with open("decoded.txt", "w") as f:
        f.write(str(bytes.fromhex(lista).decode('utf-8')))
    print("Informações traduzidas com sucesso em decoded.txt")

def encode():
    palavra = str(open("input.txt", "r", encoding="utf8").read())
    codigosrgb = []
    listahex1 = []
    palavra1 = palavra[:]
    z = 0
    if ((len(palavra.encode("utf-8").hex())/2) % 3) != 0:
        palavra1 = list(palavra)
        for x in range(0, 3 - ((len(palavra.encode("utf-8").hex())//2) % 3)):
            palavra1.append(" ")
        palavra1 = "".join(palavra1)
    y = vigenere.encode(palavra1.encode("utf-8").hex(), senha, "0123456789abcdef")
    for x in range(0, len(wrap(y, 6))):
        listahex1.append("#" + wrap(y, 6)[x])
        codigosrgb.append(ImageColor.getcolor(listahex1[x], "RGB"))
    N = int(sqrt(len(listahex1)))
    while True:
        if len(listahex1) % N == 0:
            altura = N
            largura = len(listahex1) // N
            break
        else:
            N += 1
    data = numpy.zeros((largura, altura, 3), dtype=numpy.uint8)
    for x in range(0, largura):
        for y in range(0, altura):
            data[x, y] = codigosrgb[z]
            z += 1
    image = Image.fromarray(data)
    image.save("encoded.png")
    print("Informação escondida com sucesso em encoded.png")

escolha = int(input("ENCODE[1] ou DECODE[2]? "))
senha = input("digite a senha: ").encode("utf-8").hex()
if escolha == 1:
    encode()
elif escolha == 2:
    decode()
