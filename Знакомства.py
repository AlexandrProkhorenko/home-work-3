boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


boys_sort = sorted(boys)

girl_sort = sorted(girls)


w = zip(boys_sort,girl_sort)

if len(boys) == len(girls):
    for elem in w:
        print(elem[0], elem[1])

else:
    print('У нас не одинаковое количество парней и девушек')
