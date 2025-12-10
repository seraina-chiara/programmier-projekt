import manageFiles
import helper_functions
import os
FOLDER = "sets"


# -----------------------------
# Option 1 – Neues Set erstellen
# -----------------------------
# Mateo
def create_set():
    """
    Erstellt ein neues Karteikarten-Set.
   
    Der Benutzer wird nach einem Namen und der Anzahl der Karten gefragt.
    Anschliessend werden Begriff und Definition für jede Karte abgefragt.
    Das Set wird als .txt-Datei im sets/ Ordner gespeichert.
   
    Der Set-Name wird validiert und darf nicht bereits existieren.
    Bei ungültigen Eingaben wird der Benutzer erneut zur Eingabe aufgefordert.
    """

    helper_functions.print_title("Neues Set erstellen")

    new_set_title = ""
    card_count = 0
    is_name_ok = False
    # solange der name noch nicht gut ist, abfragen
    while not is_name_ok:
        new_set_title = input("Wie soll das neue Set heissen? ")
        is_name_ok = manageFiles.check_set_name(new_set_title)

    #solange die Anzahl der Karten 0 oder kleiner ist
    while card_count <= 0:
        try:
            card_count = int(input("Wie viele Karten soll das Set haben? "))
        # Invalide Eingabe
        except ValueError:
            print("Das war keine gültige Auswahl") 

    # existiert der Ordner
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

    # Datei-Pfad zusammensetzen (Titel + .txt)
    file_path = os.path.join(FOLDER, f"{new_set_title}.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        # für alle karten iterieren
        for i in range(1, card_count + 1):
            # begriff und definition abfragen
            begriff = input(f"Geben Sie {i}. Begriff ein: ").strip()
            definition = input(f"Geben Sie {i}. Definition ein: ").strip()
            # mit = getrennt abspeichern
            file.write(f"{begriff}={definition}\n")
        print("Das Set wurde mit den gewünschten Karten abgespeichert.")
        

# -----------------------------
# Option 2 – Karten bearbeiten
# ----------------------------
# Gui
def edit_cards():
    """
    Ermöglicht dem Benutzer, ein bestehendes Karteikartenset oder einzelne Karten zu bearbeiten.
   
    Der Benutzer kann zwischen folgenden Optionen wählen:
    - Set umbenennen: Ändert den Namen eines bestehenden Sets
    - Karte bearbeiten: Aktualisiert den Inhalt einer einzelnen Karte
   
    Die Funktion läuft in einer Schleife bis der Benutzer -1 eingibt.
    """
    helper_functions.print_title("Set oder Karte bearbeiten")

    while True:
        #Menüauswahl anzeigen
        try:
            print("\n1. Set umbenennen")
            print("2. Karte bearbeiten")
            print("-1. Zurück zum Hauptmenü")

            choice = int(input("Deine Auswahl: "))

            if choice == -1:
                break

            elif choice == 1:
                edit_set_name()
            
            elif choice == 2:
                edit_card_content()

            else:
                print("Das war keine gültige Auswahl")

        except ValueError:
            print("Ungültige Eingabe, bitte geben Sie eine Zahl ein.")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")

def edit_set_name():
    """
    Benennt ein bestehendes Set um.
   
    Der Benutzer wählt ein Set aus der Liste verfügbarer Sets aus.
    Nach Bestätigung kann ein neuer Name eingegeben werden.
    Die Datei wird nur umbenannt, wenn der neue Name noch nicht existiert.
    """
    print("Welches Set soll umbenannt werden?")
    selected_file = manageFiles.select_set()

    #wenn Ordner sets leer ist
    if selected_file is None:
        print("Es konnte kein Set ausgewählt werden")
        return

    if selected_file and os.path.exists(selected_file):
        if helper_functions.get_yes_or_no("Möchten Sie dieses Set bearbeiten?"):
            
            # Neuen Namen für das Set eingeben
            new_name = input("Geben Sie den neuen Namen für das Set ein: ")
            if not new_name.endswith('.txt'):
                new_name += '.txt'
            
            # Neuen Pfad erstellen und Set umbenennen
            new_path = os.path.join(os.path.dirname(selected_file), new_name)
            if os.path.exists(new_path):
                print(f"Fehler: Ein Set mit dem Namen '{new_name}' existiert bereits. Bitte wählen Sie einen anderen Namen.")
            else:
                os.rename(selected_file, new_path)
                print(f"Set wurde in '{new_name}' umbenannt.\n")

                # Übersicht aller Sets anzeigen
                files = [f for f in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, f)) and f.endswith(".txt")]
                for i, file in enumerate(files, start=1):
                    print(f"\t{i}. {file}")

