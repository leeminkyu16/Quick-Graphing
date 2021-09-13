from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QDoubleValidator

from sklearn import linear_model, metrics
from matplotlibcanvases import SingleMplCanvas

class WidgetElasticNetRegression(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        standard_font = QFont("Times New Roman", 12)

        layout_main = QtWidgets.QHBoxLayout(self)

        self.canvas_plot = SingleMplCanvas(self, width=5, height=5, dpi=100)

        layout_right_side_bar = QtWidgets.QVBoxLayout()

        label_complexity_parameter_title = QtWidgets.QLabel()
        label_complexity_parameter_title.setText("Complexity Parameter:")
        label_complexity_parameter_title.setFont(standard_font)

        self.line_edit_complexity_paramater_value = QtWidgets.QLineEdit()
        self.line_edit_complexity_paramater_value.setText("0.1")
        line_edit_complexity_paramater_value_validator = QDoubleValidator()
        line_edit_complexity_paramater_value_validator.setBottom(0)
        self.line_edit_complexity_paramater_value.setValidator(line_edit_complexity_paramater_value_validator)
        self.line_edit_complexity_paramater_value.setFont(standard_font)
        self.line_edit_complexity_paramater_value.editingFinished.connect(self.on_editing_finished_complexity_paramater_value)

        label_mixing_parameter_title = QtWidgets.QLabel()
        label_mixing_parameter_title.setText("Mixing Parameter:")
        label_mixing_parameter_title.setFont(standard_font)

        self.line_edit_mixing_paramater_value = QtWidgets.QLineEdit()
        self.line_edit_mixing_paramater_value.setText("0.5")
        line_edit_mixing_paramater_value_validator = QDoubleValidator()
        line_edit_mixing_paramater_value_validator.setBottom(0)
        line_edit_mixing_paramater_value_validator.setTop(1)
        self.line_edit_mixing_paramater_value.setValidator(line_edit_mixing_paramater_value_validator)
        self.line_edit_mixing_paramater_value.setFont(standard_font)
        self.line_edit_mixing_paramater_value.editingFinished.connect(self.on_editing_finished_mixing_paramater_value)

        label_mean_squared_error_title = QtWidgets.QLabel()
        label_mean_squared_error_title.setText("Mean Squared Error:")
        label_mean_squared_error_title.setFont(standard_font)

        self.label_mean_squared_error_value = QtWidgets.QLabel()
        self.label_mean_squared_error_value.setFont(standard_font)
        self.label_mean_squared_error_value.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)

        label_coefficient_of_determination_title = QtWidgets.QLabel()
        label_coefficient_of_determination_title.setText("Coefficient of Determination:")
        label_coefficient_of_determination_title.setFont(standard_font)

        self.label_coefficient_of_determination_value = QtWidgets.QLabel()
        self.label_coefficient_of_determination_value.setFont(standard_font)
        self.label_coefficient_of_determination_value.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)

        label_intercept_title = QtWidgets.QLabel()
        label_intercept_title.setText("Intercept:")
        label_intercept_title.setFont(standard_font)

        self.label_intercept_value = QtWidgets.QLabel()
        self.label_intercept_value.setFont(standard_font)
        self.label_intercept_value.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)

        label_coefficient_title = QtWidgets.QLabel()
        label_coefficient_title.setText("Coefficient:")
        label_coefficient_title.setFont(standard_font)

        self.label_coefficient_value = QtWidgets.QLabel()
        self.label_coefficient_value.setFont(standard_font)
        self.label_coefficient_value.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)

        layout_right_side_bar.addWidget(label_complexity_parameter_title)
        layout_right_side_bar.addWidget(self.line_edit_complexity_paramater_value)
        layout_right_side_bar.addWidget(label_mixing_parameter_title)
        layout_right_side_bar.addWidget(self.line_edit_mixing_paramater_value)
        layout_right_side_bar.addWidget(label_mean_squared_error_title)
        layout_right_side_bar.addWidget(self.label_mean_squared_error_value)
        layout_right_side_bar.addWidget(label_coefficient_of_determination_title)
        layout_right_side_bar.addWidget(self.label_coefficient_of_determination_value)
        layout_right_side_bar.addWidget(label_intercept_title)
        layout_right_side_bar.addWidget(self.label_intercept_value)
        layout_right_side_bar.addWidget(label_coefficient_title)
        layout_right_side_bar.addWidget(self.label_coefficient_value)

        layout_main.addWidget(self.canvas_plot, 5)
        layout_main.addLayout(layout_right_side_bar, 1)

        self.update_plot()

    def update_plot(self) -> None:
        self.canvas_plot.axes.clear()

        self.canvas_plot.axes.set_title("Elastic-Net Regression")
        self.canvas_plot.axes.set_xlabel("x-values")
        self.canvas_plot.axes.set_ylabel("y-values")

        value_complexity_parameter = float(self.line_edit_complexity_paramater_value.text())
        value_mixing_parameter = float(self.line_edit_mixing_paramater_value.text())

        if (self.parent().np_data_x_train.size > 1 and self.parent().np_data_y_train.size > 1
            and self.parent().np_data_x_test.size > 1 and self.parent().np_data_y_test.size > 1):
            elasticnet_regression_model = linear_model.ElasticNet(alpha=value_complexity_parameter, l1_ratio=value_mixing_parameter)
            elasticnet_regression_model.fit(self.parent().np_data_x_train, self.parent().np_data_y_train)

            data_y_pred = elasticnet_regression_model.predict(self.parent().np_data_x_test)

            value_mean_squared_error = metrics.mean_squared_error(self.parent().np_data_y_test, data_y_pred)
            value_coefficient_of_determination = metrics.r2_score(self.parent().np_data_y_test, data_y_pred)

            train_plot_scatter = self.canvas_plot.axes.scatter(self.parent().np_data_x_train, self.parent().np_data_y_train, label="Train")
            test_plot_scatter = self.canvas_plot.axes.scatter(self.parent().np_data_x_test, self.parent().np_data_y_test, label="Test")
            self.canvas_plot.axes.plot(self.parent().np_data_x_test, data_y_pred)
            self.canvas_plot.axes.legend(handles=[train_plot_scatter, test_plot_scatter])

            self.label_mean_squared_error_value.setText(str(value_mean_squared_error))
            self.label_coefficient_of_determination_value.setText(str(value_coefficient_of_determination))
            self.label_intercept_value.setText(str(elasticnet_regression_model.intercept_[0]))
            self.label_coefficient_value.setText(str(elasticnet_regression_model.coef_[0]))
        elif(self.parent().np_data_x_train.size > 0 and self.parent().np_data_y_train.size > 0
            and self.parent().np_data_x_test.size > 0 and self.parent().np_data_y_test.size > 0):
            elasticnet_regression_model = linear_model.ElasticNet(alpha=value_complexity_parameter, l1_ratio=value_mixing_parameter)
            elasticnet_regression_model.fit(self.parent().np_data_x_train, self.parent().np_data_y_train)
            
            data_y_pred = elasticnet_regression_model.predict(self.parent().np_data_x_test)

            train_plot_scatter = self.canvas_plot.axes.scatter(self.parent().np_data_x_train, self.parent().np_data_y_train, label="Train")
            test_plot_scatter = self.canvas_plot.axes.scatter(self.parent().np_data_x_test, self.parent().np_data_y_test, label="Test")
            self.canvas_plot.axes.plot(self.parent().np_data_x_test, data_y_pred)
            self.canvas_plot.axes.legend(handles=[train_plot_scatter, test_plot_scatter])

            self.label_coefficient_of_determination_value.setText("N/A")
            self.label_intercept_value.setText(str(elasticnet_regression_model.intercept_[0]))
            self.label_coefficient_value.setText(str(elasticnet_regression_model.coef_[0]))
        else:
            self.label_coefficient_of_determination_value.setText("N/A")
            self.label_intercept_value.setText("N/A")
            self.label_coefficient_value.setText("N/A")

        self.canvas_plot.draw()
    def on_editing_finished_complexity_paramater_value(self) -> None:
        self.update_plot()

    def on_editing_finished_mixing_paramater_value(self) -> None:
        self.update_plot()