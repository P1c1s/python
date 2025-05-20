# Istruzioni varie

## Indice
1. [Istruzioni condizionali](#1-istruzioni-condizionali)
    1. [Istruzione if](#i-istruzione-if)
    2. [Operatore ternario](#ii-operatore-ternario)
2. [Cicli](#2-cicli)
   1. [Cicli enumerativi](#i-cicli-enumerativi)
   2. [Cicli non enumerativi](#ii-cicli-non-enumerativi)
3. [Funzioni](#3-funzioni)
    1. [Introduzione](#i-introduzione)
    2. [Struttura](#ii-struttura)
    3. [Argomenti](#iii-argomenti)
    4. [Tipo di ritorno](#iv-tipo-di-ritorno)
    5. [Chiamata di una funzione](#v-tipo-di-ritorno)

4. [Try](#3)

## 1. Istruzioni condizionali

### i. Istruzione if

Le istruzioni condizionali in Python consentono di eseguire diverse azioni in base a condizioni specifiche. Le istruzioni più comuni sono `if`, `elif` e `else`.

#### Esempio

```python
a = 10

if a > 0:
    print("a è positivo")
    if a > 5:
        print("a è maggiore di 5")  # Output: a è maggiore di 5
else:
    print("a è negativo o zero")
```

### ii. Operatore ternario


```python
variabile = valore_se_vero if condizione else valore_se_falso
```

## 2. Cicli

In Python, i cicli sono utilizzati per eseguire un blocco di codice ripetutamente, fino a quando una condizione specificata non è soddisfatta. I due tipi principali di cicli in Python sono il ciclo `for` e il ciclo `while`.

### i. Cicli enumerativi

I cicli enumerativi sono utilizzati per iterare su una sequenza, come una lista, una tupla, un dizionario, un insieme o una stringa. Il ciclo `for` è il principale ciclo enumerativo in Python.

#### Esempio di Ciclo `for`

```python
frutti = ["mela", "banana", "ciliegia"]

for frutto in frutti:
    print(frutto)
```
oppure

```python
for i in range(5):
    print(l[i])
```


### ii. Cicli non enumerativi

I cicli non enumerativi, come il ciclo `while`, eseguono un blocco di codice finché una condizione specificata è vera.

#### Esempio di Ciclo `while`

```python
contatore = 0

while contatore < 5:
    print(contatore)
    contatore += 1
```

```python
while True:
    risposta = input("Vuoi continuare? (s/n): ")
    if risposta.lower() == 'n':
        break
```


## 3. Funzioni

### Introduzione
Le funzioni in Python sono blocchi di codice riutilizzabili che eseguono un'operazione specifica. Possono accettare input, chiamati argomenti, e possono restituire un valore. Le funzioni aiutano a rendere il codice più organizzato e leggibile.

### Definizione di una Funzione
Per definire una funzione in Python, utilizziamo la parola chiave `def`, seguita dal nome della funzione e da parentesi tonde che possono contenere argomenti. Ecco la sintassi di base:

```python
def nome_funzione(argomento1, argomento2):
    # Corpo della funzione
    return valore
```

## i. Introduzione

Le funzioni in Python sono blocchi di codice riutilizzabili che eseguono un'operazione specifica. Possono accettare input, chiamati argomenti, e possono restituire un valore. Le funzioni aiutano a rendere il codice più organizzato e leggibile.

## ii. Struttura

Per definire una funzione, utilizziamo la parola chiave def, seguita dal nome della funzione e da parentesi tonde che possono contenere argomenti. Ecco la sintassi di base:

```python

def nome_funzione(): # "Testa della funzione"
    # Corpo della funzione
```

## iii. Argomenti
Le funzioni possono anche avere degli argomenti che gli vengono passati per essere elaborati nel corpo della funzione stessa.

```python

def nome_funzione(argomento1, argomento2):
    # Corpo della funzione
    return valore

```
 
Le funzioni possono anche accettare o meno gli argomenti.

```python
def saluto(nome="Mondo"):
    return f"Ciao, {nome}!"

print(saluto())          # Output: Ciao, Mondo!
print(saluto("Alice"))   # Output: Ciao, Alice!
```

Le funzioni possono anche accettare un numero variabile di argomenti utilizzando `*args` e `**kwargs`. Questo è utile quando non si conosce in anticipo il numero di argomenti che verranno passati alla funzione. 

`*args:` Permette di passare un numero variabile di argomenti posizionali. Gli argomenti vengono raccolti in una tupla.

```python
def somma_variabile(*args):
    return sum(args)

print(somma_variabile(1, 2, 3))  # Output: 6
print(somma_variabile(1, 2, 3, 4, 5))  # Output: 15
```

`**kwargs`: Permette di passare un numero variabile di argomenti keyword (nome-valore). Gli argomenti vengono raccolti in un dizionario.

```python
def stampa_info(**kwargs):
    for chiave, valore in kwargs.items():
        print(f"{chiave}: {valore}")

stampa_info(nome="Alice", eta=30, città="Roma")
# Output:
# nome: Alice
# eta: 30
# città: Roma
```

## iii. Tipo di ritorno

Il tipo di ritorno di una funzione è il valore che la funzione restituisce al termine della sua esecuzione. Utilizziamo la parola chiave return per specificare il valore di ritorno. Se non viene specificato alcun valore di ritorno, la funzione restituirà None per impostazione predefinita.

### Esempi

```python

def salutoNull():
    print("ciao")

def saluto():
    parola = "ciao"
    return parola

def somma(a, b):
    risultato = a + b
    return risultato

def creaLista(a, b):
    lista = []
    lista.append(a)
    lista.append(b)
    return lista

```

## iv. Chiamata di una funzione

Per chiamare una funzione, utilizziamo il suo nome seguito da parentesi tonde contenenti gli argomenti. Ecco un esempio di chiamata della funzione somma:



```python

def somma(a, b):
    risultato = a + b
    return risultato

risultato = somma(5, 3) # Chiamata della funzione somma
print(risultato)  # Output: 8
```
