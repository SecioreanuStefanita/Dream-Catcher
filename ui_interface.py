# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newMainWindowmGXiBD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 600)
        MainWindow.setStyleSheet(u"*{\n"
"border: none;\n"
"background-color:transparent;\n"
"background:none;\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"}\n"
"#centralwidget{\n"
"background-color:#1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"background-color:#16191d;\n"
"}\n"
"#leftMenuSubContainer QpushButton{\n"
"text-align :left;\n"
"padding: 2 px 10px;\n"
"border-bottom-left-radius: 100px;\n"
"border-top-left-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:#1f232a;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuContainer.setMaximumSize(QSize(48, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u"Icons/align-left (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.menuBtn, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 16, 16, 0)
        self.infoGatheringBtn = QPushButton(self.frame_2)
        self.infoGatheringBtn.setObjectName(u"infoGatheringBtn")
        self.infoGatheringBtn.setStyleSheet(u"background-color:#1f232a;\n"
"text-align :left;\n"
"padding: 2 px 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-left-radius: 10px;")
        icon1 = QIcon()
        icon1.addFile(u"Icons/terminal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoGatheringBtn.setIcon(icon1)
        self.infoGatheringBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.infoGatheringBtn)

        self.wifiCrackingBtn = QPushButton(self.frame_2)
        self.wifiCrackingBtn.setObjectName(u"wifiCrackingBtn")
        self.wifiCrackingBtn.setStyleSheet(u"\n"
"text-align :left;\n"
"padding: 2 px 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-left-radius: 10px;")
        icon2 = QIcon()
        icon2.addFile(u"Icons/wifi (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.wifiCrackingBtn.setIcon(icon2)
        self.wifiCrackingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.wifiCrackingBtn)

        self.attacksMenu = QPushButton(self.frame_2)
        self.attacksMenu.setObjectName(u"attacksMenu")
        self.attacksMenu.setStyleSheet(u"text-align :left;\n"
"padding: 2 px 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-left-radius: 10px;")
        icon3 = QIcon()
        icon3.addFile(u"Icons/codesandbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.attacksMenu.setIcon(icon3)
        self.attacksMenu.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.attacksMenu)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 16, 0, 0)
        self.exitBtn = QPushButton(self.frame_3)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setStyleSheet(u"text-align :left;\n"
"padding: 2 px 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-left-radius: 10px;")
        icon4 = QIcon()
        icon4.addFile(u"Icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon4)
        self.exitBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.exitBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.centerMenuPages.setStyleSheet(u"background-color:#2c313c;")
        self.centerMenuPages.setFrameShape(QFrame.NoFrame)
        self.info_gathering_submenu = QWidget()
        self.info_gathering_submenu.setObjectName(u"info_gathering_submenu")
        self.verticalLayout_8 = QVBoxLayout(self.info_gathering_submenu)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_14 = QFrame(self.info_gathering_submenu)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_14)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.port_scanner_goto = QPushButton(self.frame_14)
        self.port_scanner_goto.setObjectName(u"port_scanner_goto")

        self.verticalLayout_26.addWidget(self.port_scanner_goto)

        self.email_scraper_goto = QPushButton(self.frame_14)
        self.email_scraper_goto.setObjectName(u"email_scraper_goto")

        self.verticalLayout_26.addWidget(self.email_scraper_goto)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.centerMenuPages.addWidget(self.info_gathering_submenu)
        self.attacks_submenu = QWidget()
        self.attacks_submenu.setObjectName(u"attacks_submenu")
        self.verticalLayout_9 = QVBoxLayout(self.attacks_submenu)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_16 = QFrame(self.attacks_submenu)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_16)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.fhishing_goto = QPushButton(self.frame_16)
        self.fhishing_goto.setObjectName(u"fhishing_goto")

        self.verticalLayout_28.addWidget(self.fhishing_goto)


        self.verticalLayout_9.addWidget(self.frame_16)

        self.centerMenuPages.addWidget(self.attacks_submenu)
        self.wifi_submenu = QWidget()
        self.wifi_submenu.setObjectName(u"wifi_submenu")
        self.verticalLayout_7 = QVBoxLayout(self.wifi_submenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_15 = QFrame(self.wifi_submenu)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_15)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.dictionary_wifi_goto = QPushButton(self.frame_15)
        self.dictionary_wifi_goto.setObjectName(u"dictionary_wifi_goto")

        self.verticalLayout_27.addWidget(self.dictionary_wifi_goto)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.centerMenuPages.addWidget(self.wifi_submenu)

        self.verticalLayout_6.addWidget(self.centerMenuPages)

        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color:#1f232a;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 8, 4, 0)
        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon5 = QIcon()
        icon5.addFile(u"Icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon5)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignLeft)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(0)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setMinimumSize(QSize(534, 600))
        self.mainBodyContainer.setMaximumSize(QSize(16777215, 16777215))
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        font = QFont()
        font.setFamily(u"Segoe UI Emoji")
        self.headerContainer.setFont(font)
        self.headerContainer.setStyleSheet(u"background-color:#D2602A;")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(48, 48))
        self.label_5.setPixmap(QPixmap(u"Icons/logo2.jpg"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label_6.setFont(font1)
        self.label_6.setCursor(QCursor(Qt.UpArrowCursor))

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addFileBtn = QPushButton(self.frame_6)
        self.addFileBtn.setObjectName(u"addFileBtn")
        icon6 = QIcon()
        icon6.addFile(u"Icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addFileBtn.setIcon(icon6)
        self.addFileBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.addFileBtn)

        self.infoBtn = QPushButton(self.frame_6)
        self.infoBtn.setObjectName(u"infoBtn")
        icon7 = QIcon()
        icon7.addFile(u"Icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon7)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.infoBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon8 = QIcon()
        icon8.addFile(u"Icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon9 = QIcon()
        icon9.addFile(u"Icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon10 = QIcon()
        icon10.addFile(u"Icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.email_scrapper_page = QWidget()
        self.email_scrapper_page.setObjectName(u"email_scrapper_page")
        self.verticalLayout_18 = QVBoxLayout(self.email_scrapper_page)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_11 = QLabel(self.email_scrapper_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_11)

        self.frame_12 = QFrame(self.email_scrapper_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_12)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.address_edit_email_scrapper = QLineEdit(self.frame_12)
        self.address_edit_email_scrapper.setObjectName(u"address_edit_email_scrapper")
        self.address_edit_email_scrapper.setMinimumSize(QSize(8, 28))
        self.address_edit_email_scrapper.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.address_edit_email_scrapper.setFrame(True)

        self.verticalLayout_23.addWidget(self.address_edit_email_scrapper)

        self.email_scrapper_button = QPushButton(self.frame_12)
        self.email_scrapper_button.setObjectName(u"email_scrapper_button")
        self.email_scrapper_button.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u"Icons/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.email_scrapper_button.setIcon(icon11)
        self.email_scrapper_button.setIconSize(QSize(24, 24))

        self.verticalLayout_23.addWidget(self.email_scrapper_button)


        self.verticalLayout_18.addWidget(self.frame_12)

        self.label_18 = QLabel(self.email_scrapper_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_18)

        self.mainPages.addWidget(self.email_scrapper_page)
        self.email_scrapper_results_page = QWidget()
        self.email_scrapper_results_page.setObjectName(u"email_scrapper_results_page")
        self.verticalLayout_29 = QVBoxLayout(self.email_scrapper_results_page)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_17 = QFrame(self.email_scrapper_results_page)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy3)
        self.frame_17.setMinimumSize(QSize(34, 44))
        self.frame_17.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 16px")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_17)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_2 = QLabel(self.frame_17)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMinimumSize(QSize(33, 24))
        self.label_2.setStyleSheet(u"background-color: rgb(44, 49, 60);")

        self.verticalLayout_30.addWidget(self.label_2)

        self.line_2 = QFrame(self.frame_17)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"\n"
"background-color: rgb(210, 96, 42);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_30.addWidget(self.line_2)


        self.verticalLayout_29.addWidget(self.frame_17, 0, Qt.AlignTop)

        self.frame_19 = QFrame(self.email_scrapper_results_page)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_19)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_4 = QLabel(self.frame_19)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setMinimumSize(QSize(33, 24))
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_4)

        self.line_4 = QFrame(self.frame_19)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"\n"
"background-color: rgb(210, 96, 42);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_32.addWidget(self.line_4)

        self.scrollArea_2 = QScrollArea(self.frame_19)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 216, 37))
        self.verticalLayout_34 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.phones = QLabel(self.scrollAreaWidgetContents_2)
        self.phones.setObjectName(u"phones")
        self.phones.setAlignment(Qt.AlignCenter)
        self.phones.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.phones)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_32.addWidget(self.scrollArea_2)


        self.verticalLayout_29.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.email_scrapper_results_page)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_18)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_3 = QLabel(self.frame_18)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setMinimumSize(QSize(33, 24))
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_3)

        self.line_3 = QFrame(self.frame_18)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"\n"
