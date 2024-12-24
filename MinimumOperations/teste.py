class Solution(object):
    def minimumOperations(self, raiz):
        if not raiz:
            return 0
        
        niveis = []
        fila = [raiz]
        
        while fila:
            tamanho_nivel = len(fila)
            nivel_atual = []
            nova_fila = []
            for no in fila:
                nivel_atual.append(no.val)
                if no.left:
                    nova_fila.append(no.left)
                if no.right:
                    nova_fila.append(no.right)
            niveis.append(nivel_atual)
            fila = nova_fila
        
        operacoes_totais = 0
        
        for nivel in niveis:
            ordenado = sorted(nivel)
            mapa_posicao = {valor: i for i, valor in enumerate(ordenado)}
            visitado = [False] * len(nivel)
            
            for i in range(len(nivel)):
                if visitado[i] or mapa_posicao[nivel[i]] == i:
                    continue
                ciclo_tamanho = 0
                j = i
                while not visitado[j]:
                    visitado[j] = True
                    j = mapa_posicao[nivel[j]]
                    ciclo_tamanho += 1
                if ciclo_tamanho > 0:
                    operacoes_totais += (ciclo_tamanho - 1)  # CORRECAO: ciclo_tamanho - 1
        
        return operacoes_totais