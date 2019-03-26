import dbm
db = dbm.open('captions', 'c') #c significa que deve ser criado caso não exista
db['cleese.png'] = 'Photo of John Cleese'
print(db['cleese.png']) #retorna um objeto bytes
db['cleese.png'] = 'Photo of John Cleese doing a silly walk'
print(db['cleese.png'])

for key in db:
    print(key, db[key])

db.close()
