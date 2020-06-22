from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIntValidator
from untitled_python import Ui_MainWindow
import math

import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings


class untitled_python(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.action_About = 0
        self.action_Strata = 1
        self.action_Foundation = 2
        self.actionWater_Level = 3
        self.action_Show_Results = 4

        self.ui.action_About.triggered.connect(self.go_action_About)
        self.ui.action_New.triggered.connect(self.go_action_New)
        self.ui.action_Save.triggered.connect(self.go_action_Save)
        self.ui.action_Open.triggered.connect(self.go_action_Open)
        self.ui.action_Run.triggered.connect(self.go_action_Run)
        self.ui.action_Articles.triggered.connect(self.go_action_Articles)
        self.ui.action_Show_Results.triggered.connect(self.go_action_Show_Results)



        self.ui.action_Strata.triggered.connect(self.go_action_Strata)
        self.ui.action_Foundation.triggered.connect(self.go_action_Foundation)
        self.ui.actionWater_Level.triggered.connect(self.go_actionWater_Level)

        self.ui.action_Save.setEnabled(False)
        self.ui.action_Run.setEnabled(False)
        self.ui.action_Show_Results.setEnabled(False)

        self.go_action_About()

        self.ui.E_mail_label.setText(u'<p> E-Mail: <a href='"'mailto:anil_odabas@hotmail.com'"'>anil_odabas@hotmail.com</a>  </p>')
        self.ui.E_mail_label.setOpenExternalLinks(True)

        #LineEditlerden Veri tipi düzenlenmesi

        self.ui.lineEdit_weight.setValidator(QtGui.QDoubleValidator(0, 99, 2, notation = QtGui.QDoubleValidator.StandardNotation))
        self.ui.lineEdit_cohesion.setValidator(QtGui.QDoubleValidator(0, 99, 2, notation = QtGui.QDoubleValidator.StandardNotation))
        self.ui.lineEdit_angle.setValidator(QIntValidator(0, 99, self))

        self.ui.lineEdit_foundation_depth.setValidator(QtGui.QDoubleValidator(0, 99, 2, notation = QtGui.QDoubleValidator.StandardNotation))
        self.ui.lineEdit_foundation_length.setValidator(QtGui.QDoubleValidator(0, 999, 2, notation = QtGui.QDoubleValidator.StandardNotation))
        self.ui.lineEdit_foundation_width.setValidator(QtGui.QDoubleValidator(0, 999, 2, notation = QtGui.QDoubleValidator.StandardNotation))

        self.ui.lineEdit_Design.setValidator(QtGui.QDoubleValidator(0, 99, 2, notation = QtGui.QDoubleValidator.StandardNotation))
        self.ui.lineEdit_FoS.setValidator(QtGui.QDoubleValidator(0, 9, 1, notation = QtGui.QDoubleValidator.StandardNotation))
        self.ui.lineEdit_Ultimate.setValidator(QtGui.QDoubleValidator(0, 99, 2, notation = QtGui.QDoubleValidator.StandardNotation))

        #LineEditlerden Signal Alınması
        self.ui.lineEdit_weight.editingFinished.connect(self.weight_process)
        self.ui.lineEdit_cohesion.editingFinished.connect(self.cohesion_process)
        self.ui.lineEdit_angle.editingFinished.connect(self.angle_process)
        self.ui.lineEdit_foundation_depth.editingFinished.connect(self.foundation_depth_process)
        self.ui.lineEdit_foundation_length.editingFinished.connect(self.foundation_length_process)
        self.ui.lineEdit_foundation_width.editingFinished.connect(self.foundation_width_process)
        self.ui.lineEdit_FoS.editingFinished.connect(self.Fos_process)

        #RadioButtonlardan Signal Alınması

        self.ui.radioButton_1.toggled.connect(self.toogleRadio_1)
        self.ui.radioButton_2.toggled.connect(self.toggleRadio_2)
        self.ui.radioButton_3.toggled.connect(self.toggleRadio_3)
        self.ui.radioButton_4.toggled.connect(self.toggleRadio_4)

        self.ui.radioButton_1.setChecked(True)

    def toogleRadio_1(self):
        rdButon = self.sender()

        if rdButon.isChecked():
            self.BHA1 = 1
            self.BHA2 = 1
            #print(self.BHA1,self.BHA2)
        else :
            pass

    def toggleRadio_2(self):
        rdButon=self.sender()

        if rdButon.isChecked():
            self.BHA1 = 2
            self.BHA2 = 2
            #print(self.BHA1,self.BHA2)
        else :
            pass
    def toggleRadio_3(self):
        rdButon=self.sender()

        if rdButon.isChecked():
            self.BHA1 = 3
            self.BHA2 = 3
            #print(self.BHA1,self.BHA2)
        else :
            pass
    def toggleRadio_4(self):
        rdButon=self.sender()

        if rdButon.isChecked():
            self.BHA1 = 4
            self.BHA2 = 4
            #print(self.BHA1,self.BHA2)
        else :
            pass

    def weight_process(self):
        self.weight = float(self.ui.lineEdit_weight.text())
        #print(self.weight)
    def cohesion_process(self):
        self.cohesion = float(self.ui.lineEdit_cohesion.text())
        #print(self.cohesion)
    def angle_process(self):
        self.angle = float(self.ui.lineEdit_angle.text())
        print(self.angle)
    def foundation_depth_process(self):
        self.foundation_depth = float(self.ui.lineEdit_foundation_depth.text())
        #print(self.foundation_depth)
    def foundation_length_process(self):
        self.foundation_length = float(self.ui.lineEdit_foundation_length.text())
        #print(self.foundation_length)
    def foundation_width_process(self):
        self.foundation_width = float(self.ui.lineEdit_foundation_width.text())
        #print(self.foundation_width)
    def Fos_process(self):
        self.FoS = float(self.ui.lineEdit_FoS.text())
        self.Qd = self.Qu / self.FoS
        self.Qd = round(self.Qd,2)
        self.ui.lineEdit_Design.setText(str(self.Qd))

    def go_action_About(self):
        self.ui.stackedWidget.setCurrentIndex(self.action_About)

    def go_action_New(self):
        self.ui.toolBar.setEnabled(True)
        self.ui.action_Save.setEnabled(True)
        self.ui.action_Run.setEnabled(True)

    def go_action_Show_Results(self):
        self.ui.lineEdit_FoS.setText("3")
        self.FoS = float(self.ui.lineEdit_FoS.text())

        self.ui.stackedWidget.setCurrentIndex(self.action_Show_Results)
        self.ui.lineEdit_Ultimate.setText(str(self.Qu))
        self.ui.lineEdit_Ultimate.setReadOnly(True)
        self.Qd = self.Qu / self.FoS
        self.Qd = round(self.Qd,2)
        self.ui.lineEdit_Design.setText(str(self.Qd))
        self.ui.lineEdit_Design.setReadOnly(True)

    def go_action_Save(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save File","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            file = open(fileName, 'w')

            text = [self.ui.lineEdit_weight.text(),self.ui.lineEdit_cohesion.text(),self.ui.lineEdit_angle.text(),self.ui.lineEdit_foundation_depth.text(),
                    self.ui.lineEdit_foundation_length.text(),self.ui.lineEdit_foundation_width.text(),self.BHA1,self.BHA2]
            for i in text:
                file.write('%s\n' %i)

            file.close()


    def go_action_Open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open File", "","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            text = []
            file = open(fileName, 'r')
            for i in file:
                currentPlace = i[:-1]
                text.append(currentPlace)

            self.ui.lineEdit_weight.setText(text[0])
            self.ui.lineEdit_cohesion.setText(text[1])
            self.ui.lineEdit_angle.setText(text[2])
            self.ui.lineEdit_foundation_depth.setText(text[3])
            self.ui.lineEdit_foundation_length.setText(text[4])
            self.ui.lineEdit_foundation_width.setText(text[5])


            if self.BHA1 and self.BHA2 == 1:
                self.ui.radioButton_1.setChecked(True)
            else :
                pass

            if self.BHA1 and self.BHA2 == 2:
                self.ui.radioButton_2.setChecked(True)
            else :
                pass

            if self.BHA1 and self.BHA2 == 3:
                self.ui.radioButton_3.setChecked(True)
            else :
                pass

            if self.BHA1 and self.BHA2 == 4:
                self.ui.radioButton_4.setChecked(True)
            else :
                pass
        self.ui.toolBar.setEnabled(True)
        self.ui.action_Save.setEnabled(True)
        self.ui.action_Run.setEnabled(True)
        file.close()


    def parameter_control(self):

        if  self.ui.lineEdit_weight.text() == "" or self.ui.lineEdit_weight.text() == "0":
            message_box = QMessageBox.warning(self, "Warning" , "<b>Unit Weight</b> value is not valid..." )
        else:
            pass

        if  self.ui.lineEdit_cohesion.text() == "" :
            message_box = QMessageBox.warning(self, "Warning" , "<b>Cohesion of Soil</b> value is not valid..." )
        else:
            pass

        if  self.ui.lineEdit_angle.text() == "" :
            message_box = QMessageBox.warning(self, "Warning" , "<b>Angle of Friction</b> value is not valid..." )
        else:
            pass

        if self.ui.lineEdit_foundation_width == "" or self.ui.lineEdit_foundation_width == "0":
            message_box = QMessageBox.warning(self, "Warning" , "<b>Foundation Width</b> value is not valid..." )
        else:
            pass

        if self.ui.lineEdit_foundation_length == "" or self.ui.lineEdit_foundation_length == "0":
            message_box = QMessageBox.warning(self, "Warning" , "<b>Foundation Length</b> value is not valid..." )
        else:
            pass

        if self.ui.lineEdit_foundation_depth == "" :
            message_box = QMessageBox.warning(self, "Warning" , "<b>Foundation Depth</b> value is valid..." )
        else:
            pass


    def calculation(self):

        B = self.foundation_width
        L = self.foundation_length
        Df = self.foundation_depth
        c = self.cohesion

        if self.angle == 0:
            aci = 0.0000001
        else:
            aci = self.angle


        #Taşıma Gücü Faktörleri

        Nq = (math.e**(math.pi*math.tan(math.radians(aci))))*((math.tan(math.radians(45+aci/2)))**2)
        Nc = (Nq-1)*(math.tan(math.radians(aci))**-1)
        Ng = (Nq-1)*(math.tan(math.radians((1.4*aci))))

        print(Nq,Nc,Ng)


        #Şekil Faktörleri

        sc = 1 + 0.2 * (B/L) * ((math.tan(math.radians(45+aci/2)))**2)
        if aci == 0.0000001:
            sq = 1
            sg = 1
        else:
            sq = 1 + (0.1* (B/L) * ((math.tan(math.radians(45+aci/2)))**2))
            sg = 1 + (0.1* (B/L) * ((math.tan(math.radians(45+aci/2)))**2))


        print(sc,sg,sq)

        #Derinlik Faktörleri

        dc = 1 + 0.2 * (Df/B) * ((math.tan(math.radians(45+aci/2))))
        if aci == 0.0000001:
         dq = 1
         dg = 1
        else:
            dq = 1 + (0.1* (Df/B) * ((math.tan(math.radians(45+aci/2)))))
            dg = 1 + (0.1* (Df/B) * ((math.tan(math.radians(45+aci/2)))))

        print(dc,dg,dq)

        #Su Seviyesi Kontrol Birim Hacım Ağırlık Seçimi

        if self.BHA1 and self.BHA2 == 1:
            self.BHA1 = self.weight - 9.81
            self.BHA2 = self.weight - 9.81
            print(self.BHA1,self.BHA2)
        else :
            pass

        if self.BHA1 and self.BHA2 == 2:
            self.BHA1 = self.weight*(self.foundation_depth/2) + (self.weight-9.81) * (self.foundation_depth/2)
            self.BHA2 = self.weight - 9.81
            print(self.BHA1,self.BHA2)
        else :
            pass

        if self.BHA1 and self.BHA2 == 3:
            self.BHA1 = self.weight
            self.BHA2 = self.weight * (self.foundation_width/2) + (self.weight-9.81) * (self.foundation_width/2)
            print(self.BHA1,self.BHA2)
        else :
            pass

        if self.BHA1 and self.BHA2 == 4:
            self.BHA1 = self.weight
            self.BHA2 = self.weight
            print(self.BHA1,self.BHA2)
        else :
            pass


        self.Qu = self.cohesion*Nc*sc*dc + self.BHA1*Df*Nq*sq*dq + 0.5 * self.BHA2*B*Ng*sg*dg
        self.Qu = round(self.Qu,2)
        print(self.Qu)
        self.ui.action_Show_Results.setEnabled(True)


    def go_action_Run(self):

        self.parameter_control()
        self.calculation()


    def go_action_Articles(self):
        import webbrowser
        webbrowser.open_new("https://drive.google.com/file/d/1YBKb5NLmHtpYxsfirKr3aLoCxOjZRLkR/view?usp=sharing")


    def go_action_Strata(self):
        self.ui.stackedWidget.setCurrentIndex(self.action_Strata)

    def go_action_Foundation(self):
        self.ui.stackedWidget.setCurrentIndex(self.action_Foundation)

    def go_actionWater_Level(self):
        self.ui.stackedWidget.setCurrentIndex(self.actionWater_Level)



app = QApplication([])
win = untitled_python()
win.show()
app.exec_()