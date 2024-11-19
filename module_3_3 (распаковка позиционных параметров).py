#1.функция с параметрами по умолчанию.
def print_params(a=1, b='строка', c=True):
    print(f'a: {a}, b: {b}, c: {c}')

print_params()
print_params(10)
print_params(10, 'новая строка')
print_params(10, 'новая строка', False)

print_params(b=25)
print_params(c=[1, 2, 3])

#2.Распаковка параметров:
def print_params(a=1, b='строка', c=True):
    print(f'a, b, c')

values_list = [42, 'Привет', False]
values_dict = {
    'a': 3.14,
    'b': [1, 2, 3],
    'c': None}
print_params(*values_list)
print_params(**values_dict)

#3.распаковка+отдельные параметры:
def print_params(a=1, b='строка', c=True):
    print(f'a, b, c')

values_list_2 = [3.14, 'Привет']
    print_params(*values_list_2, 42)