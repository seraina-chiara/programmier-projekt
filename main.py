import os

# Mateo
def create_set():
    print(f"{'-'*40}")
    print(f"{'Set ERSTELLEN':^40}")
    print(f"{'-'*40}")

# Gui
def edit_cards():
    print(f"{'-'*40}")
    print(f"{'Set oder Karte BEARBEITEN':^40}")
    print(f"{'-'*40}")

# Dimitrjie
def learn_set():
    print(f"{'-'*40}")
    print(f"{'Set LERNEN':^40}")
    print(f"{'-'*40}")
    
# Seraina
def delete_cards():
    print(f"{'-'*40}")
    print(f"{'Set oder Karte LÖSCHEN':^40}")
    print(f"{'-'*40}")

    while True:
        try:
            option = int(input("Wollen Sie ein Set löschen (1)\noder eine Karte aus einem Set löschen (2)\nUm das Programm abbzubrechen gebe -1 ein: "))
            if  option == 1:
                print("Welches Set soll gelöscht werden?")
                selected_file = read_all_sets()
                if os.path.exists(selected_file):
                    os.remove(selected_file)
                    print(f"Set '{selected_file}' wurde gelöscht.")
                else:
                    print(f"Set '{selected_file}' existiert nicht.")
            elif(option == 2):
                print("Aus welchem Set soll eine Karte gelöscht werden?")
                selected_file = read_all_sets()
                # TODO: delete one card out of set
            elif(option == -1):
                break
        except ValueError:
            print("Das war keine gültige Auswahl")
    
    
    print("delete set")
    
def read_all_sets():
    # Ordnerpfad
    folder = "sets"
    # Alle Dateien im Ordner abrufen
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if not files:
        print("Im Ordner 'sets' wurden keine Dateien gefunden.")
    else:
        print("Verfügbare Dateien:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        while True:
            try:
                choice = int(input(f"Geben Sie das gewünschte Set an (Nummer zwischen 1 und {len(files)}): "))
                if 1 <= choice <= len(files):
                    selected_file = files[choice - 1]
                    print(f"\nDu hast '{selected_file}' ausgewählt.")
                    return folder + '/' + selected_file
                else:
                    print("Ungültige Nummer. Bitte erneut versuchen.")
            except ValueError:
                print("Bitte eine Zahl eingeben")



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
print("Geben Sie ein -1 ein um das Programm zu beenden")

option = 0


while True:
    option = input("Welche dieser Optionen möchten sie machen? ")
    

    # close application if user gives -1
    if str(option) == "-1":
        print("Programm wird beendet.")
        break

    # Validate Option
    # option has to be a digit and between 1 and 4
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
