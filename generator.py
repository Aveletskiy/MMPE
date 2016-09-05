import numpy as np

arrayX = range(1, 101)
arrayY = np.random.randint(0, 40, 100)
print(arrayX, arrayY)
f = open('data.tsv', 'w')

array2d = map(lambda x, y: [x, y], arrayX, arrayY)
[f.write(str(x) + '\t' + str(y) + '\n') for x, y in array2d]

f.close()
