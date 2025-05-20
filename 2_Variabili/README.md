
# Variabili in Python

1. [Gestione delle variabili](#gestione-delle-variabili)
    1. [Creazione di una variabile](#i-creazione-di-una-variabile)
    2. [Riutilizzo delle varibili](#ii-riutilizzo-delle-varibili)
    3. [Nomi varibili](#iii-nomi-varibili)
2. [Tipi di dato](#tipi-di-dato)
    1. [Interi](#i-interi)
    2. [Float](#ii-float)
    3. [Numeri complessi](#iii-complessi-complex)
    4. [Stringhe](#iv-stringhe-str)
    5. [Booleani](#v-booleani-bool)
    6. [None](#vi-none)
3. [Strutture dati](#strutture-dati)
    1. [Tuple](#i-tuple-tuple)
    2. [Insiemi (set)](#ii-insiemi-set)
    3. [Liste (list)](#iii-liste-list)
    4. [Dizionari (dict)](#iv-dizionari-dict)
4. [Casting](#casting)
5. [Istruzione type()](#istruzione-type)

## Gestione delle variabili

Una variabile è un contenitore - denotato da un nome - che contiene a un valore. Le variabili sono utilizzate per memorizzare dati che possono essere utilizzati e manipolati nel programma.


### i. Creazione di una variabile

Per creare una variabile in Python, basta assegnare un valore a un nome di variabile utilizzando l'operatore di assegnazione `=`. La dichiarazione non avviene in modo esplicito, inizializando la
variabile viene automaticamente anche definito il tipo.

```python
# Esempi di variabili
nome = "Alice"      # Stringa
eta = 30            # Intero
altezza = 1.75      # Float
is_student = True   # Booleano
```


Si possono anche scrivere associaizoni multiple
```python
a = b = c = 1                 # Interi
str1 = str2 = "Elisabetta"    # Stringhe
```

### ii. Riutilizzo delle varibili
Una variabile può essere sovrascritta in qualsiasi momento

```python
intero = 131299
print(intero)   # Output: 131299
intero = "ero un intero ora sono una stringa"
print(intero)   # Output: ero un intero ora sono una stringa 
```

### iii. Nomi varibili
#### Camel case 
```python
interoUno = 1
interoDue = 2
unAltroInteroAncora = 3
```

#### Snake case (best practices)
```python
intero_uno = 1
intero_due = 2
un_altro_intero_ancora = 3
```
#### Pascal Case
```
InteroUno = 1
InteroDue = 2
UnAltroInteroAncora = 3
```
#### Nomi non usabili 
```python
intero-uno = 1    # Non possono essere usati i trattiti
2intero = 2       # Non può inizare con le cifre
```

#### Case Sentive
```python
uno = 1
Uno =1
UnO = 1
UNO = 1
UN_o = 1
Un_o = 1
UN_O = 1
```


## Tipi di dato
### i. Interi
I numeri interi sono numeri senza parte decimale. Possono essere positivi o negativi.

```python
numero_intero = 13
numeroIntero = 12
Numero_Intero = 1999
```

### ii. Float

I numeri float sono numeri con la virgola mobile, ovvero numeri che possono avere una parte decimale.

```python
numero_float = 3.14
numeRo_float = 2.3
nuMeroFloa_T = 1.111
```
### iii. Complessi (complex)

I numeri complessi hanno una parte reale e una parte immaginaria, rappresentati come `a + bj`, dove `a` è la parte reale e `b` è la parte immaginaria.

```python
numero_complesso = 9 + 7j
numero_Complesso = 3 + 1j
numeroComplesso = 10j
```

### iv. Stringhe (str)

Le stringhe sono sequenze di caratteri racchiuse tra virgolette singole o doppie. Possono contenere lettere, numeri e simboli.

```python
stringaUno = "Ciao, mondo!"
stringaDue = "Ciao, Eli!"
stringaTre = "Ma quanto è carina Alessianica!?!"
stringaApiciSingoli = 'Si, si. È molto carina.'
stringaMultilinea = """"
ciao sono una stringa
multiliena
wow
"""
stringaMultipla = '''
ciao sono una stringa
multiliena
wow
''''
```
### v. Booleani (bool)

I valori booleani rappresentano la verità e possono essere solo True o False.

```python
is_vero= True
is_falso = False
```

### vi. None

Il tipo None rappresenta l'assenza di valore o un valore nullo.

```python
variabile_nulla = None
```


## Struture dati

### i. Tuple (tuple)

Le tuple sono simili alle liste, ma sono immutabili, il che significa che non possono essere modificate dopo la creazione.

```python
tupla = (1, 2, 3, "quattro")
```

### ii. Insiemi (set)

Gli insiemi sono collezioni non ordinate di elementi unici. Non possono contenere duplicati.

```python
insieme = {1, 2, 3, 4, 5}
```

### iii. Liste (list)

Le liste sono collezioni ordinate di elementi che possono contenere diversi tipi di dati. Gli elementi di una lista possono essere modificati.

```python
listaInteri = [1, 2, 3, 4, 5, 6]
listaStringhe = ["Ciao", "Feffechicca", "torna", "presto"]
listaMista = [1, 2, 3, "quattro", 5.0]
```

### iv. Dizionari (dict)

I dizionari - o array associativi - sono collezioni non ordinate di coppie chiave-valore. Le chiavi devono essere uniche e immutabili.

```python
dizionario = {"nome": "Alice", "eta": 30}
```


## Casting

Il casting in Python è il processo di conversione di un tipo di dato in un altro. Python fornisce diverse funzioni integrate per eseguire il casting tra i tipi di dati più comuni.

```python
# Esempi di casting in interi
int(1.2)          #1
int('11')         #11

# Esempi di casting in float
float(1)          #1.0
float("12")       #12.0

# Esempi di casting in carattere
chr(99)            # 'c'
str(88)           # 'X'

# Esempi di casting in float
str(1)            #'1'
str(12)           #'12'

# Esempi di casting in liste
list("ciao")      #['c', 'i', 'a', 'o']
list((2,41,19))   #[2, 41, 19]
```



## Istruzione type()
```python
type(1)                    #<class 'int'>
type(3.14)                 #<class 'float'>
type("ciao")               #<class 'str'>
type((1,2))                #<class 'tuple'>
type(["ciao","vampiro"])   #<class 'list'>
```
