import itertools as it
import numpy as np

def random_vector(list, grados, iterations=1000):
    np.zeros(shape=(grados,iterations))
    for p_carga in list:
        p_carga[0] = min_
        p_carga[1] = max_
        p_carga[2] = step
        p_carga[3] = percent
        p_carga[4] = position
        
        x = list(range(min_,max_+1,step)
        
    

x = list(range(-15,16,1))
#data = np.arange(0,15,1)
#print(len(data))
y = list(range(-35,36,1))
#y = np.arange(-10,-35,-1)

z = list(range(-100,101,1))
#z = np.arange(34,100,1)

a = list(range(-150,151,1))
#a = np.arange(0,150,1)

w = list(it.product(x,y,z,a))
#w = np.array(it.product(data,y,z,a))

#print(data, y, z)

#print(w)

print(len(w))

filtered = []

for i in w:
    if i[0] < max(x) and \
       i[1] < max(y) * 0.35 and \
       i[2] < max(z) * 0.5 and \
       i[3] < max(a) * 0.75:
        filtered.append(i)

print(len(filtered))

e = np.random.randint(0,high=len(filtered), size=1000)

sample = []

for i in e:
    sample.append(filtered[i])
    print(filtered[i])
print(len(sample))

#f = np.random.uniform(0, len(filtered), 1000)

#sample2 = []

#for uds in f:
#    sample.append(filtered[uds])
#    print(filtered[uds])

