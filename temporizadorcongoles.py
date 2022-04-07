# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Temporizador")
  
        # setting geometry
        self.setGeometry(500, 100, 400, 600)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for widgets
    def UiComponents(self):
  
        # variables
        # count variable
        self.count = 0
        self.a_goals = 0
        self.b_goals = 0
  
        # start flag
        self.start = False
  
        # creating push button to get time in seconds
        time_button = QPushButton("Fijar tiempo", self)
        # setting geometry to the push button
        time_button.setGeometry(75, 100, 100, 50)
        # adding action to the button
        time_button.clicked.connect(self.get_seconds)

        clear_all_button = QPushButton("Todo a Cero", self)
        clear_all_button.setGeometry(200,100,100,50)
        clear_all_button.clicked.connect(self.clear_all)
  
        # creating label to show the seconds
        self.tlabel = QLabel("00:00", self)
        # setting geometry of label
        self.tlabel.setGeometry(40, 200, 320, 100)
        # setting border to the label
        self.tlabel.setStyleSheet("border : 3px solid black")  
        # setting font to the label
        self.tlabel.setFont(QFont('Times', 60))  
        # setting alignment ot the label
        self.tlabel.setAlignment(Qt.AlignCenter)
  
        # creating start button
        start_button = QPushButton("Empezar/Retomar", self)  
        # setting geometry to the button
        start_button.setGeometry(40, 350, 100, 40)  
        # adding action to the button
        start_button.clicked.connect(self.start_action)  

        # creating pause button
        pause_button = QPushButton("Pausar", self)  
        # setting geometry to the button
        pause_button.setGeometry(150, 350, 100, 40)  
        # adding action to the button
        pause_button.clicked.connect(self.pause_action)
  
        # creating reset  button
        reset_button = QPushButton("Reiniciar", self)  
        # setting geometry to the button
        reset_button.setGeometry(260, 350, 100, 40)  
        # adding action to the button
        reset_button.clicked.connect(self.reset_action)  

        ateam_button = QPushButton("Local",self)
        ateam_button.setGeometry(50,425,100,50)
        aplus_button = QPushButton("+",self)
        aplus_button.setGeometry(150,425,25,25)
        aplus_button.clicked.connect(lambda: self.mod_score('a',True))
        aminus_button = QPushButton("-",self)
        aminus_button.setGeometry(150,450,25,25)
        aminus_button.clicked.connect(lambda: self.mod_score('a',False))
        self.alabel = QLabel("0", self)
        self.alabel.setGeometry(170,425,100,50)
        self.alabel.setFont(QFont('Times', 30))  
        self.alabel.setAlignment(Qt.AlignCenter)
        
        bteam_button = QPushButton("Visitante",self)
        bteam_button.setGeometry(50,500,100,50)
        bplus_button = QPushButton("+",self)
        bplus_button.setGeometry(150,500,25,25)
        bplus_button.clicked.connect(lambda: self.mod_score("b",True))
        bminus_button = QPushButton("-",self)
        bminus_button.setGeometry(150,525,25,25)
        bminus_button.clicked.connect(lambda: self.mod_score("b",False))
        self.blabel = QLabel("0", self)
        self.blabel.setGeometry(170,500,100,50)
        self.blabel.setFont(QFont('Times', 30))  
        self.blabel.setAlignment(Qt.AlignCenter)
        
        
        # creating a timer object
        timer = QTimer(self)  
        # adding action to timer
        timer.timeout.connect(self.showTime)  
        # update the timer every tenth second
        timer.start(100)

        
    # method called by timer
    def showTime(self):
  
        # checking if flag is true
        if self.start:
            # incrementing the counter
            self.count -= 1
  
            # timer is completed
            if self.count == 0:
  
                # making flag false
                self.start = False
  
                # setting text to the label
                self.tlabel.setText("FIN")
  
        if self.start:
            # getting text from count
            secs,_ = divmod(self.count,10)
            mins, secs = divmod(secs, 60)
            tiempo = '{:02d}:{:02d}'.format(mins, secs)
            #text = str(self.count / 10) + " s"
  
            # showing text
            self.tlabel.setText(tiempo)
  
  
    # method called by the push button
    def get_seconds(self):
  
        # making flag false
        self.start = False  
        # getting seconds and flag
        second, done = QInputDialog.getInt(self, 'Minutos', 'Ingrese Minutos:')
        second = second * 60  
        # if flag is true
        if done:
            # changing the value of count
            self.count = second * 10  
            # setting text to the label
            secs,_ = divmod(self.count,10)
            mins, secs = divmod(secs, 60)
            tiempo = '{:02d}:{:02d}'.format(mins, secs)
            self.tlabel.setText(tiempo)

    def clear_all(self):
        self.a_goals = 0
        self.alabel.setNum(self.a_goals)
        self.b_goals = 0
        self.blabel.setNum(self.b_goals)
        self.reset_action()

    def mod_score(self,e,b): 
        if(e=='a'):
            if(b):
                self.a_goals += 1
            else:
                if(self.a_goals>0):
                    self.a_goals -= 1
            self.alabel.setNum(self.a_goals)
        if(e=='b'):
            if(b):
                self.b_goals += 1
            else:
                if(self.b_goals>0):
                    self.b_goals -= 1
            self.blabel.setNum(self.b_goals)


    def start_action(self):
        # making flag true
        self.start = True
  
        # count = 0
        if self.count == 0:
            self.start = False
  
    def pause_action(self):
  
        # making flag false
        self.start = False
  
    def reset_action(self):
  
        # making flag false
        self.start = False
  
        # setting count value to 0
        self.count = 0
  
        # setting label text
        self.tlabel.setText("00:00")
  
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())