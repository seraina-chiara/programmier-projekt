import os
FOLDER = "sets"

def select_set():
    # Ordnerpfad
    # Alle Dateien im Ordner abrufen
    files = [f for f in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, f))]
    if not files:
        print(f"Im Ordner '{FOLDER}' wurden keine Dateien gefunden.")
        return None
    else:
        # alle Optionen der Dateien ausgeben
        print("Verfügbare Dateien:")
        for i, file in enumerate(files, start=1):
            print(f"\t{i}. {file}")

        while True:
            try:
                # Auswahl eines bestimmten Sets
                choice = int(input(f"Geben Sie das gewünschte Set an (Nummer zwischen 1 und {len(files)}): "))
                if 1 <= choice <= len(files):
                    selected_file = files[choice - 1]
                    print(f"\nSie haben '{choice}. {selected_file}' ausgewählt.")
                    return os.path.join(FOLDER, selected_file)
                else:
                    print("Ungültige Nummer. Bitte erneut versuchen.")
            except ValueError:
                print("Bitte eine Zahl eingeben")

def select_card_from_set(selected_file):
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

def load_cards_from_set(file):
    """Lädt Karteikarten aus einer Set-Datei."""

    cards1 = []
    cards = []
    try:

        with open(file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()
            for line in lines:
                line = line.strip("\n")
                cards1 = line.split("=", 1)
                cards.append(cards1)   
        return cards
    
    except FileNotFoundError:
        print(f"Die Datei {file} wurde nicht gefunden.")
        return []
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return []
        
def check_set_name(name: str):
    if not name :
        print("Bitte geben Sie etwas ein. ")
        return False
    
    files = [f for f in os.listdir(FOLDER) if os.path.isfile(os.path.join(FOLDER, f))]
    # alle namen iterieren
    for file in files:
        # falls die namen gleich sind, ist es ein fehler
        if(name.lower() == file.lower().removesuffix(".txt")):
            print(f"Der Set-Name '{name}' ist bereits vergeben.")
            return False
    
    return True
