# Вычисляет значение фитнес функции для элемента популяции
def fitnes(element):
    x = element[0]
    y = element[1]
    return (x-3*y-1) / (3*x**2 + 3*y**2 + 1)

# Вычисляет сумму всех значений фитнес функции
def sum_fitness(population):
    total_sum = 0
    for element in population:
        total_sum += element[1]

    return total_sum

# Вычисляет максимальное значение фитнес функции
def max_fitnes(population):
    temp = list()
    for element in population:
        temp.append(element[1])

    return max(temp)

# Функция реализует возможность размножения популяции
# с учетом наложенного заданием ограничения
#
# Параметры:
#    population - Списки (list) - популяция хромосом
# Возвращаемое значение:
#    Список (list) - популяция после размножения
def reproduction(population):
    a = population[0][0]
    b = population[1][0]
    c = population[2][0]

    b1 = [ b[0], a[1] ]
    c1 = [ c[0], a[1] ]
    b2 = [ a[0], b[1] ]
    c2 = [ a[0], c[1] ]

    new_population = list()
    new_population.append( [b1, fitnes(b1)] )
    new_population.append( [c1, fitnes(c1)] )
    new_population.append( [b2, fitnes(b2)] )
    new_population.append( [c2, fitnes(c2)] )

    return new_population
#
# Исходные данные
#
population = [
    #  x,   y,  fitnes
    [ [-2, -2], 0],     # P1
    [ [-1, -1], 0],     # P2
    [ [ 0,  0], 0],     # P3
    [ [ 1,  1], 0]      # P4
]

# Вычислим значения фитнес функции
for element in population:
    element[1] = fitnes(element[0])


# 
# основной цикл
#
for i in range(4):  
    # Сортируем список по убыванию.
    # Первые 3 элемента это лучшие особи популяции.
    # Выбираем их для размножения
    temp_population = sorted(population, key=lambda item: item[1], reverse=True)
    
    # Удалим хромосому низкого качества
    temp_population.pop()

    # Выполним размножение хромосос
    population = reproduction(temp_population)

    # Выполним оценку популяции
    max_value = max_fitnes(population)
    sum_value = sum_fitness(population)
    print("Номер итерации: {}".format(i+1))
    print("Качество лучшей хромосомы: {}".format(max_value))
    print("Общее качество популяции: {}".format(sum_value))