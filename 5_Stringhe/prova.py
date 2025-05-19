strutura = [{"nome": "Elisabetta", "età": 25, "occhi": "marroni", "altezza": 168}, 
            {"nome": "Alessia", "età": 25, "occhi": "verdi", "altezza": 170}, 
            {"nome": "Federica", "età": 25, "occhi": "marroni", "altezza": 167}, 
            {"nome": "Stefano", "età": 25, "occhi": "marroni", "altezza": 182}, 
            {"nome": "Fabio", "età": 25, "occhi": "marroni", "altezza": 175}, 
            {"nome": "Lorenzo", "età": 25, "occhi": "marroni", "altezza": 186}]

def stampa():
    for persona in strutura:
        for chiave in persona:
            print(persona[chiave])

def menu():
    print("1) Stampa")
    print("2) Stampa")
    print("0) Esci")

    comando = int(input("comando: "))
    if comando == 1:
        stampa()
    elif comando == 0:
        print("Ciao ciao.")
        exit

menu()