def edit_card_content():
    """
    Bearbeitet den Inhalt einer einzelnen Karte.
   
    Der Benutzer wählt zunächst ein Set und dann eine Karte aus diesem Set aus.
    Die aktuelle Karte wird angezeigt und der Benutzer kann einen neuen Inhalt eingeben.
    Der neue Inhalt muss dem Format 'Begriff=Definition' entsprechen.
   
    Bei ungültigem Format wird eine Fehlermeldung angezeigt und der Benutzer
    kann es erneut versuchen.
    """

    while True:
        print("Aus welchem Set soll eine Karte bearbeitet werden?")
        selected_file = manageFiles.select_set()

        if selected_file is None:
            print("Es konnte kein Set ausgewählt werden")
            return
            
        selected_card = manageFiles.select_card_from_set(selected_file)

        if selected_card is None:
            print("Es konnte keine Karte ausgewählt werden")
            return

        if helper_functions.get_yes_or_no("Möchten Sie diese Karte bearbeiten?"):
            # Alle Zeilen aus der Datei lesen
            with open(str(selected_file), 'r', encoding="utf-8") as file:
                lines = file.readlines()

                # Überprüfen, ob die ausgewählte Karte noch existiert
                if selected_card < 0 or selected_card >= len(lines):
                    print("Karte existiert nicht mehr.")
                    return
                
                # Ausgabe der aktuellen Karte
                print(f"\nAktuelle Karte:")
                print(f"{lines[selected_card].strip()}")

        # Eingabe des neuen Inhalts
        while True:

            new_content = input("\nGeben Sie den neuen Inhalt ein (Format: Begriff=Definition): ")
            new_content = new_content.strip()

            # Aufteilen des Inhalts in Begriff und Definition
            parts = new_content.split("=", 1)

            # Validierung des Formats
            if len(parts) < 2:
                print("Fehler: Das Format muss zwingend ein '=' enthalten.")
                continue

            begriff = parts[0].strip()
            definition = parts[1].strip()

            # Validierung, dass weder Begriff noch Definition leer sind
            if not begriff or not definition:
                print("Fehler: Weder der Begriff noch die Definition dürfen leer sein.")
                continue

            break  # Gültiger Inhalt, Schleife verlassen
    
        # Aktualisieren der ausgewählten Karte
        lines[selected_card] = f"{begriff}={definition}\n"

        # Schreibt die aktualisierten Zeilen zurück in die Datei
        with open(str(selected_file), 'w', encoding="utf-8") as file:
            file.writelines(lines)
            print("Karteninhalt wurde aktualisiert.\n")
            
        # Übersicht aller Karten anzeigen
        for i, card in enumerate(manageFiles.load_cards_from_set(selected_file), start=1):
            print(f"{i}. {card[0]} = {card[1]}")
        print() 

# -----------------------------
# Option 3 – Set oder Karte löschen
# -----------------------------
# Seraina
def delete_cards():
    """
    Hauptmenü für Löschoptionen.
   
    Der Benutzer kann zwischen folgenden Optionen wählen:
    - Ganzes Set löschen: Entfernt die komplette Set-Datei
    - Einzelne Karte löschen: Entfernt nur eine spezifische Karte aus einem Set
   
    Die Funktion läuft in einer Schleife bis der Benutzer -1 eingibt.
    """
    helper_functions.print_title("Set oder Karte löschen")

    while True:
        try:
            print("\n1. Ganzes Set löschen")
            print("2. Einzelne Karte löschen")
            print("-1. Zurück zum Hauptmenü")

            choice = int(input("Deine Auswahl: "))

            if choice == -1:
                break

            # Ein Set soll gelöscht werden
            elif choice == 1:
                delete_entire_set()

            # Eine Karte aus einem Set soll gelöscht werden   
            elif choice == 2:
                delete_single_card()

            # Ungültige aber valide Eingabe    
            else:
                print("Das war keine gültige Auswahl")
        # Invalide Eingabe
        except ValueError:
            print("Das war keine gültige Auswahl")

