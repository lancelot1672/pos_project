# 시간대 별 내역

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pymysql.cursors
import sys

class TimeDetail(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def showModal(self):
        return super().exec_()

    def setupUI(self):  # 보여주기
        self.resize(993, 805)  # 다이얼로그의 크기 설정
        self.setFixedSize(993,805)      #사이즈 고정
        self.setWindowTitle("시간대 별 매출 보기")
        self.CreateCalendar()  # 캘린더 만들기
        self.CreateTableWidget()
        self.CreateBtn()
        self.CreateLabel()
        self.CreateTextField()


    def showDate(self,date):
        date = date.toString()
        listDate = str(date).split()
        self.dateText = listDate[3] + '-' + listDate[1] + '-' +listDate[2]
        self.field.setText(self.dateText)

    def CreateCalendar(self):                                       #캘린더의 속성
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(720,30,272,183)
        self.date = self.calendar.selectedDate()
        self.calendar.clicked[QDate].connect(self.showDate)


    def CreateTableWidget(self):                                    #테이블위젯 속성
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(0,30,721,780)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(25)

        #행의 넓이 정의
        self.tableWidget.setColumnWidth(0, self.tableWidget.width() / 2)
        self.tableWidget.setColumnWidth(1, 97)
        self.tableWidget.setColumnWidth(2, 257)
        for i in range(0,25):                                                   #열 25개
            item = QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        TextList = ['시간','주문 수','총매출']

        for i in range(0, 3):                                                   #행 3개
            item = QTableWidgetItem()
            item.setText(TextList[i])
            self.tableWidget.setHorizontalHeaderItem(i, item)

        #시간 출력하기
        self.timeList = ["00:00~01:00", "01:00~02:00", "02:00~03:00", "03:00~04:00", "04:00~05:00", "05:00~06:00",
                        "06:00~07:00"
                , "07:00~08:00", "08:00~09:00", "09:00~10:00", "11:00~12:00", "12:00~13:00", "13:00~14:00",
                        "14:00~15:00", "15:00~16:00"
                , "16:00~17:00", "17:00~18:00", "18:00~19:00", "19:00~20:00", "20:00~21:00", "21:00~22:00",
                        "22:00~23:00", "23:00~24:00"]
        self.timeList2 = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00",
                        "06:00", "07:00", "08:00", "09:00", "10:00", "11:00","12:00", "13:00","14:00", "15:00",
                          "16:00", "17:00", "18:00", "19:00", "20:00", "21:00","22:00","23:00","24:00"]
        try:
            for i in range(0, len(self.timeList2)-1):
                item = self.item_AlignCenter(str(self.timeList2[i] + " ~ " + self.timeList2[i+1]))
                self.tableWidget.setItem(i, 0, QTableWidgetItem(item))
            item = self.item_AlignCenter("총 매출")
            self.tableWidget.setItem(24, 0, item)
        except Exception as e:
            print(e)

    def CreateBtn(self):                                        #버튼 속성
        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(720,240,274,31)
        self.btn1.setText("시간대 별 매출 출력")
        self.btn1.clicked.connect(self.btn1_Event)

        self.btn2 = QPushButton(self)
        self.btn2.setGeometry(720, 663, 274, 71)
        self.btn2.setText("XXXX")


        self.btn3 = QPushButton(self)
        self.btn3.setGeometry(720, 734, 274, 71)
        self.btn3.setText("뒤로가기")
        self.btn3.clicked.connect(self.btn3_Event)

    def CreateLabel(self):                                  # 레이블 속성
        self.label1 = QLabel(self)
        self.label1.setText("시간대별 매출 조회")
        self.label1.setGeometry(450,10,150,16)

    def CreateTextField(self):
        self.field = QTextEdit(self)
        self.field.setGeometry(720,210,274,31)

        # 현재시간 가져오기
        import datetime
        now = datetime.datetime.now()
        s = now.strftime('%Y-%m-%d')

        #현재시간 필드에 설정해주기
        self.field.setText(s)
        self.dateText = s

    def btn1_Event(self):               #조회하기 버튼
        self.tableWidget.clearContents()        #내용 초기화
        self.totalOrder = 0
        self.totalPrice = 0
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='ehdfbf8749',
            db='pos_db',
            charset='utf8'
        )
        try:
            for i in range(0, len(self.timeList2) - 1):

                item = self.item_AlignCenter(str(self.timeList2[i] + " ~ " + self.timeList2[i + 1]))
                self.tableWidget.setItem(i, 0, QTableWidgetItem(item))
            item = self.item_AlignCenter("총 매출")
            self.tableWidget.setItem(24, 0, QTableWidgetItem(item))
        except Exception as e:
            print(e)

        import DBCon
        for i in range(0, len(self.timeList2) - 1):
            order = DBCon.DB_order_count(conn,self.dateText,self.timeList2[i],self.timeList2[i+1])      #시간대 별 주문 수 DB 가져오기
            price = DBCon.DB_total_Price(conn,self.dateText,self.timeList2[i],self.timeList2[i+1])          #시간대 별 금액 DB 가져오기
            self.totalPrice = self.totalPrice + price           #총 금액
            self.totalOrder = self.totalOrder + order       #총 주문 수
            item = self.item_AlignCenter(str(order))
            self.tableWidget.setItem(i, 1, item)

            item = self.item_AlignCenter((str(price)))
            self.tableWidget.setItem(i, 2, item)

        item = self.item_AlignCenter(str(self.totalOrder))
        self.tableWidget.setItem(24, 1, item)

        item = self.item_AlignCenter(str(self.totalPrice))
        self.tableWidget.setItem(24, 2, item)

    def btn3_Event(self):  # 뒤로가기 버튼
        self.close()
    def item_AlignCenter(self,text):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)  # 가운데 정렬
        item.setText(text)
        return item

if __name__ == '__main__':
    app = QApplication(sys.argv)
    TimeUi = TimeDetail()
    TimeUi.show()
    sys.exit(app.exec_())
