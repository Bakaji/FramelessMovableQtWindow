import sys

import PySide2.QtGui
from PySide2 import QtWidgets
from PySide2.QtCore import Qt, QRect
from PySide2.QtWidgets import QApplication

from custom_title_bar import CustomTitleBar
from custom_widget import CustomWidget


class FramelessResizableWindow(QtWidgets.QMainWindow):
    def __init__(self, margin: int=5):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        ########### spaces around window#################"
        self.window_margin = margin
        self.setContentsMargins(self.window_margin, self.window_margin, self.window_margin, self.window_margin)
        ################ cursor position #####################
        self.cursorPositions = CursorPositions()
        self.cursorPositions.actualPosition = CursorPositions.DEFAULT
        ############# window component ##########################
        self.window_contents = CustomWidget()
        self.setCentralWidget(self.window_contents)
        self.title_bar = CustomWidget()
        self.main_widget = CustomWidget()
        self.vb1 = QtWidgets.QVBoxLayout()
        self.hb_title_bar = QtWidgets.QHBoxLayout()
        self.hb_title = QtWidgets.QHBoxLayout()
        self.hb_title_bar_buttons = QtWidgets.QHBoxLayout()
        self.close_button = QtWidgets.QPushButton("X")
        self.maximize_button = QtWidgets.QPushButton("+")
        self.minimize_button = QtWidgets.QPushButton("-")
        self.title = CustomTitleBar("this is a title", self)
        self.title_bar_layout = QtWidgets.QHBoxLayout()
        self.setup_main_widget()

    def mousePressEvent(self, event: PySide2.QtGui.QMouseEvent):
        ####################     top ########################
        if event.y() < self.window_margin:
            ##################top left #######################
            if event.x() < self.window_margin:
                self.cursorPositions.actualPosition = CursorPositions.TOP_LEFT
            else:
                #################top right ######################
                if event.x() > self.width() - self.window_margin:
                    self.cursorPositions.actualPosition = CursorPositions.TOP_RIGHT
                else:
                    #############top center #####################
                    self.cursorPositions.actualPosition = CursorPositions.TOP_CENTER
        else:
            #####################bottom######################
            if event.y() > self.height() - self.window_margin:
                ##################bottom left #######################
                if event.x() < self.window_margin:
                    self.cursorPositions.actualPosition = CursorPositions.BOTTOM_LEFT
                else:
                    #################bottom right ######################
                    if event.x() > self.width() - self.window_margin:
                        self.cursorPositions.actualPosition = CursorPositions.BOTTOM_RIGHT
                    else:
                        #############bottom center #####################
                        self.cursorPositions.actualPosition = CursorPositions.BOTTOM_CENTER
            else:
                ###############middle #######################
                ##############middle left#############################
                if event.x() < self.window_margin:
                    self.cursorPositions.actualPosition = CursorPositions.MIDDLE_LEFT
                else:
                    #############middle right  ############################
                    if event.x() > self.width() - self.window_margin:
                        self.cursorPositions.actualPosition = CursorPositions.MIDDLE_RIGHT
                    else:
                        self.cursorPositions.actualPosition = CursorPositions.DEFAULT

    def mouseReleaseEvent(self, event: PySide2.QtGui.QMouseEvent):
        self.cursorPositions.actualPosition = CursorPositions.DEFAULT

    def mouseMoveEvent(self, event: PySide2.QtGui.QMouseEvent):
        if self.cursorPositions.actualPosition >= 0:
            ####################top################################
            if self.cursorPositions.actualPosition <= 2:
                if self.cursorPositions.actualPosition == CursorPositions.TOP_LEFT:
                    # left resizing
                    bottom_side = self.y() + self.height()
                    top_side = event.globalY()
                    right_side = self.x() + self.width()
                    left_side = event.globalX()
                    self.setGeometry(QRect(left_side, top_side, right_side - left_side, bottom_side - top_side))
                    pass
                else:
                    if self.cursorPositions.actualPosition == CursorPositions.TOP_CENTER:
                        # center top resizing
                        bottom_side = self.y() + self.height()
                        top_side = event.globalY()
                        self.setGeometry(QRect(self.x(), top_side, self.width(), bottom_side - top_side))
                        pass
                    else:
                        # right top resizing
                        deference = event.globalX() - self.x()
                        bottom_side = self.y() + self.height()
                        top_side = event.globalY()
                        self.setGeometry(QRect(self.x(), top_side, deference, bottom_side - top_side))

                        pass

            else:
                ###################bottom#############################
                if self.cursorPositions.actualPosition >= 5:
                    if self.cursorPositions.actualPosition == CursorPositions.BOTTOM_LEFT:
                        # bottom left resizing
                        top_side = self.y()
                        bottom_side = event.globalY()
                        right_side = self.x() + self.width()
                        left_side = event.globalX()
                        self.setGeometry(QRect(left_side, self.y(), right_side - left_side, bottom_side - top_side))
                        pass
                    else:
                        if self.cursorPositions.actualPosition == CursorPositions.BOTTOM_CENTER:
                            # bottom center resizing
                            top_side = self.y()
                            bottom_side = event.globalY()
                            self.resize(self.width(), bottom_side - top_side)
                            pass
                        else:
                            # bottom right resizing
                            self.resize(event.x(), event.y())
                            pass
                else:
                    ################"middle###########################
                    if self.cursorPositions.actualPosition == CursorPositions.MIDDLE_RIGHT:
                        # right resizing
                        deference = event.globalX() - self.x()
                        self.resize(deference, self.height())
                        pass
                    else:
                        if self.cursorPositions.actualPosition == CursorPositions.MIDDLE_LEFT:
                            # left resizing
                            right_side = self.x() + self.width()
                            left_side = event.globalX()
                            self.setGeometry(QRect(left_side, self.y(), right_side - left_side, self.height()))

                            pass
        else:
            self.change_cursor_shape(event)

    def change_cursor_shape(self, event):
        ####################     top ########################
        if event.y() < self.window_margin:
            ##################top left #######################
            if event.x() < self.window_margin:
                QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
            else:
                #################top right ######################
                if event.x() > self.width() - self.window_margin:
                    QApplication.setOverrideCursor(Qt.SizeBDiagCursor)
                else:
                    #############top center #####################
                    QApplication.setOverrideCursor(Qt.SizeVerCursor)
        else:
            #####################bottom######################
            if event.y() > self.height() - self.window_margin:
                ##################bottom left #######################
                if event.x() < self.window_margin:
                    QApplication.setOverrideCursor(Qt.SizeBDiagCursor)
                else:
                    #################bottom right ######################
                    if event.x() > self.width() - self.window_margin:
                        QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
                    else:
                        #############bottom center #####################
                        QApplication.setOverrideCursor(Qt.SizeVerCursor)
            else:
                ###############middle #######################
                ##############middle left#############################
                if event.x() < self.window_margin:
                    QApplication.setOverrideCursor(Qt.SizeHorCursor)
                else:
                    #############middle right  ############################
                    if event.x() > self.width() - self.window_margin:
                        QApplication.setOverrideCursor(Qt.SizeHorCursor)
                    ##################### middle center #####################
                    else:
                        QApplication.setOverrideCursor(Qt.ArrowCursor)

    def setup_main_widget(self):
        self.setStyleSheet("background-color:white")
        self.vb1.setContentsMargins(0, 0, 0, 0)
        self.hb_title_bar.setContentsMargins(0, 0, 0, 0)
        self.hb_title.setContentsMargins(0, 0, 0, 0)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(12)
        size_policy.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(size_policy)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(1)
        size_policy.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
        self.title_bar.setSizePolicy(size_policy)
        self.title_bar.setMinimumSize(0, 30)
        self.main_widget.setContentsMargins(0, 0, 0, 0)
        self.close_button.setMaximumSize(30, 30)
        self.maximize_button.setMaximumSize(30, 30)
        self.minimize_button.setMaximumSize(30, 30)
        self.close_button.clicked.connect(lambda: self.close())
        self.maximize_button.clicked.connect(lambda: self.toggle())
        self.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.hb_title_bar_buttons.addWidget(self.minimize_button)
        self.hb_title_bar_buttons.addWidget(self.maximize_button)
        self.hb_title_bar_buttons.addWidget(self.close_button)
        self.hb_title_bar_buttons.setContentsMargins(0, 0, 0, 0)
        self.hb_title.addWidget(self.title)
        self.title_bar_layout.setContentsMargins(2, 2, 2, 2)
        self.title_bar_layout.addLayout(self.hb_title)
        self.title_bar_layout.addLayout(self.hb_title_bar_buttons)
        self.title_bar.setLayout(self.title_bar_layout)
        self.vb1.addWidget(self.title_bar)
        self.vb1.addWidget(self.main_widget)
        self.vb1.setSpacing(0)
        self.window_contents.setLayout(self.vb1)
        self.main_widget.setStyleSheet("background-color:yellow")
        self.title_bar.setStyleSheet("background-color:blue")
        self.close_button.setStyleSheet("border:1 solid white;background:1%;background-color:white")
        self.minimize_button.setStyleSheet("border:1 solid white;background:1%;background-color:white")
        self.maximize_button.setStyleSheet("border:1 solid white;background:1%;background-color:white")

    def toggle(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


class CursorPositions:
    TOP_LEFT = 0
    TOP_CENTER = 1
    TOP_RIGHT = 2

    MIDDLE_LEFT = 3
    MIDDLE_RIGHT = 4

    BOTTOM_LEFT = 5
    BOTTOM_CENTER = 6
    BOTTOM_RIGHT = 7

    DEFAULT = -1

    def __init__(self):
        self.actualPosition = self.DEFAULT
