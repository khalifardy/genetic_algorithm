#%%
import numpy as np
import random
import math
#%%
def insialisasi(populasi,bit):
    hasil = []
    
    
    while len(hasil) <populasi:
        temp = []
        for _ in range(bit):
            temp.append(random.randint(0,1))
        hasil.append(temp)
    
    return hasil


# %%
p = insialisasi(10,6)
# %%
def penyebut(n):
    hasil = 0
    for i in range(n):
        hitung = 1/(2**(i+1))
        hasil += hitung
    
    return hasil

def dekode(r_min,r_max,bit,individu):
    x_list = individu[:bit//2]
    y_list = individu[bit//2:]
    pembagi = penyebut(bit//2)
    pengali = (r_max - r_min)/pembagi
    pengali_2_x = 0
    pengali_2_y = 0

    

    for i,j in enumerate(x_list):
        pengali_2_x += j*(1/(2**(i+1)))
    
    x = r_min + pengali * pengali_2_x

    for i,j in enumerate(y_list):
        pengali_2_y += j*(1/(2**(i+1)))
    
    y = r_min + pengali * pengali_2_y

    return (x,y)


        

# %%
x,y = dekode(-5,5,6,p[9])
print(x,y)
# %%
def fitness(x,y):
    pembilang = math.cos(x) + math.sin(x)
    penyebut = x**2 + y **2

    return pembilang/penyebut

def select_parent(populasi):
    parent = []
    fitness_value = [fitness(dekode(-5,5,6,i)[0],dekode(-5,5,6,i)[1]) for i in populasi]

    total_fitness_value = 0
    for i in fitness_value:
        total_fitness_value += i


    probabilitas = [round(i/total_fitness_value,2) for i in fitness_value]

    while len(parent)<2:
        prob = round(random.random(),2)

        for i,j in enumerate(probabilitas):
            if j == prob and populasi[i] not in parent:
                parent.append(populasi[i])
        
    
    return parent


# %%

parent = select_parent(p)

# %%
def crossover(parent,bit):
    slic = random.randint(0,bit-1)
    parent1 = parent[0]
    parent2 = parent[1]

    kid1= []
    kid2= []

    kid1.extend(parent1[:slic])
    kid1.extend(parent2[slic:])
    kid2.extend(parent2[:slic])
    kid2.extend(parent1[slic:])

    return (kid1,kid2)

    

    
# %%
kid = crossover(parent,6)

# %%

def mutasi(kids,bit):
    for i in range(bit):
        if kids[0][i] ==0:
            kids[0][i] = 1
        else:
            kids[0][i] = 0
        
        if kids[1][i] ==0:
            kids[1][i] = 1
        else:
            kids[1][i] = 0
    
    return kids



# %%
new_kid = mutasi(kid,6)
# %%

def pembanding(populasi):
    high = ""
    temp =0
    index = ""
    new_fitness = [fitness(dekode(-5,5,6,i)[0],dekode(-5,5,6,i)[1]) for i in populasi]

    for i,j in enumerate(new_fitness):
        if  high=="":
            temp = j
            high = populasi[i]
            index = i
        else :
            if temp <= j :
                temp = j
                high = populasi[i]
                index=i
    
    return (high,index)
                



def select_generasi(population,kid,jumlah_populasi):
    new_generation = []
    extend_generation=population.copy()
    for i in kid:
        if i not in population:
            extend_generation.append(i)
    
    while len(extend_generation)>0:
        generasi,index = pembanding(extend_generation)
        new_generation.append(generasi)
        extend_generation.pop(index)

    return new_generation[:jumlah_populasi]

# %%
new_populasi = select_generasi(p,new_kid,10)
# %%
