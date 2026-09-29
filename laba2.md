# Отчёт по 2 Лабораторной работе
## Практическая часть

### Задание 1
```python
def convert_types(data):
    result = []

    for item in data:
        if isinstance(item, (int, float)):
            result.append(str(item))
        elif isinstance(item, str):
            try:
                # Сначала пробуем целое число, затем вещественное
                result.append(int(item))
            except ValueError:
                try:
                    result.append(float(item))
                except ValueError:
                    result.append(item)
        else:
            result.append(str(item))

    return result

print('Задание 1')
print(convert_types([1, "2", "hello", 3.5]))
```
```terminaloutput
['1', 2, 'hello', '3.5']
```
### Задание 2
```python
def swap_values(a, b):
    a, b = b, a
    return a, b

print('Задание 2')
print(swap_values(5, 10))
```
```terminaloutput
(10, 5)
```
### Задание 3
```python
def bool_transform(value):
    if value:
        return True
    else:
        return False

print('Задание 3')
print(bool_transform(5))
print(bool_transform(0))
```
```terminaloutput
True
False
```
### Задание 4
```python
def compound_operations(a, b):
    results = []

    current = a
    current += b
    results.append(current)

    current = a
    current -= b
    results.append(current)

    current = a
    current *= b
    results.append(current)

    current = a
    current /= b
    results.append(current)

    current = a
    current //= b
    results.append(current)

    current = a
    current %= b
    results.append(current)

    current = a
    current **= b
    results.append(current)

    return results

print('Задание 4')
print(compound_operations(10, 3))
```
```terminaloutput
[13, 7, 30, 3.3333333333333335, 3, 1, 1000]
```
### Задание 5
```python
def check_type(value, expected_type):
    if type(value).__name__ == expected_type:
        return True
    else:
        return False

print("Задание 5")
print(check_type(5, "int"))
print(check_type("5", 'int') )
```
```terminaloutput
True
False
```
### Задание 6
```python
def logical_and(a, b, c):
    if a:
        if b:
            if c:
                return True
    return False

print("Задание 6")
print(logical_and(True, 5, "x"))
print(logical_and(True, 0, "x") )
```
```terminaloutput
True
False
```
### Задание 7
```python
def logical_or(a, b, c):
    if a:
        return True
    if b:
        return True
    if c:
        return True
    return False

print("Задание 7")
print(logical_or(0, "", False) )
print(logical_or(0, 5, False) )
```
```terminaloutput
False
True
```
### Задание 8
```python
def is_between(value, low, high):
    if value >= low and value <= high:
        return True
    else:
        return False

print("Задание 8")
print(is_between(5, 1, 10))
print(is_between(15, 1, 10))
```
```terminaloutput
True
False
```
### Задание 9
```python
def print_even_numbers(n):
    for i in range(2, n + 1, 2):
        print(i)

print("Задание 9")
print_even_numbers(10)
```
```terminaloutput
2
4
6
8
10
```
### Задание 10
```python
def countdown_while(n):
    while n >= 1:
        print(n)
        n -= 1

print("Задание 10")
countdown_while(5)
```
```terminaloutput
5
4
3
2
1
```
### Задание 11
```python
def skip_multiples(n, multiple):
    for i in range(1, n + 1):
        if i % multiple == 0:
            continue
        print(i)

print("Задание 11")
skip_multiples(10, 3)
```
```terminaloutput
1
2
4
5
7
8
10
```
### Задание 12
```python
def if_elif_else_chain(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"

print("Задание 12")
print(if_elif_else_chain(5))
print(if_elif_else_chain(-3))
print(if_elif_else_chain(0))
```
```terminaloutput
positive
negative
zero
```
### Задание 13
```python
def abs_value(x):
    if x < 0:
        return -x
    else:
        return x

print("Задание 13")
print(abs_value(-5))
print(abs_value(3))
```
```terminaloutput
5
3
```
### Задание 14
```python
def binary_representation(n):
    if n == 0:
        return "0"

    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result

print("Задание 14")
print(binary_representation(10))
print(binary_representation(0))
```
```terminaloutput
1010
0
```
### Задание 15
```python
def custom_round(number, ndigits):
    factor = 10 ** ndigits
    if number >= 0:
        rounded_int = int(number * factor + 0.5)
    else:
        rounded_int = int(number * factor - 0.5)

    return float(rounded_int / factor) if ndigits == 0 else rounded_int / factor

print("Задание 15")
print(custom_round(3.14159, 2))
print(custom_round(2.5, 0))
```
```terminaloutput
3.14
3.0
```
### Задание 16
```python
def find_max_min(numbers):
    if not numbers:
        return None

    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return (max_value, min_value)

print("Задание 16")
print(find_max_min([3, 7, 1, 9, 2]))
```
```terminaloutput
(9, 1)
```
### Задание 17
```python
def all_true(iterable):
    for element in iterable:
        if not element:
            return False
    return True

print('Задание 17')
print(all_true([1, 2, 3]))
print(all_true([1, 0, 3]))
```
```terminaloutput
True
False
```
### Задание 18
```python
def any_true(iterable):
    for element in iterable:
        if element:
            return True
    return False

print('Задание 18')
print(any_true([0, "", False]))
print(any_true([0, 5, False]))
```
```terminaloutput
False
True
```
### Задание 19
```python
def custom_enumerate(sequence, start=0):
    result = []
    current_index = start
    for element in sequence:
        result.append((current_index, element))
        current_index += 1
    return result

print('Задание 19')
print(custom_enumerate(['a', 'b', 'c'], start=1))
```
```terminaloutput
[(1, 'a'), (2, 'b'), (3, 'c')]
```
### Задание 20
```python
def custom_filter(func, iterable):
    result = []
    for element in iterable:
        if func(element):
            result.append(element)
    return result

print('Задание 20')
print(custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
```
```terminaloutput
[2, 4]
```
### Задание 21
```python
def custom_map(func, iterable):
    result = []
    for element in iterable:
        result.append(func(element))
    return result

print('Задание 21')
print(custom_map(lambda x: x * 2, [1, 2, 3]))
```
```terminaloutput
[2, 4, 6]
```
### Задание 22
```python
def custom_zip(list1, list2):
    result = []
    length = min(len(list1), len(list2))
    for i in range(length):
        result.append((list1[i], list2[i]))
    return result

print('Задание 22')
print(custom_zip([1, 2, 3], ['a', 'b', 'c']))
```
```terminaloutput
[(1, 'a'), (2, 'b'), (3, 'c')]
```
### Задание 23
```python
def custom_reversed(sequence):
    result = []
    for i in range(len(sequence) - 1, -1, -1):
        result.append(sequence[i])
    return result

print('Задание 23')
print(custom_reversed([1, 2, 3, 4]))
```
```terminaloutput
[4, 3, 2, 1]
```
### Задание 24
```python
def custom_sorted(iterable, reverse=False):
    lst = list(iterable)
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if not reverse:
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
            else:
                if lst[j] < lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print('Задание 24')
print(custom_sorted([3, 1, 4, 1, 5]))
print(custom_sorted([3, 1, 4], reverse=True))
```
```terminaloutput
[1, 1, 3, 4, 5]
[4, 3, 1]
```
### Задание 25
```python
def sum_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print('Задание 25')
print(sum_digits(1234))
print(sum_digits(99))
```
```terminaloutput
10
18
```
### Задание 26
```python
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print('Задание 26')
print(count_vowels("Hello World"))
print(count_vowels("Python"))
```
```terminaloutput
3
1
```
### Задание 27
```python
def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

print('Задание 27')
print(power(2, 5))
print(power(3, 3))
```
```terminaloutput
32
27
```
### Задание 28
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print('Задание 28')
print(is_prime(17))
print(is_prime(18))
```
```terminaloutput
True
False
```
### Задание 29
```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print('Задание 29')
print(factorial(5))
print(factorial(0))
```
```terminaloutput
120
1
```
### Задание 30
```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print('Задание 30')
print(fibonacci(10))
print(fibonacci(0))
print(fibonacci(1))
```
```terminaloutput
55
0
1
```