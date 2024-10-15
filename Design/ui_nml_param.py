# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_nml_param.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import IMAGE.icon_rc

class Ui_Nml_param(object):
    def setupUi(self, Nml_param):
        if not Nml_param.objectName():
            Nml_param.setObjectName(u"Nml_param")
        Nml_param.resize(406, 369)
        icon = QIcon()
        icon.addFile(u":/programlogo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Nml_param.setWindowIcon(icon)
        Nml_param.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        Nml_param.setSizeGripEnabled(False)
        Nml_param.setModal(True)
        self.gridLayout = QGridLayout(Nml_param)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Nml_param)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.ds_min = QDoubleSpinBox(Nml_param)
        self.ds_min.setObjectName(u"ds_min")
        self.ds_min.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : white;\n"
"border-radius: 8\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : rgb(170, 255, 255);\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"\n"
"subcontrol-position:right;\n"
"image: url(:/plus.svg);\n"
"\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"subcontrol-position:left;\n"
"	image: url(:/minus.svg);\n"
"}\n"
"	")
        self.ds_min.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ds_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.ds_min.setMinimum(-9999.000000000000000)
        self.ds_min.setMaximum(9999.000000000000000)
        self.ds_min.setValue(0.000000000000000)

        self.verticalLayout_2.addWidget(self.ds_min)

        self.ds_max = QDoubleSpinBox(Nml_param)
        self.ds_max.setObjectName(u"ds_max")
        self.ds_max.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : white;\n"
"border-radius: 8\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : rgb(170, 255, 255);\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"\n"
"subcontrol-position:right;\n"
"image: url(:/plus.svg);\n"
"\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"subcontrol-position:left;\n"
"	image: url(:/minus.svg);\n"
"}\n"
"	")
        self.ds_max.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ds_max.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.ds_max.setMinimum(-9999.000000000000000)
        self.ds_max.setMaximum(9999.000000000000000)

        self.verticalLayout_2.addWidget(self.ds_max)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(Nml_param)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(163, 28))
        self.label_4.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_4)

        self.pb_auto_gk = QPushButton(Nml_param)
        self.pb_auto_gk.setObjectName(u"pb_auto_gk")
        self.pb_auto_gk.setMinimumSize(QSize(70, 0))
        self.pb_auto_gk.setMaximumSize(QSize(100, 16777215))
        self.pb_auto_gk.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_4.addWidget(self.pb_auto_gk)

        self.ds_gk_min = QDoubleSpinBox(Nml_param)
        self.ds_gk_min.setObjectName(u"ds_gk_min")
        self.ds_gk_min.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : white;\n"
"border-radius: 8\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : rgb(170, 255, 255);\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"\n"
"subcontrol-position:right;\n"
"image: url(:/plus.svg);\n"
"\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"subcontrol-position:left;\n"
"	image: url(:/minus.svg);\n"
"}\n"
"	")
        self.ds_gk_min.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ds_gk_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.ds_gk_min.setMinimum(-9999.000000000000000)
        self.ds_gk_min.setMaximum(9999.000000000000000)
        self.ds_gk_min.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.verticalLayout_4.addWidget(self.ds_gk_min)

        self.ds_gk_max = QDoubleSpinBox(Nml_param)
        self.ds_gk_max.setObjectName(u"ds_gk_max")
        self.ds_gk_max.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : white;\n"
"border-radius: 8\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : rgb(170, 255, 255);\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"\n"
"subcontrol-position:right;\n"
"image: url(:/plus.svg);\n"
"\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"subcontrol-position:left;\n"
"	image: url(:/minus.svg);\n"
"}\n"
"	")
        self.ds_gk_max.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ds_gk_max.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.ds_gk_max.setMinimum(-9999.000000000000000)
        self.ds_gk_max.setMaximum(9999.000000000000000)

        self.verticalLayout_4.addWidget(self.ds_gk_max)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Nml_param)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.ds_diff_nml = QDoubleSpinBox(Nml_param)
        self.ds_diff_nml.setObjectName(u"ds_diff_nml")
        self.ds_diff_nml.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : white;\n"
