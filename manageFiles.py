import os
FOLDER = "sets"

def select_set():
    """
    Zeigt alle verfügbaren Karteikarten-Sets an und lässt den Benutzer eines auswählen.
   
    Die Funktion listet alle .txt-Dateien im sets/ Ordner auf und fordert den Benutzer
    auf, eine Nummer einzugeben. Bei ungültigen Eingaben wird der Benutzer erneut
    zur Eingabe aufgefordert.
    """
    # Alle Dateien im Ordner abrufen - os.listdir(FOLDER) holt sich alles von Ordner sets und prüft mit os.path.file ob "sets/f" eine Datei ist
    files = [f for f in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, f)) and f.endswith(".txt")]
    #wenn nichts in der Liste files vorhanden ist
    if not files:
        print(f"Im Ordner '{FOLDER}' wurden keine Dateien gefunden.")
        return None
    else:
        # alle Optionen der Dateien ausgeben
        print("Verfügbare Dateien:")
        #in i wird die Zahl gespeichert und in file die Dateiname
        for i, file in enumerate(files, start=1):
            print(f"\t{i}. {file}")

        while True:
            try:
                # Auswahl eines bestimmten Sets
                choice = int(input(f"Geben Sie das gewünschte Set an (Nummer zwischen 1 und {len(files)}): "))
                #wenn choice zwischen 1 und len(files) ist
                if 1 <= choice <= len(files):
                    #-1 weil index bei 0 startet
                    selected_file = files[choice - 1]
                    print(f"\nSie haben '{choice}. {selected_file}' ausgewählt.")
                    #gibt komplette Pfad zurück
                    return os.path.join(FOLDER, selected_file)
                else:
                    print("Ungültige Nummer. Bitte erneut versuchen.")
            except ValueError:
                print("Bitte eine Zahl eingeben")

def select_card_from_set(selected_file):
    """
    Zeigt alle Karten aus einem Set an und lässt den Benutzer eine auswählen.
   
    Die Funktion liest alle Zeilen aus der angegebenen Set-Datei und zeigt sie
    nummeriert an. Der Benutzer kann durch Eingabe einer Nummer eine Karte auswählen.
   
    Args:
        selected_file (str): Pfad zur Set-Datei, aus der eine Karte ausgewählt werden soll
    """
    with open(str(selected_file), 'r', encoding="utf-8") as fs:
        lines = fs.readlines()

    for i, line in enumerate(lines, start=1):
        print(f"\t{i}. {line.strip()}")

    while True:
        try:
            choice = int(input(f"\nGeben Sie die gewünschte Karte an (Nummer zwischen 1 und {len(lines)}): "))
            if 1 <= choice <= len(lines):
                selected_card = lines[choice - 1].strip()
                print(f"\nSie haben '{choice}. {selected_card}' ausgewählt.")
                return choice - 1
            else:
                print("Ungültige Nummer. Bitte erneut versuchen.")
        except ValueError:
                print("Bitte eine Zahl eingeben")

def load_cards_from_set(file_path):
    """
    Lädt alle Karteikarten aus einer Set-Datei.
   
    Die Funktion liest die Set-Datei zeilenweise und teilt jede Zeile am '=' Zeichen,
    um Begriff und Definition zu trennen. Die Karten werden als Liste von Listen
    zurückgegeben, wobei jede innere Liste [Begriff, Definition] enthält.
   
    Args:
        file_path (str): Pfad zur Set-Datei, die geladen werden soll
    """

    card_pair = []
    all_cards = []
    try:

        with open(file_path, "r", encoding="utf-8") as infile:
            lines = infile.readlines()
            for line in lines:
                line = line.strip("\n")
                #in die liste card_pair z.B. ["Schweiz", "Bern"]
                card_pair = line.split("=", 1)
                all_cards.append(card_pair)   
        #gibt all_cards zurück in zweidimensionale liste z.B. [["Schweiz", "Bern"], ["..",".."]]
        return all_cards
    
    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")
        #gibt leere Liste zurück damit das Programm nicht crasht
        return []
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return []
        
def check_set_name(name: str):
    """Prüft, ob ein Name, den der User für ein neues Set eingegeben hat, zulässig ist."""
    #keine Eingabe
    if not name :
        print("Bitte geben Sie etwas ein. ")
        return False
    
    files = [f for f in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, f)) and f.endswith(".txt")]
    # alle namen iterieren
    for file in files:
        # falls die namen gleich sind, ist es ein fehler. Alles wird klein gemacht und .txt wird entfernt damit Name geprüft wird
        if(name.lower() == file.lower().removesuffix(".txt")):
            print(f"Der Set-Name '{name}' ist bereits vergeben.")
            return False
    
    return True
