import os

def read_all_sets():
    # Ordnerpfad
    folder = "sets"
    # Alle Dateien im Ordner abrufen
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if not files:
        print(f"Im Ordner '{folder}' wurden keine Dateien gefunden.")
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
                    print(f"\nDu hast '{choice - 1}. {selected_file}' ausgewählt.")
                    return folder + '/' + selected_file
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
                print(f"\nDu hast '{choice}. {selected_card}' ausgewählt.")
                return choice - 1
            else:
                print("Ungültige Nummer. Bitte erneut versuchen.")
        except ValueError:
                print("Bitte eine Zahl eingeben")

def load_cards_from_set(file):
    cards1 = []
    cards = []
    with open(file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()
        for line in lines:
            line = line.strip("\n")
            cards1 = line.split("=")
            cards.append(cards1)   
    return cards
        
