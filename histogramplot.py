from PyQt4.QtCore import *
from PyQt4.QtGui import *




class HistogramPlot(QGraphicsScene):
    """ HistogramPloth is a subclass of QPixmap and draws a length frequency histogram of fish by sex
    """
    def __init__(self, parent=None):
        super(HistogramPlot, self).__init__(parent)
        
        self.mLengthBars=[]
        self.fLengthBars=[]
        self.uLengthBars=[]

        # add frame
            
        self.addLine(QLineF(0, 0, 80, 0))
        self.addLine(QLineF(0, 1, 0, -20))
        self.scale=1.
        font=QFont('helvetica', 2, -1, False)
        # ticks
        for i in range(8):
            self.addLine(QLineF(i*10, 0, i*10, 1))
            t=self.addText(str(i*10), font)
            t.setPos(QPointF(i*10-6, 0))
            
    def rescale(self, scale):
        self.scale=scale
        for i in range(80):
            r=self.mLengthBars[i].rect()
            r.setHeight(r.height()*scale)
            self.mLengthBars[i].setRect(r)
            r=self.uLengthBars[i].rect()
            r.setHeight(r.height()*scale)
            self.uLengthBars[i].setRect(r)
            r=self.fLengthBars[i].rect()
            r.setHeight(r.height()*scale)
            self.fLengthBars[i].setRect(r)

        
        
    def clearPlot(self):
        for x in self.uLengthBars:
            self.removeItem(x)
        for x in self.fLengthBars:
            self.removeItem(x)
        for x in self.mLengthBars:
            self.removeItem(x)
            
        self.mLengthBars=[]
        self.fLengthBars=[]
        self.uLengthBars=[]
        linePen=QPen(Qt.black, 0)
        ubrush=QBrush(Qt.gray, Qt.SolidPattern)
        mbrush=QBrush(Qt.white, Qt.SolidPattern)
        fbrush=QBrush(Qt.black, Qt.SolidPattern)
        barsize=1
        for i in range(80):
            self.uLengthBars.append(self.addRect(QRectF(i, 0, barsize, 0), linePen, ubrush))
            self.fLengthBars.append(self.addRect(QRectF(i, 0, barsize,0), linePen, fbrush))
            self.mLengthBars.append(self.addRect(QRectF(i, 0, barsize,0), linePen, mbrush))
            
            
    def update(self, length, sex):
        """
        Called periodically by a timer to update the count.
        """
        
        if sex=='Male':
            r=self.mLengthBars[length].rect()
            r.setHeight(r.height()-self.scale)
            self.mLengthBars[length].setRect(r)
            r=self.fLengthBars[length].rect()
            r.setHeight(r.height()-self.scale)
            self.fLengthBars[length].setRect(r)
            r=self.uLengthBars[length].rect()
            r.setHeight(r.height()-self.scale)
            self.uLengthBars[length].setRect(r)
        elif sex=='Female':
            r=self.fLengthBars[length].rect()
            r.setHeight(r.height()-self.scale)
            self.fLengthBars[length].setRect(r)
            r=self.uLengthBars[length].rect()
            r.setHeight(r.height()-self.scale)
            self.uLengthBars[length].setRect(r)
        else:
            r=self.uLengthBars[length].rect()
            r.setHeight(r.height()-self.scale)
            self.uLengthBars[length].setRect(r)
        
        
        
