import genanki
import pyperclip
from deep_translator import GoogleTranslator


def pass_and_validate_id():
    default_id = "1703611906346"
    default_path = "/home/grzesiek/.local/share/Anki2/User 1/collection.anki2"
    add_flashcard(int(default_id), default_path)


def add_flashcard(deck_id, deck_path):
    model_id = 1607392319
    model = genanki.Model(
        model_id,
        'My Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{Answer}}',
            },
        ]
    )
    copied_text = pyperclip.paste()
    try:
        translated_text = GoogleTranslator(source='auto', target='pl').translate(copied_text)
    except Exception as e:
        print(f"Failed to translate text: {e}")
        return

    my_note = genanki.Note(
        model=model,
        fields=[copied_text, translated_text]
    )
    deck = genanki.Deck(deck_id, "Rosyjski")
    deck.add_note(my_note)
    genanki.Package(deck).write_to_file('output.apkg')


if __name__ == "__main__":
    pass_and_validate_id()
