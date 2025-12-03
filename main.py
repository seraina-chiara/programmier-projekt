import helper_functions
import card_functions


# -----------------------------
# Hauptmenü anzeigen
# -----------------------------
def show_menu():
    """Zeigt das Hauptmenü mit allen verfügbaren Optionen an."""

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
    """
    Hauptschleife für die Menüauswahl.
    Verarbeitet Benutzereingaben und ruft entsprechende Funktionen auf.
    Läuft bis der Benutzer -1 eingibt.
    """

    while True:
        show_menu()
        #prüft, ob der eingegebene Wert eine Zahl (integer) ist
        try:
            option = int(input("Welche dieser Optionen möchten Sie auswählen? "))
        
        #wenn es ein anderer Wert ist wird der Fehler aufgefengen und das Menu wieder angezeigt 
        except ValueError:
            print("Diese Option ist nicht gültig")
            continue

        # close application if user gives -1
        if option == -1:
            print("Programm wird beendet.")
            break
        
        #Wenn eine Zahl von 1-4 eingegeben wird, wird die entsprechende Funktion aus card_functions.py aufgerufen
        if option == 1:
            card_functions.create_set()
        elif option == 2:
            card_functions.edit_cards()
        elif option == 3:
            card_functions.delete_cards()
        elif option == 4:
            card_functions.learn_set()
        
        #Wenn ein integer eingegeben wird der nicht zwischen 1-4 und -1 ist, wird eine Meldung angezeigt
        else: 
            print("Das ist keine gültige Auswahl")


def main():
    #Ruft die Funktion print_title() aus Datei helper_functions.py und zeigt Titel MemoCards
    helper_functions.print_title("MemoCards")
    #Funktion choose_option() wird ausgeführt                                           
    choose_option()                                                                     


if __name__ == '__main__':
    main()
