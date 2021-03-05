#tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена', 'Сергей', 'Владимир', 'Вурдалак']
#klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис']
klasses = ['9А', '7В', '9Б', '9В']

# Способ 1 (спойлер с лекции), используем модуль itertools
from itertools import zip_longest
print(f'Способ 1: {list(zip_longest(tutors, klasses, fillvalue=None))}')

# Способ 2 (читерский) - используем zip()
klasses.extend([None for i in range(len(tutors) - len(klasses))]) if len(tutors) > len(klasses) else None
print(f'Способ 2: {list(zip(tutors, klasses))}')

# Способ 3, перепишем функцию zip до правильного состояния функции zip_longest
# жаль только что мы "не знаем" ни объекты ни исключения

def zippo(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
# Адаптировать ентот кусок
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

# эта штука работает потому что klasses расширен значениями Null во втором способе
print(f'Способ 3: {list(zippo(tutors, klasses))}')

