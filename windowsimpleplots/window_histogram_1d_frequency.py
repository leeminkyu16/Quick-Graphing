from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QDoubleValidator

import numpy as np

from matplotlibcanvases import SingleMplCanvas

class WindowHistogram1DFrequency(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Quick Graphing - 1D Frequency Histogram")

        self.data_values = []

        font_times_12 = QFont("Times New Roman", 12)
        font_times_14 = QFont("Times New Roman", 14)
        font_times_16 = QFont("Times New Roman", 16)
        font_times_16_underline = QFont("Times New Roman", 16)
        font_times_16_underline.setUnderline(True)

        layout_main = QtWidgets.QVBoxLayout(self)

        layout_top = QtWidgets.QHBoxLayout()

        layout_plot_titles = QtWidgets.QVBoxLayout()

        label_plot_title = QtWidgets.QLabel()
        label_plot_title.setText("Title:")
        label_plot_title.setFont(font_times_14)

        label_plot_xlabel = QtWidgets.QLabel()
        label_plot_xlabel.setText("x-axis Label:")
        label_plot_xlabel.setFont(font_times_14)

        layout_plot_titles.addWidget(label_plot_title)
        layout_plot_titles.addWidget(label_plot_xlabel)

        layout_plot_values = QtWidgets.QVBoxLayout()

        self.line_edit_plot_title = QtWidgets.QLineEdit()
        self.line_edit_plot_title.setText("General Histogram")
        self.line_edit_plot_title.setFont(font_times_14)
        self.line_edit_plot_title.editingFinished.connect(self.on_finished_editing_line_edit_plot_title)

        self.line_edit_plot_xlabel = QtWidgets.QLineEdit()
        self.line_edit_plot_xlabel.setText("x-values")
        self.line_edit_plot_xlabel.setFont(font_times_14)
        self.line_edit_plot_xlabel.editingFinished.connect(self.on_finished_editing_line_edit_plot_xlabel)

        layout_plot_values.addWidget(self.line_edit_plot_title)
        layout_plot_values.addWidget(self.line_edit_plot_xlabel)

        layout_top.addLayout(layout_plot_titles)
        layout_top.addLayout(layout_plot_values)

        layout_bottom = QtWidgets.QHBoxLayout()

        self.canvas_plot = SingleMplCanvas(self, width=5, height=5, dpi=100)

        layout_right_side_bar = QtWidgets.QVBoxLayout()

        label_values_title = QtWidgets.QLabel()
        label_values_title.setText("Points")
        label_values_title.setFont(font_times_16_underline)

        self.list_widget_values = QtWidgets.QListWidget()
        self.list_widget_values.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_widget_values.setFont(font_times_12)

        button_remove_value = QtWidgets.QPushButton()
        button_remove_value.setText("Remove Selected Values")
        button_remove_value.setFont(font_times_14)
        button_remove_value.clicked.connect(self.on_click_remove_value)

        layout_line_edit_value = QtWidgets.QHBoxLayout()

        label_line_edit_value = QtWidgets.QLabel()
        label_line_edit_value.setText("Value:")
        label_line_edit_value.setFont(font_times_16)

        self.line_edit_value = QtWidgets.QLineEdit()
        self.line_edit_value.setValidator(QDoubleValidator())
        self.line_edit_value.setFont(font_times_16)

        layout_line_edit_value.addWidget(label_line_edit_value)
        layout_line_edit_value.addWidget(self.line_edit_value)

        button_add_value = QtWidgets.QPushButton()
        button_add_value.setText("Add Value")
        button_add_value.setFont(font_times_14)
        button_add_value.clicked.connect(self.on_click_button_add_value)

        layout_right_side_bar.addWidget(label_values_title)
        layout_right_side_bar.addWidget(self.list_widget_values)
        layout_right_side_bar.addWidget(button_remove_value)
        layout_right_side_bar.addLayout(layout_line_edit_value)
        layout_right_side_bar.addWidget(button_add_value)

        layout_bottom.addWidget(self.canvas_plot, 5)
        layout_bottom.addLayout(layout_right_side_bar, 1)

        layout_main.addLayout(layout_top, 1)
        layout_main.addLayout(layout_bottom, 5)

        self.update_plots()
        self.update_list()

    def update_plots(self) -> None:
        self.canvas_plot.axes.clear()

        self.canvas_plot.axes.set_title(self.line_edit_plot_title.text())
        self.canvas_plot.axes.set_xlabel(self.line_edit_plot_xlabel.text())
        self.canvas_plot.axes.set_ylabel("Frequency")

        self.canvas_plot.axes.hist(self.data_values)

        self.canvas_plot.draw()

    def update_list(self) -> None:
        self.list_widget_values.clear()
        for index, item in enumerate(self.data_values):
            self.list_widget_values.insertItem(index, str(item))

    def on_click_remove_value(self) -> None:
        indices_to_delete = []
        for item in self.list_widget_values.selectedIndexes():
            indices_to_delete.append(item.row())
        indices_to_delete.sort(reverse=True)
        for index in indices_to_delete:
            del self.data_values[index]

        self.update_plots()
        self.update_list()

    def on_click_button_add_value(self) -> None:
        self.data_values.append(float(self.line_edit_value.text()))

        self.update_plots()
        self.update_list()

    def on_finished_editing_line_edit_plot_title(self) -> None:
        self.update_plots()

    def on_finished_editing_line_edit_plot_xlabel(self) -> None:
        self.update_plots()