"background-color: rgb(210, 96, 42);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_3)

        self.scrollArea_3 = QScrollArea(self.frame_18)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 148, 37))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.emails = QLabel(self.scrollAreaWidgetContents_3)
        self.emails.setObjectName(u"emails")
        self.emails.setAlignment(Qt.AlignCenter)
        self.emails.setWordWrap(True)

        self.verticalLayout_35.addWidget(self.emails)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_31.addWidget(self.scrollArea_3)


        self.verticalLayout_29.addWidget(self.frame_18)

        self.mainPages.addWidget(self.email_scrapper_results_page)
        self.port_scanner_page = QWidget()
        self.port_scanner_page.setObjectName(u"port_scanner_page")
        self.verticalLayout_21 = QVBoxLayout(self.port_scanner_page)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 9)
        self.label_20 = QLabel(self.port_scanner_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_20)

        self.frame_11 = QFrame(self.port_scanner_page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setEnabled(True)
        self.frame_11.setMinimumSize(QSize(40, 40))
        self.frame_11.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.port_scan_domain = QLineEdit(self.frame_11)
        self.port_scan_domain.setObjectName(u"port_scan_domain")
        self.port_scan_domain.setMinimumSize(QSize(8, 28))
        self.port_scan_domain.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")

        self.verticalLayout_22.addWidget(self.port_scan_domain)

        self.start_port_scan_btn = QPushButton(self.frame_11)
        self.start_port_scan_btn.setObjectName(u"start_port_scan_btn")
        self.start_port_scan_btn.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.start_port_scan_btn.setIcon(icon11)
        self.start_port_scan_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_22.addWidget(self.start_port_scan_btn)


        self.verticalLayout_21.addWidget(self.frame_11)

        self.label_21 = QLabel(self.port_scanner_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_21)

        self.mainPages.addWidget(self.port_scanner_page)
        self.port_scanner_results_page = QWidget()
        self.port_scanner_results_page.setObjectName(u"port_scanner_results_page")
        self.port_scanner_results_page.setStyleSheet(u"border-radius:16px;")
        self.verticalLayout_24 = QVBoxLayout(self.port_scanner_results_page)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_13 = QFrame(self.port_scanner_results_page)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy5)
        self.frame_13.setMinimumSize(QSize(33, 34))
        font2 = QFont()
        font2.setPointSize(14)
        self.frame_13.setFont(font2)
        self.frame_13.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 16px")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_13)
        self.verticalLayout_25.setSpacing(8)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_13)
        self.label_23.setObjectName(u"label_23")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy6)
        self.label_23.setStyleSheet(u"background-color: rgb(44, 49, 60);")

        self.verticalLayout_25.addWidget(self.label_23)

        self.line = QFrame(self.frame_13)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"\n"
