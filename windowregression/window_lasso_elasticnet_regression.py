from PyQt5 import QtCore, QtWidgets
from sklearn.model_selection import train_test_split

from .widget_lasso_regression import WidgetLassoRegression
from .widget_elasticnet_regression import WidgetElasticNetRegression
from .widget_right_side_bar import WidgetRightSideBar

import numpy as np
import random

class WindowLassoElasticnetRegression(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Quick Graphing - Linear/Ridge Regression")

        main_layout = QtWidgets.QHBoxLayout()

        grid_layout = QtWidgets.QGridLayout()

        self.data_x_train = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
        self.data_x_test = [5, 25, 45, 65, 85]
        self.data_y_train = [1, 20, 30, 49, 64, 65, 68, 75, 82, 95]
        self.data_y_test = [5, 25, 45, 65, 85]

        self.test_size = 0.2
        
        self.np_data_x_train = np.array(self.data_x_train)[:, np.newaxis]
        self.np_data_x_test = np.array(self.data_x_test)[:, np.newaxis]
        self.np_data_y_train = np.array(self.data_y_train)[:, np.newaxis]
        self.np_data_y_test = np.array(self.data_y_test)[:, np.newaxis]

        self.widget_linear_regression = WidgetLassoRegression(self)
        self.widget_ridge_regression = WidgetElasticNetRegression(self)

        self.widget_right_side = WidgetRightSideBar(self)

        grid_layout.addWidget(self.widget_linear_regression, 0, 0, 1, 1)
        grid_layout.addWidget(self.widget_ridge_regression, 1, 0, 1, 1)

        main_layout.addLayout(grid_layout, 5)
        main_layout.addWidget(self.widget_right_side, 1)

        self.setLayout(main_layout)

    def update_plots(self) -> None:
        self.np_data_x_train = np.array(self.data_x_train)[:, np.newaxis]
        self.np_data_x_test = np.array(self.data_x_test)[:, np.newaxis]
        self.np_data_y_train = np.array(self.data_y_train)[:, np.newaxis]
        self.np_data_y_test = np.array(self.data_y_test)[:, np.newaxis]

        self.widget_linear_regression.update_plot()
        self.widget_ridge_regression.update_plot()
        
    def update_list(self) -> None:
        self.widget_right_side.update_list()

    def randomize_test_train(self) -> None:
        self.data_x_train, self.data_x_test, self.data_y_train, self.data_y_test = train_test_split(
            self.data_x_train + self.data_x_test,
            self.data_y_train + self.data_y_test,
            test_size=self.test_size,
            random_state=random.randint(1, 100)
        )
        self.update_plots()
        self.update_list()