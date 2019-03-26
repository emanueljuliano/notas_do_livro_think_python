import pickle #necessário usar pickle pois bancos de dados apensa aceitam string
t = [1, 2, 3]
print(pickle.dumps(t))

t1 = [1, 2, 3, 4]
s = pickle.dumps(t1) #transforma objeto em string
t2 = pickle.loads(s) #reconstrói objeto
print(t2)
print(t1 == t2)
print(t1 is t2)

#ação se tornou tão comum que encapsularam em um módulo chamado #shelve