"background-color: rgb(210, 96, 42);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_25.addWidget(self.line)


        self.verticalLayout_24.addWidget(self.frame_13)

        self.scrollArea = QScrollArea(self.port_scanner_results_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 261, 228))
        self.verticalLayout_33 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.port_scanner_result_txt = QLabel(self.scrollAreaWidgetContents)
        self.port_scanner_result_txt.setObjectName(u"port_scanner_result_txt")

        self.verticalLayout_33.addWidget(self.port_scanner_result_txt)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_24.addWidget(self.scrollArea)

        self.mainPages.addWidget(self.port_scanner_results_page)
        self.loader_page = QWidget()
        self.loader_page.setObjectName(u"loader_page")
        self.verticalLayout_16 = QVBoxLayout(self.loader_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_20 = QFrame(self.loader_page)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_20)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.loader_label = QLabel(self.frame_20)
        self.loader_label.setObjectName(u"loader_label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.loader_label.sizePolicy().hasHeightForWidth())
        self.loader_label.setSizePolicy(sizePolicy7)
        self.loader_label.setMinimumSize(QSize(0, 0))
        self.loader_label.setMaximumSize(QSize(16777215, 16777215))
        self.loader_label.setStyleSheet(u"")
        self.loader_label.setScaledContents(True)
        self.loader_label.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.loader_label)


        self.verticalLayout_16.addWidget(self.frame_20)

        self.mainPages.addWidget(self.loader_page)
        self.wifi_cracking_page = QWidget()
        self.wifi_cracking_page.setObjectName(u"wifi_cracking_page")
        self.verticalLayout_41 = QVBoxLayout(self.wifi_cracking_page)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_22 = QFrame(self.wifi_cracking_page)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_22)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.scrollArea_4 = QScrollArea(self.frame_22)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 179, 163))
        self.verticalLayout_39 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.discovered_wifi_text = QLabel(self.scrollAreaWidgetContents_4)
        self.discovered_wifi_text.setObjectName(u"discovered_wifi_text")
        self.discovered_wifi_text.setWordWrap(True)

        self.verticalLayout_39.addWidget(self.discovered_wifi_text)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_38.addWidget(self.scrollArea_4)


        self.verticalLayout_41.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.wifi_cracking_page)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 40))
        self.frame_23.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_23)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.wifi_address_name_text_edit = QLineEdit(self.frame_23)
        self.wifi_address_name_text_edit.setObjectName(u"wifi_address_name_text_edit")

        self.verticalLayout_40.addWidget(self.wifi_address_name_text_edit)


        self.verticalLayout_41.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.wifi_cracking_page)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(90, 30))
        self.frame_25.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 14px;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.fast_wifi_button = QPushButton(self.frame_25)
        self.fast_wifi_button.setObjectName(u"fast_wifi_button")
        self.fast_wifi_button.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.fast_wifi_button)


        self.horizontalLayout_14.addWidget(self.frame_25)

        self.frame_27 = QFrame(self.frame_24)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(90, 30))
        self.frame_27.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 14px;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_27)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.intensive_wifi_button = QPushButton(self.frame_27)
        self.intensive_wifi_button.setObjectName(u"intensive_wifi_button")

        self.verticalLayout_43.addWidget(self.intensive_wifi_button)


        self.horizontalLayout_14.addWidget(self.frame_27)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(90, 30))
        self.frame_26.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 14px;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_26)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.custom_wifi_button = QPushButton(self.frame_26)
        self.custom_wifi_button.setObjectName(u"custom_wifi_button")
        self.custom_wifi_button.setStyleSheet(u"")

        self.verticalLayout_42.addWidget(self.custom_wifi_button)


        self.horizontalLayout_14.addWidget(self.frame_26)


        self.verticalLayout_41.addWidget(self.frame_24)

        self.mainPages.addWidget(self.wifi_cracking_page)
        self.wifi_cracking_results = QWidget()
        self.wifi_cracking_results.setObjectName(u"wifi_cracking_results")
        self.verticalLayout_17 = QVBoxLayout(self.wifi_cracking_results)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_21 = QFrame(self.wifi_cracking_results)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 16px")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_21)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_14 = QLabel(self.frame_21)
        self.label_14.setObjectName(u"label_14")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy8)
        self.label_14.setMinimumSize(QSize(33, 24))
        self.label_14.setMaximumSize(QSize(400, 33))
        self.label_14.setStyleSheet(u"background-color: rgb(44, 49, 60);")

        self.verticalLayout_37.addWidget(self.label_14)

        self.line_7 = QFrame(self.frame_21)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"\n"
