# Mateo
def create_set():
    print("Create set")

# Gui
def edit_cards():
    print("Edit set")

# Dimitrjie
def learn_set():
    print("Learn set")
    
# Seraina
def delete_cards():
    print("Learn set")
    
    

 # Introduce User   
print(f"{'-'*40}")
print(f"{'MemoCards':^40}")
print(f"{'-'*40}")

# Give the user its options
print("\nWähle aus zwischen diesen Optionen:")
print("\t1. Neues Karteikartenset anlegen")
print("\t2. Bestehende Karten aus einem Set bearbeiten")
print("\t3. Bestehende Karten aus einem Set löschen")
print("\t4. Bestehendes Set üben")

option = input("Welche dieser drei Optionen möchten sie machen? ")

# Validate Option
# option has to be a digit and between 1 and 3
if(option.isdigit() and 1 <= int(option) <= 4):
    print(f"Du hast die Option {option} gewählt!")
    option = int(option)
    if(option == 1):
        create_set()
    elif(option == 2):
        edit_cards()
    elif(option == 3):
        delete_cards()
    elif(option == 4):
        learn_set()
else: 
    print("Das ist keine gültige Auswahl")
