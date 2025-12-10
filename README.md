# MemoCards - Karteikarten-Lernprogramm

Ein einfaches, benutzerfreundliches Kommandozeilen-Programm zum Erstellen, Verwalten und Üben von digitalen Karteikarten. Perfekt für effektives Lernen und Memorieren von Begriffen, Definitionen und Fakten.

## 📋 Projektbeschreibung

MemoCards ist eine Python-Anwendung, die es Benutzern ermöglicht, eigene Karteikarten-Sets zu erstellen und diese interaktiv zu üben. Das Programm bietet eine intuitive Menüführung und speichert alle Karteikarten in einfachen Textdateien, die jederzeit bearbeitet oder gelöscht werden können.

**Ideal für:**
- Vokabeln lernen
- Prüfungsvorbereitung
- Allgemeinwissen trainieren
- Definitionen und Fachbegriffe memorieren

## ✨ Hauptfunktionen

### 1. Neues Karteikartenset anlegen
- Erstellen Sie ein neues Set mit einem individuellen Namen
- Definieren Sie die Anzahl der Karten
- Geben Sie für jede Karte einen Begriff und eine Definition ein
- Automatische Speicherung im `sets/` Ordner

### 2. Bestehende Karten bearbeiten
- **Sets umbenennen:** Ändern Sie den Namen eines bestehenden Sets
- **Karteninhalte bearbeiten:** Aktualisieren Sie Begriff oder Definition einzelner Karten
- Sofortige Speicherung aller Änderungen

### 3. Sets oder Karten löschen
- **Komplettes Set löschen:** Entfernen Sie ein gesamtes Karteikarten-Set
- **Einzelne Karte löschen:** Entfernen Sie spezifische Karten aus einem Set
- Sicherheitsabfrage vor jeder Löschung

### 4. Karteikarten üben
- Interaktives Abfragen der Karteikarten
- Sofortiges Feedback mit ✅/❌ Symbolen
- Anzeige der richtigen Antwort bei Fehlern
- Möglichkeit, falsch beantwortete Karten erneut zu üben
- Fortschrittsanzeige nach jeder Übungsrunde

## 🚀 Installation

### Voraussetzungen
- Python 3.7 oder höher
- Keine externen Bibliotheken erforderlich (nur Python Standard-Bibliothek)

### Schritt-für-Schritt-Anleitung

1. **Repository klonen oder herunterladen:**
   ```bash
   git clone <repository-url>
   cd programmier-projekt
   ```

2. **Projektstruktur überprüfen:**
   Stellen Sie sicher, dass folgende Dateien vorhanden sind:
   - `main.py`
   - `manageFiles.py`

3. **Programm ausführen:**
   ```bash
   python main.py
   ```

   Oder unter Windows:
   ```bash
   py main.py
   ```

## 💡 Verwendung

### Programm starten

```bash
python main.py
```

### Hauptmenü-Übersicht

Nach dem Start sehen Sie folgendes Menü:

```
----------------------------------------
              MemoCards
----------------------------------------

Wähle aus zwischen diesen Optionen:
    1. Neues Karteikartenset anlegen
    2. Bestehende Karten aus einem Set bearbeiten
    3. Set oder Karten aus einem Set löschen
    4. Bestehendes Set üben
Geben Sie ein -1 ein um das Programm zu beenden
```

### Beispiel-Workflows

#### Neues Set erstellen

1. Wählen Sie Option `1`
2. Geben Sie einen Namen ein (z.B. "Deutsch-Vokabeln")
3. Geben Sie die Anzahl der Karten ein (z.B. 5)
4. Für jede Karte:
   - Begriff eingeben (z.B. "Haus")
   - Definition eingeben (z.B. "house")

```
Wie soll das neue Set heissen? Deutsch-Vokabeln
Wie viele Karten soll das Set haben? 3
Gib 1. Begriff ein: Haus
Gib 1. Definition ein: house
Gib 2. Begriff ein: Auto
Gib 2. Definition ein: car
Gib 3. Begriff ein: Baum
Gib 3. Definition ein: tree
Das Set wurde mit den gewünschten Karten abgespeichert.
```

#### Karte bearbeiten

