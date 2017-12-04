
# --------------- Python 47 ---------------
# ----- Tabelarni pregled stepenovanja ----

# Tabelarni pregled stepenovanja eksponentom od 2 do 10

niz1 = "{0:>2}{1:>5}{2:>6}{3:>7}{4:>8}{5:>9}{6:>10}{7:>10}{8:>11}{9:>12}"
niz2 = "{0:>2}{1:>6}{2:>6}{3:>7}{4:>8}{5:>9}{6:>9}{7:>10}{8:>11}{9:>12}"

print("------ Tabelarni pregled stepenovanja brojeva 1-10 eksponentom od 2 do 10 ------")

print(niz2.format('n', 'n**2', 'n**3', 
                      'n**4', 'n**5', 'n**6',
                      'n**7', 'n**8', 'n**9', 
                              'n**10'))
print("--------------------------------------------------------------------------------")

for n in range(1, 11):
    print(niz1.format(n, n**2, n**3, 
                        n**4, n**5, n**6, 
                              n**7, n**8, n**9, 
                                    n**10))
        
    
