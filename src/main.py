from textual.app import App
from textual.widgets import Button, Footer, Header, Input, Markdown

class Writer(App):
    CSS_PATH = "styles.css"

    def compose(self):
        yield Header()
        yield Footer()
        yield Markdown("Hello World")
        yield Input()

if __name__ == "__main__":
    app = Writer()
    app.run()
