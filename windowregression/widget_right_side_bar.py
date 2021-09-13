from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QDoubleValidator

import numpy as np
import itertools

import random

class WidgetRightSideBar(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        font_times_16 = QFont("Times New Roman", 16)
        font_times_16_underline = QFont("Times New Roman", 16)
        font_times_16_underline.setUnderline(True)
        font_times_14 = QFont("Times New Roman", 14)
        font_times_12 = QFont("Times New Roman", 12)

        layout_main = QtWidgets.QVBoxLayout(self)

        label_list_widget_train_points_title = QtWidgets.QLabel()
        label_list_widget_train_points_title.setText("Training Points")
        label_list_widget_train_points_title.setFont(font_times_16_underline)

        self.list_widget_train_points = QtWidgets.QListWidget()
        self.list_widget_train_points.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_widget_train_points.setFont(font_times_12)
        for index, item in enumerate(np.column_stack((self.parent().data_x_train, self.parent().data_y_train))):
            self.list_widget_train_points.insertItem(index, np.array2string(item, separator=","))

        label_list_widget_test_points_title = QtWidgets.QLabel()
        label_list_widget_test_points_title.setText("Testing Points")
        label_list_widget_test_points_title.setFont(font_times_16_underline)

        self.list_widget_test_points = QtWidgets.QListWidget()
        self.list_widget_test_points.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_widget_test_points.setFont(font_times_12)
        for index, item in enumerate(np.column_stack((self.parent().data_x_test, self.parent().data_y_test))):
            self.list_widget_test_points.insertItem(index, np.array2string(item, separator=","))

        button_remove_point = QtWidgets.QPushButton()
        button_remove_point.setText("Remove Selected Points")
        button_remove_point.setFont(font_times_14)
        button_remove_point.clicked.connect(self.remove_point_on_click)

        layout_line_edit_x = QtWidgets.QHBoxLayout()

        label_line_edit_x = QtWidgets.QLabel()
        label_line_edit_x.setText("x:")
        label_line_edit_x.setFont(font_times_16)

        self.line_edit_x = QtWidgets.QLineEdit()
        self.line_edit_x.setValidator(QDoubleValidator())
        self.line_edit_x.setFont(font_times_16)

        layout_line_edit_x.addWidget(label_line_edit_x)
        layout_line_edit_x.addWidget(self.line_edit_x)
        
        layout_line_edit_y = QtWidgets.QHBoxLayout()

        label_line_edit_y = QtWidgets.QLabel()
        label_line_edit_y.setText("y:")
        label_line_edit_y.setFont(font_times_16)

        self.line_edit_y = QtWidgets.QLineEdit()
        self.line_edit_y.setValidator(QDoubleValidator())
        self.line_edit_y.setFont(font_times_16)

        layout_line_edit_y.addWidget(label_line_edit_y)
        layout_line_edit_y.addWidget(self.line_edit_y)

        button_add_train_point = QtWidgets.QPushButton()
        button_add_train_point.setText("Add Train Point")
        button_add_train_point.setFont(font_times_14)
        button_add_train_point.clicked.connect(self.add_train_point_on_click)

        button_add_test_point = QtWidgets.QPushButton()
        button_add_test_point.setText("Add Test Point")
        button_add_test_point.setFont(font_times_14)
        button_add_test_point.clicked.connect(self.add_test_point_on_click)

        button_add_ten_rand_points = QtWidgets.QPushButton()
        button_add_ten_rand_points.setText("Add 10 Random Points")
        button_add_ten_rand_points.setFont(font_times_14)
        button_add_ten_rand_points.clicked.connect(self.button_add_ten_rand_points_on_click)

        layout_line_edit_test_size = QtWidgets.QHBoxLayout()

        label_line_edit_test_size = QtWidgets.QLabel()
        label_line_edit_test_size.setText("Test Size:")
        label_line_edit_test_size.setFont(font_times_16)

        self.line_edit_test_size = QtWidgets.QLineEdit()
        self.line_edit_test_size.setText("0.2")
        line_edit_test_size_validator = QDoubleValidator()
        line_edit_test_size_validator.setBottom = 0
        line_edit_test_size_validator.setTop = 1
        self.line_edit_test_size.setValidator(QDoubleValidator())
        self.line_edit_test_size.setFont(font_times_16)
        self.line_edit_test_size.editingFinished.connect(self.on_finished_editing_line_edit_test_size)

        layout_line_edit_test_size.addWidget(label_line_edit_test_size)
        layout_line_edit_test_size.addWidget(self.line_edit_test_size)

        button_randomize_train_test = QtWidgets.QPushButton()
        button_randomize_train_test.setText("Randomize Train/Test")
        button_randomize_train_test.setFont(font_times_14)
        button_randomize_train_test.clicked.connect(self.button_randomize_train_test_on_click)

        layout_main.addWidget(label_list_widget_train_points_title)
        layout_main.addWidget(self.list_widget_train_points)
        layout_main.addWidget(label_list_widget_test_points_title)
        layout_main.addWidget(self.list_widget_test_points)
        layout_main.addWidget(button_remove_point)
        layout_main.addLayout(layout_line_edit_x)
        layout_main.addLayout(layout_line_edit_y)
        layout_main.addWidget(button_add_train_point)
        layout_main.addWidget(button_add_test_point)
        layout_main.addWidget(button_add_ten_rand_points)
        layout_main.addLayout(layout_line_edit_test_size)
        layout_main.addWidget(button_randomize_train_test)


    def update_list(self) -> None:
        self.list_widget_train_points.clear()
        for index, item in enumerate(np.column_stack((self.parent().data_x_train, self.parent().data_y_train))):
            self.list_widget_train_points.insertItem(index, np.array2string(item, separator=","))

        self.list_widget_test_points.clear()
        for index, item in enumerate(np.column_stack((self.parent().data_x_test, self.parent().data_y_test))):
            self.list_widget_test_points.insertItem(index, np.array2string(item, separator=","))

    def button_randomize_train_test_on_click(self) -> None:
        self.parent().randomize_test_train()

    def remove_point_on_click(self) -> None:
        indices_to_delete = []
        for item in self.list_widget_train_points.selectedIndexes():
            indices_to_delete.append(item.row())
        indices_to_delete.sort(reverse=True)
        for index in indices_to_delete:
            del self.parent().data_x_train[index]
            del self.parent().data_y_train[index]

        indices_to_delete = []
        for item in self.list_widget_test_points.selectedIndexes():
            indices_to_delete.append(item.row())
        indices_to_delete.sort(reverse=True)
        for index in indices_to_delete:
            del self.parent().data_x_test[index]
            del self.parent().data_y_test[index]

        self.parent().update_plots()
        self.parent().update_list()

    def add_train_point_on_click(self) -> None:
        self.parent().data_x_train.append(float(self.line_edit_x.text()))
        self.parent().data_y_train.append(float(self.line_edit_y.text()))

        self.parent().update_plots()
        self.parent().update_list()

    def add_test_point_on_click(self) -> None:
        self.parent().data_x_test.append(float(self.line_edit_x.text()))
        self.parent().data_y_test.append(float(self.line_edit_y.text()))

        self.parent().update_plots()
        self.parent().update_list()

    def on_finished_editing_line_edit_test_size(self) -> None:
        self.parent().test_size = float(self.line_edit_test_size.text())

    def button_add_ten_rand_points_on_click(self) -> None:
        for _ in itertools.repeat(None, 10 - round(10 * self.parent().test_size)):
            random_number = random.randint(1, 100)
            self.parent().data_x_train.append(random_number)
            self.parent().data_y_train.append(random_number + random.randint(-20, 20))

        for _ in itertools.repeat(None, round(10 * self.parent().test_size)):
            random_number = random.randint(1, 100)
            self.parent().data_x_test.append(random_number)
            self.parent().data_y_test.append(random_number + random.randint(-20, 20))
        self.parent().update_plots()
        self.parent().update_list()

    