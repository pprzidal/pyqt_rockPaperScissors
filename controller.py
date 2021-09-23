from PyQt6.QtWidgets import QApplication
import model, view, sys

"""
"""
class Controller:
    def __init__(self):
        self.model = model.Model()
        self.view = view.View()


if __name__ == "__main__":
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())