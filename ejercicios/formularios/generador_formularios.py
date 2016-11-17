#!/usr/bin/env python3
#encoding=utf-8
from random import randint

FICHERO_OPCIONES = "opciones.txt"

RADIO_SIN_ID        ="<input type='radio' name='{0}' value='{2}'> {1} "
CHECKBOX_SIN_ID     ="<input type='checkbox' name='{0}' value='{2}'> {1} "
RADIO_CON_ID        ="<input type='radio' name='{0}' id='{2}' value='{3}'> {1} "
CHECKBOX_CON_ID     ="<input type='checkbox' name='{0}' id='{2} value='{2}''> {1} "
OPTION              ="<option value='{0}'>{1}</option>"
SELECT              ="<select name='{0}' {1}>"
LETRAS_PROHIBIDAS_EN_IDS                ="ÁÉÍÓÚáéíóúÑñ "
LETRAS_SUSTITUTAS_DE_PROHIBIDAS_EN_IDS  ="AEIOUaeiouNn_"
DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS=dict()


class GeneradorFormularios(object):
    def __init__(self):
        self.DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS=dict()
        for pos in range(0, len(LETRAS_PROHIBIDAS_EN_IDS)):
            letra_prohibida=LETRAS_PROHIBIDAS_EN_IDS[pos]
            letra_sustituta=LETRAS_SUSTITUTAS_DE_PROHIBIDAS_EN_IDS[pos]
            self.DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS[ord(letra_prohibida)]=letra_sustituta
        print (self.DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS)
    
    def get_lineas_fichero(self, nombre_fichero):
        lineas=[]
        f=open(nombre_fichero, "r", encoding="utf-8")
        lineas=f.readlines()
        lineas_sin_fin_de_linea=[]
        for l in lineas:
            lineas_sin_fin_de_linea.append ( l.strip() )
        return lineas_sin_fin_de_linea
    
    def get_linea_opciones(self):
        lineas=self.get_lineas_fichero(FICHERO_OPCIONES)
        num_azar=randint(0, len(lineas)-1)
        return lineas[num_azar]
    
    def generar_controles(self, cadena_control, con_fin_linea=True):
        html=""
        linea=self.get_linea_opciones()
        opciones=linea.split(":")
        for o in opciones[1:]:
            valor=o.lower()
            valor=valor.translate(self.DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS)
            valor=opciones[0]+"_"+valor
            if con_fin_linea:
                html+=cadena_control.format(opciones[0], o, valor) + "<br/>\n"
            else:
                html+=cadena_control.format(opciones[0], o, valor)
        return html
    
    def generar_radios(self, con_fin_linea=True):
        resultado= self.generar_controles ( RADIO_SIN_ID, con_fin_linea )
        return resultado
    
    def generar_checkboxes(self, con_fin_linea=True):
        resultado= self.generar_controles ( CHECKBOX_SIN_ID, con_fin_linea )
        return resultado
    
    def generar_options(self,  multiple=True):
        linea=self.get_linea_opciones()
        opciones=linea.split(":")
        
        if multiple:
            html=SELECT.format(opciones[0], "multiple='multiple'") 
        else:
            html=SELECT.format(opciones[0])
        html+="\n"
        for o in opciones[1:]:
            valor=opciones[0]+"_"+o
            id=o.lower()
            id=id.translate(self.DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS)
            html+=OPTION.format(id, o, id)  + "\n"
        html+="</select>\n"
        return html
    
    
g=GeneradorFormularios()

print (g.generar_radios())
print (g.generar_checkboxes())
print (g.generar_options())