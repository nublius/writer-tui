import os

class Document:
    def __init__(self, file_name, folder="dest"):
        # Absolute path to destination folder
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.folder = os.path.join(base_dir, folder)
        os.makedirs(self.folder, exist_ok=True)

        # Full path to file
        self.file_path = os.path.join(self.folder, file_name)

        # Check if file exists(empty if new)
        self._ensure_empty()

    def _ensure_empty(self):
        if not os.path.exists(self.file_path):
            open(self.file_path, "x").close()

    def append(self, line):
        with open(self.file_path, "a") as f:
            f.write(line + "  \n")

    def read_all(self):
        with open(self.file_path, "r") as f:
            return f.read().splitlines()

    def read_text(self):
        with open(self.file_path, "r") as f:
            return f.read()
