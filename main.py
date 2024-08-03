from PySide6.QtWidgets import QApplication, QCheckBox, QLabel, QComboBox, QPushButton
from PySide6.QtCore import Qt
from ui_main4 import QMainWindow, Ui_MainWindow
import sys
from qt_material import apply_stylesheet


class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    """Ventana principal"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tiempos de fabricación")
        self.setFixedSize(1120, 609)
        # self.showMaximized()

        # Ocultamos por defecto campos, que serán visibles si el checkbox está activado
        self.lbl_operarios_loteado_prod.hide()
        self.le_operarios_loteado_prod.hide()
        self.lbl_operarios_etiquetado_prod.hide()
        self.le_operarios_etiquetado_prod.hide()
        self.lbl_operarios_idioma_prod.hide()
        self.le_operarios_etiquetado_idioma.hide()
        self.lbl_operarios_encajado_prod.hide()
        self.le_operarios_encajado_prod.hide()
        self.lbl_operarios_pack_prod.hide()
        self.le_operarios_pack_prod.hide()
        self.lbl_operarios_limp_fab.hide()
        self.le_operarios_limp_fab.hide()
        self.lbl_operarios_sec.hide()
        self.le_operarios_sec.hide()
        self.lbl_operarios_env.hide()
        self.le_operarios_env.hide()
        

        # Listas/Diccionario para los comboBox
        # diccionario={"tipo_XXXXX":minutos_limpieza}

        self.tipos_fabricacion = {"Emulsión": 240, "Gel": 180, "Solución": 120}
        self.tipos_vaciado = ["Bomba", "Manual"]
        self.tipos_envases = ["Tubos", "Tarros", "Frascos"]
        self.tipos_envasado = ["Manual", "Máquina", "Automático"]
        self.tipos_loteado = ["Automático", "Manual"]
        self.tipos_etiquetado = ["Automático", "Manual"]
        self.tipos_encajado_tubos = ["Sin separadores", "Con separadores"]

        # Asignación de datos a los comboBox de la aplicación
        self.cmb_fabricacion_fab.addItems(list(self.tipos_fabricacion.keys()))
        self.cmb_vaciado_fab.addItems(self.tipos_vaciado)
        self.cmb_prep_env.addItems(self.tipos_envases)
        self.cmb_env.addItems(self.tipos_envasado)
        self.cmb_loteado_prod_sec.addItems(self.tipos_loteado)
        self.cmb_etiquetado_prod_sec.addItems(self.tipos_etiquetado)
        self.cmb_pack_sec.addItems(self.tipos_encajado_tubos)

        # Signals and Slots
        self.btn_reset.clicked.connect(self.reset)
        self.cb_pesada_fab.stateChanged.connect(self.estado_pesada)
        self.cb_fabricacion_fab.stateChanged.connect(self.estado_fabricacion)
        self.cb_vaciado_fab.stateChanged.connect(self.estado_vaciado)
        self.cb_prep_env.stateChanged.connect(self.prep_envasado)
        self.cb_envasado_env.stateChanged.connect(self.envasado)
        self.cb_loteado_prod_sec.stateChanged.connect(self.loteado_prod)
        self.cb_etiquetado_prod_sec.stateChanged.connect(self.etiquetado_prod)
        self.cb_etiq_idioma_sec.stateChanged.connect(self.etiquetado_idioma)
        self.cb_encajado_sec.stateChanged.connect(self.encajado)
        self.cb_pack_sec.stateChanged.connect(self.pack)
        self.cb_limpieza_fab.stateChanged.connect(self.limpieza_fab)
        self.cb_limpieza_sec.stateChanged.connect(self.limpieza_asec)
        self.cb_limpieza_env.stateChanged.connect(self.limpieza_env)

        self.btn_calcular_fab.clicked.connect(self.total_fabricacion)

    def reset(self):
        self.le_cantidad_fab.setText("")

        self.cb_pesada_fab.setChecked(False)
        self.le_pesada_fab.setEnabled(False)
        self.le_pesada_fab.setText("")

        self.cb_fabricacion_fab.setChecked(False)
        self.cmb_fabricacion_fab.setEnabled(False)
        self.cmb_fabricacion_fab.setCurrentIndex(-1)

        self.cb_vaciado_fab.setChecked(False)
        self.cmb_vaciado_fab.setEnabled(False)
        self.cmb_vaciado_fab.setCurrentIndex(-1)

        self.cb_limpieza_fab.setChecked(False)

        self.le_operarios_env.setText("")

        self.cb_prep_env.setChecked(False)
        self.cmb_prep_env.setEnabled(False)
        self.cmb_prep_env.setCurrentIndex(-1)

        self.cb_envasado_env.setChecked(False)
        self.cmb_env.setEnabled(False)
        self.cmb_env.setCurrentIndex(-1)

        self.cb_limpieza_env.setChecked(False)

        self.le_operarios_env.setText("")

        self.le_total_env.setText("")

        self.cb_loteado_prod_sec.setChecked(False)
        self.cmb_loteado_prod_sec.setEnabled(False)
        self.cmb_loteado_prod_sec.setCurrentIndex(-1)

        self.cb_etiquetado_prod_sec.setChecked(False)
        self.cmb_etiquetado_prod_sec.setEnabled(False)
        self.cmb_etiquetado_prod_sec.setCurrentIndex(-1)

        self.cb_encajado_sec.setChecked(False)

        self.cb_etiq_idioma_sec.setChecked(False)

        self.cb_pack_sec.setChecked(False)
        self.cmb_pack_sec.setEnabled(False)
        self.cmb_pack_sec.setCurrentIndex(-1)

        self.cb_limpieza_sec.setChecked(False)

        self.le_operarios_loteado_prod.setText("")
        self.le_operarios_etiquetado_prod.setText("")
        self.le_operarios_etiquetado_idioma.setText("")
        self.le_operarios_encajado_prod.setText("")
        self.le_operarios_pack_prod.setText("")
        self.le_operarios_sec.setText("")

        self.le_total_sec.setText("")
        self.le_total_produccion.setText("")

        self.le_total_fab.setText("")

        self.le_cantidad_fab.setFocus()

    def estado_pesada(self, estado):
        # print(f"Line Edit:{self.le_pesada_fab.isEnabled()}")
        if estado == 2:
            self.le_pesada_fab.setEnabled(True)
        else:
            self.le_pesada_fab.setEnabled(False)

        # print(f"Line Edit:{self.le_pesada_fab.isEnabled()}")
        # print(f"Estado:{estado}")

    def estado_fabricacion(self, estado):
        if estado == 2:
            self.cmb_fabricacion_fab.setEnabled(True)

        else:
            self.cmb_fabricacion_fab.setEnabled(False)

    def estado_vaciado(self, estado):
        if estado == 2:
            self.cmb_vaciado_fab.setEnabled(True)

        else:
            self.cmb_vaciado_fab.setEnabled(False)

    def prep_envasado(self, estado):
        if estado == 2:
            self.cmb_prep_env.setEnabled(True)

        else:
            self.cmb_prep_env.setEnabled(False)

    def envasado(self, estado):
        if estado == 2:
            self.cmb_env.setEnabled(True)

        else:
            self.cmb_env.setEnabled(False)

    def loteado_prod(self, estado):
        if estado == 2:
            self.cmb_loteado_prod_sec.setCurrentIndex(-1)
            self.cmb_loteado_prod_sec.setEnabled(True)
            self.cmb_loteado_prod_sec.currentIndexChanged.connect(
                self.loteado_prod_activado
            )
            # self.lbl_operarios_loteado_prod.show()
            # self.le_operarios_loteado_prod.show()
        else:
            self.cmb_loteado_prod_sec.setCurrentIndex(-1)
            self.lbl_operarios_loteado_prod.hide()
            self.le_operarios_loteado_prod.hide()
            self.cmb_loteado_prod_sec.setEnabled(False)

    def loteado_prod_activado(self, indice):
        if indice == 1:
            self.lbl_operarios_loteado_prod.show()
            self.le_operarios_loteado_prod.show()
        elif indice == 0:
            self.cmb_loteado_prod_sec.setCurrentIndex(0)
            # self.cmb_loteado_prod_sec.setEnabled(False)
            self.lbl_operarios_loteado_prod.hide()
            self.le_operarios_loteado_prod.hide()

    def etiquetado_prod(self, estado):
        if estado == 2:

            self.cmb_etiquetado_prod_sec.setCurrentIndex(-1)
            self.cmb_etiquetado_prod_sec.setEnabled(True)
            self.cmb_etiquetado_prod_sec.currentIndexChanged.connect(
                self.etiquetado_prod_activado
            )
            # self.lbl_operarios_loteado_prod.show()
            # self.le_operarios_loteado_prod.show()
        else:
            self.cmb_etiquetado_prod_sec.setCurrentIndex(-1)
            self.lbl_operarios_etiquetado_prod.hide()
            self.le_operarios_etiquetado_prod.hide()
            self.cmb_etiquetado_prod_sec.setEnabled(False)

    def etiquetado_prod_activado(self, indice):
        if indice == 1:
            self.lbl_operarios_etiquetado_prod.show()
            self.le_operarios_etiquetado_prod.show()
        elif indice == 0:
            self.cmb_etiquetado_prod_sec.setCurrentIndex(0)
            # self.cmb_loteado_prod_sec.setEnabled(False)
            self.lbl_operarios_etiquetado_prod.hide()
            self.le_operarios_etiquetado_prod.hide()

    def encajado(self, estado):

        if estado == 2:

            self.lbl_operarios_encajado_prod.show()
            self.le_operarios_encajado_prod.show()
            self.le_operarios_encajado_prod.setFocus()
            # self.cmb_etiquetado_prod_sec.currentIndexChanged.connect(self.encajado_activado)

        else:
            self.lbl_operarios_encajado_prod.hide()
            self.le_operarios_encajado_prod.hide()

    def etiquetado_idioma(self, estado):

        if estado == 2:

            self.lbl_operarios_idioma_prod.show()
            self.le_operarios_etiquetado_idioma.show()
            self.le_operarios_etiquetado_idioma.setFocus()
            # self.cmb_etiquetado_prod_sec.currentIndexChanged.connect(self.encajado_activado)

        else:
            self.lbl_operarios_idioma_prod.hide()
            self.le_operarios_etiquetado_idioma.hide()

    def pack(self, estado):
        if estado == 2:

            self.cmb_pack_sec.setCurrentIndex(-1)
            self.cmb_pack_sec.setEnabled(True)
            self.cmb_pack_sec.currentIndexChanged.connect(self.pack_activado)
            # self.lbl_operarios_loteado_prod.show()
            # self.le_operarios_loteado_prod.show()
        else:
            self.cmb_pack_sec.setCurrentIndex(-1)
            self.lbl_operarios_pack_prod.hide()
            self.le_operarios_pack_prod.hide()
            self.cmb_pack_sec.setEnabled(False)

    def pack_activado(self):

        self.lbl_operarios_pack_prod.show()
        self.le_operarios_pack_prod.show()

    def limpieza_fab(self, estado):

        if estado == 2:

            self.lbl_operarios_limp_fab.show()
            self.le_operarios_limp_fab.show()
            self.le_operarios_limp_fab.setFocus()
            # self.cmb_etiquetado_prod_sec.currentIndexChanged.connect(self.encajado_activado)

        else:
            self.lbl_operarios_limp_fab.hide()
            self.le_operarios_limp_fab.hide()


    def limpieza_env(self, estado):

        if estado == 2:

            self.lbl_operarios_env.show()
            self.le_operarios_env.show()
            self.le_operarios_env.setFocus()
            # self.cmb_etiquetado_prod_sec.currentIndexChanged.connect(self.encajado_activado)

        else:
            self.lbl_operarios_env.hide()
            self.le_operarios_env.hide()


    def limpieza_asec(self, estado):

        if estado == 2:

            self.lbl_operarios_sec.show()
            self.le_operarios_sec.show()
            self.le_operarios_sec.setFocus()
            # self.cmb_etiquetado_prod_sec.currentIndexChanged.connect(self.encajado_activado)

        else:
            self.lbl_operarios_sec.hide()
            self.le_operarios_sec.hide()

    def limpieza_sec2(self, estado):

        if estado == 2:

            self.lbl_operarios_encajado_prod.show()
            self.le_operarios_encajado_prod.show()
            self.le_operarios_encajado_prod.setFocus()
            # self.cmb_etiquetado_prod_sec.currentIndexChanged.connect(self.encajado_activado)

        else:
            self.lbl_operarios_encajado_prod.hide()
            self.le_operarios_encajado_prod.hide()


    # FABRICACIÓN
    def calcular_pesada(self):

        componentes = self.le_pesada_fab.text()
        if not componentes:
            raise ValueError("La cantidad no puede estar vacia")
        try:
            componentes = int(self.le_pesada_fab.text())
            tiempo_pesada = componentes * 5

        except ValueError:
            raise ValueError("La cantidad debe ser un número entero")

        return tiempo_pesada

    def calcular_fabricacion(self):

        # Comprobar que la cantidad es válida
        cantidad_texto = self.le_cantidad_fab.text()
        if not cantidad_texto:
            raise ValueError("La cantidad no puede estar vacía")
        try:
            cantidad = int(cantidad_texto)
        except ValueError:
            raise ValueError("La cantidad debe ser un número entero")

        # Comprobar que el valor es válido
        tipo_fabricacion = self.cmb_fabricacion_fab.currentText()
        # print(f"Tipo de fabricación:{tipo_fabricacion}")
        if tipo_fabricacion not in self.tipos_fabricacion:
            raise ValueError("Tipo de fabricación no válido")

        tiempo_fab = self.tipos_fabricacion[tipo_fabricacion]
        return tiempo_fab

    def calcular_vaciado(self):
        cantidad_fabricada = int(self.le_cantidad_fab.text())
        if 0 < cantidad_fabricada <= 25:
            tiempo_vac = 15
        elif 25 < cantidad_fabricada <= 200:
            tiempo_vac = 25
        else:
            tiempo_vac = 45

        return tiempo_vac

    def calcular_limpieza_fab(self):

        cantidad_fabricada = int(self.le_cantidad_fab.text())
        tipo_producto = self.cmb_fabricacion_fab.currentText()

        # Diccionario que mapea los reactores con sus capacidades máximas
        reactores = {
            "P055": (0, 25),
            "P019": (50, 200),
            "P020": (200, 400),
            "P016": (0, 200),  # Solo para Solución
            "P017": (200, 500),  # Solo para Solución
        }

        # Diccionario que mapea los tipos de productos con sus tiempos de limpieza
        tiempos_limpieza = {
            "Emulsión": {"P055": 30, "P019": 45, "P020": 60},
            "Solución": {"P016": 20, "P017": 30, "P019": 45},
            "Gel": {"P055": 45, "P019": 60, "P020": 75},
        }

        # Seleccionar el reactor adecuado según la cantidad fabricada
        for reactor, capacidad in reactores.items():
            if capacidad[0] <= cantidad_fabricada <= capacidad[1]:
                if tipo_producto == "Solución" and reactor not in ["P016", "P017"]:
                    continue
                break
        else:
            raise ValueError(
                "No se encontró un reactor adecuado para la cantidad fabricada"
            )

        # Calcular el tiempo de limpieza según el reactor y el tipo de producto
        tiempo_limpieza = tiempos_limpieza[tipo_producto][reactor]

        return tiempo_limpieza

    def total_fabricacion(self):

        tiempo = (
            self.calcular_pesada()
            + self.calcular_fabricacion()
            + self.calcular_vaciado()
            + self.calcular_limpieza_fab()
        )
        self.le_total_fab.setText(str(tiempo))

    # ACONDICIONAMIENTO PRIMARIO
    def calcular_prep_env(self):

        if self.cmb_prep_env.currentIndex == 2:

            pass

    def calcular_env(self):
        pass

    def calcuclar_limpieza_env():
        pass

    # ACONDICIONAMIENTO SECUNDARIO
    def calcular_loteado_prod_sec(self):

        # si loteado automatico: tiempo se incluye en el envasado
        # si loteado es manual:preparacion maquina+loteado

        pass

    def calcular_etiquetado_prod_sec(self):
        pass

    def calcular_encajado_prod_esc(self):
        pass

    def calcular_eti_idioma_prod_esc(self):
        pass

    def calcular_pack_sec(self):

        pass

    def limpieza_sec(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue_500.xml")
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
