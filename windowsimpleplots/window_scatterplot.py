from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QDoubleValidator

import numpy as np

from matplotlibcanvases import SingleMplCanvas

class WindowScatterplot(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Quick Graphing - Scatterplot")

        self.data_x = []
        self.data_y = []

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

        label_plot_ylabel = QtWidgets.QLabel()
        label_plot_ylabel.setText("y-axis Label:")
        label_plot_ylabel.setFont(font_times_14)

        layout_plot_titles.addWidget(label_plot_title)
        layout_plot_titles.addWidget(label_plot_xlabel)
        layout_plot_titles.addWidget(label_plot_ylabel)

        layout_plot_values = QtWidgets.QVBoxLayout()

        self.line_edit_plot_title = QtWidgets.QLineEdit()
        self.line_edit_plot_title.setText("General Scatterplot")
        self.line_edit_plot_title.setFont(font_times_14)
        self.line_edit_plot_title.editingFinished.connect(self.on_finished_editing_line_edit_plot_title)

        self.line_edit_plot_xlabel = QtWidgets.QLineEdit()
        self.line_edit_plot_xlabel.setText("x-values")
        self.line_edit_plot_xlabel.setFont(font_times_14)
        self.line_edit_plot_xlabel.editingFinished.connect(self.on_finished_editing_line_edit_plot_xlabel)

        self.line_edit_plot_ylabel = QtWidgets.QLineEdit()
        self.line_edit_plot_ylabel.setText("y-values")
        self.line_edit_plot_ylabel.setFont(font_times_14)
        self.line_edit_plot_ylabel.editingFinished.connect(self.on_finished_editing_line_edit_plot_ylabel)

        layout_plot_values.addWidget(self.line_edit_plot_title)
        layout_plot_values.addWidget(self.line_edit_plot_xlabel)
        layout_plot_values.addWidget(self.line_edit_plot_ylabel)

        layout_top.addLayout(layout_plot_titles)
        layout_top.addLayout(layout_plot_values)

        layout_bottom = QtWidgets.QHBoxLayout()

        self.canvas_plot = SingleMplCanvas(self, width=5, height=5, dpi=100)

        layout_right_side_bar = QtWidgets.QVBoxLayout()

        label_points_title = QtWidgets.QLabel()
        label_points_title.setText("Points")
        label_points_title.setFont(font_times_16_underline)

        self.list_widget_points = QtWidgets.QListWidget()
        self.list_widget_points.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_widget_points.setFont(font_times_12)

        button_remove_point = QtWidgets.QPushButton()
        button_remove_point.setText("Remove Selected Points")
        button_remove_point.setFont(font_times_14)
        button_remove_point.clicked.connect(self.on_click_remove_point)

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

        button_add_point = QtWidgets.QPushButton()
        button_add_point.setText("Add Point")
        button_add_point.setFont(font_times_14)
        button_add_point.clicked.connect(self.on_click_button_add_point)

        layout_line_edit_y.addWidget(label_line_edit_y)
        layout_line_edit_y.addWidget(self.line_edit_y)

        layout_right_side_bar.addWidget(label_points_title)
        layout_right_side_bar.addWidget(self.list_widget_points)
        layout_right_side_bar.addWidget(button_remove_point)
        layout_right_side_bar.addLayout(layout_line_edit_x)
        layout_right_side_bar.addLayout(layout_line_edit_y)
        layout_right_side_bar.addWidget(button_add_point)

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
        self.canvas_plot.axes.set_ylabel(self.line_edit_plot_ylabel.text())

        self.canvas_plot.axes.scatter(self.data_x, self.data_y)
        
        self.canvas_plot.draw()
    
    def update_list(self) -> None:
        self.list_widget_points.clear()
        for index, item in enumerate(np.column_stack((self.data_x, self.data_y))):
            self.list_widget_points.insertItem(index, np.array2string(item, separator=","))

    def on_click_remove_point(self) -> None:
        indices_to_delete = []
        for item in self.list_widget_points.selectedIndexes():
            indices_to_delete.append(item.row())
        indices_to_delete.sort(reverse=True)
        for index in indices_to_delete:
            del self.data_x[index]
            del self.data_y[index]

        self.update_plots()
        self.update_list()

    def on_click_button_add_point(self) -> None:
        self.data_x.append(float(self.line_edit_x.text()))
        self.data_y.append(float(self.line_edit_y.text()))

        self.update_plots()
        self.update_list()

    def on_finished_editing_line_edit_plot_title(self) -> None:
        self.update_plots()

    def on_finished_editing_line_edit_plot_xlabel(self) -> None:
        self.update_plots()

    def on_finished_editing_line_edit_plot_ylabel(self) -> None:
        self.update_plots()