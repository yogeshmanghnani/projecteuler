#File created by Yogesh Manghnani

listOfAllTheDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listOfPermutations = []
for a in listOfAllTheDigits:
    lista = listOfAllTheDigits[:]
    lista.remove(a)
    for b in lista:
        listb = lista[:]
        listb.remove(b)
        for c in listb:
            listc = listb[:]
            listc.remove(c)
            for d in listc:
                listd = listc[:]
                listd.remove(d)
                for e in listd:
                    liste = listd[:]
                    liste.remove(e)
                    for f in liste:
                        listf = liste[:]
                        listf.remove(f)
                        for g in listf:
                            listg = listf[:]
                            listg.remove(g)
                            for h in listg:
                                listh = listg[:]
                                listh.remove(h)
                                for i in listh:
                                    listi = listh[:]
                                    listi.remove(i)
                                    for j in listi:
                                        listj = listi[:]
                                        listj.remove(j)
                                        permutation = int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j))
                                        listOfPermutations.append(permutation)
                                        

listOfPermutations.sort()
print(listOfPermutations[999999])
                                        
                            