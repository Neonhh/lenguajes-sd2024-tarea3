
import pytest
from funciones import tipos, registro

ATOMIC = 0
REGISTRO = 1
REGISTRO_VARIANTE = 2

def test_guardar_tipo_atomico():
    # Limpiar el diccionario de tipos antes de cada test
    tipos.clear()
    
    # Guardar un tipo atómico
    nombre = "int"
    representacion = 4
    alineacion = 4
    tipos[nombre] = [ATOMIC, int(representacion), int(alineacion)]
    
    assert nombre in tipos
    assert tipos[nombre] == [ATOMIC, representacion, alineacion]

def test_registro():
    # Limpiar el diccionario de tipos antes de cada test
    tipos.clear()
    
    # Definir tipos atómicos
    tipos["int"] = [ATOMIC, 4, 4]
    tipos["float"] = [ATOMIC, 8, 8]
    
    # Crear un registro
    nombre = "miRegistro"
    elementos = ["int", "float"]
    esVariante = False
    registro(nombre, elementos, esVariante)
    
    assert nombre in tipos
    assert tipos[nombre][0] == REGISTRO
    assert tipos[nombre][1] == [4, 8]
    assert tipos[nombre][2] == [4, 8]

def test_registro_variante():
    # Limpiar el diccionario de tipos antes de cada test
    tipos.clear()
    
    # Definir tipos atómicos
    tipos["int"] = ["atomic", 4, 4]
    tipos["float"] = ["atomic", 8, 8]
    
    # Crear un registro variante
    nombre = "miRegistroVariante"
    elementos = ["int", "float"]
    esVariante = True
    registro(nombre, elementos, esVariante)
    
    assert nombre in tipos
    assert tipos[nombre][0] == REGISTRO_VARIANTE
    assert tipos[nombre][1] == [4, 8]
    assert tipos[nombre][2] == [4, 8]

if __name__ == "__main__":
    pytest.main()