import card_functions
import helper_functions


# -----------------------------
# Hauptmenü anzeigen
# -----------------------------
def show_menu():
    """Zeigt das Hauptmenü mit allen verfügbaren Optionen an."""

    print("\nBitte wählen Sie eine der folgenden Optionen:")
    print("\t1. Neues Karteikartenset anlegen")
    print("\t2. Bestehende Karten aus einem Set bearbeiten")
    print("\t3. Set oder Karten aus einem Set löschen")
    print("\t4. Bestehendes Set üben")
    print("Geben Sie ein -1 ein um das Programm zu beenden.")



def choose_option():
    """
    Hauptschleife für die Menüauswahl.
    Verarbeitet Benutzereingaben und ruft entsprechende Funktionen auf.
    Läuft bis der Benutzer -1 eingibt.
    """

    while True:
        show_menu()
        
        try:
            option = int(input("Welche dieser Optionen möchten Sie auswählen? "))
        except ValueError:
            print("Bitte geben Sie eine Zahl ein (1-4 oder -1 zum Beenden).")
            continue

        # close application if user gives -1
        if option == -1:
            print("Programm wird beendet.")
            break

        if option == 1:
            card_functions.create_set()
        elif option == 2:
            card_functions.edit_cards()
        elif option == 3:
            card_functions.delete_cards()
        elif option == 4:
            card_functions.learn_set()
        else: 
            print("Bitte wählen Sie eine Option zwischen 1 und 4 oder -1 zum Beenden.")


def main():
    """
    Haupteinstiegspunkt des MemoCards-Programms.
   
    Zeigt den Titel an und startet die Hauptmenü-Schleife,
    die dem Benutzer ermöglicht, Karteikarten-Sets zu erstellen,
    zu bearbeiten, zu löschen oder zu üben.
    """
    #Ruft die Funktion print_title() aus Datei helper_functions.py und zeigt Titel MemoCards
    helper_functions.print_title("MemoCards")
    choose_option()


if __name__ == '__main__':
    main()
