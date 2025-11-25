import manageFiles
import os
FOLDER = "sets"


# -----------------------------
# Hauptmenü anzeigen
# -----------------------------
def show_menu():
    print("\nWähle aus zwischen diesen Optionen:")
    print("\t1. Neues Karteikartenset anlegen")
    print("\t2. Bestehende Karten aus einem Set bearbeiten")
    print("\t3. Set oder Karten aus einem Set löschen")
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

    new_set_title = ""
    card_count = 0
    is_name_ok = False
    # solange der name noch nicht gut ist, abfragen
    while not is_name_ok:
        new_set_title = input("Wie soll das neue Set heissen? ")
        is_name_ok = manageFiles.check_set_name(new_set_title)

    while card_count <= 0:
        try:
            card_count = int(input("Wie viele Karten soll das Set haben? "))
        # Invalide Eingabe
        except ValueError:
            print("Das war keine gültige Auswahl") 

    # exisitert der Ordner
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

    # Datei-Pfad zusammensetzen (Titel + .txt)
    file_path = os.path.join(FOLDER, f"{new_set_title}.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        # für alle karten iterieren
        for i in range(1, card_count + 1):
            # begriff und definition abfragaen
            begriff = input(f"Gib {i}. Begriff ein: ")
            definition = input(f"Gib {i}. Definition ein: ")
            # mit = getrennt abspeichern
            file.write(f"{begriff}={definition}\n")
        print("Das Set wurde mit den gewünschten Karten abgespeichert.")
        

# -----------------------------
# Option 2 – Karten bearbeiten
# ----------------------------
# Gui
def edit_cards():
    print_title("Set oder Karte bearbeiten")

    while True:
            #Menüauswahl anzeigen
            try:
                print("\n1. Set bearbeiten")
                print("2. Karte bearbeiten")
                print("-1. Zurück zum Hauptmenü")

                choice = int(input("Deine Auswahl: "))

                if choice == -1:
                    break

                elif choice == 1:
                    print("Welches Set soll bearbeitet werden?")
                    selected_file = manageFiles.select_set()

                    if selected_file is None:
                        print("Es konnte kein Set ausgewählt werden")
                        break

                    if selected_file and os.path.exists(selected_file):
                        if get_yes_or_no("Möchten Sie dieses Set bearbeiten?"):

                            # Neuen Namen für das Set eingeben
                            new_name = input("Geben Sie den neuen Namen für das Set ein: ")
                            if not new_name.endswith('.txt'):
                                new_name += '.txt'
                            
                            #Neues Pfad erstellen und Set umbenennen
                            new_path = os.path.join(os.path.dirname(selected_file), new_name)
                            os.rename(selected_file, new_path)
                            print(f"Set wurde in '{new_name}' umbenannt.")

                elif choice == 2:
                    print("Aus welchem Set soll eine Karte bearbeitet werden?")
                    selected_file = manageFiles.select_set()

                    if selected_file is None:
                        print("Es konnte kein Set ausgewählt werden")
                        break
                        
                    selected_card = manageFiles.select_card_from_set(selected_file)

                    if selected_card is None:
                        print("Es konnte keine Karte ausgewählt werden")
                        break

                    if get_yes_or_no("Möchten Sie diese Karte bearbeiten?"):
                        # Alle Zeilen aus der Datei lesen
                        with open(str(selected_file), 'r', encoding="utf-8") as file:
                            lines = file.readlines()
                            # Überprüfen, ob die ausgewählte Karte noch existiert
                            if selected_card < 0 or selected_card >= len(lines):
                                print("Karte existiert nicht mehr.")
                                break
                            # Ausgabe der aktuellen Karte
                            print(f"\nAktuelle Karte:")
                            print(f"{lines[selected_card].strip()}")
                        #Eingabe des neuen Inhalts
                        new_content = input("\nGeben Sie den neuen Inhalt ein: ")
                        lines[selected_card] = new_content + "\n"
                        # Schreibt die aktualisierten Zeilen zurück in die Datei
                        with open(str(selected_file), 'w', encoding="utf-8") as file:
                            file.writelines(lines)
                            print("Karteninhalt wurde aktualisiert.")

                else:
                    print("Das war keine gültige Auswahl")

            except ValueError:
                print("Ungültige Eingabe, bitte geben Sie eine Zahl ein.")
            except Exception as e:
                print(f"Ein Fehler ist aufgetreten: {e}")


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

            # -1 bedeutet abbrechen
            if choice == -1:
                break

            # Ein Set soll gelöscht werden
            elif choice == 1:
                print("Welches Set soll gelöscht werden?")
                selected_file = manageFiles.select_set()

                # falls ein set gewählt wurde, und diese datei auch exisitert
                if selected_file and os.path.exists(selected_file):
                    # bestätigung
                    if get_yes_or_no("Sind Sie sicher?"):
                        # löschen der ganzen datei
                        os.remove(selected_file)
                        print(f"Set '{selected_file}' wurde gelöscht.")
                else:
                    print(f"Set '{selected_file}' existiert nicht.")

            # Eine Karte aus einem Set soll gelöscht werden   
            elif choice == 2:
                print("Aus welchem Set soll eine Karte gelöscht werden?")
                selected_file = manageFiles.select_set()

                # überprüfung ob die datei exisitert
                if selected_file is None:
                    print("Es konnte kein Set ausgewählt werden")
                    break

                selected_card = manageFiles.select_card_from_set(selected_file)

                # überprüfung ob eine karte gewählt werden konnte
                if selected_card is None:
                    print("Es konnte keine Karte ausgewählt werden")
                    break

                # bestätigung
                if get_yes_or_no("Sind Sie sicher?"):
                    # liesst alle zeilen ein
                    with open(str(selected_file), 'r', encoding="utf-8") as fs:
                        # speichert alle zeilen in die variabel lines
                        lines = fs.readlines()
                    # löscht die gewünschte zeile aus der variabel
                    del lines[selected_card]
                    # überschreibt das die ganze datei mit der variabel lines
                    # die gelöschte zeile ist nun nicht mehr drin
                    with open(str(selected_file), 'w', encoding="utf-8") as fs:
                        fs.writelines(lines)
            # Ungültige aber valide Eingabe    
            else:
                print("Das war keine gültige Auswahl")
        # Invalide Eingabe
        except ValueError:
            print("Das war keine gültige Auswahl")

  
# -----------------------------
# Option 4 – Lernen
# -----------------------------
# Dimitrjie
def learn_set():
    print_title("Set lernen")

    file = manageFiles.select_set()
    cards = manageFiles.load_cards_from_set(file)
    
    current_cards = cards.copy()  # Karten, die aktuell geübt werden
    print("-" * 40)

    while current_cards:
        wrong_cards = []
        counter = 0
        for card in current_cards:
            begriff = card[0]
            definition = card[1]
            print(begriff)
            answer = input("Antwort: ")
            if answer.lower() == definition.lower():
                print("✅ Richtig!\n")
                counter += 1
            else:
                print(f"❌ Falsch! Richtige Antwort: {definition}\n")
                wrong_cards.append(card)
        print("-" * 40)
        print(f"Du hast bisher {counter} von {len(cards)} Fragen richtig beantwortet")
        print("-" * 40)

        if not wrong_cards:
            print("Super! Alle Karten richtig beantwortet 🎉")
            break  
        
        while True:
            again = input("Möchtest du die falsch beantworteten Karten erneut üben? j/n: ").lower()
            if again =="j":    
                break
            elif again == "n":
                current_cards = []
                break 
            else:
                print("Bitte nur 'j' oder 'n' eingeben.")

        current_cards = wrong_cards  

    print(f"Übung beendet. Insgesamt richtig beantwortet: {counter} von {len(cards)} Fragen")

 
# -----------------------------
# Hilfsfunktion: Titel hübsch drucken
# -----------------------------
def print_title(title):
    print("\n" + "-" * 40)
    print(title.center(40))
    print("-" * 40)

# -----------------------------
# Hilfsfunktion: Validierte Ja/Nein Eingabe
# Returns: ein Boolean (True/False)
# -----------------------------
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
