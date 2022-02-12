from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime, Qt
import sys
import pymysql.cursors

class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        import DBCon
        self.conn = DBCon.DB_connect()

    def setupUi(self):
        self.resize(860, 616)
        self.setFixedSize(860,616)
        self.setWindowTitle("카페 POS")
        self.index = 0
        self.totalPrice = 0                   #총 금액
        self.createtableWidget()      # tabelWidget 만드는 함수
        self.createLineEdit()
        self.createBtn()         #버튼 만드는 함수
        self.createLabel()
        self.detail = []

    def createLineEdit(self):
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(240, 260, 181, 31)
        self.lineEdit.setText("0")

    def createLabel(self):
        self.totalLabel = QtWidgets.QLabel(self)
        self.totalLabel.setGeometry(180,270,56,12)
        self.totalLabel.setText("총 금액 : ")

        self.timeLabel = QtWidgets.QLabel(self)
        self.timeLabel.setGeometry(740,585,231,16)
        time = QDateTime.currentDateTime()
        self.timeLabel.setText(time.toString('yyyy.MM.dd hh:mm:ss'))

    def createtableWidget(self):
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 421, 261))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnWidth(0, self.tableWidget.width() / 3)
        self.tableWidget.setColumnWidth(1, 95)
        self.tableWidget.setColumnWidth(2, self.tableWidget.width() / 3)

        headerList = ["   1","   2","   3","   4","   5","   6","   7","   8","   9","   10","  11","   12"]
        rowList = ["상 품 명","수  량","금  액"]

        for i in range(0,8):
            item = QtWidgets.QTableWidgetItem()
            item.setText(headerList[i])
            self.tableWidget.setVerticalHeaderItem(i, item)

        for i in range(0,3):
            item = self.item_AlignCenter(str(rowList[i]))
            self.tableWidget.setHorizontalHeaderItem(i, item)

    def createBtn(self):            #버튼 속성
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn3 = QtWidgets.QPushButton(self)
        self.btn4 = QtWidgets.QPushButton(self)
        self.btn5 = QtWidgets.QPushButton(self)
        self.btn6 = QtWidgets.QPushButton(self)
        self.btn7 = QtWidgets.QPushButton(self)
        self.btn8 = QtWidgets.QPushButton(self)
        self.btn9 = QtWidgets.QPushButton(self)
        self.btn10 = QtWidgets.QPushButton(self)
        self.btn11 = QtWidgets.QPushButton(self)
        self.btn12 = QtWidgets.QPushButton(self)
        self.btn13 = QtWidgets.QPushButton(self)
        self.btn14 = QtWidgets.QPushButton(self)
        self.btn15 = QtWidgets.QPushButton(self)
        self.btn16 = QtWidgets.QPushButton(self)
        self.btn17 = QtWidgets.QPushButton(self)
        self.btn18 = QtWidgets.QPushButton(self)
        self.btn19 = QtWidgets.QPushButton(self)
        self.btn20 = QtWidgets.QPushButton(self)
        self.btn21 = QtWidgets.QPushButton(self)
        self.btn22 = QtWidgets.QPushButton(self)
        self.cardBtn = QtWidgets.QPushButton(self)
        self.cashBtn = QtWidgets.QPushButton(self)
        self.cancleBtn = QtWidgets.QPushButton(self)
        self.btnSetGeometry()
        self.btnEventConn()

    def btnSetGeometry(self):
        self.cardBtn.setGeometry(420,0,221,111)
        self.cashBtn.setGeometry(640,0,221,111)
        self.cancleBtn.setGeometry(420,110,111,71)
        self.btn1.setGeometry(420,180,111,71)
        self.btn2.setGeometry(530,180,111,71)
        self.btn3.setGeometry(640,180,111,71)
        self.btn4.setGeometry(750,180,111,71)
        self.btn5.setGeometry(420,250,111,71)
        self.btn6.setGeometry(530,250,111,71)
        self.btn7.setGeometry(640,250,111,71)
        self.btn8.setGeometry(750,250,111,71)
        self.btn9.setGeometry(420,320,111,71)
        self.btn10.setGeometry(530,320,111,71)
        self.btn11.setGeometry(640,320,111,71)
        self.btn12.setGeometry(750,320,111,71)
        self.btn13.setGeometry(420,390,111,71)
        self.btn14.setGeometry(530,390,111,71)
        self.btn15.setGeometry(640,390,111,71)
        self.btn16.setGeometry(750, 390, 111, 71)
        self.btn17.setGeometry(420, 460, 221, 111)
        self.btn18.setGeometry(640, 460, 221, 111)
        self.btn19.setGeometry(0, 350, 211, 111)
        self.btn20.setGeometry(210, 350, 211, 111)
        self.btn21.setGeometry(0, 460, 211, 111)
        self.btn22.setGeometry(210, 460, 211, 111)

        self.btn1.setText("H아메리카노\n3000")
        self.btn2.setText("ICE아메리카노\n3000")
        self.btn3.setText("H카페라떼\n4000")
        self.btn4.setText("ICE카페라떼\n4000")
        self.btn5.setText("H카푸치노\n4000")
        self.btn6.setText("ICE카푸치노\n4000")
        self.btn7.setText("H바닐라라떼\n4500")
        self.btn8.setText("ICE바닐라라떼\n4500")
        self.btn9.setText("H헤이즐넛라떼\n4500")
        self.btn10.setText("ICE헤이즐넛라떼\n4500")
        self.btn11.setText("H돌체라떼\n4500")
        self.btn12.setText("ICE돌체라떼\n5000")
        self.btn13.setText("자바칩프라페\n5500")
        self.btn14.setText("플레인요거트\n5000")
        self.btn15.setText("X")
        self.btn16.setText("└샷추가\n500")
        self.btn17.setText("시간대 별 매출")
        self.btn18.setText("18")
        self.btn19.setText("19")
        self.btn20.setText("20")
        self.btn21.setText("판매 내역")
        self.btn22.setText("통계")
        self.cardBtn.setText("카드")
        self.cashBtn.setText("현금")
        self.cancleBtn.setText("All\nClear")

    def btnEventConn(self):
        self.cancleBtn.clicked.connect(self.clear_btn_Event)
        self.cardBtn.clicked.connect(self.cardBtn_Event)
        self.cashBtn.clicked.connect(self.cashBtn_Event)

        self.btn1.clicked.connect(self.btn1_Event)
        self.btn2.clicked.connect(self.btn2_Event)
        self.btn3.clicked.connect(self.btn3_Event)
        self.btn4.clicked.connect(self.btn4_Event)
        self.btn5.clicked.connect(self.btn5_Event)
        self.btn6.clicked.connect(self.btn6_Event)
        self.btn7.clicked.connect(self.btn7_Event)
        self.btn8.clicked.connect(self.btn8_Event)
        self.btn9.clicked.connect(self.btn9_Event)
        self.btn16.clicked.connect(self.btn16_Event)
        self.btn10.clicked.connect(self.btn10_Event)
        self.btn11.clicked.connect(self.btn11_Event)
        self.btn12.clicked.connect(self.btn12_Event)
        self.btn13.clicked.connect(self.btn13_Event)
        self.btn14.clicked.connect(self.btn14_Event)
        self.btn15.clicked.connect(self.btn15_Event)
        self.btn17.clicked.connect(self.btn17_Event)
        self.btn21.clicked.connect(self.search_Detail)
        self.btn22.clicked.connect(self.search_Statistics)

    def btn_clicked(self):
        self.totalPrice = self.totalPrice + int(self.menuPrice)
        item = self.item_AlignCenter(str(self.menuName))
        self.tableWidget.setItem(self.index, 0, item)

        item = self.item_AlignCenter(str("1"))
        self.tableWidget.setItem(self.index, 1, item)

        item = self.item_AlignCenter(str(self.menuPrice))
        self.tableWidget.setItem(self.index, 2, item)

        self.lineEdit.setText(str(self.totalPrice))
        self.index = self.index + 1

    def clear_btn_Event(self):        #All Clear 버튼
        self.tableWidget.clearContents()
        self.index = 0
        self.totalPrice = 0
        self.detail.clear()
        self.lineEdit.setText(str(self.totalPrice))

    def btn1_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn1.text().split()
        print(self.btn1.text())
        self.detail.append(self.btn1.text())
        self.btn_clicked()

    def btn2_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn2.text().split()
        self.detail.append(self.btn2.text())
        self.btn_clicked()

    def btn3_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn3.text().split()
        self.detail.append(self.btn3.text())
        self.btn_clicked()

    def btn4_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn4.text().split()
        self.detail.append(self.btn4.text())
        self.btn_clicked()

    def btn5_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn5.text().split()
        self.detail.append(self.btn5.text())
        self.btn_clicked()

    def btn6_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn6.text().split()
        self.detail.append(self.btn6.text())
        self.btn_clicked()

    def btn7_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn7.text().split()
        self.detail.append(self.btn7.text())
        self.btn_clicked()

    def btn8_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn8.text().split()
        self.detail.append(self.btn8.text())
        self.btn_clicked()

    def btn9_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn9.text().split()
        self.detail.append(self.btn9.text())
        self.btn_clicked()

    def btn10_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn10.text().split()
        self.detail.append(self.btn10.text())
        self.btn_clicked()

    def btn11_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn11.text().split()
        self.detail.append(self.btn11.text())
        self.btn_clicked()

    def btn12_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn12.text().split()
        self.detail.append(self.btn12.text())
        self.btn_clicked()

    def btn13_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn13.text().split()
        self.detail.append(self.btn13.text())
        self.btn_clicked()

    def btn14_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn14.text().split()
        self.detail.append(self.btn14.text())
        self.btn_clicked()

    def btn15_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn15.text().split()
        self.detail.append(self.btn15.text())
        self.btn_clicked()
    def btn16_Event(self):
        # 버튼의 Text 가져오기 한 후 split
        self.menuName, self.menuPrice = self.btn16.text().split()
        self.detail.append(self.btn16.text())
        self.btn_clicked()

    def btn17_Event(self):
        try:
            import DetailTime
            detail = DetailTime.TimeDetail()
            detail.showModal()

        except Exception as e:
            print(e)

    def search_Detail(self):            # 매출 내역 Dialog
        try:
            #새로운 py파일 import (띄울 파일)
            import SearhjDetailEx

            # 새로운 파일 import (SearchDetailEx) 한거의 클래스 명(MyWindow)
            # 클래스를 불러와서 변수에 넣기
            sde = SearhjDetailEx.MyWindow()

            # showModel 메서드를 통해 새로운 창 띄우기
            sde.showModal()

        except Exception as e:
            print(e)

    def search_Statistics(self):           # 통계 내역 보기
        import MonthStateUpdate
        msu = MonthStateUpdate.MonthStateClass()
        msu.showModal()

    def dialog_open(self,text):         # 계산하기 dialog 열기
        try:
            import PaymentUI
            payui = PaymentUI.PayUI(self.conn, text,self.detail,self.menuString,self.totalPrice)
            payui.showModal()

        except Exception as e:
            print(e)

    def cardBtn_Event(self):        #카드 버튼 이벤트
        self.menuText = []  # 메뉴 명만 모아놓은것
        self.menuPricelist = []  # 가격만 모아놓은 리스트
        self.menuString = ""  # 메뉴 명만 모아놓은것

        for i in range(self.index):
            print(self.tableWidget.item(i, 0).text(), self.tableWidget.item(i, 2).text())

            self.menuText.append(self.tableWidget.item(i, 0).text())
            self.menuPricelist.append(self.tableWidget.item(i, 2).text())

            self.menuString = str(self.menuString) + self.tableWidget.item(i, 0).text()
            if i != self.index - 1:
                self.menuString = self.menuString + ","

        self.dialog_open("카드 계산")       # dialog 오픈
        self.tableWidget.clearContents()
        self.clear_btn_Event()
        self.repaint()


    def cashBtn_Event(self):        #현금 결제 버튼
        self.menuText = []  # 메뉴 명만 모아놓은것
        self.menuPricelist = []  # 가격만 모아놓은 리스트
        self.menuString = ""  # 메뉴 명만 모아놓은것
        for i in range(self.index):
            print(self.tableWidget.item(i, 0).text(), self.tableWidget.item(i, 2).text())

            self.menuText.append(self.tableWidget.item(i, 0).text())
            self.menuPricelist.append(self.tableWidget.item(i, 2).text())

            self.menuString = str(self.menuString) + self.tableWidget.item(i, 0).text()
            if i != self.index - 1:
                self.menuString = self.menuString + ","

        self.dialog_open("현금 계산")       # dialog 오픈
        self.clear_btn_Event()
        self.repaint()

    def item_AlignCenter(self,text):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)  # 가운데 정렬
        item.setText(text)
        return item

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainUI()
    ui.show()
    sys.exit(app.exec_())