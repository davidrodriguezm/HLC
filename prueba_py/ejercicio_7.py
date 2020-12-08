d1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
d2 = {'uno':1,'dos':2}
d3 = {'five': 5, 'six': 6}

print('valor three=',d1.get('three'),'valor five=',d1.get('five','no hay'))
print(d2,' elementos:',len(d2))
d2.clear()
print(d2,' elementos:',len(d2))
d2 =d1.copy()
print(d2,' elementos:',len(d2))
print('quito el one:',d2.pop('one'))
print(d2,' elementos:',len(d2))
d1.update(d3)
for clave,valor in d1.items():
    print(clave,":",valor,end=",")