from textual import on
from textual.app import App
from textual.widgets import Button, Footer, Header, Input, Markdown, Static
from document import Document

class TextDisplay(Static):
    def compose(self):
        yield Markdown("", id="markdown")

class InputBox(Static):
    def compose(self):
        yield Input(id="input")

class Writer(App):
    doc: Document | None = None

    BINDINGS = [

    ]

    CSS_PATH = "styles.css"

    def compose(self):
        yield Header()
        yield Footer()
        yield TextDisplay(id="text_display")
        yield InputBox(id="input_box")

    @on(Input.Submitted)
    def on_input_submitted(self, event: Input.Submitted) -> None:
        submitted_text = event.value
        
        if not self.doc:
            self.doc = Document(f"{submitted_text}.md")
            if self.doc.read_text() == "":
                self.doc.append(f"# {submitted_text}")
        else:
            self.doc.append(submitted_text)

        text_display = self.query_one("#text_display", TextDisplay)
        markdown_widget = text_display.query_one("#markdown", Markdown)
        markdown_widget.update(self.doc.read_text())
        input_box = self.query_one("#input", Input)
        input_box.value = ""



if __name__ == "__main__":
    app = Writer()
    app.run()
