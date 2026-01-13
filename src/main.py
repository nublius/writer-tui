import pytermgui as ptg

def main():
    input_field = ptg.InputField(
        prompt="> "
    )

    content_box = ptg.Container(
        ptg.Label("hello world")
    )

    layout = ptg.Container(
        content_box,
        input_field,
    )

    window = ptg.Window(
        layout,
        title="Writer TUI",
        expand=True
    )

    window.center(1)

    manager = ptg.WindowManager()
    manager.add(window)

    manager.run()

main()
