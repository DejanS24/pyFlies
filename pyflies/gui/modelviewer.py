from PyQt5 import QtGui
from PyQt5.Qt import Qt, QObject, QGraphicsScene, QGraphicsView, QPixmap, QPainter


class ModelGraphScene(QGraphicsScene):

    def load_svg(self, svg_file):
        # item = QtSvg.QGraphicsSvgItem(svg_file)
        self.clear()
        item = QPixmap(svg_file)
        self.item = self.addPixmap(item)
        self.setSceneRect(self.item.boundingRect())


class ModelGraphView(QGraphicsView):
    """
    View widget for the experiment model.
    """
    ZOOM_IN_SCALE = 1.2589254

    def __init__(self, scene):
        super(ModelGraphView, self).__init__(scene)

        # SceneView has capability to track mouse events, enable it
        self.setMouseTracking(True)

        # Anchor under mouse
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        # Seting hints which enable antialiasing
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.TextAntialiasing)

    def wheelEvent(self, wheel_event):
        """
        Event handler for mouse wheel event over view enabling
        point zoom feature.
        """
        delta = wheel_event.delta()

        if delta > 0:
            self.scale(self.ZOOM_IN_SCALE, self.ZOOM_IN_SCALE)
        elif delta < 0:
            self.scale(1/self.ZOOM_IN_SCALE, 1/self.ZOOM_IN_SCALE)

    def fit_in_view(self):
        """
        Fit in view
        """
        self.centerOn(self.scene().item)
        self.fitInView(self.scene().item.boundingRect(), Qt.KeepAspectRatio)