"background-color: rgb(210, 96, 42);")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_37.addWidget(self.line_7)

        self.section_1 = QLabel(self.frame_21)
        self.section_1.setObjectName(u"section_1")

        self.verticalLayout_37.addWidget(self.section_1)

        self.line_5 = QFrame(self.frame_21)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color: rgb(210, 96, 42);")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_37.addWidget(self.line_5)

        self.section_2 = QLabel(self.frame_21)
        self.section_2.setObjectName(u"section_2")

        self.verticalLayout_37.addWidget(self.section_2)

        self.section_3 = QLabel(self.frame_21)
        self.section_3.setObjectName(u"section_3")

        self.verticalLayout_37.addWidget(self.section_3)


        self.verticalLayout_17.addWidget(self.frame_21)

        self.mainPages.addWidget(self.wifi_cracking_results)
        self.phishing_attack_page = QWidget()
        self.phishing_attack_page.setObjectName(u"phishing_attack_page")
        self.verticalLayout_44 = QVBoxLayout(self.phishing_attack_page)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.scrollArea_5 = QScrollArea(self.phishing_attack_page)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 363, 867))
        self.verticalLayout_45 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.frame_43 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_43)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_44)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_29 = QLabel(self.frame_44)
        self.label_29.setObjectName(u"label_29")
        sizePolicy6.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy6)
        self.label_29.setStyleSheet(u"")

        self.verticalLayout_54.addWidget(self.label_29)

        self.line_11 = QFrame(self.frame_44)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"\n"
"background-color: rgb(210, 96, 42);")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_54.addWidget(self.line_11)


        self.verticalLayout_53.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_43)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_30 = QLabel(self.frame_45)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_20.addWidget(self.label_30)

        self.email_field = QLineEdit(self.frame_45)
        self.email_field.setObjectName(u"email_field")
        self.email_field.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")

        self.horizontalLayout_20.addWidget(self.email_field)


        self.verticalLayout_53.addWidget(self.frame_45)

        self.lineEdit_4 = QLineEdit(self.frame_43)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_53.addWidget(self.lineEdit_4)

        self.frame_46 = QFrame(self.frame_43)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_31 = QLabel(self.frame_46)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_21.addWidget(self.label_31)

        self.password_field = QLineEdit(self.frame_46)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")

        self.horizontalLayout_21.addWidget(self.password_field)


        self.verticalLayout_53.addWidget(self.frame_46)


        self.verticalLayout_45.addWidget(self.frame_43)

        self.frame_38 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_38)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_39)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_27 = QLabel(self.frame_39)
        self.label_27.setObjectName(u"label_27")
        sizePolicy6.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy6)
        self.label_27.setStyleSheet(u"")

        self.verticalLayout_51.addWidget(self.label_27)

        self.line_10 = QFrame(self.frame_39)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"\n"