1. Wählen Sie Option `2`
2. Wählen Sie `2. Karte bearbeiten`
3. Wählen Sie das gewünschte Set aus
4. Wählen Sie die zu bearbeitende Karte
5. Geben Sie den neuen Inhalt ein (Format: `Begriff=Definition`)

#### Set löschen

1. Wählen Sie Option `3`
2. Wählen Sie `1. Ganzes Set löschen`
3. Wählen Sie das zu löschende Set
4. Bestätigen Sie mit `j` (ja) oder `n` (nein)

#### Set üben

1. Wählen Sie Option `4`
2. Wählen Sie das gewünschte Set
3. Beantworten Sie die Fragen
4. Nach jeder Runde:
   - Sehen Sie Ihre Punktzahl
   - Entscheiden Sie, ob Sie falsche Antworten wiederholen möchten

```
Set lernen
----------------------------------------
Haus
Antwort: house
✅ Richtig!

Auto
Antwort: vehicle
❌ Falsch! Richtige Antwort: car

----------------------------------------
Du hast bisher 1 von 2 Fragen richtig beantwortet
----------------------------------------
Möchtest du die falsch beantworteten Karten erneut üben? j/n: j
```

## Projektstruktur

```
programmier-projekt/
│
├── main.py                         # Hauptprogramm mit Menülogik
│   ├── show_menu()                # Zeigt das Hauptmenü an
│   └── choose_option()            # Verarbeitet Benutzerauswahl
│
├── card_functions.py               # Kartenverwaltungsfunktionen
Karteikarten-Sets (Mateo)
│   ├── create_set()               # Erstellt neue Sets
Bearbeitungsoptionen (Gui)
│   ├── edit_cards()               # Hauptmenü für Bearbeitung
│   │   ├── edit_set_name()        # Benennt ein Set um
│   │   └── edit_card_content()    # Bearbeitet Karteninhalt
Löschoptionen (Seraina)
│   ├── delete_cards()             # Hauptmenü für Löschoptionen 
│   │   ├── delete_entire_set()    # Löscht ein komplettes Set
│   │   └── delete_single_card()   # Löscht eine einzelne Karte
Interaktives lernen (Dimitrjie)
│   └── learn_set()                # Interaktiver Übungsmodus 
│
├── helper_functions.py             # Hilfsfunktionen 
│   ├── print_title()              # Formatierte Titelausgabe
│   └── get_yes_or_no()            # Ja/Nein-Abfragen
│
├── manageFiles.py                  # Datei-Management
│   ├── select_set()               # Interaktive Set-Auswahl
│   ├── select_card_from_set()     # Interaktive Karten-Auswahl
│   ├── load_cards_from_set()      # Lädt Karten aus Datei
│   └── check_set_name()           # Validiert Set-Namen
│
├── sets/                           # Ordner für Karteikarten-Sets (wird automatisch erstellt)
│   ├── Allgemeinwissen.txt
│   └── ...                        # Weitere Set-Dateien
│
└── README.md                       # Diese Datei
```

### Dateiformat

Karteikarten werden als einfache Textdateien im Format `Begriff=Definition` gespeichert:

```
Hauptstadt der Schweiz=Bern
Hauptstadt von Deutschland=Berlin
Hauptstadt von Frankreich=Paris
```

## Voraussetzungen

### Python-Version
- **Python 3.9 oder höher** 

### Benötigte Bibliotheken
Alle verwendeten Module sind Teil der Python Standard-Bibliothek:
- `os` - Datei- und Ordnerverwaltung

**Keine Installation externer Pakete erforderlich**


## Technische Details

### Verwendete Python-Konzepte
- Funktionen und Modularisierung
- Datei-I/O mit Kontextmanagern (`with`-Statements)
- Fehlerbehandlung mit `try-except`-Blöcken
- Listen und String-Manipulation
- Schleifen (`while`, `for`) und bedingte Anweisungen
- UTF-8 Encoding für internationale Zeichen

### Datenverarbeitung
- Karteikarten werden als Listen von `[Begriff, Definition]` gespeichert
- Dateien verwenden UTF-8 Encoding
- Trennzeichen zwischen Begriff und Definition: `=`



