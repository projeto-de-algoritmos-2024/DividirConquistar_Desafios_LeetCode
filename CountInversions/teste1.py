class Solution(object):
    def numberOfPermutations(self, n, requirements):
        MOD = 10**9 + 7
        
        # Descobrir o maximo de inversoess necessario
        max_inv = 0
        for end_i, cnt_i in requirements:
            if cnt_i > max_inv:
                max_inv = cnt_i
        
        ## dp[i][c] será a quantidade de permutações de tamanho i com c inversoes
        dp = [[0]*(max_inv+1) for _ in range(n+1)]
        dp[0][0] = 1 
        
        for i in range(1, n+1):
            for c in range(max_inv+1):
                dp[i][c] = dp[i-1][c]
  
        print("DP gerada (incompleta):")
        for i in range(n+1):
            print("i =", i, ":", dp[i])
        
        return dp[n][0] % MOD
