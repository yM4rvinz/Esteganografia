def alfabetar(alfabeto):
    alfabeto2 = alfabeto[:] * 2
    for x in range(0, len(alfabeto)):
        globals()["listaR{}".format(x)] = alfabeto2[x:(x + len(alfabeto))]

def encode(texto, chave, alfabeto):
    alfabetar(alfabeto)
    saida = []
    if len(texto) / len(chave) != 1:
        if len(chave) < len(texto):
            chave = chave[:] * ((len(texto) // len(chave)) + 1)
        for i in range(len(texto), len(chave)):
            chave = chave[:len(texto)] + chave[len(texto) + 1:]
    for x in range(0, len(texto)):
        saida.append(globals()["listaR{}".format(alfabeto.index(chave[x]))][alfabeto.index(texto[x])])
    return "".join(saida)

def decode(saida, chave, alfabeto):
    alfabetar(alfabeto)
    texto = []
    if len(saida) / len(chave) != 1:
        if len(chave) < len(saida):
            chave = chave[:] * ((len(saida) // len(chave)) + 1)
        for i in range(len(saida), len(chave)):
            chave = chave[:len(saida)] + chave[len(saida) + 1:]
    for x in range(0, len(saida)):
        texto.append(alfabeto[globals()["listaR{}".format(alfabeto.index(chave[x]))].index(saida[x])])
    return "".join(texto)