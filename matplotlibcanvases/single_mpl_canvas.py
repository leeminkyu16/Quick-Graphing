from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class SingleMplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100) -> None:
        fig = Figure(figsize = (width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(figure=fig)