import sys

from PySide2.QtWidgets import QApplication

from FW import FramelessResizableWindow

if __name__ == '__main__':
    app = QApplication()
    fr = FramelessResizableWindow(3)
    fr.resize(300,300)
    fr.show()
    sys.exit(app.exec_())