"background-color: rgb(210, 96, 42);")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_51.addWidget(self.line_10)


        self.verticalLayout_50.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_40)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_24 = QLabel(self.frame_40)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_52.addWidget(self.label_24)

        self.body_text_edit = QTextEdit(self.frame_40)
        self.body_text_edit.setObjectName(u"body_text_edit")
        self.body_text_edit.setStyleSheet(u"")

        self.verticalLayout_52.addWidget(self.body_text_edit)


        self.verticalLayout_50.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_38)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_28 = QLabel(self.frame_41)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_19.addWidget(self.label_28)

        self.subject_line_edit = QLineEdit(self.frame_41)
        self.subject_line_edit.setObjectName(u"subject_line_edit")

        self.horizontalLayout_19.addWidget(self.subject_line_edit)


        self.verticalLayout_50.addWidget(self.frame_41)


        self.verticalLayout_45.addWidget(self.frame_38)

        self.frame_42 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_42)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_48 = QFrame(self.frame_42)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_48)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_32 = QLabel(self.frame_48)
        self.label_32.setObjectName(u"label_32")
        sizePolicy6.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy6)
        self.label_32.setStyleSheet(u"")

        self.verticalLayout_55.addWidget(self.label_32)

        self.line_12 = QFrame(self.frame_48)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setStyleSheet(u"\n"
"background-color: rgb(210, 96, 42);")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_55.addWidget(self.line_12)


        self.verticalLayout_46.addWidget(self.frame_48)

        self.frame_28 = QFrame(self.frame_42)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_49 = QFrame(self.frame_28)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_33 = QLabel(self.frame_49)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_22.addWidget(self.label_33)

        self.to_line_edit = QLineEdit(self.frame_49)
        self.to_line_edit.setObjectName(u"to_line_edit")

        self.horizontalLayout_22.addWidget(self.to_line_edit)


        self.horizontalLayout_16.addWidget(self.frame_49)

        self.label_12 = QLabel(self.frame_28)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.openAddFileEmailMenuBtn = QPushButton(self.frame_28)
        self.openAddFileEmailMenuBtn.setObjectName(u"openAddFileEmailMenuBtn")
        icon12 = QIcon()
        icon12.addFile(u"Icons/paperclip-portocaliu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openAddFileEmailMenuBtn.setIcon(icon12)
        self.openAddFileEmailMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.openAddFileEmailMenuBtn)


        self.verticalLayout_46.addWidget(self.frame_28)

        self.label_13 = QLabel(self.frame_42)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setWordWrap(True)

        self.verticalLayout_46.addWidget(self.label_13)


        self.verticalLayout_45.addWidget(self.frame_42)

        self.frame_47 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_47)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_50 = QFrame(self.frame_47)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_50)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_34 = QLabel(self.frame_50)
        self.label_34.setObjectName(u"label_34")
        sizePolicy6.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy6)
        self.label_34.setStyleSheet(u"")

        self.verticalLayout_56.addWidget(self.label_34)

        self.line_13 = QFrame(self.frame_50)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setStyleSheet(u"\n"
"background-color: rgb(210, 96, 42);")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_56.addWidget(self.line_13)


        self.verticalLayout_47.addWidget(self.frame_50)

        self.frame_31 = QFrame(self.frame_47)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_33)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.option64BitBtn = QPushButton(self.frame_33)
        self.option64BitBtn.setObjectName(u"option64BitBtn")

        self.verticalLayout_49.addWidget(self.option64BitBtn)


        self.horizontalLayout_17.addWidget(self.frame_33)

        self.line_6 = QFrame(self.frame_31)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background-color: rgb(210, 96, 42);")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.line_6)

        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_32)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.option32BitBtn = QPushButton(self.frame_32)
        self.option32BitBtn.setObjectName(u"option32BitBtn")

        self.verticalLayout_48.addWidget(self.option32BitBtn)


        self.horizontalLayout_17.addWidget(self.frame_32)


        self.verticalLayout_47.addWidget(self.frame_31)


        self.verticalLayout_45.addWidget(self.frame_47)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_44.addWidget(self.scrollArea_5)

        self.mainPages.addWidget(self.phishing_attack_page)
        self.phishing_attack_results_page = QWidget()
        self.phishing_attack_results_page.setObjectName(u"phishing_attack_results_page")
        self.verticalLayout_57 = QVBoxLayout(self.phishing_attack_results_page)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.frame_36 = QFrame(self.phishing_attack_results_page)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_36)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.scrollArea_7 = QScrollArea(self.frame_36)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 149, 55))
        self.verticalLayout_64 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.output_email_send = QLabel(self.scrollAreaWidgetContents_7)
        self.output_email_send.setObjectName(u"output_email_send")
        self.output_email_send.setWordWrap(True)

        self.verticalLayout_64.addWidget(self.output_email_send)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_65.addWidget(self.scrollArea_7)


        self.verticalLayout_57.addWidget(self.frame_36)

        self.line_8 = QFrame(self.phishing_attack_results_page)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"background-color: rgb(210, 96, 42);")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_57.addWidget(self.line_8)

        self.label_19 = QLabel(self.phishing_attack_results_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(True)

        self.verticalLayout_57.addWidget(self.label_19)

        self.line_9 = QFrame(self.phishing_attack_results_page)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"background-color: rgb(210, 96, 42);")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_57.addWidget(self.line_9)

        self.frame_29 = QFrame(self.phishing_attack_results_page)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy9)
        self.frame_29.setMinimumSize(QSize(30, 30))
        self.frame_29.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 14px;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_29)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.openTerminalButton = QPushButton(self.frame_29)
        self.openTerminalButton.setObjectName(u"openTerminalButton")
        sizePolicy9.setHeightForWidth(self.openTerminalButton.sizePolicy().hasHeightForWidth())
        self.openTerminalButton.setSizePolicy(sizePolicy9)
        self.openTerminalButton.setIcon(icon1)
        self.openTerminalButton.setIconSize(QSize(32, 32))

        self.verticalLayout_58.addWidget(self.openTerminalButton)


        self.verticalLayout_57.addWidget(self.frame_29, 0, Qt.AlignHCenter)

        self.mainPages.addWidget(self.phishing_attack_results_page)
        self.welcomePage = QWidget()
        self.welcomePage.setObjectName(u"welcomePage")
        self.verticalLayout_59 = QVBoxLayout(self.welcomePage)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.frame_30 = QFrame(self.welcomePage)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy10)
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_51 = QFrame(self.frame_30)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_51)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_35 = QLabel(self.frame_51)
        self.label_35.setObjectName(u"label_35")
        sizePolicy6.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy6)
        self.label_35.setStyleSheet(u"")

        self.verticalLayout_60.addWidget(self.label_35)

        self.line_14 = QFrame(self.frame_51)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setStyleSheet(u"\n"
"background-color: rgb(210, 96, 42);")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_60.addWidget(self.line_14)


        self.horizontalLayout_18.addWidget(self.frame_51)


        self.verticalLayout_59.addWidget(self.frame_30)

        self.scrollArea_6 = QScrollArea(self.welcomePage)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 128, 1044))
        self.verticalLayout_63 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.frame_34 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_34)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_25 = QLabel(self.frame_34)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setWordWrap(True)

        self.verticalLayout_62.addWidget(self.label_25)


        self.verticalLayout_63.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"background-color:#D2602A;\n"
