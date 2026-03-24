def est_bi_stochastique(matrice):
    n = len(matrice)

    if not all(len(row) == n for row in matrice):
        return False

    
    for ligne in matrice:
        if not all(0 <= x <= 1 for x in ligne):
            return False

    
    for i, ligne in enumerate(matrice):
        if not abs(sum(ligne) - 1.0) < 1e-9:
            return False

   
    for j in range(n):
        somme_colonne = sum(matrice[i][j] for i in range(n))
        if not abs(somme_colonne - 1.0) < 1e-9:
            return False

    return True

