#
# Исходные данные
#

# Количество итераций
K=3

# Список связей
graph = [
    [1, 5],
    [5, 2],
    [5, 3],
    [4, 2],
    [4, 3]
]

# Начальная популяция
population = [
    [1, 2, 3, 4, 5],
    [2, 1, 3, 4, 5],
    [5, 2, 3, 4, 1]
]

# Список для хранения значений фитнес функции ("L")
population_L = []

# Вычисляет расстояние между соединёнными элементами графика
#
# Параметры:
#    element - список (list) - элемент популяции
#
# Возвращаемое значение:
#    Число - длина всех связей
def fitnes(element):
    summa = 0
    for path in graph:
        ind_1 = element.index(path[0])    # позиция 1-го элемента
        ind_2 = element.index(path[1])    # позиция 2-го элемента
        summa += abs(ind_1 - ind_2)        # определение расстояния между элементами 
    return summa

# Возвращает индекс лучшего элемента списка "population"
def best_element(L):
    best = min(L)
    return L.index(best)

# Возвращает индекс худшего элемента списка "population"
def worse_element(L):
    worse = max(L)
    return L.index(worse)

# функция инверсивной мутации
#
# Параметры:
#    element - cписок (list) - элемент популяции
#    position - Число - позиция, с которой выполняется мутация. В данном случае номер итерации.
#
# Возвращаемое значение:
#     список (list) - элемент списка "population" после мутации     
def mutate(element, position):
    sub_element = element[position:]
    return element[0:position] + list(reversed(sub_element))

#
# Основной цикл
#
for i in range(K):
    # При каждой итерации очищаем оценку популяции
    # и вычисляем её снова
    population_L.clear()
    
    # Для каждого элемента популяции вычислим оценку популяции (фитнес функцию)
    for element in population:
        L_val = fitnes(element)
        population_L.append(L_val)

    # Определим лучший и худший элемент
    best = best_element(population_L) 
    worse = worse_element(population_L)

    # Выполним мутацию лучшего элемента
    new_element = mutate(population[best], i+1)

    # Заменим худший элемент на новый элемент "new_element"
    population[worse] = new_element

min_value = min(population_L)
ind_min_value = population_L.index(min_value)
best_element = population[ind_min_value] 

print("Ответ: лучший элемент - {}, минимальное значение - {}".format(best_element, min_value))