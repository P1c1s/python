# Operazioni sulle Stringhe in Python

Questo documento fornisce una panoramica delle operazioni di base che puoi eseguire sulle stringhe in Python.

## Indice

1. [Creazione di una stringa](#1-creazione-di-una-stringa)
2. [Accesso ai caratteri](#2-accesso-ai-caratteri)
3. [Modifica di una stringa](#3-modifica-di-una-stringa)
4. [Concatenazione di stringhe](#4-concatenazione-di-stringhe)
5. [Formattazione di stringhe](#5-formattazione-di-stringhe)
6. [Metodi delle stringhe](#6-metodi-delle-stringhe)
7. [Ricerca e sostituzione](#7-ricerca-e-sostituzione)
8. [Iterazione su una stringa](#8-iterazione-su-una-stringa)
9. [F-string - formattazione elegante](#9-f-string)

## 1. Creazione di una stringa

Puoi creare una stringa in Python utilizzando le virgolette singole `'` o doppie `"`.

```python
# Creazione di una stringa
stringa1 = "Ciao, Mondo!"
stringa2 = 'Python è fantastico!'
```

## 2. Accesso ai caratteri

Puoi accedere ai singoli caratteri di una stringa utilizzando l'indice, che inizia da 0.

```python

# Accesso al primo carattere
primo_carattere = stringa1[0]  # 'C'

# Accesso all'ultimo carattere
ultimo_carattere = stringa2[-1]  # 'o'
```

## 3. Modifica di una stringa

Le stringhe in Python sono immutabili, il che significa che non puoi modificare i caratteri di una stringa esistente. Tuttavia, puoi creare una nuova stringa.

```python

# Creazione di una nuova stringa
nuova_stringa = stringa1.replace("Mondo", "Python")  # "Ciao, Python!"
```

## 4. Concatenazione di stringhe

Puoi concatenare due o più stringhe utilizzando l'operatore `+`.

```python

stringa_concatenata = stringa1 + " " + stringa2  # "Ciao, Mondo! Python è fantastico!"
```

## 5. Formattazione di stringhe

Puoi formattare le stringhe utilizzando il metodo `format()` o le f-string (Python 3.6+).

```python

nome = "Mario"
saluto = f"Ciao, {nome}!"  # "Ciao, Mario!"
```

## 6. Metodi delle stringhe

Python offre molti metodi utili per lavorare con le stringhe. Ecco alcuni esempi:

```python

# Convertire in maiuscolo
stringa_maiuscola = stringa1.upper()  # "CIAO, MONDO!"

# Convertire in minuscolo
stringa_minuscola = stringa2.lower()  # "python è fantastico!"

# Contare i caratteri
lunghezza = len(stringa1)  # 13
```

## 7. Ricerca e sostituzione

Puoi cercare e sostituire parti di una stringa utilizzando i metodi `find()` e `replace()`.

```python

# Ricerca di una sottostringa
posizione = stringa1.find("Mondo")  # 6

# Sostituzione di una sottostringa
stringa_modificata = stringa2.replace("fantastico", "incredibile")  # "Python è incredibile!"
```

## 8. Iterazione su una stringa

Puoi iterare su una stringa utilizzando un ciclo `for`.

```python

for carattere in stringa1:
    print(carattere)
```

## 9. F-String

```python
nome = "Alice"
f"Benvenuta, {nome}!"  # "Benvenuta, Alice!"
```

altro
```python
stringa = "ciao"
stringa.count('a') # Output 1 
```

