# Istruzioni varie

## Indice
1. [Istruzioni condizionali](#1-istruzioni-condizionali)
    1. [If](#if)
    2. [Operatore ternario](#operatore-ternario)
2. [Cicli](#2-cicli)
   1. [Cicli enumerativi](#cicli-enumerativi)
   2. [Cicli non enumerativi](#cicli-non-enumerativi)
3. [Funzioni](#3-funzioni)
    1. [Introduzione](#introduzione)
4. [Try](#3)

## 1. Istruzioni condizionali

### If

Le istruzioni condizionali in Python consentono di eseguire diverse azioni in base a condizioni specifiche. Le istruzioni più comuni sono `if`, `elif` e `else`.

### Esempio di Istruzione condizionale

```python
a = 10

if a > 0:
    print("a è positivo")
    if a > 5:
        print("a è maggiore di 5")  # Output: a è maggiore di 5
else:
    print("a è negativo o zero")
```

### Operatore ternario


```python
variabile = valore_se_vero if condizione else valore_se_falso
```


## Introduzione ai Cicli

In Python, i cicli sono utilizzati per eseguire un blocco di codice ripetutamente, fino a quando una condizione specificata non è soddisfatta. I due tipi principali di cicli in Python sono il ciclo `for` e il ciclo `while`.

## 2. Cicli

### 2.1 Cicli enumerativi

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


### 2.2 Cicli non enumerativi

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