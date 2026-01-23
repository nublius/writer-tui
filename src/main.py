from textual.app import App
from textual.widgets import Button, Footer, Header, Input, Markdown, Static

class TextDisplay(Static):
    def compose(self):
        yield Markdown("Hello world", id="markdown")

class InputBox(Static):
    def compose(self):
        yield Input(id="input")

class Writer(App):
    CSS_PATH = "styles.css"

    def compose(self):
        yield Header()
        yield Footer()
        yield TextDisplay(id="text_display")
        yield InputBox(id="input_box")

if __name__ == "__main__":
    app = Writer()
    app.run()
