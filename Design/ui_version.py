# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_version.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)
import IMAGE.icon_rc

class Ui_QVersion(object):
    def setupUi(self, QVersion):
        if not QVersion.objectName():
            QVersion.setObjectName(u"QVersion")
        QVersion.resize(400, 200)
        QVersion.setMinimumSize(QSize(400, 200))
        QVersion.setMaximumSize(QSize(400, 200))
        icon = QIcon()
        icon.addFile(u":/programlogo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        QVersion.setWindowIcon(icon)
        QVersion.setWindowOpacity(1.000000000000000)
        QVersion.setStyleSheet(u"")
        self.label = QLabel(QVersion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-5, 25, 150, 150))
        self.label.setMinimumSize(QSize(140, 140))
        self.label.setPixmap(QPixmap(u":/LASMASTER.png"))
        self.label.setScaledContents(True)
        self.label.setMargin(-60)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_2 = QLabel(QVersion)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(171, 26, 89, 26))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_5 = QLabel(QVersion)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(171, 82, 223, 32))
        font1 = QFont()
        font1.setWeight(QFont.Medium)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_5.setFont(font1)
        self.label_5.setTabletTracking(False)
        self.label_5.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_6 = QLabel(QVersion)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(170, 140, 181, 26))
        self.label_6.setWordWrap(False)
        self.layoutWidget = QWidget(QVersion)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(171, 58, 120, 18))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(63, 15))

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)


        self.retranslateUi(QVersion)

        QMetaObject.connectSlotsByName(QVersion)
    # setupUi

    def retranslateUi(self, QVersion):
        QVersion.setWindowTitle(QCoreApplication.translate("QVersion", u"\u0412\u0435\u0440\u0441\u0438\u044f \u041f\u041e", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("QVersion", u"LasMaster", None))
        self.label_5.setText(QCoreApplication.translate("QVersion", u"LasMaster-\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0434\u043b\u044f \u0438\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u0438 \u0434\u0430\u043d\u043d\u044b\u0445 \u043a\u0430\u0440\u043e\u0442\u0430\u0436\u0430", None))
        self.label_6.setText(QCoreApplication.translate("QVersion", u"Copyright \u00a9 2024 \u00abLasMaster\u00bb", None))
        self.label_3.setText(QCoreApplication.translate("QVersion", u"\u0412\u0435\u0440\u0441\u0438\u044f \u041f\u041e: ", None))
        self.label_4.setText(QCoreApplication.translate("QVersion", u"Alpha 0.1", None))
    # retranslateUi

