# Operazioni sulle Liste in Python

Questo documento fornisce una panoramica delle operazioni di base che puoi eseguire sulle liste in Python.

## Indice
1. [Creazione di una lista](#1-creazione-di-una-lista)
2. [Lunghezza di una lista](#lunghezza-di-una-lista)
2. [Accesso agli elementi](#2-accesso-agli-elementi)
3. [Modifica di una lista](#3-modifica-di-una-lista)
4. [Aggiunta di elementi](#4-aggiunta-di-elementi)
5. [Rimozione di elementi](#5-rimozione-di-elementi)
6. [Ordinamento di una lista](#6-ordinamento-di-una-lista)
7. [Iterazione su una lista](#7-iterazione-su-una-lista)
8. [Controllo lista vuota](#7-iterazione-su-una-lista)

## 1. Creazione di una lista

Puoi creare una lista in Python utilizzando le parentesi quadre `[]`.

```python
# Creazione di una lista vuota
lista_vuota = []

# Creazione di una lista con elementi
lista_numeri = [1, 2, 3, 4, 5]
lista_frutta = ["mela", "banana", "ciliegia"]
```
## Lunghezza di una lista
```
# Lista con tre elementi
lista = [1, 2, 3]

# Creazione di una lista con elementi
len(lista)
```

## 2. Accesso agli elementi

Puoi accedere agli elementi di una lista utilizzando l'indice, che inizia da 0.

```python

# Accesso al primo elemento
primo_elemento = lista_numeri[0]  # 1

# Accesso all'ultimo elemento
ultimo_elemento = lista_frutta[-1]  # "ciliegia"
```

## 3. Modifica di una lista

Puoi modificare un elemento di una lista assegnando un nuovo valore all'indice desiderato.

```python
lista_numeri = [1, 2, 3, 4, 5]
# Modifica del secondo elemento
lista_numeri[1] = 20  # lista_numeri diventa [1, 20, 3, 4, 5]
```

## 3. Aggiunta di elementi

Puoi aggiungere elementi a una lista utilizzando il metodo `append()` o `insert()`.

```python

# Aggiunta di un elemento alla fine della lista
lista_numeri.append(6)  # lista_numeri diventa [1, 20, 3, 4, 5, 6]

# Aggiunta di un elemento in una posizione specifica
lista_frutta.insert(1, "arancia")  # lista_frutta diventa ["mela", "arancia", "banana", "ciliegia"]
```


## 4. Rimozione di elementi

Puoi rimuovere elementi da una lista utilizzando il metodo `remove()` o `pop()`.


```python
# Rimozione di un elemento specifico
lista_frutta.remove("banana")  # lista_frutta diventa ["mela", "arancia", "ciliegia"]

# Rimozione dell'ultimo elemento
ultimo_elemento = lista_numeri.pop()  # rimuove 6 e lo assegna a ultimo_elemento
```

## 5. Ordinamento di una lista

Puoi ordinare una lista utilizzando il metodo `sort()` o la funzione `sorted()`.

```python

# Ordinamento in loco
lista_numeri.sort()  # lista_numeri diventa [1, 3, 4, 5, 20]

# Ordinamento senza modificare la lista originale
lista_ordinata = sorted(lista_frutta)  # lista_ordinata contiene ["arancia", "ciliegia", "mela"]
```

## 6. Iterazione su una lista

Puoi iterare su una lista utilizzando un ciclo `for`.

```python

for frutta in lista_frutta:
    print(frutta)
```

## Controllo lista vuota

```python
lista = []

if len(lista) == 0:
    ...


if not lista:
    print("Vuota.")
else:
    print("Piena.")
```