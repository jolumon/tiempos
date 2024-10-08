from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QComboBox,
    QPushButton,
    QDialog,
    QVBoxLayout
)
from PySide6.QtCore import Qt
from ui_main6 import QMainWindow, Ui_MainWindow
from auxiliares import VentanaFaltanDatos, VentanaCantidadSuperior, VentanaNumeroEntero, VentanaComponentesVacio, VentanaErrorCalculoFabricacion, VentanaErrorSeleccion, VentanaDivisionCero
import sys
from qt_material import apply_stylesheet


class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    """Ventana principal"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tiempos de fabricación")
        self.setFixedSize(1120, 609)
        # self.fabricacion.setStyleSheet("QGroupBox::title { color: blue; }")  # Cambia el color del título a azul
        # self.showMaximized()

        # Constantes
        # Número de unidades para realizar el cálculo, es decir, tiempo para cada 1000 uds.
        self.UNIDADES_CALCULO = 1000
        self.PREPARACION_MAQUINA_LOTEADO = 10  # 10 minutos

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
        self.lbl_capacidad_env.hide()
        self.cmb_capacidad.hide()

        # Listas/Diccionario para los comboBox

        self.tipos_fabricacion = {"Emulsión": 240, "Gel": 180, "Solución": 120}
        self.tipos_vaciado = ["Bomba", "Manual"]
        self.tipos_envases = ["Tubos", "Tarros", "Frascos"]
        self.tipos_envasado = ["Manual", "Máquina", "Automático"]
        self.tipos_loteado = ["Automático", "Manual"]
        self.tipos_etiquetado = ["Automático", "Manual"]
        self.tipos_encajado_tubos = ["Sin separadores", "Con separadores"]
        self.tiempos_fabricacion = {
            "Emulsión": 240, "Gel": 180, "Solución": 120}
        self.capacidades = {
            "Tubos": [5, 10, 15, 75, 100, 200],
            "Tarros": [50, 250, 300, 500, 1000],
            "Frascos": [15, 30, 50, 100, 125, 150, 200, 250, 500, 1000],
        }
        self.tiempos_envasado = {"Emulsión": {"Máquina": 120, "Automático": 90},
                                 "Gel": {"Máquina": 120, "Automático": 90},
                                 "Solución": {"Manual": 240, "Máquina": 120, "Automático": 90}}

        self.tipos_envasado = {
            "Manual": {"Tarros": 40, "Frascos": 40},
            "Máquina": {"Tubos": 30, "Tarros": 30, "Frascos": 30},
            "Automático": {"Tubos": 120, "Tarros": 35, "Frascos": 35},
        }

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
        self.le_total_fab.textChanged.connect(self.actualizarTotal)
        self.le_total_env.textChanged.connect(self.actualizarTotal)
        self.le_total_sec.textChanged.connect(self.actualizarTotal)

        self.btn_calcular_fab.clicked.connect(self.total_fabricacion)
        self.btn_calcular_env.clicked.connect(self.total_envasado)
        self.btn_calcular_sec.clicked.connect(self.total_envasado)

        self.cmb_prep_env.currentTextChanged.connect(
            self.actualizar_capacidades)
        self.cmb_capacidad.currentTextChanged.connect(self.mostrar_unidades)

        self.btn_guardar.clicked.connect(self.guardar)

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

        self.le_unidades.setText("")

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
            self.lbl_capacidad_env.show()
            self.cmb_capacidad.show()
            # self.cmb_prep_env.setFocus()

        else:
            self.cmb_prep_env.setEnabled(False)
            self.lbl_capacidad_env.hide()
            self.cmb_capacidad.hide()

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

        if self.cb_pesada_fab.isChecked():
            componentes = self.le_pesada_fab.text()
            if not componentes:
                raise ValueError("La cantidad no puede estar vacia")
                ventana_componentes_vacio = VentanaComponentesVacio()
                ventana_componentes_vacio.exec()
            try:
                componentes = int(self.le_pesada_fab.text())
                tiempo_pesada = componentes * 5

            except ValueError:
                raise ValueError("La cantidad debe ser un número entero")
                ventana_numero_entero = VentanaNumeroEntero()
                ventana_numero_entero.exex()

        else:
            tiempo_pesada = 0

        return tiempo_pesada

    def calcular_fabricacion(self):

        # Comprobar que la cantidad es válida
        cantidad_texto = self.le_cantidad_fab.text()
        if not cantidad_texto:
            raise ValueError("La cantidad no puede estar vacía")
            ventana_componentes_vacio = VentanaComponentesVacio()
            ventana_componentes_vacio.exec()
        try:
            cantidad = int(cantidad_texto)
            if cantidad > 400:
                ventana_capacidad = VentanaCantidadSuperior()
                ventana_capacidad.exec()
                print('Cantidad superior a la capciad de máxima del reactor')
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
        # numero_operarios_limp= self.

        # Diccionario que mapea los reactores con sus capacidades máximas
        reactores = {
            "P055": (0, 25),
            "Cubo": (25, 50),
            "P019": (50, 200),
            "P020": (200, 400),
            "P016": (0, 200),  # Solo para Solución
            "P017": (200, 500),  # Solo para Solución
        }

        # Diccionario que mapea los tipos de productos con sus tiempos de limpieza
        tiempos_limpieza = {
            "Emulsión": {"P055": 30, "P019": 45, "P020": 60, "Cubo": 10},
            "Solución": {"P016": 20, "P017": 30, "P019": 45, "Cubo": 10},
            "Gel": {"Cubo": 10, "P055": 45, "P019": 60, "P020": 75},
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
        try:
            tiempo = (
                self.calcular_pesada()
                + self.calcular_fabricacion()
                + self.calcular_vaciado()
                + self.calcular_limpieza_fab()
            )
            self.le_total_fab.setText(str(tiempo))
        except Exception:
            ventana_faltan_datos = VentanaErrorCalculoFabricacion()
            ventana_faltan_datos.exec()

    # ACONDICIONAMIENTO PRIMARIO

    def actualizar_capacidades(self, envase):

        # Limpia las opciones actuales del cmb_capacidad
        self.cmb_capacidad.clear()

        # Agrega las capacidades correspondientes al envase seleccionado
        if envase in self.capacidades:
            self.cmb_capacidad.addItems(map(str, self.capacidades[envase]))

    def calcular_prep_env(self):
        # envases = {"Tubos": [5, 10, 15, 75, 100, 200],
        #            "Tarros": [50, 250, 300, 500],
        #            "Frascos": [15, 30, 50, 100, 125, 150, 200, 250, 500, 1000]}

        tipos_envasado = {
            "Manual": {"Tarros": 40, "Frascos": 40},
            "Máquina": {"Tubos": 30, "Tarros": 30, "Frascos": 30},
            "Automático": {"Tubos": 120, "Tarros": 35, "Frascos": 35},
        }

        if self.cb_prep_env.isChecked():
            envase = self.cmb_prep_env.currentText()
            tipo_envasado = self.cmb_env.currentText()

            if tipo_envasado != "" and envase != "":
                # Obtener el valor correspondiente al tipo de envasado seleccionado
                valor_tipo_envasado = tipos_envasado[tipo_envasado][envase]
                print(
                    f"El tiempo para {envase} con envasado {tipo_envasado} es: {valor_tipo_envasado}"
                )
                print(
                    f'Tiempo de envasado-calcular_prep_env:{valor_tipo_envasado}')
                # self.le_total_env.setText(str(valor_tipo_envasado))
                return valor_tipo_envasado

    def obtener_cantidad_fabricada(self):
        try:
            cantidad_fabricada = int(self.le_cantidad_fab.text())
            return cantidad_fabricada
        except ValueError:
            ventana_dato_incorrecto = VentanaNumeroEntero()
            ventana_dato_incorrecto.exec()
        except Exception:
            ventana_faltan_datos = VentanaFaltanDatos()
            ventana_faltan_datos.exec()

    def obtener_capacidad(self):
        try:
            if self.cmb_capacidad.currentText() != "":
                capacidad = int(self.cmb_capacidad.currentText())/1000
                return capacidad
        except ValueError:
            ventana_dato_incorrecto = VentanaNumeroEntero()
            ventana_dato_incorrecto.exec()
        except Exception:
            ventana_faltan_datos = VentanaFaltanDatos()
            ventana_faltan_datos.exec()

    def mostrar_unidades(self):
        cantidad_fabricada = self.obtener_cantidad_fabricada()
        capacidad = self.obtener_capacidad()
        unidades = int(cantidad_fabricada/capacidad)
        self.le_unidades.setText(str(unidades))
        return unidades

    def calcular_env(self):
        try:
            # Tiempos de envasado para 1000 uds y 2 operarios.

            unidades = self.mostrar_unidades()
            print(f'Unidades:{unidades}')

            if self.obtener_capacidad() > 500:
                tiempo_envasado = (unidades*60*2)/self.UNIDADES_CALCULO
            else:
                tiempo_envasado = (unidades*60)/self.UNIDADES_CALCULO
            print(f'Tiempo de envasado-calcular_env:{tiempo_envasado}')
            return tiempo_envasado
        except Exception:
            ventana_faltan_datos = VentanaFaltanDatos()
            ventana_faltan_datos.exec()

    def calcuclar_limpieza_env(self):
        # Tiempo de limpieza 60' por operario
        if self.le_operarios_env.text() != "":
            try:
                operarios = int(self.le_operarios_env.text())
                tiempo_limpieza_env = 60/operarios
                return tiempo_limpieza_env
            except ZeroDivisionError:
                ventana_div_cero = VentanaDivisionCero()
                ventana_div_cero.exec()

    def total_envasado(self):
        
        tiempo = (
            self.calcular_prep_env() +
            self.calcular_env()
            + self.calcuclar_limpieza_env()

        )
        self.le_total_env.setText(str(tiempo))
        

    # ACONDICIONAMIENTO SECUNDARIO

    def calcular_loteado_prod_sec(self):

        # si loteado automatico: tiempo se incluye en el envasado
        # si loteado es manual:preparacion maquina+loteado

        preparacion_maquina = 10
        tiempo_loteado = 0

        tipo_loteado = self.cmb_loteado_prod_sec.text()
        if not tipo_loteado:
            ventana_loteado = VentanaFaltanDatos()
            ventana_loteado.exec()
        else:
            if tipo_loteado in self.tipos_loteado:
                print(f'Has elegido: {tipo_loteado}')

                if tipo_loteado == "Manual":
                    # Hay que estimar el tiempo de loteado correctamente
                    tiempo_loteado = 0.12*int(self.le_unidades.text())
                    preparacion_maquina = 15

            else:
                print('Tiene que elegir una opción')

        tiempo_loteado_total = preparacion_maquina+tiempo_loteado
        return tiempo_loteado_total

    def calcular_etiquetado_prod_sec(self):
        # Etiquetado manual producto 0.3 minutos / unidad / operario

        # Etiquetado automatico producto 0.09 minutos/unidad
        etiquetado_prod = self.cb_etiquetado_prod_sec.isChecked()
        tipo_etiquetado_prod = self.cmb_etiquetado_prod_sec.currentText()
        if etiquetado_prod:
            try:
                if tipo_etiquetado_prod == 'Manual':

                    operarios_etiq = int(
                        self.le_operarios_etiquetado_prod.text())
                    tiempo_etiquetado_prod = 0.3 * \
                        int(self.le_unidades.text())/(operarios_etiq)

                if tipo_etiquetado_prod == 'Automático':

                    tiempo_etiquetado_prod = 0.09*int(self.le_unidades.text())
            except:
                print('Comprobar las unidades en envasado')
                ventana = VentanaFaltanDatos()
                ventana.exec()
            # try:
            #     tiempo_etiquetado_prod = 0.3*int(self.le_unidades.text())/(
            #         operarios_etiq) if "Manual" in self.tipos_etiquetado else 0.09*int(self.le_unidades.text())
            # except Exception:
            #     print('Comprobar las unidades en envasado y operarios en etiquetado acond_sec')
            #     ventana = VentanaFaltanDatos()
            #     ventana.exec()
        else:
            tiempo_etiquetado_prod = 0

        return tiempo_etiquetado_prod

    def calcular_encajado_prod_esc(self):

        # Hay que añadir el tiempo de loteado de las cajas 0.12 minutos / unidad / operario

        # Encajado producto 1000 uds 480 minutos 1 operario
        pass

    def calcular_eti_idioma_prod_esc(self):
        pass

    def calcular_pack_sec(self):
        # Encajado 1000 unidades 100 minutos, es decir, 1 unidad 0.1 minutos.

        pass

    def limpieza_sec(self):

        pass

    def calcular_acond_secundario(self):

        pass

    def actualizarTotal(self):
        print("ActualizarTotal")
        try:
            print("Dentro del try")

            # valor_fab = int(self.le_total_fab.text())
            # print(f'Valor fab:{valor_fab}')
            if self.le_total_fab.text() == "":
                valor_fab = 0
            else:
                valor_fab = int(self.le_total_fab.text())
            print(f"Valor fab: {valor_fab}")
            if self.le_total_env.text() == "":
                valor_aprim = 0
            else:
                valor_aprim = float(self.le_total_env.text())
            print(f"Valor aprim: {valor_aprim}")

            # valor_asec = float(self.le_total_sec.text())
            # tiempo_total = valor_fab + valor_aprim + valor_asec
            tiempo_total = valor_fab + valor_aprim
            self.le_total_produccion.setText(str(tiempo_total))
        except ValueError:
            print(f"Dentro del except")
            ventana_error = VentanaFaltanDatos()
            ventana_error.exec()
            # ventana_error.show()
            # QtCore.QCoreApplication.processEvents()
            self.le_total_produccion.setText("")

    def guardar(self):
        print('Guardado')
        pass


if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app, theme="light_blue_500.xml")
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
