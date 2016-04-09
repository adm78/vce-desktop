import sys, os
from PyQt4 import QtGui, QtCore, QtSvg

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 905, 900)
        self.setWindowTitle("Visual Chemical Engineering")
        self.setWindowIcon(QtGui.QIcon('bitmap/vcelogo.png'))

        extractAction = QtGui.QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Exit the Application')
        extractAction.triggered.connect(self.close_application)

        openEditor = QtGui.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip("Open Editor")
        openEditor.triggered.connect(self.editor)

        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QtGui.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)

        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(openEditor)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        solverMenu = mainMenu.addMenu("&Solver")

        mainMenu.setNativeMenuBar(False)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.move(300,840)

        reactorAction = QtGui.QAction(QtGui.QIcon('bitmap/reactor.png'), 'reactor mode', self)
        reactorAction.triggered.connect(self.showReactor)

        distillationAction = QtGui.QAction(QtGui.QIcon('bitmap/distillation.png'), 'distillation mode', self)
        distillationAction.triggered.connect(self.showDistillation)

        self.toolBar = self.addToolBar("Mode Selector")
        self.toolBar.addAction(reactorAction)
        self.toolBar.addAction(distillationAction)
        self.toolBar.setIconSize(QtCore.QSize(50,50))

        checkBox = QtGui.QCheckBox('Enlarge Window', self)
        checkBox.move(130, 50)
        checkBox.resize(checkBox.minimumSizeHint())
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 810, 500, 20)

        self.btn = QtGui.QPushButton("Solve",self)
        self.btn.move(200,840)
        self.btn.clicked.connect(self.download)

        self.Tdial = QtGui.QDial(self)
        self.Tdial.move(700,800)
        self.Tdial.resize(QtCore.QSize(50,50))

        self.Pdial = QtGui.QDial(self)
        self.Pdial.move(750,800)
        self.Pdial.resize(QtCore.QSize(50,50))

        self.Qdial = QtGui.QDial(self)
        self.Qdial.move(800,800)
        self.Qdial.resize(QtCore.QSize(50,50))

        _fromUtf8 = QtCore.QString.fromUtf8

        # temporarily removing the main png to test svg imports
        # pic = QtGui.QLabel(self)
        # pic.setGeometry(200, 100, 1000, 700)
        # pixmap_tmp = QtGui.QPixmap(os.getcwd() + "/bitmap/reactor_mod.png")
        # pixmap = pixmap_tmp.scaled(pic.size(), QtCore.Qt.KeepAspectRatio)
        # pic.setPixmap(pixmap)

        # testing svg imports
        self.svgWidget = QtSvg.QSvgWidget(os.getcwd() + '/vector/distillation_base.svg', self)
        self.svgWidget.setGeometry(200, 100, 700, 700)
        self.svgWidget.show()

        self.doubleSpinBox = QtGui.QDoubleSpinBox(self)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.doubleSpinBox.move(730,855)

        self.mdiArea = QtGui.QMdiArea(self)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.mdiArea.setGeometry(5,100,190,700)
        #self.mdiArea.move(10,100)
        sub = QtGui.QMdiSubWindow()
        sub.setWidget(QtGui.QTextEdit())
        sub.setWindowTitle("subwindow 1")
        sub.setGeometry(0,0,190,700)
        self.mdiArea.addSubWindow(sub)
        sub.show()


        self.show()

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)


    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def showReactor(self):
        self.svgWidget = QtSvg.QSvgWidget(os.getcwd() + '/vector/reactor_mod.svg', self)
        self.svgWidget.setGeometry(200, 100, 700, 700)
        self.svgWidget.show()

    def showDistillation(self):
        self.svgWidget = QtSvg.QSvgWidget(os.getcwd() + '/vector/distillation_base.svg', self)
        self.svgWidget.setGeometry(200, 100, 700, 700)
        self.svgWidget.show()


    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50, 1800, 1200)
        else:
            self.setGeometry(50, 50, 905, 900)



    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Exit Application",
                                            "Are you sure you wish to exit the application?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("good bye")
            sys.exit()
        else:
            pass




def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