"border-radius:16px;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_35)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_35)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(200, 200))
        self.label_22.setFrameShadow(QFrame.Plain)
        self.label_22.setLineWidth(0)
        self.label_22.setPixmap(QPixmap(u":/Icons/Icons/logo2.jpg"))
        self.label_22.setScaledContents(True)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_22.setWordWrap(True)

        self.verticalLayout_61.addWidget(self.label_22, 0, Qt.AlignHCenter)


        self.verticalLayout_63.addWidget(self.frame_35)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_59.addWidget(self.scrollArea_6)

        self.mainPages.addWidget(self.welcomePage)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMaximumSize(QSize(200, 416))
        self.rightMenuContainer.setStyleSheet(u"background-color:#1f232a;\n"
"border-radius:4px;")
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(8, 8, 8, 8)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMaximumSize(QSize(200, 16777215))
        self.rightMenuSubContainer.setStyleSheet(u"background-color:#2c313c;")
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(8, 8, 8, 8)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color:#1f232a;\n"
"border-radius:16px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        icon13 = QIcon()
        icon13.addFile(u"Icons/x-circle-portocaliu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeRightMenuBtn.setIcon(icon13)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.addAFilePages = QStackedWidget(self.rightMenuSubContainer)
        self.addAFilePages.setObjectName(u"addAFilePages")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFont(font3)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.browse_file_1 = QPushButton(self.page_4)
        self.browse_file_1.setObjectName(u"browse_file_1")
        self.browse_file_1.setIcon(icon12)
        self.browse_file_1.setIconSize(QSize(24, 24))

        self.verticalLayout_13.addWidget(self.browse_file_1)

        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setIndent(0)

        self.verticalLayout_13.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.addAFilePages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_9)

        self.browse_file_2 = QPushButton(self.page_5)
        self.browse_file_2.setObjectName(u"browse_file_2")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(44, 49, 60, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.browse_file_2.setPalette(palette)
        self.browse_file_2.setIcon(icon12)
        self.browse_file_2.setIconSize(QSize(24, 24))

        self.verticalLayout_14.addWidget(self.browse_file_2)

        self.addAFilePages.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.addAFilePages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupContainer.setObjectName(u"popupContainer")
        self.popupContainer.setMinimumSize(QSize(0, 40))
        self.popupContainer.setStyleSheet(u"background-color:#1f232a;")
        self.verticalLayout_19 = QVBoxLayout(self.popupContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.popupSubContainer = QWidget(self.popupContainer)
        self.popupSubContainer.setObjectName(u"popupSubContainer")
        self.popupSubContainer.setMinimumSize(QSize(0, 40))
        self.popupSubContainer.setStyleSheet(u"border-radius:16px;")
        self.verticalLayout_20 = QVBoxLayout(self.popupSubContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_15 = QLabel(self.popupSubContainer)
        self.label_15.setObjectName(u"label_15")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_15.setFont(font4)

        self.verticalLayout_20.addWidget(self.label_15)

        self.frame_9 = QFrame(self.popupSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color:#2c313c;\n"
"border-radius:16px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.popup_txt = QLabel(self.frame_9)
        self.popup_txt.setObjectName(u"popup_txt")
        sizePolicy1.setHeightForWidth(self.popup_txt.sizePolicy().hasHeightForWidth())
        self.popup_txt.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setPointSize(10)
        self.popup_txt.setFont(font5)
        self.popup_txt.setAlignment(Qt.AlignCenter)
        self.popup_txt.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.popup_txt)

        self.closePopupBtn = QPushButton(self.frame_9)
        self.closePopupBtn.setObjectName(u"closePopupBtn")
        icon14 = QIcon()
        icon14.addFile(u"Icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closePopupBtn.setIcon(icon14)
        self.closePopupBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closePopupBtn, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.frame_9)


        self.verticalLayout_19.addWidget(self.popupSubContainer)


        self.verticalLayout_10.addWidget(self.popupContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.footerContainer.setEnabled(True)
        self.footerContainer.setMinimumSize(QSize(0, 48))
        self.footerContainer.setMaximumSize(QSize(16777215, 16777215))
        self.footerContainer.setStyleSheet(u"background-color:#2c313c;")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(8, 0, 8, 0)
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_12.addWidget(self.label_16)


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        sizePolicy.setHeightForWidth(self.sizeGrip.sizePolicy().hasHeightForWidth())
        self.sizeGrip.setSizePolicy(sizePolicy)
        self.sizeGrip.setMinimumSize(QSize(24, 24))
        self.sizeGrip.setMaximumSize(QSize(24, 24))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.sizeGrip)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.infoGatheringBtn.setDefault(False)
        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(7)
        self.addAFilePages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.infoGatheringBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Info Gathering", None))
#endif // QT_CONFIG(tooltip)
        self.infoGatheringBtn.setText(QCoreApplication.translate("MainWindow", u"Info Gathering", None))
#if QT_CONFIG(tooltip)
        self.wifiCrackingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Wi-Fi Cracking", None))
#endif // QT_CONFIG(tooltip)
        self.wifiCrackingBtn.setText(QCoreApplication.translate("MainWindow", u"WI-FI Cracking", None))
#if QT_CONFIG(tooltip)
        self.attacksMenu.setToolTip(QCoreApplication.translate("MainWindow", u"Phising Attack", None))
#endif // QT_CONFIG(tooltip)
        self.attacksMenu.setText(QCoreApplication.translate("MainWindow", u"Attacks", None))
#if QT_CONFIG(tooltip)
        self.exitBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.exitBtn.setText("")
        self.port_scanner_goto.setText(QCoreApplication.translate("MainWindow", u"Port Scanner", None))
        self.email_scraper_goto.setText(QCoreApplication.translate("MainWindow", u"Email Scraper", None))
        self.fhishing_goto.setText(QCoreApplication.translate("MainWindow", u"Phishing Attack", None))
        self.dictionary_wifi_goto.setText(QCoreApplication.translate("MainWindow", u"Dictionary Attack", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Detailed Options", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dream Catcher", None))
#if QT_CONFIG(tooltip)
        self.addFileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Open Attach a File Menu", None))
#endif // QT_CONFIG(tooltip)
        self.addFileBtn.setText("")
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Info", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText("")
#if QT_CONFIG(tooltip)
        self.frame_7.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Full Screen", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Please input the domain you want to crawl for emails", None))
        self.address_edit_email_scrapper.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input the address....", None))
        self.email_scrapper_button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Once you entered the email, the program will begin to crawl the website, the results will be saved in the files and shown below", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email Scrapper Results", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#d2602a;\">Phone numbers</span></p></body></html>", None))
        self.phones.setText(QCoreApplication.translate("MainWindow", u"phone_Numbers_placeholder", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#d2602a;\">Emails</span></p></body></html>", None))
        self.emails.setText(QCoreApplication.translate("MainWindow", u"emails_placeholder", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Enter the domain you want to be scanned", None))
        self.port_scan_domain.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input the domain...", None))
        self.start_port_scan_btn.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"The domain will be scanned using your Public Ip and a range of 10 random other ones in the same network", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Port Scanner Results</span></p></body></html>", None))
        self.port_scanner_result_txt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#d2602a;\">Port: </span><span style=\" color:#ffffff;\">placeholder_port</span></p><p><span style=\" color:#d2602a;\">Port Type: </span><span style=\" color:#ffffff;\">placeholder_port_type</span></p><p><span style=\" color:#d2602a;\">Status: </span><span style=\" color:#ffffff;\">placeholder_port_status</span></p><p><span style=\" color:#d2602a;\">Protocol: </span><span style=\" color:#ffffff;\">placeholder_port_protocol</span></p><p><span style=\" color:#d2602a;\">Product: </span><span style=\" color:#ffffff;\">placeholder_port_product</span><br/></p><p><br/></p></body></html>", None))
        self.loader_label.setText("")
        self.discovered_wifi_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Icons/Icons/chevron-left.svg\"/><img src=\":/Icons/Icons/rss.svg\"/><img src=\":/Icons/Icons/chevron-right.svg\"/><span style=\" font-size:14pt; color:#d2602a;\">Name: </span><span style=\" font-weight:600; color:#ffffff;\">placeholder_wifi_name</span></p><p><br/></p><p><br/></p></body></html>", None))
        self.wifi_address_name_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the WIFI you want to crack...", None))
        self.fast_wifi_button.setText(QCoreApplication.translate("MainWindow", u"Fast ", None))
        self.intensive_wifi_button.setText(QCoreApplication.translate("MainWindow", u"Intensive", None))
        self.custom_wifi_button.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">WIFI Cracking Results</span></p></body></html>", None))
        self.section_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#d2602a;\">Result: </span><span style=\" color:#ffffff;\">placeholder_result</span></p><p><span style=\" color:#d2602a;\">Number of tries: </span><span style=\" color:#ffffff;\">placeholder_no_tries</span></p><p><span style=\" color:#d2602a;\">Time elapsed: </span><span style=\" color:#ffffff;\">placeholder_time_elapsed</span></p><p><br/></p></body></html>", None))
        self.section_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Icons/Icons/wifi.svg\"/><span style=\" color:#d2602a;\">WIFI Name: </span><span style=\" color:#ffffff;\">placeholder_wifi_name</span></p></body></html>", None))
        self.section_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Icons/Icons/key.svg\"/><span style=\" color:#d2602a;\">Password: </span><span style=\" color:#ffffff;\">placeholder_password</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter Credentials</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Email: ", None))
        self.email_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the email address...", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Password: ", None))
        self.password_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the password for the address...", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Contents</p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Body:", None))
        self.body_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write whatever message you want to send, at the end of it a link with the payload will be attached to infect the target", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Subject: ", None))
        self.subject_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the subject of the email...", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>To</p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"To: ", None))
        self.to_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter destination", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.openAddFileEmailMenuBtn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"You can click the paper clip button to choose a file from a previous email crawl done by the app", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Options</p></body></html>", None))
        self.option64BitBtn.setText(QCoreApplication.translate("MainWindow", u"64 bit", None))
        self.option32BitBtn.setText(QCoreApplication.translate("MainWindow", u"32 bit", None))
        self.output_email_send.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Output: <span style=\" color:#d2602a;\">output_placeholder</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>For the next steps please press the button below to open up a terminal. Then type the following command to enter via SSH on a Linode hosted machine that has the server script. Input the following command: <span style=\" color:#d2602a;\">ssh root@1ServerIPHere</span> then please type in the password: <span style=\" color:#d2602a;\">ServerPasswordHere </span><span style=\" color:#ffffff;\">. Then type in </span><span style=\" color:#d2602a;\">./server</span><span style=\" color:#ffffff;\"> to start the server and listen for incoming connections.  In case the output is not Emails were sent successfully there was an error sending emails, please correct the error in order to proceed.</span></p></body></html>", None))
        self.openTerminalButton.setText(QCoreApplication.translate("MainWindow", u"Open Terminal", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">WELCOME</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Welcome to <span style=\" color:#d2602a;\">Dream Catcher</span><span style=\" color:#ffffff;\">. This is a desktop solution made by </span><span style=\" color:#d2602a;\">Secioreanu Ionel Stefanita</span><span style=\" color:#ffffff;\">. This project was developed as a final project for faculty and it is still in development. The following steps describe what an expected flow lokks like. </span><span style=\" color:#d2602a;\">Happy hunting!</span></p><p><span style=\" color:#d2602a;\">FLOW:</span></p><p><span style=\" color:#d2602a;\">1. Scan WIFI Networks and crack one</span></p><p><span style=\" color:#d2602a;\">2. Scan the ports of the target website</span></p><p><span style=\" color:#d2602a;\">3.Scan the website for emails and phone numbers</span></p><p><span style=\" color:#d2602a;\">4.Cast the bait with the email phishing attack and follow the steps on the screen to connect to an infected machine via a Reverse Shell script.</span></p></body></html>", None))
        self.label_22.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Add a file", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Add a file from your computer to act as a dictonary for the attack", None))
#if QT_CONFIG(tooltip)
        self.browse_file_1.setToolTip(QCoreApplication.translate("MainWindow", u"Attach a file", None))
#endif // QT_CONFIG(tooltip)
        self.browse_file_1.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Or leave it blank and use the app pre-made dictionaries", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Add a file from your computer to act as the email list for the phishing attack. Please paste the file outputed by the program found in the Dream_Catcher folder", None))
        self.browse_file_2.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Info Message", None))
        self.popup_txt.setText(QCoreApplication.translate("MainWindow", u"This applications was made by Secioreanu Ionel Stefanita as a final project", None))
#if QT_CONFIG(tooltip)
        self.closePopupBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Popup", None))
#endif // QT_CONFIG(tooltip)
        self.closePopupBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Copyright Secioreanu Ionel Stefanita", None))
    # retranslateUi

