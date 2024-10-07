
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QSizePolicy




class Plot(FigureCanvas):
    def __init__(self, fig, parent=None):
        self.fig = fig
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        pass