def delete_entire_set():
    """
    Löscht ein komplettes Set.
   
    Der Benutzer wählt ein Set aus der Liste aus.
    Vor der Löschung wird eine Sicherheitsabfrage (j/n) durchgeführt.
    Die komplette Set-Datei wird gelöscht.
    """
    selected_file = manageFiles.select_set()

    # falls ein set gewählt wurde, und diese datei auch existiert
    if selected_file and os.path.exists(selected_file):
        # bestätigung
        if helper_functions.get_yes_or_no("Sind Sie sicher?"):
            # löschen der ganzen datei
            os.remove(selected_file)
            print(f"Set '{selected_file}' wurde gelöscht.")
    else:
        print(f"Set '{selected_file}' existiert nicht.")

def delete_single_card():
    """
    Löscht eine einzelne Karte aus einem Set.
   
    Der Benutzer wählt zunächst ein Set und dann eine Karte aus diesem Set aus.
    Vor der Löschung wird eine Sicherheitsabfrage (j/n) durchgeführt.
    Nur die ausgewählte Karte wird aus dem Set entfernt.
    """
    selected_file = manageFiles.select_set()

    # überprüfung ob ein set gewählt werden konnte
    if selected_file is None:
        print("Es konnte kein Set ausgewählt werden")
        return

    selected_card = manageFiles.select_card_from_set(selected_file)

    # überprüfung ob eine karte gewählt werden konnte
    if selected_card is None:
        print("Es konnte keine Karte ausgewählt werden")
        return

    # bestätigung
    if helper_functions.get_yes_or_no("Sind Sie sicher?"):

        # liest alle zeilen ein
        with open(str(selected_file), 'r', encoding="utf-8") as fs:
            
            # speichert alle zeilen in die variabel lines
            lines = fs.readlines()

        # löscht die gewünschte zeile aus der variabel
        del lines[selected_card]

        # überschreibt das die ganze datei mit der variabel lines
        with open(str(selected_file), 'w', encoding="utf-8") as fs:
            fs.writelines(lines)
        print("Karte wurde erfolgreich gelöscht.")

# -----------------------------
# Option 4 – Lernen
# -----------------------------
# Dimitrije
def learn_set():
    """
    Interaktiver Lernmodus für Karteikarten.
   
    Der Benutzer wählt ein Set aus und wird dann zu allen Begriffen abgefragt.
    Nach jeder Antwort erhält der Benutzer sofortiges Feedback.
   
    Nach jeder Runde wird die Anzahl richtiger Antworten angezeigt.
    Falsch beantwortete Karten können wiederholt werden, bis alle Karten
    korrekt beantwortet wurden oder der Benutzer abbricht.
   
    Die Funktion ist case-insensitive (Gross-/Kleinschreibung wird ignoriert).
    """

    helper_functions.print_title("Set lernen")

    #Ruft die Funktion aus manageFiles auf, die den Pfad zurückgibt
    file_path = manageFiles.select_set()
    
    if file_path is None:
        return
    
    #Lädt die Datei in eine Liste von Listen z.B. [["Schweiz", "Bern"], ["..",".."]]
    cards = manageFiles.load_cards_from_set(file_path)
    
    current_cards = cards.copy()
    print("-" * 40)

    counter = 0

    #solange Karten in current_cards vorhanden sind
    while current_cards:
        wrong_cards = []
        for card in current_cards:
            #linke Element zB. "Schweiz"
            begriff = card[0]
            #rechte Element z.B. "Bern"
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
        print(f"Sie haben bisher {counter} von {len(cards)} Fragen richtig beantwortet")
        print("-" * 40)

        #Wenn die Liste wrong_cards leer ist, dann wird die Übung beendet
        if not wrong_cards:
            print("Super! Alle Karten richtig beantwortet 🎉")
            break  
        

        while True:
            again = input("Möchten Sie die falsch beantworteten Karten erneut üben? j/n: ").lower()
            if again =="j":    
                #Schleife geht weiter, aber nur wrong_cards werden geprüft
                break
            elif again == "n":
                #liste wird geleert und somit die Schleife von oben abgebrochen
                current_cards = []
                break 
            else:
                print("Bitte nur 'j' oder 'n' eingeben.")

        #nächste Runde sind nur die Karten, die wir falsch hatten
        current_cards = wrong_cards  

    print(f"Übung beendet. Insgesamt richtig beantwortet: {counter} von {len(cards)} Fragen")