"border-radius: 8\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : rgb(170, 255, 255);\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"\n"
"subcontrol-position:right;\n"
"image: url(:/plus.svg);\n"
"\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"subcontrol-position:left;\n"
"	image: url(:/minus.svg);\n"
"}\n"
"	")
        self.ds_diff_nml.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ds_diff_nml.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.ds_diff_nml.setMinimum(-9999.000000000000000)
        self.ds_diff_nml.setMaximum(9999.000000000000000)

        self.verticalLayout.addWidget(self.ds_diff_nml)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Nml_param)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label)

        self.ds_a3 = QDoubleSpinBox(Nml_param)
        self.ds_a3.setObjectName(u"ds_a3")
        self.ds_a3.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : white;\n"
"border-radius: 8\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : rgb(170, 255, 255);\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"\n"
"subcontrol-position:right;\n"
"image: url(:/plus.svg);\n"
"\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"subcontrol-position:left;\n"
"	image: url(:/minus.svg);\n"
"}\n"
"	")
        self.ds_a3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ds_a3.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.ds_a3.setMinimum(-9999.000000000000000)
        self.ds_a3.setMaximum(9999.000000000000000)

        self.verticalLayout_3.addWidget(self.ds_a3)

        self.ds_a4 = QDoubleSpinBox(Nml_param)
        self.ds_a4.setObjectName(u"ds_a4")
        self.ds_a4.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : white;\n"
"border-radius: 8\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : rgb(170, 255, 255);\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"\n"
"subcontrol-position:right;\n"
"image: url(:/plus.svg);\n"
"\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"subcontrol-position:left;\n"
"	image: url(:/minus.svg);\n"
"}")
        self.ds_a4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ds_a4.setMinimum(-99998.000000000000000)
        self.ds_a4.setMaximum(99999.000000000000000)

        self.verticalLayout_3.addWidget(self.ds_a4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Nml_param)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet(u"QPushButton {\n"
"  border-radius: 8px;\n"
"  outline: 0px;\n"
"  background-color:rgb(213, 232, 255);\n"
"  border: 1px solid rgb(0, 170, 255);\n"
"  font-size: 15px\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(240, 240, 240);\n"
"  border: 2px solid rgb(0, 85, 255);\n"
" }\n"
"QPushButton:hover {\n"
"  background-color:rgba(213, 232, 255, 150);\n"
" }\n"
"")
        self.buttonBox.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(Nml_param)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.ds_k = QDoubleSpinBox(Nml_param)
        self.ds_k.setObjectName(u"ds_k")
        self.ds_k.setMinimumSize(QSize(150, 22))
        self.ds_k.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : white;\n"
"border-radius: 8\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : rgb(170, 255, 255);\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"\n"
"subcontrol-position:right;\n"
"image: url(:/plus.svg);\n"
"\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"subcontrol-position:left;\n"
"	image: url(:/minus.svg);\n"
"}\n"
"	")
        self.ds_k.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.ds_k, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.label_6 = QLabel(Nml_param)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ds_t1 = QDoubleSpinBox(Nml_param)
        self.ds_t1.setObjectName(u"ds_t1")
        self.ds_t1.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : white;\n"
"border-radius: 8\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : rgb(170, 255, 255);\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"\n"
"subcontrol-position:right;\n"
"image: url(:/plus.svg);\n"
"\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"subcontrol-position:left;\n"
"	image: url(:/minus.svg);\n"
"}")
        self.ds_t1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ds_t1.setMaximum(7686786.000000000000000)

        self.horizontalLayout_3.addWidget(self.ds_t1)

        self.ds_t2 = QDoubleSpinBox(Nml_param)
        self.ds_t2.setObjectName(u"ds_t2")
        self.ds_t2.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : white;\n"
"border-radius: 8\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : rgb(170, 255, 255);\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"\n"
"subcontrol-position:right;\n"
"image: url(:/plus.svg);\n"
"\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"subcontrol-position:left;\n"
"	image: url(:/minus.svg);\n"
"}")
        self.ds_t2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ds_t2.setMaximum(7868768.000000000000000)

        self.horizontalLayout_3.addWidget(self.ds_t2)

        self.ds_t3 = QDoubleSpinBox(Nml_param)
        self.ds_t3.setObjectName(u"ds_t3")
        self.ds_t3.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : white;\n"
