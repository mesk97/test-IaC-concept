

# На улице стоят n непокрашенных домов в ряд. 

# Известна стоимость покраски каждого дома в каждый цвет (красный, зеленый, синий).

# Жильцы этих домов большие завистники, поэтому никакие два дома, стоящие рядом, не могут иметь одинакового покраса.

# Найти минимальную стоимость покраски всех домов при указанных условиях.

# Входные данные: houses[][3] – массив стоимости покраски в каждый цвет для каждого дома

# Пример
# // первый дом можно покрасить за 1 в красный, за 2 в зеленый, за 3 в синий
# // второй дом – за 3 в красный, за 2 в зеленый, за 1 в синий
# findMinPrice([[1, 2, 3], [3, 2, 1]]) => 2


1          2         3
2     3    1    3    1    2
3 1  1 2   3 1  2 1  2 3  1 3