import sys

from PyQt5.QtWidgets import QApplication

from translator import Translator
from translator_gui import Ui_MainWindow
from vocab import vocabulary
from events import EventHandler

def main():
    
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    tr = Translator(vocabulary)
    ev = EventHandler(ui, tr)
    ui.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()