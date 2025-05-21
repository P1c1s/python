# Operazioni sulle Stringhe in Python

Questo documento fornisce una panoramica delle operazioni di base che puoi eseguire sulle stringhe in Python.

## Indice

1. [Creazione di una stringa](#1-creazione-di-una-stringa)
2. [Accesso ai caratteri](#2-accesso-ai-caratteri)
3. [Concatenazione di stringhe](#3-concatenazione-di-stringhe)
4. [Iterazione su una stringa](#4-iterazione-su-una-stringa)
5. [Funzioni standard](#5-funzioni-standard)
    1. [len(s)](#i-lens)
    2. [s.lower()](#ii-slower)
    3. [s.upper()](#iii-supper)
    4. [s.strip()](#iv-sstrip)
    5. [s.split(sep)](#v-ssplitsep)
    6. [s.join(iterable)](#vi.-sjoiniterable)
    7. [s.replace(old, new)](#vii-sreplaceold-new)
    8. [s.find(sub)](#viii-sfindsub)
    9. [s.count(sub)](#ix-scountsub)
    10. [s.startswith(prefix)](#x-sstartswithprefix)
    11. [s.endswith(suffix)](#xi-sendwithsuffix)
    12. [s.capitalize()](#xii-scapitalize)
    13. [s.title()](#xiii-stitle)
    14. [s.isdigit()](#xiv-sisdigit)
    15. [s.isalpha()](#xv-sisalpha)
6. [Slicing](#6-slicing)
7. [Formattazione di stringhe](#7-formattazione-di-stringhe)
    1. [F-strings](#i-f-strings)
    2. [Metodo format()](#ii-metodo-format)


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

```python
stringa1 = "Ciao"
stringa2 = "Mondo"
risultato = stringa1 + " " + stringa2
print(risultato)  # Output: "Ciao Mondo"
```

## 3. Concatenazione di stringhe
La concatenazione di stringhe è l'operazione che unisce due o più stringhe in una sola. L'operatore `+` concatena (unisce) due stringhe.

```python
s1 = "Ciao"
s2 = "Mondo"
s3 = s1 + " " + s2
print(s3) # Output: "Ciao Mondo"
```

## 4. Iterazione su una stringa

Puoi iterare su una stringa utilizzando un ciclo `for`.

```python
stringa = "Hola"
for carattere in stringa:
    print(carattere)
```

## 5. Funzioni standard

### i. len(s)
Restituisce la lunghezza della stringa `s`.

```python
stringa = "Feffe"
print(len(stringa))    # Output: 5
```

### ii. s.lower()
Restituisce una copia della stringa `s` convertita in minuscolo.

```python
stringa = "EliSabeTtA"
print(stringa.lower())    # Output: elisabetta
```

### iii. `s.upper()`
Restituisce una copia della stringa `s` convertita in maiuscolo.

```python
stringa = "colonnello"
print(stringa.upper())    # Output: Colonnello
```

### iv. s.strip()
Restituisce una copia della stringa `s` senza spazi bianchi all'inizio e alla fine.

```python
stringa = " Alessianica "
print(stringa.strip())  # Output: "Alessianica"
```

### v. `s.split(sep)`
Divide la stringa `s` in una lista di sottostringhe utilizzando il separatore `sep`.

```python
stringa = "Stefano,Fappio"
print(stringa.split(","))  # Output: ["Stefano", "Fappio"]
```

### vi. `s.join(iterable)`
Unisce gli elementi di un iterable (come una lista) in una singola stringa, separandoli con la stringa `s`.

```python
lista_di_stringhe = ["Stefano", "non sta bene"]
print(" ".join(lista_di_stringhe))  # Output: "Stefano non sta bene"
```

### vii. `s.replace(old, new)`
Restituisce una copia della stringa `s` con tutte le occorrenze di `old` sostituite da `new`.

```python
stringa = "Ciao Eli"
print(stringa.replace("Eli", "Ale"))  # Output: "Ciao Ale"
```

### viii. `s.find(sub)`
Restituisce l'indice della prima occorrenza della sottostringa `sub` in `s`, oppure -1 se non trovata.

```python
stringa = "Ada"
print(stringa.find("d"))  # Output: 1
print(stringa.find("o"))  # Output: -1
```

### ix. `s.count(sub)`
Restituisce il numero di occorrenze della sottostringa `sub` in `s`.

```python
stringa = "Ciao Fabio come stai. Come sei bello Fabio."
print(stringa.count("Fabio"))  # Output: 2

```

### x. `s.startswith(prefix)`
Restituisce `True` se la stringa `s` inizia con il prefisso `prefix`, altrimenti `False`.

```python
stringa = "Siamo patatini"
print(stringa.startswith("Siam"))  # Output: True
print(stringa.startswith("Non Siam"))  # Output: False
```

### xi. `s.endswith(suffix)`
Restituisce `True` se la stringa `s` termina con il suffisso `suffix`, altrimenti `False`.

```python
stringa = "Ch'ha detto?"
print(stringa.endswith("?"))  # Output: True
print(stringa.endswith("!"))  # Output: False
```

### xii. `s.capitalize()`
Restituisce una copia della stringa `s` con il primo carattere maiuscolo e gli altri caratteri in minuscolo.

```python
stringa = "riccio"
print(stringa.capitalize())  # Output: "Riccio"
```

### xiii. `s.title()`
Restituisce una copia della stringa `s` con il primo carattere di ogni parola in maiuscolo.

```python
stringa = "torniamo in romania?"
print(stringa.title())  # Output: "Torniamo In Romania?"

```

### xiv. `s.isdigit()`
Restituisce `True` se tutti i caratteri della stringa `s` sono cifre, altrimenti `False`.

```python
stringa = "343"
print(stringa.isdigit())  # Output: True
```

### xv. `s.isalpha()`
Restituisce `True` se tutti i caratteri della stringa `s` sono lettere, altrimenti `False`.

```python
stringa = "343a"
print(stringa.isdigit())  # Output: False
```

## 6. Slicing
Lo slicing in Python è una tecnica che consente di estrarre una parte di una sequenza, come una stringa, una lista o una tupla. Puoi specificare un intervallo di indici per ottenere una sottosequenza. 

### i. Sintassi slicing

`sequenza[start:end:step]`
* `start`: l'indice da cui iniziare l'estrazione (inclusivo).
* `end`: l'indice fino a cui estrarre (esclusivo).
* `step`: il passo con cui avanzare (opzionale).


```python

stringa = "Ciao Elisabetta come stai?"

# Estrai i primi 4 caratteri
primi_quattro = stringa[0:4]
print(primi_quattro)  # Output: Ciao

# Estrai i caratteri dalla posizione 5 alla fine
dalla_posizione_5 = stringa[5:]
print(dalla_posizione_5)  # Output: Elisabetta come stai?

# Estrai i caratteri da 0 a 15 con un passo di 2
con_passo_di_2 = stringa[0:16:2]
print(con_passo_di_2)  # Output: CaiEiaoeai

# Estrai l'intera stringa
intera_stringa = stringa[:]
print(intera_stringa)  # Output: Ciao Elisabetta come stai?

# Estrai gli ultimi 6 caratteri
ultimi_sei = stringa[-6:]
print(ultimi_sei)  # Output: stai?

# Estrai la stringa al contrario
inversa = stringa[::-1]
print(inversa)  # Output: ?iat semoc attebisalE oaiC

# Estrai i caratteri da 0 a 20 con un passo di 2
con_passo_di_2_fino_a_20 = stringa[0:20:2]
print(con_passo_di_2_fino_a_20)  # Output: CaiEiaoe


```

## 7. Formattazione di stringhe
La formattazione delle stringhe in Python consente di inserire variabili o valori all'interno di una stringa in modo leggibile e flessibile.

### i. F-strings
Le f-strings sono un modo semplice e intuitivo per formattare le stringhe. Puoi inserire variabili direttamente all'interno delle parentesi graffe {}.

```python
nome = "Alice"
eta = 30
messaggio = f"Benvenuta, {nome}! Hai {eta} anni."
print(messaggio)  # Output: Benvenuta, Alice! Hai 30 anni.
```

### ii. Metodo format()
Il metodo format() consente di inserire variabili in una stringa utilizzando segnaposto {}.

```python
nome = "Alice"
eta = 30
messaggio = "Benvenuta, {}! Hai {} anni.".format(nome, eta)
print(messaggio)  # Output: Benvenuta, Alice! Hai 30 anni.
```