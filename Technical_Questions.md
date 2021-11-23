# Programistyczne pytania rekrutacyjne

## Comprehensions:
Comprehensions to uproszczony, jednolinijkowy sposób tworzenia list, słowników oraz generatorów.

```python
my_list = [2 ** i for i in range(20)]
```
```python
my_dict = {f'position - {i + 1}:': 2 ** i for i in range(20)}
```

## Dekorator:
Dekorator to funkcja, która przyjmuje inną funkcję jako parametr, modyfikuje ją i zwraca wynik.

```python
def multiply(a, b):
    return a * b

# Decorator
def multiply_decorator(fun, c):
    return fun * c
```

## Krotki:
Krotkę (tuple) definiujemy poprzez przecinek, nie nawiasy np.
```python
a = 1, 2, 3, 4
```
```python
b = (1, )
```
```python
c = (1, 2, 3, 4)
```

## Elementy <u>prywatne</u> w klasach:
W Pythonie wszystko jest publiczne. Istnieje jednak konwencja tworzenia elementów prywatnych poprzez dodawanie _ na
początku nazwy:
```python
class MyClass:
    _my_str = 'Some String'
    return _my_str
```
Poprzez dodanie dwóch __ element będzie niewidoczny poza klasą, ale można obejść następująco:
```python
class MyClass:
    __private = 'Some Private String'

MyClass._MyClass__private
```

# sort() i sorted():
sorted() to funkcja, która przyjmuje listę jako parametr i zwraca posortowaną listę.
```python
>>> a = [1, 75, 234, 34, 2, 87]
>>> b = sorted(a)
>>> b
[1, 2, 34, 75, 87, 234]
```
sort() to metoda listy, która sortuje daną listę
```python
>>> a = [1, 75, 234, 34, 2, 87]
>>> a.sort()
>>> a
[1, 2, 34, 75, 87, 234]
```

## Krotka vs Lista:
### Listy:
* mutowalne
* wolniejsze od tupli
* nie mogą być kluczem w słowniku
* ograniczone nawiasami kwadratowymi
### Tuple (Krotka):
* niemutowalne
* szybsze od list
* mogą być kluczami w słowniku
* ograniczone nawiasami okrągłymi

## Funckje lambda:
Lambda to uproszczony, anonimowy zapis funkcji używany do tworzenia prostych funkcji.
Funkcja jest anonimowa, ale można przypisać ją i wywołać ze zmiennej.
```python
return lambda x : x ** 2
```

## Jednoliniowe wyrażenia warunkowe:
```python
>>> x, y = 10, 20
>>> smaller = x if x < y else y
10
```

## Generatory:
Generator to funkcja która, za pomocą ```yeld``` zwraca iterowalny obiekt.
Obiekt ten nie jest zapisany w pamięci więc może być poprany z iteratora tylko raz.

Generatory dają nam możliwość wstrzymania funkcji na pewien czas co jest przydatne przy przetwarzaniu dużych
zestawów danych.
```python
def power():
    a = 1
    while True:
        yeld(a ** 2)
        a += 1

for i in power():
    print(i)
    if i > 2048:
        break
```

# Czy funkcja musi zwracać wynik:
Tak, funkcja zawsze zwróci wynik, choć instrukcja ```return``` nie jest wymagana.
W przypadku braku instrukcji ```return``` funkcja zwróci ```None```

## Atrybuty Klas a atrybuty obiektów:
Atrybuty obiektów są specyficzne tylko dla danej instancji (obiektu) tej klasy i nie mają wpływu na inne instancje klasy.

Atrybuty (zmienne) klas mają wartość na poziomie klasy i są dzielone między wszystkimi instancjami tej klasy.
Jeśli zmienna zostanie zmieniona na poziomie klasy, zmienna ta we wszystkich instancjach tej klasy również będzie zmieniona
```python
class MyClass:
    class_attr = 'To jest zmienna klasy'

    def __init(self):
        self.instance_attr = 'To jest zmienna obiektu'
```

# Nazwa aktualnie wykonywanego modułu:
Aby pobrać nazwę aktualnie wykonywanego modułu, należy użyć magicznej metody ```__name__```, Python umieszcza tam nazwę
aktualnego modułu. Nie działa to jednak w linii komend, ponieważ zwróci tam zawsze ```__main__```

# Do czego używamy ```__init__.py```:
Plik ```__init__.py``` sprawia, że python traktuje dany folder jako zawierający pakiety. Plik ten może być pusty,
ale musi istnieć w katalogu.

# Co robi instrukcja ```pass```:
Instrukcja ```pass``` nie robi niczego.
W pythonie blok kodu nie może pozostać pusty, w związku z czym używamy instrukcji pass do wypełnienia bloku kodu,
który chcemy dokończyć później lub po prostu zostawić pusty.

# Co to jest PEP-8:
PEP-8 to dokument opisujący standard kodowania w Python np. ilość linii między klasami, zasady nazewnictwa klas, funckji itd.
