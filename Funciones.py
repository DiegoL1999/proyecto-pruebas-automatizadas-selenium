import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

Tiempo = .10


class funciones_isolucion():

    def __init__(self, driver):
        self.driver = driver

    def Navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        return t

    def SEX(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(((By.XPATH, elemento))))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def SEI(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(((By.ID, elemento))))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    def texto_multiple(self, tipo, elemento, texto, Tiempo=.1):
        if (tipo == "id"):
            try:
                val = self.SEI(elemento)
                val.clear()
                val.send_keys(texto)
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + elemento)
        elif (tipo == "xpath"):
            try:
                val = self.SEX(elemento)
                val.clear()
                val.send_keys(texto)
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + elemento)

    def click_multiple(self, tipo, elemento, Tiempo=.1):
        if (tipo == "xpath"):
            try:
                val = self.SEX(elemento)
                val.click()
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("Hay un problema con el boton" + elemento)
        elif (tipo == "id"):
            try:
                val = self.SEI(elemento)
                val.click()
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("Hay un problema con el boton")

    def check_multiple(self, tipo, elemtento, Tiempo=.1):
        if (tipo == "xpath"):
            try:
                val = self.SEX(elemtento)
                val.click()
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("Hay un problema con el check")
        elif (tipo == "id"):
            try:
                val = self.SEI(elemtento)
                val.click()
                print("Click en el elemenento {} ".format(elemtento))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("Hay un problema con el check")

    def select_xpath_type(self, formato, tipo, elemento, dato, Tiempo=.1):
        if (formato == "xpath"):
            try:
                val = self.SEX(elemento)
                val = Select(val)
                if (tipo == "text"):
                    val.select_by_visible_text(dato)
                elif (tipo == "index"):
                    val.select_by_index(dato)
                elif (tipo == "value"):
                    val.select_by_value(dato)
                print("El campo seleccionado es {} ".format(dato))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("Hay un problema con la lista")
        elif (formato == "id"):
            try:
                val = self.SEI(elemento)
                val = Select(val)
                if (tipo == "text"):
                    val.select_by_visible_text(dato)
                elif (tipo == "index"):
                    val.select_by_index(dato)
                elif (tipo == "value"):
                    val.select_by_value(dato)
                print("El campo seleccionado es {} ".format(dato))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("Hay un problema con la lista")

    def Mouse_doble(self, tipo, selector, tiempo=2):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("double click en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(((By.ID, selector))))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Haciendo doble clic en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def clic_XY(self, tipo, selector, x, y, tiempo=2):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.move_by_offset(val, x, y).click().perform()
                print("clic al elemento{} coordenada{}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(((By.ID, selector))))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                act = ActionChains(self.driver)
                act.move_by_offset(val, x, y).click().perform()
                print("clic al elemento{} coordenada{}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
