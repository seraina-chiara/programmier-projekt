import os
import helper_functions
FOLDER = "sets"

def get_available_sets():
    """
    Gibt eine Liste aller verfügbaren Karteikarten-Sets zurück.
    Gibt eine leere Liste zurück, wenn keine Dateien gefunden werden.
    """
    if not os.path.exists(FOLDER):
        return []
        
    files = [f for f in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, f)) and f.endswith(".txt")]
    return files

def get_set_path(filename):
    """Gibt den vollständigen Pfad für einen gegebenen Dateinamen zurück."""
    return os.path.join(FOLDER, filename)

def read_lines_from_set(file_path):
    """
    Liest alle Zeilen aus einer Set-Datei.
    Gibt eine Liste von Strings (Zeilen) zurück.
    """
    if not os.path.exists(file_path):
        return []
        
    with open(file_path, 'r', encoding="utf-8") as fs:
        return fs.readlines()


def select_set():
    """
    Zeigt alle verfügbaren Karteikarten-Sets an und lässt den Benutzer eines auswählen.
   
    Die Funktion listet alle .txt-Dateien im sets/ Ordner auf und fordert den Benutzer
    auf, eine Nummer einzugeben. Bei ungültigen Eingaben wird der Benutzer erneut
    zur Eingabe aufgefordert.
    """
    files = get_available_sets()

    #wenn nichts in der Liste files vorhanden ist
    if not files:
        print(f"Im Ordner '{FOLDER}' wurden keine Dateien gefunden.")
        return None
    else:
        helper_functions.print_sets(files)

        while True:
            try:
                # Auswahl eines bestimmten Sets
                choice = int(input(f"Geben Sie das gewünschte Set an (Nummer zwischen 1 und {len(files)}, oder -1 zum Abbrechen): "))
                # Wenn -1, dann abbrechen
                if choice == -1:
                    return None
                #wenn choice zwischen 1 und len(files) ist
                elif 1 <= choice <= len(files):
                    #-1 weil index bei 0 startet
                    selected_file = files[choice - 1]
                    print(f"\nSie haben '{choice}. {selected_file}' ausgewählt.")
                    #gibt komplette Pfad zurück
                    return get_set_path(selected_file)
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
    lines = read_lines_from_set(str(selected_file))

#Validierung ob lines leer ist
    if not lines:
        print("Dieses Set enthält keine Karten.")
        return None

# Alle Karten anzeigen
    helper_functions.print_cards(load_cards_from_set(selected_file))

    while True:
        try:
            # Auswahl einer bestimmten Karte
            choice = int(input(f"\nGeben Sie die gewünschte Karte an (Nummer zwischen 1 und {len(lines)}, oder -1 zum Abbrechen): "))
            # Wenn -1, dann abbrechen
            if choice == -1:
                return None
            elif 1 <= choice <= len(lines):
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
        return []
    except OSError as e:
        print(f"Dateifehler: {e}")
        return []
        
def check_set_name(name: str):
    """Prüft, ob ein Name, den der User für ein neues Set eingegeben hat, zulässig ist."""
    #keine Eingabe
    if not name:
        print("Bitte geben Sie etwas ein.")
        return False
    
    files = get_available_sets()
    # alle namen iterieren
    for file in files:
        # falls die namen gleich sind, ist es ein fehler. Alles wird klein gemacht und .txt wird entfernt damit Name geprüft wird
        if(name.lower() == file.lower().removesuffix(".txt")):
            print(f"Der Set-Name '{name}' ist bereits vergeben.")
            return False
    
    return True
