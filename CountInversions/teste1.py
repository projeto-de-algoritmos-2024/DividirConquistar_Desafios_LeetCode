class Solution(object):
    def numberOfPermutations(self, n, requirements):
        MOD = 10**9 + 7
        
        req_map = {}
        max_inv = 0
        for end_i, cnt_i in requirements:
            req_map[end_i+1] = cnt_i
            if cnt_i > max_inv:
                max_inv = cnt_i
        
        # dp[i][c]: numero de permutacoes de tamanho i com c inversoes
        dp = [[0]*(max_inv+1) for _ in range(n+1)]
        dp[0][0] = 1
        
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0]
            for c in range(1, max_inv+1):
                val = dp[i][c-1] + dp[i-1][c]
                if c - i >= 0:
                    val -= dp[i-1][c - i]
                dp[i][c] = val % MOD
            
            if i in req_map:
                required = req_map[i]
                keep = dp[i][required]
                for c in range(max_inv+1):
                    dp[i][c] = 0
                dp[i][required] = keep
            
            print("dp após filtrar i =", i, ":", dp[i])
        
        return dp[n][req_map[n]] % MOD
