import argparse

# Creazione del parser degli argomenti
parser = argparse.ArgumentParser(description="Descrizione del file con parametri da riga di comando")

# Aggiunta dell"argomento obbligatorio
parser.add_argument("arg_obbligatorio", help="Descrizione dell'argomento obbligatorio")

# Aggiunta dell"argomento opzionale
parser.add_argument("-a", "--arg_opzionale", help="Descrizione dell'argomento opzionale")

# Parsing degli argomenti da riga di comando
args = parser.parse_args()

# Utilizzo degli argomenti
print("L'argomento obbligatorio è:", args.arg_obbligatorio)
if args.arg_opzionale:
    print("L'argomento opzionale è:", args.arg_opzionale)
else:
    print("L'argomento opzionale non è stato specificato.")

# python run.py valore_obbligatorio
# python run.py valore_obbligatorio --arg_opzionale valore_opzionale