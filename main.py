import function

peta =  {'A':set(['B','C','D']),
         'B':set(['A','D']),
         'C':set(['A','D','E']),
         'D':set(['A','C','E','F','B']),
         'E':set(['D','C','G','F']),
         'F':set(['D','G','E']),
         'G':set(['F','E']),
         # 'H':set(['D','C','G','L']),
         # 'I':set(['C','J','K']),
         # 'J':set(['I']),
         # 'K':set(['L','I']),
         # 'L':set(['K','H'])
         }

print("\nDFS ")
print(function.dfs(peta,'B','E'))
print("\nBFS ")
print(function.bfs(peta,'B','E'))
print()