"border-radius: 8\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 2px solid rgb(0, 170, 255);\n"
"background : rgb(170, 255, 255);\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"\n"
"subcontrol-position:right;\n"
"image: url(:/plus.svg);\n"
"\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"subcontrol-position:left;\n"
"	image: url(:/minus.svg);\n"
"}")
        self.ds_t3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ds_t3.setMaximum(768768.000000000000000)

        self.horizontalLayout_3.addWidget(self.ds_t3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_6, 2, 0, 1, 1)


        self.retranslateUi(Nml_param)
        self.buttonBox.accepted.connect(Nml_param.accept)
        self.buttonBox.rejected.connect(Nml_param.reject)

        QMetaObject.connectSlotsByName(Nml_param)
    # setupUi

    def retranslateUi(self, Nml_param):
        Nml_param.setWindowTitle(QCoreApplication.translate("Nml_param", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043c\u0435\u0442\u043e\u0434\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Nml_param", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u0433\u043b\u0443\u0431\u0438\u043d \u0434\u043b\u044f \u043e\u043f\u043e\u0440\u043d\u044b\u0445 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439", None))
        self.ds_min.setPrefix(QCoreApplication.translate("Nml_param", u"\u041e\u0442 ", None))
        self.ds_min.setSuffix(QCoreApplication.translate("Nml_param", u" \u043c", None))
        self.ds_max.setPrefix(QCoreApplication.translate("Nml_param", u"\u0414\u043e ", None))
        self.ds_max.setSuffix(QCoreApplication.translate("Nml_param", u" \u043c", None))
        self.label_4.setText(QCoreApplication.translate("Nml_param", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0413\u041a \u0434\u043b\u044f \u0434\u0432\u043e\u0439\u043d\u043e\u0433\u043e \u0440\u0430\u0437\u043d\u043e\u0441\u0442\u043d\u043e\u0433\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.pb_auto_gk.setText(QCoreApplication.translate("Nml_param", u"\u0410\u0432\u0442\u043e ", None))
        self.ds_gk_min.setSuffix(QCoreApplication.translate("Nml_param", u" ur/h min ", None))
        self.ds_gk_max.setPrefix("")
        self.ds_gk_max.setSuffix(QCoreApplication.translate("Nml_param", u" ur/h max", None))
        self.label_3.setText(QCoreApplication.translate("Nml_param", u"\u0420\u0430\u0441\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043a\u0440\u0438\u0432\u044b\u0445 \u042f\u041c\u041a \u0432 %", None))
        self.ds_diff_nml.setPrefix("")
        self.ds_diff_nml.setSuffix(QCoreApplication.translate("Nml_param", u" %", None))
        self.label.setText(QCoreApplication.translate("Nml_param", u"\u041f\u0435\u0442\u0440\u043e\u0444\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b", None))
        self.ds_a3.setPrefix(QCoreApplication.translate("Nml_param", u"\u04303=", None))
        self.ds_a3.setSuffix("")
        self.ds_a4.setPrefix(QCoreApplication.translate("Nml_param", u"a4=", None))
        self.label_5.setText(QCoreApplication.translate("Nml_param", u"\u0413\u0440\u0430\u043d\u0438\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u041a\u0433\u043b", None))
        self.label_6.setText(QCoreApplication.translate("Nml_param", u"\u0412\u0440\u0435\u043c\u044f \u0444\u0438\u043a\u0446\u0430\u0446\u0438\u0438 \u042f\u041c\u0420 \u043a\u0440\u0438\u0432\u044b\u0445", None))
        self.ds_t1.setPrefix(QCoreApplication.translate("Nml_param", u"t1=", None))
        self.ds_t1.setSuffix(QCoreApplication.translate("Nml_param", u" \u043c\u0441", None))
        self.ds_t2.setPrefix(QCoreApplication.translate("Nml_param", u"t2=", None))
        self.ds_t2.setSuffix(QCoreApplication.translate("Nml_param", u" \u043c\u0441", None))
        self.ds_t3.setPrefix(QCoreApplication.translate("Nml_param", u"t3=", None))
        self.ds_t3.setSuffix(QCoreApplication.translate("Nml_param", u" \u043c\u0441", None))
    # retranslateUi

