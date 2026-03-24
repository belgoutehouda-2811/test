notes  = []
with open("notes(admis-recale).txt","r") as f :
    for ligne in f :
        for n in ligne.split():
            notes.append(float(n))

moyenne = sum(notes) / len(notes)
print(round(moyenne, 2))

with open ("notes.txt","w") as f2:
    for note in notes:
        statut="admis" if note >= 10 else "recale"
        f2.write(f"{note:.1f} {statut}\n")
        print(f"{note:.1f} {statut}")