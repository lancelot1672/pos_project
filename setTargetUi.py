from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pymysql.cursors
from PyQt5 import QtGui
import sys

class TargetUi(QDialog):
    def __init__(self,month):
        super().__init__()
        self.month = int(month)
        self.setupUI()

    def showModal(self):
        return super().exec_()

    def setupUI(self):  # 보여주기
        self.resize(400, 300)  # 다이얼로그의 크기 설정
        self.setFixedSize(400,300)      #사이즈 고정
        self.setWindowTitle("목표액 설정하기")

        self.createBtn()
        self.createLabel()
        self.createTextField()

    def createBtn(self):
        self.inputBtn = QPushButton(self)
        self.inputBtn.setText("설정")
        self.inputBtn.setGeometry(80,240,101,41)
        self.inputBtn.clicked.connect(self.inputEvent)

        self.cancelBtn = QPushButton(self)
        self.cancelBtn.setText("취소")
        self.cancelBtn.setGeometry(220, 240, 101, 41)
        self.cancelBtn.clicked.connect(self.cancelEvent)

    def inputEvent(self):
        target = self.field.toPlainText()
        target = int(target)

        #디비 처리
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='ehdfbf8749',
            db='pos_db',
            charset='utf8'
        )
        curs = conn.cursor()
        sql = "update targetsales set target = %s where month = %s;"
        # curs.execute(sql,('H아메리카노,ICE아메리카노',8000,'카드'))
        curs.execute(sql,(target,self.month))
        conn.commit()
        self.close()

    def cancelEvent(self):
        self.close()
        
    def createLabel(self):
        self.label = QLabel(self)
        self.label.setText("목표액을 설정해주세요")
        font = self.fontSet("Arial Black",20)
        self.label.setFont(font)
        self.label.setGeometry(60,30,291,71)

    def fontSet(self,family,size):          #폰트 설정하는 함수
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(size)
        return font

    def createTextField(self):
        self.field = QTextEdit(self)
        self.field.setGeometry(60,130,281,31)
        self.field.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tu = TargetUi(12)
    tu.show()
    sys.exit(app.exec_())