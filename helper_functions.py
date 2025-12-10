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
        answer = input(f"{question} (j/n): ").lower()
        if answer == 'j':
            return True
        elif answer == 'n':
            return False
        else:
            print("Bitte geben Sie j oder n ein")


def print_sets(files):
    """
    Gibt eine nummerierte Liste von Sets aus.
    """
    print("Verfügbare Dateien:")
    for i, file in enumerate(files, start=1):
        print(f"\t{i}. {file}")


def print_cards(cards):
    """
    Gibt eine nummerierte Liste von Karten aus.
    """
    print("Verfügbare Karten:")
    for i, card in enumerate(cards, start=1):
        print(f"{i}. {card[0]} = {card[1]}")

