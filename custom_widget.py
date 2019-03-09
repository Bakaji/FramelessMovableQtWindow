import PySide2.QtGui
from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication


class CustomWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setContentsMargins(0, 0, 0, 0)

    def mouseMoveEvent(self, event: PySide2.QtGui.QMouseEvent):
        QApplication.setOverrideCursor(Qt.ArrowCursor)