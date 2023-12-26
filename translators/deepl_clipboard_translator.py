import webbrowser
import pyperclip
from urllib.parse import quote


def translate():
    text = pyperclip.paste()
    encoded_text = quote(text)
    webbrowser.open(f"https://www.deepl.com/translator#auto/en/{encoded_text}")


if __name__ == "__main__":
    translate()
