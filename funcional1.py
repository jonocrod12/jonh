from selenium import webdriver
import time
import os
import sys

web = webdriver.Chrome()
web.get('https://appswls.entel.cl/ContratacionOnLineMovil/mis_pap_paso1?idPlan=P1928&paso=1A&origen=APP_Movil&_ga=')

#Temporizador para que deje cargar
time.sleep(2)

#Variables
RutVar = "200416759"
TelVar = "975660370"
EmailVar = "pepito@gmail.com"

CloseVent = web.find_element_by_xpath('//*[@id="formPaso1A"]/div[3]/div/div/div[1]/button')
confirmador = CloseVent.is_displayed()

#Verificador si hay ventana o no
if (confirmador==True):
    CloseVent.click() #Cierra ventana

time.sleep(3)

#Ingresa el codigo RUT
RutZone = web.find_element_by_xpath('//*[@id="rut"]')
RutZone.send_keys(RutVar)

#Ingresa el numero TEL
TelZone = web.find_element_by_xpath('//*[@id="telefono"]')
TelZone.send_keys(TelVar)

#Ingresa el correo
EmailZone = web.find_element_by_xpath('//*[@id="email"]')
EmailZone.send_keys(EmailVar)

time.sleep(1)

#TRY CATCH de RUT
error = web.find_element_by_xpath('//*[@id="formPaso1A"]/div[2]/div[2]/div/div').get_attribute("class")
print("------RUT------")
print(error)
if ((error) == "form-input error-input normal"):
    errores_rut = True
else:
    errores_rut = False

#TRY CATCH de TEL
error = web.find_element_by_xpath('//*[@id="formPaso1A"]/div[2]/div[3]/div/div').get_attribute("class")
print("------TEL------")
print(error)
if ((error) == "form-input error-input normal"):
    errores_tel = True
else:
    errores_tel = False

#Analitico logico (true = hay errores, false = no hay errores)
puente = (errores_rut == True or errores_tel == True)
print(puente)

#Submit
Siguiente = web.find_element_by_xpath('//*[@id="btnContinuar"]')
Siguiente.click()

