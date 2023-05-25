import time

import pytest
from selenium import webdriver
from Funciones import funciones_isolucion
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def driver():
    ser = Service("C:\drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    driver.get("https://qa.isolucion.co/PaginaLogin.aspx")
    driver.maximize_window()
    f = funciones_isolucion(driver)
    f.texto_multiple("id", "UserText", "administrador")
    f.texto_multiple("id", "PasswordText", "12345")
    f.click_multiple("id", "btnLogin")
    yield driver
    print("test finalizado")


@pytest.mark.tarea
def test_uno(driver):
    try:
        f = funciones_isolucion(driver)
        bt1 = driver.find_element(By.XPATH, "//a[contains(.,'Tareas')]")
        bt1.click()
        bt2 = driver.find_element(By.XPATH, "(//div[contains(.,'Agendar tareas')])[5]")
        bt2.click()
        f.select_xpath_type("xpath", "text", "//select[@id='ContentPlaceHolder1_ddlTipoTarea']", "Tarea Genérica")
        f.texto_multiple("id", "ContentPlaceHolder1_txtNomTarea", "PruebaQA5")
        f.texto_multiple("id", "ContentPlaceHolder1_txtDescripcion", "Descripcion de la tarea creada.")
        f.click_multiple("id", "ContentPlaceHolder1_imbBuscarUsuario")
        driver.switch_to.frame(driver.find_element(By.ID, "ContainerIframe"))
        f.click_multiple("xpath", "(//input[contains(@type,'checkbox')])[4]")
        f.click_multiple("id", "MainContentPlaceHolder_btnGrabar")
        f.click_multiple("id", "ContentPlaceHolder1_imbFechaFin")
        f.click_multiple("xpath", "//div[contains(@id,'ContentPlaceHolder1_ceFechaFinActividad_day_5_0')]")
        f.check_multiple("id", "ContentPlaceHolder1_chkRequiereRespuesta")
        f.click_multiple("id", "ContentPlaceHolder1_btnGrabar")
        time.sleep(10)
        print("Tarea Creada con exito.")
    except Exception as ex:
        print(ex)
        print("No se pudo ejecutar el test")


@pytest.mark.Documento
def test_dos(driver):
    try:
        f = funciones_isolucion(driver)
        bt3 = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle'][contains(.,'Documentacion')]")
        bt3.click()
        btn4 = driver.find_element(By.XPATH,
                                   "(//div[contains(.,'Administración de los documentos del sistema de gestión.')])[4]")
        btn4.click()
        f.click_multiple('xpath', "//a[contains(@id,'1')][@class='LinkPestania'][contains(.,'Nuevo')]")
        f.click_multiple('xpath', "//i[contains(@class,'fa fa-file-text fa-3x')]")
        f.check_multiple('id', "ContentPlaceHolder1_ctrSucursalNuevo_chbEsNivelGlobal")
        f.select_xpath_type('id', 'value', "ContentPlaceHolder1_ddlPlantillaNuevo", 'Formato')
        f.texto_multiple('id', "ContentPlaceHolder1_txtNombre", 'DocumentoPruebaQA')
        f.texto_multiple('id', "ContentPlaceHolder1_txtdecimalVersionNuevo", '1')
        f.click_multiple('id', 'ContentPlaceHolder1_imbJerarquiaBusqueda')
        driver.switch_to.frame(driver.find_element(By.ID, "ContainerIframe"))
        f.click_multiple('id', 'MainContentPlaceHolder_trvJerarquicot0')
        f.click_multiple('id', 'ContentPlaceHolder1_btnGrabar')
        time.sleep(10)
        print('Documento creado con exito')
    except Exception as ex:
        print(ex)
        print("No se pudo ejecutar el test")


@pytest.mark.Cargue
def test_tres(driver):
    try:
        f = funciones_isolucion(driver)
        btn5 = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle'][contains(.,'Sistemas')]")
        btn5.click()
        btn6 = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle'][contains(.,'Configuración')]")
        btn6.click()
        f.click_multiple('xpath', "(//span[contains(.,'Opciones avanzadas (Incluye parametrización)')])[1]")
        f.click_multiple('xpath', "//h4[@class='ng-binding'][contains(.,'Cargar Tablas Básicas')]")
        f.select_xpath_type('id', 'value', 'ContentPlaceHolder1_ddlTablasBasicas', 'SSTFuncionario')
        f.click_multiple('id', 'btnpaso2')
        adj = driver.find_element(By.ID, "FileUpload1")
        adj.send_keys("C:/Users/diego.loaiza/Downloads/SSTFuncionario_20232724092720_2_Trabajadores.xlsm")
        f.click_multiple('xpath', "//a[contains(@id,'btnpaso3')]")
        f.click_multiple('xpath', "//a[contains(@id,'ContentPlaceHolder1_lnSubirArchivo1')]")
        print("Se ha realizado un cargue.")
    except Exception as ex:
        print(ex)
        print("No se pudo ejecutar el test")


@pytest.mark.ltdoDeDmtos
def test_cuatro(driver):
    try:
        f = funciones_isolucion(driver)
        bt3 = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle'][contains(.,'Documentacion')]")
        bt3.click()
        btn4 = driver.find_element(By.XPATH,
                                   "(//div[contains(.,'Administración de los documentos del sistema de gestión.')])[4]")
        btn4.click()
        f.texto_multiple('xpath', "//input[contains(@id,'txtBuscarAZ')]", "DocumentoPruebaQA")
        f.click_multiple("xpath", "//input[contains(@id,'imbBuscarBuscardorAZ')]")
        f.click_multiple("id", "ContentPlaceHolder1_gvLista_imgVistaPrevia_0")
        print("Se realizo la vista previa del documento de forma exitosa")
        time.sleep(10)
    except Exception as ex:
        print(ex)
        print("No se pudo ejecutar el test")


@pytest.mark.ltdotareas
def test_cinco(driver):
    try:
        f = funciones_isolucion(driver)
        bt1 = driver.find_element(By.XPATH, "//a[contains(.,'Tareas')]")
        bt1.click()
        btn5 = driver.find_element(By.XPATH, "(//div[contains(.,'Listado de tareas')])[5]")
        btn5.click()
        f.click_multiple("xpath", "//a[contains(@id,'0')][@title='Descripcion de la tarea creada.'][contains(.,'PruebaQA5')]")
        f.texto_multiple("xpath", "//textarea[contains(@id,'ContentPlaceHolder1_txtObservaciones')]", "observacion de la tarea")
        f.check_multiple("xpath", "//input[contains(@id,'chkEstadoCierre')][@type='checkbox']")
        f.click_multiple("xpath", "//input[contains(@id,'ContentPlaceHolder1_btnGrabar')]")
        time.sleep(5)
        print("la tarea a sido gestionada con Exito")
    except Exception as ex:
        print(ex)
        print("No se pudo ejecutar el test")

@pytest.mark.prueba
def test_prueba(driver):
    print("prueba")

#Gina comentario
#Comentario 2
#comentario Diego

#Gina comentario
#Comentario 2

#diego
