from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont

from windowsimpleplots import WindowScatterplot, WindowHistogram1DFrequency, WindowHistogram2DFrequency
from windowregression import WindowLinearRidgeRegression, WindowLassoElasticnetRegression

class WindowMain(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Quick Graphing")

        font_times_16 = QFont("Times New Roman", 16)
        font_times_16_bold = QFont("Times New Roman", 16)
        font_times_16_bold.setBold(True)

        layout_main = QtWidgets.QVBoxLayout()

        label_main = QtWidgets.QLabel()
        label_main.setText("Quick Graphing")
        label_main.setFont(font_times_16_bold)

        button_scatterplot = QtWidgets.QPushButton()
        button_scatterplot.setText("Scatterplot")
        button_scatterplot.setFont(font_times_16)
        button_scatterplot.clicked.connect(self.on_click_button_scatterplot)

        button_frequency_1d_histogram = QtWidgets.QPushButton()
        button_frequency_1d_histogram.setText("Frequency 1D Histogram")
        button_frequency_1d_histogram.setFont(font_times_16)
        button_frequency_1d_histogram.clicked.connect(self.on_click_button_frequency_1d_histogram)

        button_frequency_2d_histogram = QtWidgets.QPushButton()
        button_frequency_2d_histogram.setText("Frequency 2D Histogram")
        button_frequency_2d_histogram.setFont(font_times_16)
        button_frequency_2d_histogram.clicked.connect(self.on_click_button_frequency_2d_histogram)

        button_regression_linear_ridge = QtWidgets.QPushButton()
        button_regression_linear_ridge.setText("Linear/Ridge Regression")
        button_regression_linear_ridge.setFont(font_times_16)
        button_regression_linear_ridge.clicked.connect(self.on_click_button_regression_linear_ridge)

        button_regression_lasso_elasticnet = QtWidgets.QPushButton()
        button_regression_lasso_elasticnet.setText("LASSO/ElasticNet Regression")
        button_regression_lasso_elasticnet.setFont(font_times_16)
        button_regression_lasso_elasticnet.clicked.connect(self.on_click_button_regression_lasso_elasticnet)

        layout_main.addWidget(label_main, 1)
        layout_main.addWidget(button_scatterplot, 1)
        layout_main.addWidget(button_frequency_1d_histogram, 1)
        layout_main.addWidget(button_frequency_2d_histogram, 1)
        layout_main.addWidget(button_regression_linear_ridge, 1)
        layout_main.addWidget(button_regression_lasso_elasticnet, 1)

        self.setLayout(layout_main)

    def on_click_button_scatterplot(self):
        self.window_scatterplot = WindowScatterplot()
        self.window_scatterplot.show()

    def on_click_button_frequency_1d_histogram(self):
        self.window_frequency_1d_histogram = WindowHistogram1DFrequency()
        self.window_frequency_1d_histogram.show()

    def on_click_button_frequency_2d_histogram(self):
        self.window_frequency_2d_histogram = WindowHistogram2DFrequency()
        self.window_frequency_2d_histogram.show()

    def on_click_button_regression_linear_ridge(self):
        self.window_linear_ridge_regression = WindowLinearRidgeRegression()
        self.window_linear_ridge_regression.show()

    def on_click_button_regression_lasso_elasticnet(self):
        self.window_lasso_elasticnet_regression = WindowLassoElasticnetRegression()
        self.window_lasso_elasticnet_regression.show()
