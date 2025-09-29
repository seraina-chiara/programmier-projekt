def create_set():
    print("Create set")


def edit_set():
    print("Edit set")


def learn_set():
    print("Learn set")
    
    

 # Introduce User   
print(f"{'-'*40}")
print(f"{'MemoCards':^40}")
print(f"{'-'*40}")

# Give the user its options
print("\nWähle aus zwischen diesen Optionen:")
print("1. Neues Karteikartenset anlegen")
print("2. Bestehende Karten aus einem Set bearbeiten")
print("3. Bestehendes Set üben")

option = input("Welche dieser drei Optionen möchten sie machen? ")

# Validate Option
# option has to be a digit and between 1 and 3
if(option.isdigit() and 1 <= int(option) <= 3):
    print(f"Du hast die Option {option} gewählt!")
    option = int(option)
    if(option == 1):
        create_set()
    elif(option == 2):
        edit_set()
    elif(option == 3):
        learn_set()
    else:
        print("Das ist keine gültige Auswahl")
else: 
    print("Das ist keine gültige Auswahl")
