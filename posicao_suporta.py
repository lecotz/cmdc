def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    tamanho_mapa = len(mapa)
    if linha < 0 or coluna < 0 or (orientacao == 'v' and linha + blocos > tamanho_mapa) or (orientacao == 'h' and coluna + blocos > tamanho_mapa):
        return False
    for i in range(blocos):
        if orientacao == 'v':
            if mapa[linha + i][coluna] != ' ':
                return False
        else:  
            if mapa[linha][coluna + i] != ' ':
                return False

    return True
