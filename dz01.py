from pulp import LpMaximize, LpProblem, LpVariable

# Створюємо задачу лінійного програмування
problem = LpProblem("Maximize_Production", LpMaximize)

# Оголошуємо змінні (кількість одиниць лимонаду та фруктового соку)
lemonade = LpVariable("Lemonade", lowBound=0, cat='Continuous')  # Одиниці Лимонаду
juice = LpVariable("Juice", lowBound=0, cat='Continuous')        # Одиниці Фруктового соку

# Метою є максимізація загальної кількості продуктів
problem += lemonade + juice, "Total_Production"

# Обмеження на ресурси:
# Вода: 2 одиниці на кожен лимонад та кожен фруктовий сік
problem += 2 * lemonade + juice <= 100, "Water_Limit"

# Цукор: 1 одиниця на кожен лимонад
problem += lemonade <= 50, "Sugar_Limit"

# Лимонний сік: 1 одиниця на кожен лимонад
problem += lemonade <= 30, "Lemon_Squeeze_Limit"

# Фруктове пюре: 2 одиниці на кожен фруктовий сік
problem += 2 * juice <= 40, "Fruit_Puree_Limit"

# Розв'язуємо задачу
problem.solve()

# Показуємо результати
print(f"Максимальна кількість Лимонаду: {lemonade.varValue}")
print(f"Максимальна кількість Фруктового соку: {juice.varValue}")
print(f"Максимальна загальна кількість продуктів: {lemonade.varValue + juice.varValue}")
