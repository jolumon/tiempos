# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main4xQCsKd.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1120, 609)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.fabricacion = QGroupBox(self.centralwidget)
        self.fabricacion.setObjectName(u"fabricacion")
        self.horizontalLayout = QHBoxLayout(self.fabricacion)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_cantidad_fab = QLabel(self.fabricacion)
        self.lbl_cantidad_fab.setObjectName(u"lbl_cantidad_fab")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_cantidad_fab)

        self.le_cantidad_fab = QLineEdit(self.fabricacion)
        self.le_cantidad_fab.setObjectName(u"le_cantidad_fab")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_cantidad_fab)

        self.cb_pesada_fab = QCheckBox(self.fabricacion)
        self.cb_pesada_fab.setObjectName(u"cb_pesada_fab")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.cb_pesada_fab)

        self.le_pesada_fab = QLineEdit(self.fabricacion)
        self.le_pesada_fab.setObjectName(u"le_pesada_fab")
        self.le_pesada_fab.setEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_pesada_fab)

        self.cb_fabricacion_fab = QCheckBox(self.fabricacion)
        self.cb_fabricacion_fab.setObjectName(u"cb_fabricacion_fab")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.cb_fabricacion_fab)

        self.cmb_fabricacion_fab = QComboBox(self.fabricacion)
        self.cmb_fabricacion_fab.setObjectName(u"cmb_fabricacion_fab")
        self.cmb_fabricacion_fab.setEnabled(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.cmb_fabricacion_fab)

        self.cb_vaciado_fab = QCheckBox(self.fabricacion)
        self.cb_vaciado_fab.setObjectName(u"cb_vaciado_fab")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.cb_vaciado_fab)

        self.cmb_vaciado_fab = QComboBox(self.fabricacion)
        self.cmb_vaciado_fab.setObjectName(u"cmb_vaciado_fab")
        self.cmb_vaciado_fab.setEnabled(False)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.cmb_vaciado_fab)

        self.cb_limpieza_fab = QCheckBox(self.fabricacion)
        self.cb_limpieza_fab.setObjectName(u"cb_limpieza_fab")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.cb_limpieza_fab)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.formLayout_2.setItem(7, QFormLayout.LabelRole, self.verticalSpacer)

        self.lbl_total_fab = QLabel(self.fabricacion)
        self.lbl_total_fab.setObjectName(u"lbl_total_fab")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.lbl_total_fab)

        self.le_total_fab = QLineEdit(self.fabricacion)
        self.le_total_fab.setObjectName(u"le_total_fab")
        self.le_total_fab.setReadOnly(True)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.le_total_fab)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(9, QFormLayout.FieldRole, self.verticalSpacer_4)

        self.btn_calcular_fab = QPushButton(self.fabricacion)
        self.btn_calcular_fab.setObjectName(u"btn_calcular_fab")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.btn_calcular_fab)

        self.lbl_operarios_limp_fab = QLabel(self.fabricacion)
        self.lbl_operarios_limp_fab.setObjectName(u"lbl_operarios_limp_fab")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.lbl_operarios_limp_fab)

        self.le_operarios_limp_fab = QLineEdit(self.fabricacion)
        self.le_operarios_limp_fab.setObjectName(u"le_operarios_limp_fab")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.le_operarios_limp_fab)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.horizontalLayout_2.addWidget(self.fabricacion)

        self.aprimario = QGroupBox(self.centralwidget)
        self.aprimario.setObjectName(u"aprimario")
        self.verticalLayout = QVBoxLayout(self.aprimario)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.cb_prep_env = QCheckBox(self.aprimario)
        self.cb_prep_env.setObjectName(u"cb_prep_env")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.cb_prep_env)

        self.cmb_prep_env = QComboBox(self.aprimario)
        self.cmb_prep_env.setObjectName(u"cmb_prep_env")
        self.cmb_prep_env.setEnabled(False)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.cmb_prep_env)

        self.cb_envasado_env = QCheckBox(self.aprimario)
        self.cb_envasado_env.setObjectName(u"cb_envasado_env")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.cb_envasado_env)

        self.cmb_env = QComboBox(self.aprimario)
        self.cmb_env.setObjectName(u"cmb_env")
        self.cmb_env.setEnabled(False)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.cmb_env)

        self.cb_limpieza_env = QCheckBox(self.aprimario)
        self.cb_limpieza_env.setObjectName(u"cb_limpieza_env")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.cb_limpieza_env)

        self.lbl_operarios_env = QLabel(self.aprimario)
        self.lbl_operarios_env.setObjectName(u"lbl_operarios_env")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.lbl_operarios_env)

        self.le_operarios_env = QLineEdit(self.aprimario)
        self.le_operarios_env.setObjectName(u"le_operarios_env")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.le_operarios_env)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.formLayout_3.setItem(5, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.line_4 = QFrame(self.aprimario)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.line_4)

        self.total_aprimario = QLabel(self.aprimario)
        self.total_aprimario.setObjectName(u"total_aprimario")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.total_aprimario)

        self.le_total_env = QLineEdit(self.aprimario)
        self.le_total_env.setObjectName(u"le_total_env")
        self.le_total_env.setReadOnly(True)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.le_total_env)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_3.setItem(8, QFormLayout.FieldRole, self.verticalSpacer_5)

        self.btn_calcular_env = QPushButton(self.aprimario)
        self.btn_calcular_env.setObjectName(u"btn_calcular_env")

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.btn_calcular_env)


        self.verticalLayout.addLayout(self.formLayout_3)


        self.horizontalLayout_2.addWidget(self.aprimario)

        self.asecundario = QGroupBox(self.centralwidget)
        self.asecundario.setObjectName(u"asecundario")
        self.verticalLayout_2 = QVBoxLayout(self.asecundario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.cb_loteado_prod_sec = QCheckBox(self.asecundario)
        self.cb_loteado_prod_sec.setObjectName(u"cb_loteado_prod_sec")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.cb_loteado_prod_sec)

        self.cmb_loteado_prod_sec = QComboBox(self.asecundario)
        self.cmb_loteado_prod_sec.setObjectName(u"cmb_loteado_prod_sec")
        self.cmb_loteado_prod_sec.setEnabled(False)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.cmb_loteado_prod_sec)

        self.lbl_operarios_loteado_prod = QLabel(self.asecundario)
        self.lbl_operarios_loteado_prod.setObjectName(u"lbl_operarios_loteado_prod")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.lbl_operarios_loteado_prod)

        self.le_operarios_loteado_prod = QLineEdit(self.asecundario)
        self.le_operarios_loteado_prod.setObjectName(u"le_operarios_loteado_prod")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.le_operarios_loteado_prod)

        self.cb_etiquetado_prod_sec = QCheckBox(self.asecundario)
        self.cb_etiquetado_prod_sec.setObjectName(u"cb_etiquetado_prod_sec")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.cb_etiquetado_prod_sec)

        self.cmb_etiquetado_prod_sec = QComboBox(self.asecundario)
        self.cmb_etiquetado_prod_sec.setObjectName(u"cmb_etiquetado_prod_sec")
        self.cmb_etiquetado_prod_sec.setEnabled(False)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.cmb_etiquetado_prod_sec)

        self.lbl_operarios_etiquetado_prod = QLabel(self.asecundario)
        self.lbl_operarios_etiquetado_prod.setObjectName(u"lbl_operarios_etiquetado_prod")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.lbl_operarios_etiquetado_prod)

        self.le_operarios_etiquetado_prod = QLineEdit(self.asecundario)
        self.le_operarios_etiquetado_prod.setObjectName(u"le_operarios_etiquetado_prod")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.le_operarios_etiquetado_prod)

        self.cb_encajado_sec = QCheckBox(self.asecundario)
        self.cb_encajado_sec.setObjectName(u"cb_encajado_sec")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.cb_encajado_sec)

        self.cb_etiq_idioma_sec = QCheckBox(self.asecundario)
        self.cb_etiq_idioma_sec.setObjectName(u"cb_etiq_idioma_sec")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.cb_etiq_idioma_sec)

        self.lbl_operarios_idioma_prod = QLabel(self.asecundario)
        self.lbl_operarios_idioma_prod.setObjectName(u"lbl_operarios_idioma_prod")

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.lbl_operarios_idioma_prod)

        self.le_operarios_etiquetado_idioma = QLineEdit(self.asecundario)
        self.le_operarios_etiquetado_idioma.setObjectName(u"le_operarios_etiquetado_idioma")

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.le_operarios_etiquetado_idioma)

        self.cb_pack_sec = QCheckBox(self.asecundario)
        self.cb_pack_sec.setObjectName(u"cb_pack_sec")

        self.formLayout_4.setWidget(8, QFormLayout.LabelRole, self.cb_pack_sec)

        self.cmb_pack_sec = QComboBox(self.asecundario)
        self.cmb_pack_sec.setObjectName(u"cmb_pack_sec")
        self.cmb_pack_sec.setEnabled(False)

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.cmb_pack_sec)

        self.cb_limpieza_sec = QCheckBox(self.asecundario)
        self.cb_limpieza_sec.setObjectName(u"cb_limpieza_sec")

        self.formLayout_4.setWidget(10, QFormLayout.LabelRole, self.cb_limpieza_sec)

        self.lbl_operarios_sec = QLabel(self.asecundario)
        self.lbl_operarios_sec.setObjectName(u"lbl_operarios_sec")

        self.formLayout_4.setWidget(11, QFormLayout.LabelRole, self.lbl_operarios_sec)

        self.le_operarios_sec = QLineEdit(self.asecundario)
        self.le_operarios_sec.setObjectName(u"le_operarios_sec")

        self.formLayout_4.setWidget(11, QFormLayout.FieldRole, self.le_operarios_sec)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.formLayout_4.setItem(12, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.lbl_total_sec = QLabel(self.asecundario)
        self.lbl_total_sec.setObjectName(u"lbl_total_sec")

        self.formLayout_4.setWidget(13, QFormLayout.LabelRole, self.lbl_total_sec)

        self.le_total_sec = QLineEdit(self.asecundario)
        self.le_total_sec.setObjectName(u"le_total_sec")
        self.le_total_sec.setReadOnly(True)

        self.formLayout_4.setWidget(13, QFormLayout.FieldRole, self.le_total_sec)

        self.verticalSpacer_6 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_4.setItem(14, QFormLayout.FieldRole, self.verticalSpacer_6)

        self.btn_calcular_sec = QPushButton(self.asecundario)
        self.btn_calcular_sec.setObjectName(u"btn_calcular_sec")

        self.formLayout_4.setWidget(15, QFormLayout.FieldRole, self.btn_calcular_sec)

        self.lbl_operarios_pack_prod = QLabel(self.asecundario)
        self.lbl_operarios_pack_prod.setObjectName(u"lbl_operarios_pack_prod")

        self.formLayout_4.setWidget(9, QFormLayout.LabelRole, self.lbl_operarios_pack_prod)

        self.le_operarios_pack_prod = QLineEdit(self.asecundario)
        self.le_operarios_pack_prod.setObjectName(u"le_operarios_pack_prod")

        self.formLayout_4.setWidget(9, QFormLayout.FieldRole, self.le_operarios_pack_prod)

        self.lbl_operarios_encajado_prod = QLabel(self.asecundario)
        self.lbl_operarios_encajado_prod.setObjectName(u"lbl_operarios_encajado_prod")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.lbl_operarios_encajado_prod)

        self.le_operarios_encajado_prod = QLineEdit(self.asecundario)
        self.le_operarios_encajado_prod.setObjectName(u"le_operarios_encajado_prod")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.le_operarios_encajado_prod)


        self.verticalLayout_2.addLayout(self.formLayout_4)


        self.horizontalLayout_2.addWidget(self.asecundario)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_total_producion = QLabel(self.centralwidget)
        self.lbl_total_producion.setObjectName(u"lbl_total_producion")

        self.horizontalLayout_3.addWidget(self.lbl_total_producion)

        self.le_total_produccion = QLineEdit(self.centralwidget)
        self.le_total_produccion.setObjectName(u"le_total_produccion")
        self.le_total_produccion.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.le_total_produccion)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_reset = QPushButton(self.centralwidget)
        self.btn_reset.setObjectName(u"btn_reset")

        self.horizontalLayout_3.addWidget(self.btn_reset)

        self.btn_calcular_total = QPushButton(self.centralwidget)
        self.btn_calcular_total.setObjectName(u"btn_calcular_total")

        self.horizontalLayout_3.addWidget(self.btn_calcular_total)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tiempos de producci\u00f3n", None))
        self.fabricacion.setTitle(QCoreApplication.translate("MainWindow", u"Fabricaci\u00f3n", None))
        self.lbl_cantidad_fab.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.le_cantidad_fab.setPlaceholderText(QCoreApplication.translate("MainWindow", u"kg de fabricaci\u00f3n", None))
        self.cb_pesada_fab.setText(QCoreApplication.translate("MainWindow", u"Pesada", None))
        self.le_pesada_fab.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce n\u00ba componentes", None))
        self.cb_fabricacion_fab.setText(QCoreApplication.translate("MainWindow", u"Fabricaci\u00f3n", None))
        self.cmb_fabricacion_fab.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.cb_vaciado_fab.setText(QCoreApplication.translate("MainWindow", u"Vaciado", None))
        self.cmb_vaciado_fab.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.cb_limpieza_fab.setText(QCoreApplication.translate("MainWindow", u"Limpieza", None))
        self.lbl_total_fab.setText(QCoreApplication.translate("MainWindow", u"Total / min", None))
        self.le_total_fab.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutos", None))
        self.btn_calcular_fab.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.lbl_operarios_limp_fab.setText(QCoreApplication.translate("MainWindow", u"Operarios", None))
        self.aprimario.setTitle(QCoreApplication.translate("MainWindow", u"Acondicionamiento primario", None))
        self.cb_prep_env.setText(QCoreApplication.translate("MainWindow", u"Preparaci\u00f3n envasado", None))
        self.cmb_prep_env.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Formato", None))
        self.cb_envasado_env.setText(QCoreApplication.translate("MainWindow", u"Envasado", None))
        self.cmb_env.setCurrentText("")
        self.cmb_env.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.cb_limpieza_env.setText(QCoreApplication.translate("MainWindow", u"Limpieza", None))
        self.lbl_operarios_env.setText(QCoreApplication.translate("MainWindow", u"Operarios", None))
        self.total_aprimario.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.le_total_env.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutos", None))
        self.btn_calcular_env.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.asecundario.setTitle(QCoreApplication.translate("MainWindow", u"Acondicionamiento secundario", None))
        self.cb_loteado_prod_sec.setText(QCoreApplication.translate("MainWindow", u"Loteado producto", None))
        self.cmb_loteado_prod_sec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Modo", None))
        self.lbl_operarios_loteado_prod.setText(QCoreApplication.translate("MainWindow", u"Operarios loteado", None))
        self.cb_etiquetado_prod_sec.setText(QCoreApplication.translate("MainWindow", u"Etiquetado producto", None))
        self.cmb_etiquetado_prod_sec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.lbl_operarios_etiquetado_prod.setText(QCoreApplication.translate("MainWindow", u"Operarios Etiquetado", None))
        self.cb_encajado_sec.setText(QCoreApplication.translate("MainWindow", u"Encajado", None))
        self.cb_etiq_idioma_sec.setText(QCoreApplication.translate("MainWindow", u"Etiquetado idioma", None))
        self.lbl_operarios_idioma_prod.setText(QCoreApplication.translate("MainWindow", u"Operarios idioma", None))
        self.cb_pack_sec.setText(QCoreApplication.translate("MainWindow", u"Pack", None))
        self.cmb_pack_sec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.cb_limpieza_sec.setText(QCoreApplication.translate("MainWindow", u"Limpieza", None))
        self.lbl_operarios_sec.setText(QCoreApplication.translate("MainWindow", u"Operarios limpieza", None))
        self.lbl_total_sec.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.le_total_sec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutos", None))
        self.btn_calcular_sec.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.lbl_operarios_pack_prod.setText(QCoreApplication.translate("MainWindow", u"Operarios packaging", None))
        self.lbl_operarios_encajado_prod.setText(QCoreApplication.translate("MainWindow", u"Operarios encajado", None))
        self.lbl_total_producion.setText(QCoreApplication.translate("MainWindow", u"Tiempo total", None))
        self.le_total_produccion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minutos", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_calcular_total.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
    # retranslateUi

