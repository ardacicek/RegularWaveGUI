from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow
from regularWave import Wave
from time import sleep

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow() #self.ui'ı main window classına bağladık
        self.ui.setupUi(self) #ui elemanına main window içindeki elemanları bağladık

        self.ui.btn_calculate.clicked.connect(self.calculate) #burada butonlara tıklandığında çalıştıralacak fonksiyonları bağlıyoruz. her buton için bir satır.


    def calculate(self):

        H0 = float(self.ui.txt_H0.text())
        T = float(self.ui.txt_T.text())
        h = float(self.ui.txt_h.text())
        alpha0 = float(self.ui.txt_dwApproach.text())

        wave = Wave(H0, T, h, alpha0)
        
        self.ui.lbl_resultL.setText('%.2f'%wave.waveLength())
        self.ui.progressBar.setProperty("value", 16.7)
        sleep(0.1)

        self.ui.lbl_resultCg.setText('%.2f'%wave.groupVelocity())
        self.ui.progressBar.setProperty("value", 33.3)
        sleep(0.1)

        self.ui.lbl_resultApproach.setText('%.2f'%wave.approachAngle())
        self.ui.progressBar.setProperty("value", 50.0)
        sleep(0.1)

        self.ui.lbl_resultShoaling.setText('%.2f'%wave.shoalingCoefficient())
        self.ui.progressBar.setProperty("value", 66.8)
        sleep(0.1)

        self.ui.lbl_resultRefraction.setText('%.2f'%wave.refractionCoefficient())
        self.ui.progressBar.setProperty("value", 83.5)
        sleep(0.1)

        self.ui.lbl_resultHeight.setText('%.2f'%wave.waveHeight())
        self.ui.progressBar.setProperty("value", 100.0)
        sleep(0.1)



        # self.ui.re
        # senderText = self.sender().text() #sender() komutu burada fonksiyona sokulan elemanı temsil ediyor.
        # result = 0

        # if senderText == "Toplama": #bu noktada MainWindow.py içindeki self.btn_toplama.setText parametresinin "Toplama" olması lazım. Yani isimler eşleşmeli
        #     result = float(self.ui.txt_sayi1.text()) + float(self.ui.txt_sayi2.text())

        # elif senderText == "Çıkarma":
        #     result = float(self.ui.txt_sayi1.text()) - float(self.ui.txt_sayi2.text())

        # elif senderText == "Çarpma":
        #     result = float(self.ui.txt_sayi1.text()) * float(self.ui.txt_sayi2.text())

        # elif senderText == "Bölme":
        #     result = float(self.ui.txt_sayi1.text()) / float(self.ui.txt_sayi2.text())

        # elif senderText == "S1^S2":
        #     result = float(self.ui.txt_sayi1.text()) ** float(self.ui.txt_sayi2.text())

        # self.ui.lbl_result.setText("Sonuç: " + str(result))
    
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec())

app()