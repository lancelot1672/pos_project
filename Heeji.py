# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc\PycharmProjects\Kiosk__\UI\Menu_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from DB import order_DAO
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLabel
import mariadb
import base64

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        # db에서 꺼내와서 리스트에 넣어주는 기능 추가
        # db 파이썬 파일 import
        # conn = 파일.db_connect()
        # conn.cursor 해서 sql문 적용시키기
        # 가져오면 => 리스트 안에 튜플로 들어가나?
        # 여기서 setupUI 정의하기

        # 장바구니 넣기 하면 값이 저장되는 주문 리스트

        self.basket = []


        self.count = 0
        db = order_DAO.order_DAO()
        self.conn = db.db_connect()

        # 카테고리 '커피/라떼' 메뉴 이름 , 가격
        self.menu_list = db.menu_list(self.conn)

        # 카테고리 '에이드/스무디' 메뉴 이름 , 가격
        self.menu_list2 = db.menu_list2(self.conn)

        # 카테고리 '차' 메뉴 이름 , 가격
        self.menu_list3 = db.menu_list3(self.conn)

        # 카테고리 '커피/라떼' 길이
        self.max_count = len(self.menu_list)

        # 카테고리 '에이드/스무디' 길이
        self.max_count2 = len(self.menu_list2)

        # 카테고리 '차' 길이
        self.max_count3 = len(self.menu_list3)

        pass

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(290, 602)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 291, 471))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.menu_img = QtWidgets.QPushButton(self.tab)
        self.menu_img.setGeometry(QtCore.QRect(85, 30, 121, 131))
        self.menu_img.setText("")


        # '카테고리 '커피/라떼' 이미지
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\pc\\PycharmProjects\\Kiosk__\\UI\\../Image/에스프레소.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_img.setIcon(icon)
        self.menu_img.setIconSize(QtCore.QSize(160, 140))
        self.menu_img.setObjectName("menu_img")

        self.menu_name = QtWidgets.QLabel(self.tab)
        self.menu_name.setGeometry(QtCore.QRect(50, 170, 181, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        self.menu_name.setFont(font)
        self.menu_name.setObjectName("menu_name")

        self.menu_price = QtWidgets.QLabel(self.tab)
        self.menu_price.setGeometry(QtCore.QRect(90, 210, 101, 31))

        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.menu_price.setFont(font)
        self.menu_price.setObjectName("menu_price")

        self.menu_num = QtWidgets.QSpinBox(self.tab)
        self.menu_num.setGeometry(QtCore.QRect(80, 250, 121, 31))


        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.menu_num.setFont(font)
        self.menu_name.setAlignment(Qt.AlignCenter)
        self.menu_price.setAlignment(Qt.AlignCenter)
        self.menu_num.setObjectName("menu_num")
        self.front = QtWidgets.QPushButton(self.tab)
        self.front.setGeometry(QtCore.QRect(10, 310, 131, 51))
        font = QtGui.QFont()

        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.front.setFont(font)
        self.front.setObjectName("front")
        self.back = QtWidgets.QPushButton(self.tab)
        self.back.setGeometry(QtCore.QRect(150, 310, 131, 51))
        font = QtGui.QFont()

        self.front.clicked.connect(lambda: self.front_clicked(Dialog)) # 메뉴 앞으로 가기

        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setObjectName("back")

        self.basket_btn = QtWidgets.QPushButton(self.tab)
        self.basket_btn.setGeometry(QtCore.QRect(10, 370, 271, 61))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.basket_btn.setFont(font)
        self.basket_btn.setObjectName("basket_btn")

        self.tabWidget.addTab(self.tab, "")

        self.back.clicked.connect(lambda: self.back_clicked(Dialog))

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.menu_img_2 = QtWidgets.QPushButton(self.tab_2)
        self.menu_img_2.setGeometry(QtCore.QRect(90, 20, 101, 141))
        self.menu_img_2.setText("")

        # '카테고리 '에이드/스무디' 이미지
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\pc\\PycharmProjects\\Kiosk__\\UI\\../Image/자몽.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.menu_img_2.setIcon(icon1)
        self.menu_img_2.setIconSize(QtCore.QSize(160, 140))
        self.menu_img_2.setObjectName("menu_img_2")

        self.menu_name_2 = QtWidgets.QLabel(self.tab_2)
        self.menu_name_2.setGeometry(QtCore.QRect(40, 170, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.menu_name_2.setFont(font)
        self.menu_name_2.setObjectName("menu_name_2")
        self.menu_price_2 = QtWidgets.QLabel(self.tab_2)
        self.menu_price_2.setGeometry(QtCore.QRect(90, 210, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.menu_price_2.setFont(font)
        self.menu_price_2.setObjectName("menu_price_2")
        self.menu_num_2 = QtWidgets.QSpinBox(self.tab_2)
        self.menu_num_2.setGeometry(QtCore.QRect(80, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.menu_num_2.setFont(font)
        self.menu_name_2.setAlignment(Qt.AlignCenter)
        self.menu_price_2.setAlignment(Qt.AlignCenter)
        self.menu_num_2.setObjectName("menu_num_2")
        self.front_2 = QtWidgets.QPushButton(self.tab_2)
        self.front_2.setGeometry(QtCore.QRect(10, 310, 131, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.front_2.setFont(font)
        self.front_2.setObjectName("front_2")
        self.front_2.clicked.connect(lambda: self.front2_clicked(Dialog))
        self.back_2 = QtWidgets.QPushButton(self.tab_2)
        self.back_2.setGeometry(QtCore.QRect(150, 310, 131, 51))
        self.back_2.clicked.connect(lambda: self.back2_clicked(Dialog))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back_2.setFont(font)

        self.back_2.setObjectName("back_2")
        self.basket_btn_2 = QtWidgets.QPushButton(self.tab_2)
        self.basket_btn_2.setGeometry(QtCore.QRect(10, 370, 271, 61))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.basket_btn_2.setFont(font)
        self.basket_btn_2.setObjectName("basket_btn_2")
        self.tabWidget.addTab(self.tab_2, "")




        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.menu_num_3 = QtWidgets.QSpinBox(self.tab_3)
        self.menu_num_3.setGeometry(QtCore.QRect(80, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.menu_num_3.setFont(font)
        self.menu_num_3.setObjectName("menu_num_3")
        self.menu_price_3 = QtWidgets.QLabel(self.tab_3)
        self.menu_price_3.setGeometry(QtCore.QRect(90, 210, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.menu_price_3.setFont(font)
        self.menu_price_3.setObjectName("menu_price_3")
        self.menu_name_3 = QtWidgets.QLabel(self.tab_3)
        self.menu_name_3.setGeometry(QtCore.QRect(50, 170, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.menu_name_3.setFont(font)
        self.menu_name_3.setObjectName("menu_name_3")
        self.menu_name_3.setAlignment(Qt.AlignCenter)
        self.menu_price_3.setAlignment(Qt.AlignCenter)
        self.menu_img_3 = QtWidgets.QPushButton(self.tab_3)
        self.menu_img_3.setGeometry(QtCore.QRect(70, 30, 131, 131))
        self.menu_img_3.setText("")

        # '카테고리 '차' 이미지

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\pc\\PycharmProjects\\Kiosk__\\UI\\../Image/레몬차.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.menu_img_3.setIcon(icon2)
        self.menu_img_3.setIconSize(QtCore.QSize(160, 140))
        self.menu_img_3.setObjectName("menu_img_3")

        self.back_3 = QtWidgets.QPushButton(self.tab_3)
        self.back_3.setGeometry(QtCore.QRect(150, 310, 131, 51))
        self.back_3.clicked.connect(lambda: self.back3_clicked(Dialog))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back_3.setFont(font)
        self.back_3.setObjectName("back_3")
        self.front_3 = QtWidgets.QPushButton(self.tab_3)
        self.front_3.clicked.connect(lambda: self.front3_clicked(Dialog))
        self.front_3.setGeometry(QtCore.QRect(10, 310, 131, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.front_3.setFont(font)
        self.front_3.setObjectName("front_3")
        self.basket_btn_3 = QtWidgets.QPushButton(self.tab_3)
        self.basket_btn_3.setGeometry(QtCore.QRect(10, 370, 271, 61))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.basket_btn_3.setFont(font)
        self.basket_btn_3.setObjectName("basket_btn_3")
        self.tabWidget.addTab(self.tab_3, "")
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        # 카테고리 '커피/라떼' 장바구니 넣기 버튼 이벤트
        self.basket_btn.clicked.connect(lambda: self.basket_btn_clicked(Dialog))

        # 카테고리 '에이드/스무디' 장바구니 넣기 버튼 이벤트
        self.basket_btn_2.clicked.connect(lambda: self.basket_btn_2_clicked(Dialog))

        # 카테고리 '커피/라떼' 장바구니 넣기 버튼 이벤트
        self.basket_btn_3.clicked.connect(lambda: self.basket_btn_3_clicked(Dialog))

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 291, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:rgb(126, 182, 255)")
        self.label_2.setObjectName("label_2")
        # 메뉴 선택 완료 버튼
        self.menu_select_btn = QtWidgets.QPushButton(Dialog)
        self.menu_select_btn.setGeometry(QtCore.QRect(10, 530, 271, 61))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.menu_select_btn.setFont(font)
        self.menu_select_btn.setObjectName("menu_select_btn")


        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #def menu_db(self, Dialog):

    # 이전 메뉴 버튼 이벤트 (카테고리 '커피/라떼')
    def front_clicked (self, Dialog):
        self.back.setEnabled(True)

        # 뒤로 버튼 클릭시 인덱스 -1
        if self.count != 0:
            self.count -= 1

        # menu_list에서 메뉴 이름 받아오기
        self.menu_name.setText(self.menu_list[self.count][0])

        # menu_list에서 메뉴 가격 받아오기
        self.menu_price.setText(self.menu_list[self.count][1])

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap((self.menu_list[self.count][2])), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.menu_img.setIcon(icon)
        self.menu_img.setIconSize(QtCore.QSize(160, 140))
        self.menu_img.setObjectName("menu_img")

        self.menu_num.setValue(0)

        # 마지막 인덱스 일 때 앞으로 버튼 비활성화
        if self.count == 0:
            self.front.setDisabled(True)



    # 다음 메뉴 버튼 이벤트 (카테고리 '커피/라떼')
    def back_clicked(self, Dialog):
        self.front.setEnabled(True)

        # 앞으로 버튼 클릭시 인덱스 +1
        if self.count != self.max_count:
            self.count += 1

            # count에 맞는 메뉴명, 가격, 이미지 받아와서 출력하기

            self.menu_name.setText(self.menu_list[self.count][0])
            self.menu_price.setText(self.menu_list[self.count][1])

            # 원래 count-1.ver
            #self.menu_name.setText(self.menu_list[self.count][0])
            #self.menu_price.setText(self.menu_list[self.count][1])

            #print(self.menu_list[self.count-1][2])
            self.menu_num.setValue(0)

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap((self.menu_list[self.count][2])), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            self.menu_img.setIcon(icon)
            self.menu_img.setIconSize(QtCore.QSize(160, 140))
            self.menu_img.setObjectName("menu_img")

            # 마지막 인덱스 일 때 다음 메뉴 버튼 비활성화
            if self.count == self.max_count:
                self.back.setDisabled(True)

    # 이전 메뉴 버튼 이벤트 (카테고리 '에이드/스무디')
    def front2_clicked(self, Dialog):
            self.back_2.setEnabled(True)

            # 뒤로 버튼 클릭시 인덱스 -1
            if self.count != 0:
                self.count -= 1

            # menu_list에서 메뉴 이름 받아오기
            self.menu_name_2.setText(self.menu_list2[self.count][0])

            # menu_list에서 메뉴 가격 받아오기
            self.menu_price_2.setText(self.menu_list2[self.count][1])

            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(self.menu_list2[self.count][2]), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            self.menu_img_2.setIcon(icon1)
            self.menu_img_2.setIconSize(QtCore.QSize(160, 140))
            self.menu_img_2.setObjectName("menu_img_2")
            self.menu_num.setValue(0)

            # 마지막 인덱스 일 때 앞으로 버튼 비활성화
            if self.count == 0:
                self.front_2.setDisabled(True)

    # 다음 메뉴 버튼 이벤트 (카테고리 '에이드/스무디')
    def back2_clicked(self, Dialog):
        try:
            self.front_2.setEnabled(True)

            # 앞으로 버튼 클릭시 인덱스 +1
            if self.count != self.max_count2:
                self.count += 1
                # count에 맞는 메뉴명, 가격, 이미지 받아와서 출력하기

                self.menu_name_2.setText(self.menu_list2[self.count][0])
                self.menu_price_2.setText(self.menu_list2[self.count][1])

                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(self.menu_list2[self.count][2]), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                self.menu_img_2.setIcon(icon1)
                self.menu_img_2.setIconSize(QtCore.QSize(160, 140))
                self.menu_img_2.setObjectName("menu_img_2")
                self.menu_num.setValue(0)

                # 마지막 인덱스 일 때 다음 메뉴 버튼 비활성화
                if self.count == self.max_count2:
                    self.back_2.setDisabled(True)
        except Exception as e:
            print(e)

    # 이전 메뉴 버튼 이벤트 (카테고리 '차')
    def front3_clicked(self, Dialog):
            self.back_3.setEnabled(True)

            # 뒤로 버튼 클릭시 인덱스 -1
            if self.count != 0:
                self.count -= 1

            # menu_list에서 메뉴 이름 받아오기
            self.menu_name_3.setText(self.menu_list3[self.count][0])

            # menu_list에서 메뉴 가격 받아오기

            self.menu_price_3.setText(self.menu_list3[self.count][1])

            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(self.menu_list3[self.count][2]),QtGui.QIcon.Normal, QtGui.QIcon.Off)

            self.menu_img_3.setIcon(icon2)
            self.menu_img_3.setIconSize(QtCore.QSize(160, 140))
            self.menu_img_3.setObjectName("menu_img_3")
            self.menu_num.setValue(0)

            # 마지막 인덱스 일 때 앞으로 버튼 비활성화
            if self.count == 0:
                self.front_3.setDisabled(True)

    # 다음 메뉴 버튼 이벤트 (카테고리 '차')
    def back3_clicked(self, Dialog):
        try:
            self.front_3.setEnabled(True)
            # 앞으로 버튼 클릭시 인덱스 +1
            if self.count != self.max_count3:
                self.count += 1

                # count에 맞는 메뉴명, 가격, 이미지 받아와서 출력하기

                self.menu_name_3.setText(self.menu_list3[self.count ][0])
                self.menu_price_3.setText(self.menu_list3[self.count ][1])

                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap(self.menu_list3[self.count][2]), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                self.menu_img_3.setIcon(icon2)
                self.menu_img_3.setIconSize(QtCore.QSize(160, 140))
                self.menu_img_3.setObjectName("menu_img_3")
                self.menu_num.setValue(0)

                # 마지막 인덱스 일 때 다음 메뉴 버튼 비활성화
                if self.count == self.max_count3:
                    self.back_3.setDisabled(True)
        except Exception as e:
            print(e)

    # 카테고리 '커피/라떼' 장바구니 넣기 버튼 이벤트
    def basket_btn_clicked(self, Dialog):
        self.val = self.menu_num.value()

        if self.val != 0:
            self.orders = {'Menu': ' ', 'Price': 0, 'Count': 0}
            self.orders['Menu'] = self.menu_list[self.count][0]
            self.orders['Price'] = int(self.menu_list[self.count][1])
            self.orders['Count'] = self.val
            #print(self.menu_list[self.count][0], self.menu_list[self.count][1], str(self.val) + ' 개')

            self.basket.append(self.orders)

            print(self.basket)


    # 카테고리 '에이드/스무디' 장바구니 넣기 버튼 이벤트
    def basket_btn_2_clicked(self, Dialog):
        self.val = self.menu_num_2.value()

        if self.val != 0:
            print(self.menu_list2[self.count][0],self.menu_list2[self.count][1], str(self.val) + ' 개')


    # 카테고리 '차' 장바구니 넣기 버튼 이벤트
    def basket_btn_3_clicked(self, Dialog):
        self.val = self.menu_num_3.value()

        if self.val != 0:
            print(self.menu_list3[self.count][0],self.menu_list3[self.count][1], str(self.val) + ' 개')



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        # (카테고리 '커피/라떼') 에 맞는 count 값 받아와서 출력
        self.menu_name.setText(self.menu_list[self.count][0])
        self.menu_price.setText(self.menu_list[self.count][1])

        self.front.setText(_translate("Dialog", "이전 메뉴"))
        self.back.setText(_translate("Dialog", "다음 메뉴"))
        self.basket_btn.setText(_translate("Dialog", "장바구니 넣기"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "커피 / 라떼"))

        # (카테고리 '에이드/스무디') 에 맞는 count 값 받아와서 출력
        self.menu_name_2.setText(self.menu_list2[self.count][0])
        self.menu_price_2.setText(self.menu_list2[self.count][1])

        self.front_2.setText(_translate("Dialog", "이전 메뉴"))
        self.back_2.setText(_translate("Dialog", "다음 메뉴"))
        self.basket_btn_2.setText(_translate("Dialog", "장바구니 넣기"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "에이드 / 스무디"))

        # (카테고리 '차') 에 맞는 count 값 받아와서 출력
        self.menu_name_3.setText(self.menu_list3[self.count][0])
        self.menu_price_3.setText(self.menu_list3[self.count][1])

        self.front_3.setText(_translate("Dialog", "이전 메뉴"))
        self.back_3.setText(_translate("Dialog", "다음 메뉴"))
        self.basket_btn_3.setText(_translate("Dialog", "장바구니 넣기"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "  차   "))

        self.menu_select_btn.setText(_translate("Dialog", "메뉴 선택 완료"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">메뉴 주문</p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())