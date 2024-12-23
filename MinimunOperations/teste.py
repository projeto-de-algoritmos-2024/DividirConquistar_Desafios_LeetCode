class Solution(object):
    def minimumOperations(self, raiz):
        """
        :type raiz: Optional[TreeNode]
        :rtype: int
        """
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
      
        return 0
