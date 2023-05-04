from library import insialisasi,select_parent,crossover,mutasi,select_generasi,dekode,fitness

p = insialisasi(10,6)

for i in range(100):
    parent = select_parent(p)
    kids = mutasi(crossover(parent,6),6)
    p = select_generasi(p,kids,10)
    x,y = dekode(-5,5,6,p[0])
    fit = fitness(x,y)
    print(
        "Generasi {}: x={},y={},fitness={}".format(i+1,x,y,fit)
    )

    



