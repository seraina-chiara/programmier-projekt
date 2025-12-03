# -----------------------------
# Hilfsfunktion: Titel hübsch drucken
# -----------------------------
def print_title(title):
    """Zeigt gewünschten Titel an"""
    SEPARATOR_WIDTH = 40
    print("\n" + "-" * SEPARATOR_WIDTH)
    print(title.center(SEPARATOR_WIDTH))
    print("-" * SEPARATOR_WIDTH)

# -----------------------------
# Hilfsfunktion: Validierte Ja/Nein Eingabe
# Returns: ein Boolean (True/False)
# -----------------------------
def get_yes_or_no(question):
    """Validierte Ja/Nein Eingabe"""
    while True:
        answer = input(f"{question} (j/n): ")
        if answer == 'j':
            return True
        elif answer == 'n':
            return False
        else:
            print("Bitte geben Sie j oder n ein")