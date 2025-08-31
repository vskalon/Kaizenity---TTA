# Документация калькулятора

## 📋 Обзор

Калькулятор - это простой класс для выполнения математических операций с сохранением истории операций.

## 🚀 Использование

### Базовые операции

```python
from src.calculator import Calculator

# Создание экземпляра
calc = Calculator()

# Сложение
result = calc.add(5, 3)  # 8

# Вычитание
result = calc.subtract(10, 4)  # 6

# Умножение
result = calc.multiply(6, 7)  # 42

# Деление
result = calc.divide(15, 3)  # 5.0
```

### История операций

```python
# Получение истории
history = calc.get_history()
# ['5 + 3 = 8', '10 - 4 = 6', '6 * 7 = 42', '15 / 3 = 5.0']

# Очистка истории
calc.clear_history()
```

## 📚 API Reference

### Calculator

Основной класс калькулятора.

#### Методы

##### `add(a, b)`
Сложение двух чисел.

**Параметры:**
- `a` (int/float) - первое число
- `b` (int/float) - второе число

**Возвращает:**
- `int/float` - результат сложения

**Пример:**
```python
result = calc.add(5, 3)  # 8
```

##### `subtract(a, b)`
Вычитание двух чисел.

**Параметры:**
- `a` (int/float) - уменьшаемое
- `b` (int/float) - вычитаемое

**Возвращает:**
- `int/float` - результат вычитания

**Пример:**
```python
result = calc.subtract(10, 4)  # 6
```

##### `multiply(a, b)`
Умножение двух чисел.

**Параметры:**
- `a` (int/float) - первый множитель
- `b` (int/float) - второй множитель

**Возвращает:**
- `int/float` - результат умножения

**Пример:**
```python
result = calc.multiply(6, 7)  # 42
```

##### `divide(a, b)`
Деление двух чисел.

**Параметры:**
- `a` (int/float) - делимое
- `b` (int/float) - делитель

**Возвращает:**
- `float` - результат деления

**Исключения:**
- `ValueError` - при попытке деления на ноль

**Пример:**
```python
result = calc.divide(15, 3)  # 5.0
```

##### `get_history()`
Получение истории операций.

**Возвращает:**
- `list` - список строк с операциями

**Пример:**
```python
history = calc.get_history()
# ['5 + 3 = 8', '10 - 4 = 6']
```

##### `clear_history()`
Очистка истории операций.

**Пример:**
```python
calc.clear_history()
```

## 🧪 Тестирование

Для запуска тестов используйте:

```bash
python tests/test_calculator.py
```

### Покрытие тестами

- ✅ Сложение
- ✅ Вычитание
- ✅ Умножение
- ✅ Деление
- ✅ Деление на ноль (исключение)
- ✅ История операций
- ✅ Очистка истории

## 📝 Примеры использования

### Простой калькулятор

```python
from src.calculator import Calculator

def main():
    calc = Calculator()
    
    print("🧮 Простой калькулятор")
    
    # Ввод от пользователя
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    operation = input("Введите операцию (+,-,*,/): ")
    
    # Выполнение операции
    if operation == '+':
        result = calc.add(a, b)
    elif operation == '-':
        result = calc.subtract(a, b)
    elif operation == '*':
        result = calc.multiply(a, b)
    elif operation == '/':
        result = calc.divide(a, b)
    else:
        print("Неизвестная операция!")
        return
    
    print(f"Результат: {result}")
    print(f"История: {calc.get_history()}")

if __name__ == "__main__":
    main()
```

### Калькулятор с меню

```python
from src.calculator import Calculator

def show_menu():
    print("\n🧮 Калькулятор")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. История")
    print("6. Очистить историю")
    print("0. Выход")

def main():
    calc = Calculator()
    
    while True:
        show_menu()
        choice = input("Выберите операцию: ")
        
        if choice == '0':
            break
        elif choice in ['1', '2', '3', '4']:
            a = float(input("Первое число: "))
            b = float(input("Второе число: "))
            
            if choice == '1':
                result = calc.add(a, b)
            elif choice == '2':
                result = calc.subtract(a, b)
            elif choice == '3':
                result = calc.multiply(a, b)
            elif choice == '4':
                result = calc.divide(a, b)
            
            print(f"Результат: {result}")
        elif choice == '5':
            history = calc.get_history()
            if history:
                print("История операций:")
                for op in history:
                    print(f"  {op}")
            else:
                print("История пуста")
        elif choice == '6':
            calc.clear_history()
            print("История очищена")

if __name__ == "__main__":
    main()
```

## 🔧 Расширение функциональности

### Добавление новых операций

```python
def power(self, a, b):
    """Возведение в степень"""
    result = a ** b
    self.history.append(f"{a} ^ {b} = {result}")
    return result

def sqrt(self, a):
    """Квадратный корень"""
    result = a ** 0.5
    self.history.append(f"√{a} = {result}")
    return result
```

### Сохранение истории в файл

```python
def save_history_to_file(self, filename):
    """Сохранение истории в файл"""
    with open(filename, 'w', encoding='utf-8') as f:
        for operation in self.history:
            f.write(operation + '\n')

def load_history_from_file(self, filename):
    """Загрузка истории из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            self.history = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
```

## 📋 Планы развития

- [ ] Добавление тригонометрических функций
- [ ] Поддержка комплексных чисел
- [ ] Графический интерфейс
- [ ] Сохранение истории в базу данных
- [ ] Поддержка единиц измерения
- [ ] Режим программируемого калькулятора

---

**Версия:** 1.0  
**Дата:** 2024-12-19  
**Автор:** Совместный проект
