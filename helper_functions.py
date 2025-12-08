
def print_title(title):
    """Hilfsfunktion: Titel hübsch drucken"""
    SEPARATOR_WIDTH = 40
    print("\n" + "-" * SEPARATOR_WIDTH)
    print(title.center(SEPARATOR_WIDTH))
    print("-" * SEPARATOR_WIDTH)


def get_yes_or_no(question):
    """
    Hilfsfunktion: Validierte Ja/Nein Eingabe
    Returns: ein Boolean (True/False)
    """
    while True:
        answer = input(f"{question} (j/n): ")
        if answer == 'j':
            return True
        elif answer == 'n':
            return False
        else:
            print("Bitte geben Sie j oder n ein")