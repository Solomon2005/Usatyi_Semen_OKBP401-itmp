NIL = None

def pair(head_val, tail_val):
    return lambda select: select(head_val, tail_val)

def head(lst):
    return lst(lambda h, t: h)

def tail(lst):
    return lst(lambda h, t: t)

def make_list(*args):
    def build(index):
        if index == len(args):
            return NIL
        return pair(args[index], build(index + 1))
    return build(0)

def list_to_string(lst):
    def to_str(current, acc):
        if current is NIL:
            return f"[{acc[:-2]}]" if acc else "[]"
        return to_str(tail(current), acc + str(head(current)) + ", ")
    return to_str(lst, "")

def list_range(low, high):
    if low > high:
        return NIL
    return pair(low, list_range(low + 1, high))

def foldl(func, lst, acc):
    if lst is NIL:
        return acc
    return foldl(func, tail(lst), func(acc, head(lst)))

def list_sum(lst):
    return foldl(lambda acc, x: acc + x, lst, 0)

def fact(n):
    if n == 0:
        return 1
    return foldl(lambda acc, x: acc * x, list_range(1, n), 1)

def list_to_py(lst):
    return foldl(lambda acc, x: acc + [x], lst, [])

def list_reverse(lst):
    return foldl(lambda acc, x: pair(x, acc), lst, NIL)

def foldr(func, lst, acc):
    if lst is NIL:
        return acc
    return func(head(lst), foldr(func, tail(lst), acc))

def list_map(func, lst):
    return foldr(lambda x, acc: pair(func(x), acc), lst, NIL)

def list_filter(pred, lst):
    return foldr(lambda x, acc: pair(x, acc) if pred(x) else acc, lst, NIL)

def sum_odd_squares(lst):
    odds = list_filter(lambda x: x % 2 != 0, lst)
    squares = list_map(lambda x: x ** 2, odds)
    return list_sum(squares)

def list_concat(lst1, lst2):
    return foldr(lambda x, acc: pair(x, acc), lst1, lst2)

def list_replace(lst, index, value):
    def replace_helper(current, curr_idx):
        if current is NIL:
            return NIL
        if curr_idx == index:
            return pair(value, tail(current))
        return pair(head(current), replace_helper(tail(current), curr_idx + 1))
    return replace_helper(lst, 0)

if __name__ == "__main__":
    mylst = make_list(1, 2, 3, 4, 5)
    print("Созданный список:", list_to_string(mylst))
    
    range_lst = list_range(10, 14)
    print("Диапазон (10-14):", list_to_string(range_lst))
    
    print("Сумма элементов:", list_sum(mylst))
    
    print("Факториал 5!:", fact(5))
    
    print("Стандартный список Python:", list_to_py(mylst))
    
    print("Развернутый список:", list_to_string(list_reverse(mylst)))
    
    mapped = list_map(lambda x: x * 10, mylst)
    print("Отображение (*10):", list_to_string(mapped))
    
    filtered = list_filter(lambda x: x % 2 == 0, mylst)
    print("Фильтрация (четные):", list_to_string(filtered))
    
    print("Сумма квадратов нечетных:", sum_odd_squares(mylst))
    
    concat_lst = list_concat(mylst, range_lst)
    print("Объединение списков:", list_to_string(concat_lst))
    
    replaced = list_replace(mylst, 2, 99)
    print("Замена элемента с индексом 2 на 99:", list_to_string(replaced))
