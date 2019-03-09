import PySide2.QtGui
from PySide2.QtCore import Qt, QPoint
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel


class CustomTitleBar(QLabel):
    def __init__(self, text, window: QMainWindow):
        super().__init__()
        self.setMouseTracking(True)
        self.setText(text)
        self.parent_window = window
        self.setContentsMargins(0, 0, 0, 0)
        self.parent_window.oldPos = self.parent_window.pos()

    def mousePressEvent(self, ev: PySide2.QtGui.QMouseEvent):
        self.parent_window.oldPos = ev.globalPos()

    def mouseMoveEvent(self, event: PySide2.QtGui.QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            QApplication.setOverrideCursor(Qt.ArrowCursor)
            delta = QPoint(event.globalPos() - self.parent_window.oldPos)
            self.parent_window.move(self.parent_window.x() + delta.x(), self.parent_window.y() + delta.y())
            self.parent_window.oldPos = event.globalPos()
