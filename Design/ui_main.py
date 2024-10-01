# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LasMaster.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableView, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import IMAGE.icon_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(461, 550)
        mainWindow.setMinimumSize(QSize(461, 424))
        icon = QIcon()
        icon.addFile(u":/programlogo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        self.open_p = QAction(mainWindow)
        self.open_p.setObjectName(u"open_p")
        self.open_p.setCheckable(False)
        icon1 = QIcon()
        icon1.addFile(u":/Open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_p.setIcon(icon1)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.open_p.setFont(font)
        self.save_p = QAction(mainWindow)
        self.save_p.setObjectName(u"save_p")
        icon2 = QIcon()
        icon2.addFile(u":/Save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_p.setIcon(icon2)
        self.save_p.setFont(font)
        self.close_p = QAction(mainWindow)
        self.close_p.setObjectName(u"close_p")
        icon3 = QIcon()
        icon3.addFile(u":/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_p.setIcon(icon3)
        self.close_p.setFont(font)
        self.import_p = QAction(mainWindow)
        self.import_p.setObjectName(u"import_p")
        icon4 = QIcon()
        icon4.addFile(u":/import.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.import_p.setIcon(icon4)
        self.import_p.setFont(font)
        self.export_p = QAction(mainWindow)
        self.export_p.setObjectName(u"export_p")
        icon5 = QIcon()
        icon5.addFile(u":/export.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.export_p.setIcon(icon5)
        self.export_p.setFont(font)
        self.save_as_p = QAction(mainWindow)
        self.save_as_p.setObjectName(u"save_as_p")
        icon6 = QIcon()
        icon6.addFile(u":/save_as.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_as_p.setIcon(icon6)
        self.save_as_p.setFont(font)
        self.create_p = QAction(mainWindow)
        self.create_p.setObjectName(u"create_p")
        icon7 = QIcon()
        icon7.addFile(u":/Create.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.create_p.setIcon(icon7)
        self.create_p.setFont(font)
        self.version_p = QAction(mainWindow)
        self.version_p.setObjectName(u"version_p")
        self.version_p.setCheckable(False)
        self.version_p.setChecked(False)
        icon8 = QIcon()
        icon8.addFile(u":/version.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.version_p.setIcon(icon8)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.version_p.setFont(font1)
        self.version_p.setVisible(True)
        self.version_p.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.guide = QAction(mainWindow)
        self.guide.setObjectName(u"guide")
        icon9 = QIcon()
        icon9.addFile(u":/Guide.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.guide.setIcon(icon9)
        self.guide.setFont(font1)
        self.horizont = QAction(mainWindow)
        self.horizont.setObjectName(u"horizont")
        icon10 = QIcon()
        icon10.addFile(u":/X.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.horizont.setIcon(icon10)
        self.vertical = QAction(mainWindow)
        self.vertical.setObjectName(u"vertical")
        icon11 = QIcon()
        icon11.addFile(u":/Y.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.vertical.setIcon(icon11)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(300, 300))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.tabWidget.setFont(font2)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideRight)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qb_method = QComboBox(self.tab)
        self.qb_method.addItem("")
        self.qb_method.setObjectName(u"qb_method")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.qb_method.sizePolicy().hasHeightForWidth())
        self.qb_method.setSizePolicy(sizePolicy1)
        self.qb_method.setMinimumSize(QSize(208, 30))
        self.qb_method.setMaximumSize(QSize(248, 30))
        self.qb_method.setStyleSheet(u"QComboBox {\n"
"    border-radius: 3px;\n"
"	background-color:rgb(213, 232, 255)\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: rgb(85, 170, 255);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgb(170, 170, 255);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: rgb(78, 119, 255);\n"
"}")
        self.qb_method.setDuplicatesEnabled(False)
        self.qb_method.setModelColumn(0)

        self.horizontalLayout_2.addWidget(self.qb_method, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.pb_setting_meth = QPushButton(self.tab)
        self.pb_setting_meth.setObjectName(u"pb_setting_meth")
        sizePolicy1.setHeightForWidth(self.pb_setting_meth.sizePolicy().hasHeightForWidth())
        self.pb_setting_meth.setSizePolicy(sizePolicy1)
        self.pb_setting_meth.setMinimumSize(QSize(200, 30))
        self.pb_setting_meth.setMaximumSize(QSize(200, 30))
        self.pb_setting_meth.setStyleSheet(u"QPushButton {\n"
"  border-radius: 8px;\n"
"  outline: 0px;\n"
"  background-color:rgb(213, 232, 255);\n"
"  border: 1px solid rgb(0, 170, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(240, 240, 240);\n"
"  border: 2px solid rgb(0, 85, 255);\n"
" }\n"
"QPushButton:hover {\n"
"  background-color:rgba(213, 232, 255, 150);\n"
" }")

        self.horizontalLayout_2.addWidget(self.pb_setting_meth, 0, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.pb_import_las = QPushButton(self.tab)
        self.pb_import_las.setObjectName(u"pb_import_las")
        self.pb_import_las.setMinimumSize(QSize(123, 30))
        self.pb_import_las.setMaximumSize(QSize(145, 30))
        self.pb_import_las.setStyleSheet(u"QPushButton {\n"
"  border-radius: 8px;\n"
"  outline: 0px;\n"
"  background-color:rgb(213, 232, 255);\n"
"  border: 1px solid rgb(0, 170, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(240, 240, 240);\n"
"  border: 2px solid rgb(0, 85, 255);\n"
" }\n"
"QPushButton:hover {\n"
"  background-color:rgba(213, 232, 255, 150);\n"
" }")

        self.horizontalLayout.addWidget(self.pb_import_las, 0, Qt.AlignmentFlag.AlignLeft)

        self.qb_curves = QComboBox(self.tab)
        self.qb_curves.setObjectName(u"qb_curves")
        self.qb_curves.setMinimumSize(QSize(150, 30))
        self.qb_curves.setMaximumSize(QSize(150, 30))
        self.qb_curves.setStyleSheet(u"QComboBox {\n"
"    border-radius: 3px;\n"
"	background-color:rgb(213, 232, 255)\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: rgb(85, 170, 255);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgb(170, 170, 255);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: rgb(78, 119, 255);\n"
"}")
        self.qb_curves.setFrame(False)
        self.qb_curves.setModelColumn(0)

        self.horizontalLayout.addWidget(self.qb_curves, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.pb_add_curve = QPushButton(self.tab)
        self.pb_add_curve.setObjectName(u"pb_add_curve")
        self.pb_add_curve.setMinimumSize(QSize(122, 30))
        self.pb_add_curve.setMaximumSize(QSize(145, 30))
        self.pb_add_curve.setSizeIncrement(QSize(0, 0))
        self.pb_add_curve.setStyleSheet(u"QPushButton {\n"
"  border-radius: 8px;\n"
"  outline: 0px;\n"
"  background-color:rgb(213, 232, 255);\n"
"  border: 1px solid rgb(0, 170, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(240, 240, 240);\n"
"  border: 2px solid rgb(0, 85, 255);\n"
" }\n"
"QPushButton:hover {\n"
"  background-color:rgba(213, 232, 255, 150);\n"
" }")

        self.horizontalLayout.addWidget(self.pb_add_curve, 0, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.tw_curves = QTreeWidget(self.tab)
        self.tw_curves.setObjectName(u"tw_curves")
        self.tw_curves.setAnimated(False)
        self.tw_curves.setColumnCount(2)
        self.tw_curves.header().setCascadingSectionResizes(False)
        self.tw_curves.header().setMinimumSectionSize(40)
        self.tw_curves.header().setHighlightSections(False)
        self.tw_curves.header().setProperty("showSortIndicator", False)

        self.verticalLayout.addWidget(self.tw_curves)

        self.pb_delete = QPushButton(self.tab)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setMinimumSize(QSize(100, 30))
        self.pb_delete.setStyleSheet(u"QPushButton {\n"
"  border-radius: 8px;\n"
"  outline: 0px;\n"
"  background-color:rgb(213, 232, 255);\n"
"  border: 1px solid rgb(0, 170, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(240, 240, 240);\n"
"  border: 2px solid rgb(0, 85, 255);\n"
" }\n"
"QPushButton:hover {\n"
"  background-color:rgba(213, 232, 255, 150);\n"
" }")

        self.verticalLayout.addWidget(self.pb_delete, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pb_build = QPushButton(self.tab)
        self.pb_build.setObjectName(u"pb_build")
        self.pb_build.setMinimumSize(QSize(100, 30))
        self.pb_build.setMaximumSize(QSize(150, 30))
        self.pb_build.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pb_build.setStyleSheet(u"QPushButton {\n"
"  border-radius: 8px;\n"
"  outline: 0px;\n"
"  background-color:rgb(213, 232, 255);\n"
"  border: 1px solid rgb(0, 170, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(240, 240, 240);\n"
"  border: 2px solid rgb(0, 85, 255);\n"
" }\n"
"QPushButton:hover {\n"
"  background-color:rgba(213, 232, 255, 150);\n"
" }")

        self.verticalLayout.addWidget(self.pb_build, 0, Qt.AlignmentFlag.AlignRight)

        self.tabWidget.addTab(self.tab, "")
        self.interpretator = QWidget()
        self.interpretator.setObjectName(u"interpretator")
        self.interpretator.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.interpretator)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.qw_interpret = QWidget(self.interpretator)
        self.qw_interpret.setObjectName(u"qw_interpret")

        self.verticalLayout_2.addWidget(self.qw_interpret)

        self.tabWidget.addTab(self.interpretator, "")
        self.out_info = QWidget()
        self.out_info.setObjectName(u"out_info")
        self.gridLayout_3 = QGridLayout(self.out_info)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pb_excel = QPushButton(self.out_info)
        self.pb_excel.setObjectName(u"pb_excel")
        self.pb_excel.setStyleSheet(u"QPushButton {\n"
"  border-radius: 8px;\n"
"  outline: 0px;\n"
"  background-color:rgb(213, 232, 255);\n"
"  border: 1px solid rgb(0, 170, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(240, 240, 240);\n"
"  border: 2px solid rgb(0, 85, 255);\n"
" }\n"
"QPushButton:hover {\n"
"  background-color:rgba(213, 232, 255, 150);\n"
" }")

        self.gridLayout_3.addWidget(self.pb_excel, 1, 0, 1, 1)

        self.qv_table_status = QTableView(self.out_info)
        self.qv_table_status.setObjectName(u"qv_table_status")

        self.gridLayout_3.addWidget(self.qv_table_status, 0, 0, 1, 1)

        self.tabWidget.addTab(self.out_info, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(mainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 461, 23))
        font3 = QFont()
        font3.setPointSize(10)
        self.menuBar.setFont(font3)
        self.help = QMenu(self.menuBar)
        self.help.setObjectName(u"help")
        self.file = QMenu(self.menuBar)
        self.file.setObjectName(u"file")
        self.tools = QMenu(self.menuBar)
        self.tools.setObjectName(u"tools")
        self.scale_2 = QMenu(self.tools)
        self.scale_2.setObjectName(u"scale_2")
        icon12 = QIcon()
        icon12.addFile(u":/scale.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.scale_2.setIcon(icon12)
        mainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.file.menuAction())
        self.menuBar.addAction(self.tools.menuAction())
        self.menuBar.addAction(self.help.menuAction())
        self.help.addAction(self.version_p)
        self.help.addAction(self.guide)
        self.file.addAction(self.open_p)
        self.file.addAction(self.create_p)
        self.file.addSeparator()
        self.file.addAction(self.save_p)
        self.file.addAction(self.save_as_p)
        self.file.addAction(self.close_p)
        self.file.addSeparator()
        self.file.addAction(self.import_p)
        self.file.addAction(self.export_p)
        self.tools.addAction(self.scale_2.menuAction())
        self.scale_2.addAction(self.horizont)
        self.scale_2.addAction(self.vertical)

        self.retranslateUi(mainWindow)
        self.pb_import_las.clicked.connect(self.import_p.trigger)
        self.pb_delete.clicked.connect(self.tw_curves.clear)

        self.tabWidget.setCurrentIndex(0)
        self.qb_method.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"LasMaster", None))
        self.open_p.setText(QCoreApplication.translate("mainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
#if QT_CONFIG(shortcut)
        self.open_p.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.save_p.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
#if QT_CONFIG(shortcut)
        self.save_p.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.close_p.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443", None))
#if QT_CONFIG(shortcut)
        self.close_p.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.import_p.setText(QCoreApplication.translate("mainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0444\u0430\u0439\u043b\u0430", None))
#if QT_CONFIG(shortcut)
        self.import_p.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.export_p.setText(QCoreApplication.translate("mainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0444\u0430\u0439\u043b\u0430", None))
#if QT_CONFIG(shortcut)
        self.export_p.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.save_as_p.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
#if QT_CONFIG(shortcut)
        self.save_as_p.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.create_p.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
#if QT_CONFIG(shortcut)
        self.create_p.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.version_p.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f \u041f\u041e", None))
        self.guide.setText(QCoreApplication.translate("mainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.horizont.setText(QCoreApplication.translate("mainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431 \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0439", None))
        self.vertical.setText(QCoreApplication.translate("mainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439", None))
        self.qb_method.setItemText(0, QCoreApplication.translate("mainWindow", u"\u0410\u0432\u0442\u043e \u0418\u0442\u0435\u0440\u043f\u0435\u0440\u0430\u0442\u0438\u0446\u0438\u044f \u043f\u043e \u0413\u041a \u0438 \u042f\u041c\u041a", None))

        self.qb_method.setCurrentText("")
        self.qb_method.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043c\u0435\u0442\u043e\u0434\u0430 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u0438", None))
        self.pb_setting_meth.setText(QCoreApplication.translate("mainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043c\u0435\u0442\u043e\u0434\u0430", None))
        self.pb_import_las.setText(QCoreApplication.translate("mainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 LAS", None))
        self.qb_curves.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043a\u0440\u0438\u0432\u043e\u0439", None))
        self.pb_add_curve.setText(QCoreApplication.translate("mainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0440\u0438\u0432\u0443\u044e", None))
        ___qtreewidgetitem = self.tw_curves.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("mainWindow", u"\u041a\u0440\u0438\u0432\u0430\u044f", None));
        self.pb_delete.setText(QCoreApplication.translate("mainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u0440\u0438\u0432\u044b\u0435", None))
        self.pb_build.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"\u0412\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.interpretator), QCoreApplication.translate("mainWindow", u"\u041f\u043b\u0430\u043d\u0448\u0435\u0442", None))
        self.pb_excel.setText(QCoreApplication.translate("mainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 Excel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.out_info), QCoreApplication.translate("mainWindow", u"\u0412\u044b\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.help.setTitle(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.file.setTitle(QCoreApplication.translate("mainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.tools.setTitle(QCoreApplication.translate("mainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.scale_2.setTitle(QCoreApplication.translate("mainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431", None))
    # retranslateUi

