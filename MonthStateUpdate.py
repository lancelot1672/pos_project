# 월별 통계

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import pymysql.cursors
import sys

class MonthStateClass(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def showModal(self):
        return super().exec_()

    def setupUI(self):  # 보여주기
        self.resize(1071,764)  # 다이얼로그의 크기 설정
        self.setFixedSize(1071,764)      #사이즈 고정
        self.setWindowTitle("월별 통계 내역 보기")
        self.createCalendar()  # 캘린더 만들기
        self.createTableWidget()
        self.createBtn()
        self.createLabel()
        self.createTextBrowser()
        self.createTargetPer()

    def showDate(self,date):
        date = date.toString()
        listDate = str(date).split()
        self.month = listDate[1]
        self.dateText = listDate[3] + '-' + listDate[1] + '-'              #YYYY-MM-
        self.textBrowser.setText(self.dateText)

    def setTableDayText(self):
        for i in range(0, 31):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)  # 가운데 정렬
            item.setText(str(i+1))
            self.tableWidget.setItem(i, 0, QTableWidgetItem(item))


    def createBtn(self):
        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(780,240,271,41)
        self.btn1.setText("통계 내기")
        self.btn1.clicked.connect(self.btn1_Event)

        self.btn2 = QPushButton(self)
        self.btn2.setGeometry(780, 450, 271, 81)
        self.btn2.setText("목표 달성액 설정")
        self.btn2.clicked.connect(self.btn2_Event)

        self.btn3 = QPushButton(self)
        self.btn3.setGeometry(780, 530, 271, 81)
        self.btn3.setText("뒤로가기")
        self.btn3.clicked.connect(self.btn3_Event)

    def btn1_Event(self):               #조회하기 버튼
        self.tableWidget.clearContents()        #내용 초기화
        self.monthLabel.setText(self.month)
        self.setTableDayText()
        self.getPrice()
        self.getTarget()
        self.targetPriceCalc()


    def getTarget(self):
        curs = self.conn.cursor()
        sql = "select target from targetsales where month = %s";
        curs.execute(sql,self.month)
        rows = curs.fetchone()
        self.value = rows[0]
        self.targetPriceLabel.setText(str(self.value))


    def getPrice(self):
        self.month_total_price = 0

        import DBCon
        self.conn = pymysql.connect(host='localhost',user='root',password='ehdfbf8749',db='pos_db',charset='utf8')

        for i in range(1,32):
            day_total_price = DBCon.DB_get_total_price(self.conn, self.dateText + str(i))         #하루씩 총매출 가져오기
            self.month_total_price = self.month_total_price + int(day_total_price)
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)       #가운데 정렬
            item.setText(str(day_total_price))
            self.tableWidget.setItem(i-1,1,QTableWidgetItem(item))
        self.connentTotalLabel.setText(str(self.month_total_price))     #현재까지 총 매출 출력
        
    def btn2_Event(self):  # 목표 달성액 설정 버튼
        import setTargetUi
        tu = setTargetUi.TargetUi(self.month)
        tu.showModal()

    def btn3_Event(self):  # 뒤로가기 버튼
        self.close()

    def createTargetPer(self):          #목표 달성율 LCD 표시
        self.lcdNum = QLCDNumber(self)
        self.lcdNum.setGeometry(20,30,161,91)
        self.lcdNum.display("99")


    def createTextBrowser(self):
        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setGeometry(780,210,271,31)
        font = self.fontSet("Agency FB", 10)  # 사용자 지정 폰트 함수
        self.textBrowser.setFont(font)

        # 현재시간 가져오기
        import datetime
        now = datetime.datetime.now()
        time = now.strftime('%Y-%m-')
        self.month = now.strftime('%m')
        self.day = now.strftime('%d')

        # 현재시간 필드에 설정해주기
        self.textBrowser.setText(time)
        self.dateText = time

    def createCalendar(self):                                       #캘린더의 속성
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(780,20,272,183)
        self.date = self.calendar.selectedDate()
        self.calendar.clicked[QDate].connect(self.showDate)

    def createTableWidget(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(250,130,501,481)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(31)

        # 행의 넓이 정의
        self.tableWidget.setColumnWidth(0, self.tableWidget.width() / 5)
        self.tableWidget.setColumnWidth(1, 377)

        for i in range(0, 31):  # 열 31개
            item = QTableWidgetItem()

            self.tableWidget.setVerticalHeaderItem(i, item)

        TextList = ["일","매출"]

        for i in range(0, 2):  # 헤더 2개 설정하기
            item = QTableWidgetItem()
            item.setText(TextList[i])
            self.tableWidget.setHorizontalHeaderItem(i, item)

    def createLabel(self):
        self.label1 = QLabel(self)
        self.label1.setText("목표 달성율")
        self.label1.setGeometry(50,10,101,16)

        font = self.fontSet("Arial", 12)  # 사용자 지정 폰트 함수
        self.label1.setFont(font)

        self.label2 = QLabel(self)
        self.label2.setText("월 목표액 : ")
        self.label2.setGeometry(360,30,351,31)

        font = self.fontSet("Britannic Bold",20)    # 사용자 지정 폰트 함수
        font.setItalic(False)
        self.label2.setFont(font)

        self.label3 = QLabel(self)
        self.label3.setText("현재 총매출 : ")
        self.label3.setGeometry(400,80,101,16)

        font = self.fontSet("Arial", 12)  # 사용자 지정 폰트 함수
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label3.setFont(font)

        self.monthLabel = QLabel(self)      # ~~월
        self.monthLabel.setText("   --")
        self.monthLabel.setGeometry(310,30,50,30)

        font = self.fontSet("Britannic Bold",20)    # 사용자 지정 폰트 함수
        self.monthLabel.setFont(font)

        self.targetPriceLabel = QLabel(self)
        self.targetPriceLabel.setText("")
        self.targetPriceLabel.setGeometry(510,30,211,30)

        font = self.fontSet("Britannic Bold",20)    # 사용자 지정 폰트 함수
        font.setItalic(False)
        self.targetPriceLabel.setFont(font)

        self.connentTotalLabel = QLabel(self)
        self.connentTotalLabel.setText("-")
        self.connentTotalLabel.setGeometry(510,80,71,16)

        font = self.fontSet("Arial",12)
        self.connentTotalLabel.setFont(font)

    def targetPriceCalc(self):          #목표 달성율 계산
        # 목표액 계산
        self.a = int(self.value) / 31
        self.abc = int(self.month_total_price) / (self.a * int(self.day))
        abcd = int(self.abc * 100)
        self.lcdNum.display(abcd)


    def fontSet(self,family,size):          #폰트 설정하는 함수
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(size)
        return font

if __name__ == '__main__':
    app = QApplication(sys.argv)
    msc = MonthStateClass()
    msc.show()
    sys.exit(app.exec_())