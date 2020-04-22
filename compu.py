import itertools

#start dice donde empieza
#step el paso
counter = itertools.count(start = 5,step= 2.5)

data = [100,200,300,400]
#los mete a una tupla con un numero
daily_data = list(zip(itertools.count(), data))

print(daily_data)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

letters = ["a","b","c","d"]
numbers = [0,1,2,3,4,5]
names = ["Corey", "Nicole"]

#podemos hacer combinaciones y permutaciones
result = itertools.combinations(letters, 2)

for item in result:
	print (item)

#combinamos distintas listas
combined = itertools.chain(letters, numbers, names)

for item in combined:
	print(item)


#GroupBy

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

def get(person):
	return person["state"]

dog = itertools.groupby(people, get)

d = {}
for key, group in dog:
	d[key] = len(list(group))

print(d)

max_key = max(d, key=d.get)

print(max_key)
	