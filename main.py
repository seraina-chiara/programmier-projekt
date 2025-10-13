import manageFiles
import os


# -----------------------------
# Hauptmenü anzeigen
# -----------------------------
def show_menu():
    print("\nWähle aus zwischen diesen Optionen:")
    print("\t1. Neues Karteikartenset anlegen")
    print("\t2. Bestehende Karten aus einem Set bearbeiten")
    print("\t3. Bestehende Karten aus einem Set löschen")
    print("\t4. Bestehendes Set üben")
    print("Geben Sie ein -1 ein um das Programm zu beenden")


# -----------------------------
# Auswahl im Hauptmenü
# -----------------------------
def choose_option():
    while True:
        show_menu()
        try:
            option = int(input("Welche dieser Optionen möchten sie machen? "))
        except ValueError:
            print("Diese Option ist nicht valid")
            continue

        # close application if user gives -1
        if option == -1:
            print("Programm wird beendet.")
            break

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

# -----------------------------
# Option 1 – Neues Set erstellen
# -----------------------------
# Mateo
def create_set():
    print_title("Neues Set erstellen")

# -----------------------------
# Option 2 – Karten bearbeiten
# ----------------------------
# Gui
def edit_cards():
    print_title("Set oder Karte bearbeiten")

# -----------------------------
# Option 3 – Set oder Karte löschen
# -----------------------------
# Seraina
def delete_cards():
    print_title("Set oder Karte löschen")

    while True:
        try:
            print("\n1. Ganzes Set löschen")
            print("2. Einzelne Karte löschen")
            print("-1. Zurück zum Hauptmenü")

            choice = int(input("Deine Auswahl: "))

            if choice == -1:
                break

            elif choice == 1:
                print("Welches Set soll gelöscht werden?")
                selected_file = manageFiles.read_all_sets()

                if selected_file and os.path.exists(selected_file):
                    if get_yes_or_no("Sind Sie sicher?"):
                        os.remove(selected_file)
                        print(f"Set '{selected_file}' wurde gelöscht.")
                else:
                    print(f"Set '{selected_file}' existiert nicht.")

                
            elif choice == 2:
                print("Aus welchem Set soll eine Karte gelöscht werden?")
                selected_file = manageFiles.read_all_sets()

                if selected_file is None:
                    print("Es konnte kein Set ausgewählt werden")
                    break

                selected_card = manageFiles.select_card_from_set(selected_file)

                if selected_card is None:
                    print("Es konnte keine Karte ausgewählt werden")
                    break

                if get_yes_or_no("Sind Sie sicher?"):
                    with open(str(selected_file), 'r', encoding="utf-8") as fs:
                        lines = fs.readlines()
                    del lines[selected_card]
                    with open(str(selected_file), 'w', encoding="utf-8") as fs:
                        fs.writelines(lines)
                
            else:
                print("Das war keine gültige Auswahl")
        except ValueError:
            print("Das war keine gültige Auswahl")

  
# -----------------------------
# Option 4 – Lernen
# -----------------------------
# Dimitrjie
def learn_set():
    print_title("Set lernen")
    
 
# -----------------------------
# Hilfsfunktion: Titel hübsch drucken
# -----------------------------
def print_title(title):
    print("\n" + "-" * 40)
    print(title.center(40))
    print("-" * 40)

def get_yes_or_no(question):
    while True:
        answer = input(f"{question} (j/n): ")
        if answer == 'j':
            return True
        elif answer == 'n':
            return False
        else:
            print("Bitte geben sie j oder n ein")

def main():
    print_title("MemoCards")
    choose_option()


if __name__ == '__main__':
    main()
