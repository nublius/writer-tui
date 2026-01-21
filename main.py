from textual.app import App
from textual.widgets import Button, Footer, Header, Input, Log

class HelloApp(App):
    def compose(self):
        yield Static("Hello world!")

if __name__ == "__main__":
    app = HelloApp()
    app.run()
