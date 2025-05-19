# Guida agli Operatori in Python

Python supporta diversi tipi di operatori che consentono di eseguire operazioni su variabili e valori. Gli operatori possono essere suddivisi in diverse categorie.

## Indice

1. [Operatori aritmetici](#1-operatori-aritmetici)
2. [Operatori di assegnazione](#2-operatori-di-assegnazione)
3. [Operatori di confronto](#3-operatori-di-confronto)
4. [Operatori logici](#4-operatori-logici)
5. [Operatori bitwise](#5-operatori-bitwise)
6. [Operatori di identità](#6-operatori-di-identità)
7. [Operatori di appartenenza](#7-operatori-di-appartenenza)

## 1. Operatori aritmetici

Gli operatori aritmetici vengono utilizzati per eseguire operazioni matematiche.

| Operatore | Nome               | Esempio          |
|-----------|---------------------------|------------------|
| `=`       | Assegnazione              | `a = 1`          |
| `+`       | Somma                     | `a + b`          |
| `-`       | Sottrazione               | `a - b`          |
| `*`       | Moltiplicazione           | `a * b`          |
| `/`       | Divisione (float)         | `a / b`          |
| `//`      | Divisione intera          | `a // b`         |
| `%`       | Modulo                    | `a % b`          |
| `**`      | Potenza                   | `a ** b`         |

### Esempi

```python
a = 10
b = 3
print(a + b)     # Output: 13
print(a - b)     # Output: 7
print(a * b)     # Output: 30
print(a / b)     # Output: 3.3333...
print(a // b)    # Output: 3
print(a % b)     # Output: 1
print(a ** b)    # Output: 1000
```

## 2. Operatori di assegnazione

| Operatore | Descrizione               | Esempio          |
|-----------|---------------------------|------------------|
| `+=`      | Assegnazione semplice     | `a += 1`         |
| `-=`      | Aggiunta e assegnazione   | `a -= 1`         |
| `*=`      | Moltiplicazione e assegnazione              | `a /= 1`         |
| `/=`      | Divisione e assegnazione   | `a -= 1`         |
| `//=`     | Divisione intera e assegnazione | `a //= 2`        |
| `%=`      | Modulo e assegnazione           | `a %= 2`        |
| `**=`     | Potenza e assegnazione          | `a **= 2`        |


### Esempi
```python
a = 10
a += 5  # a = 15
print(a)  # Output: 15

a -= 3  # a = 12
print(a)  # Output: 12

a *= 2  # a = 24
print(a)  # Output: 24

a /= 4  # a = 6.0
print(a)  # Output: 6.0

a //= 2  # a = 3.0
print(a)  # Output: 3.0

a %= 2  # a = 1.0
print(a)  # Output: 1.0

a **= 3  # a = 1.0
print(a)  # Output: 1.0
```


## 3. Operatori di confronto

Gli operatori di confronto vengono utilizzati per confrontare due valori.

| Operatore | Descrizione                     | Esempio         |
|-----------|---------------------------------|------------------|
| `==`      | Uguale                          | `a == b`         |
| `!=`      | Diverso                         | `a != b`         |
| `>`       | Maggiore                        | `a > b`          |
| `<`       | Minore                          | `a < b`          |
| `>=`      | Maggiore o uguale              | `a >= b`         |
| `<=`      | Minore o uguale                | `a <= b`         |

```python
a = 10
b = 5

# Operatore uguale
print(a == b)  # Output: False (10 non è uguale a 5)

# Operatore diverso
print(a != b)  # Output: True (10 è diverso da 5)

# Operatore maggiore
print(a > b)   # Output: True (10 è maggiore di 5)

# Operatore minore
print(a < b)   # Output: False (10 non è minore di 5)

# Operatore maggiore o uguale
print(a >= b)  # Output: True (10 è maggiore o uguale a 5)

# Operatore minore o uguale
print(a <= b)  # Output: False (10 non è minore o uguale a 5)
```

## 4. Operatori logici

| Operatore | Descrizione                     | Esempio         |
|-----------|---------------------------------|------------------|
| `and`     | E logico                       | `a and b`        |
| `or`      | O logico                       | `a or b`         |
| `not`     | Negazione logica               | `not a`          |

### Esempi

```python
a = True
b = False

# Operatore and
print(a and b)  # Output: False (entrambi devono essere True)

# Operatore or
print(a or b)   # Output: True (almeno uno deve essere True)

# Operatore not
print(not a)    # Output: False (inverte il valore di a)
print(not b)    # Output: True (inverte il valore di b)
```

## 5. Operatori bitwise

| Operatore | Descrizione                     | Esempio         |
|-----------|---------------------------------|------------------|
| `&`       | AND bitwise                    | `a & b`          |
| `\|`      | OR bitwise                     | `a \| b`          |
| `^`       | XOR bitwise                    | `a ^ b`          |
| `~`       | NOT bitwise                    | `~a`             |
| `<<`      | Shift a sinistra               | `a << 2`         |
| `>>`      | Shift a destra                 | `a >> 2`         |

### Esempi

```python
a = 10  # In binario: 1010
b = 4   # In binario: 0100

# Operatore AND bitwise
print(a & b)  # Output: 0 (In binario: 0000)

# Operatore OR bitwise
print(a | b)  # Output: 14 (In binario: 1110)

# Operatore XOR bitwise
print(a ^ b)  # Output: 14 (In binario: 1110)

# Operatore NOT bitwise
print(~a)     # Output: -11 (In binario: ...11110101, complemento a 2)

# Operatore Shift a sinistra
print(a << 2) # Output: 40 (In binario: 101000)

# Operatore Shift a destra
print(a >> 2) # Output: 2 (In binario: 0010)
```

## 6. Operatori di identità

| Operatore | Descrizione                     | Esempio         |
|-----------|---------------------------------|------------------|
| `is`      | Verifica se due variabili puntano allo stesso oggetto | `a is b`         |
| `is not`  | Verifica se due variabili non puntano allo stesso oggetto | `a is not b`     |

### Esempi

```python
a = [1, 2, 3]
b = a  # b punta allo stesso oggetto di a
c = [1, 2, 3]  # c è una nuova lista con gli stessi valori di a

# Operatore is
print(a is b)      # Output: True (a e b puntano allo stesso oggetto)
print(a is c)      # Output: False (a e c sono oggetti diversi in memoria)

# Operatore is not
print(a is not b)  # Output: False (a e b sono lo stesso oggetto)
print(a is not c)  # Output: True (a e c sono oggetti diversi)
```

## 7. Operatori di appartenenza

| Operatore  | Descrizione                                         | Esempio         |
|------------|-----------------------------------------------------|------------------|
| `in`       | Verifica se un valore è presente in una sequenza   | `x in lista`     |
| `not in`   | Verifica se un valore non è presente in una sequenza| `x not in lista` |


### Esempi

```python
lista = [1, 2, 3, 4, 5]
x = 3
y = 6

# Operatore in
print(x in lista)      # Output: True (3 è presente nella lista)
print(y in lista)      # Output: False (6 non è presente nella lista)

# Operatore not in
print(x not in lista)  # Output: False (3 è presente nella lista)
print(y not in lista)  # Output: True (6 non è presente nella lista)
```