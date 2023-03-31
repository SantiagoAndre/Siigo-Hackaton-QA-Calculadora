

## Hackaton QA Prueba de calculadora

### Integrantes

Santiago Ramirez
Oscar Daniel Mejia


### Tecnologias utilizadas

1. Python
2. Selenum Python
2. Unittest Python

### Requerimientos

```pip install requirements.txt`


### Estructura del proyecto
Los dos archivos principales son:
1. test_api.py: Tests del API
2. test_selenium.py: Test de la interfaz con selenium
3. gateway: En esta carpeta se encuentran dos archivos encargados de comunicarse con la calculadora a traves del API, y la intefaz grafica

### Como ejecutar las pruebas

1. Ejecutar pruebas de API: `python test_api.py`
1. Ejecutar pruebas de la interfaz: `python test_selenium.py`


### Evidencias

Casos de pruebas ejecutados:

A nivel de API se ejecutaron diferentes pruebas como:
-  divicion por 0:
    - Comportamiento esperado:
        Mensaje de error: Attempted to divide by zero.
    - Resultado: Exitoso
-  Enviar letras y no numeros:
    - Comportamiento esperado:
        status code: 400
    - Resultado: Exitoso
-  Enviar numeros de mas de 22 digitos:
    - Comportamiento esperado:
        status code: 400
        mensaje de error: 
    - Resultado: Fallido, la calculadora retorno un error




La interfaz no muestra mensajes de error, a nivel de Interfaz se ejecutaron diferentes pruebas:

-  Validar funcionamiento del display: Al oprimir un boton debe aparecer el simbolo correspondiente en la interfaz
    - Proceso: Oprimir boton 3
    - Comportamiento esperado: Aparece el 3 en el display
    - Resultado: Exitoso
-  Validar operacion suma: 
    - Proceso: Se oprime la tecla 3 , luego +, luego 3, luego igual.
    - Comportamiento esperado: Aparece el 6 en el display
    - Resultado: Exitoso

-  Validar operacion multiplicar: 
    - Proceso: Se oprime la tecla 3 , luego *, luego 3, luego igual.
    - Comportamiento esperado: Aparece el 9 en el display
    - Resultado: Exitoso

-  Validar operacion resta: 
    - Proceso: Se oprime la tecla 3 , luego -, luego 3, luego igual.
    - Comportamiento esperado: Aparece el 0 en el display
    - Resultado: Exitoso


-  Validar operacion divicion: 
    - Proceso: Se oprime la tecla 6 , luego /, luego 3, luego igual.
    - Comportamiento esperado: Aparece el 2 en el display
    - Resultado: Exitoso

-  Ejecutar operacion imcompleta y oprimir igual: 
    - Proceso: Se oprime la tecla 6 , luego /, luego igual.
    - Comportamiento esperado: Se desactiva el boton '='
    - Resultado: Exitoso
-  Validar  divicion por 0: 
    - Proceso: Se oprime la tecla 9, luego 9  , luego /, luego 0, luego igual.
    - Comportamiento esperado: Aparece un 0 en la pantalla(Aqui deberia mostrar un error o algo parecido)
    - Resultado: Exitoso


### Como funcionan las pruebas de selenium.

Al lanzar los tests de selenium pasa lo siguiente:

1. Se abre el navegador en la paginad e la calculadora
2. Se obtienen todos los botones y se valida que bonton es(si es 0, 1, +, *), y se guardan en un diccionario.
3. Inician las pruebas, usando el gateway de la calculadora, aqui ya se hacen pruebas como la siguiente:

```py
    def test_case_8(self):
        '''El usuario intenta hacer una divicion por 0'''
        # Oprime dos veces el boton 9
        self.calculator.input_number(99)
        # Oprime el boton dividir
        self.calculator.press_button("/")
        # Oprime el boton 0
        self.calculator.press_button("0")
        # Oprime el boton igual
        self.calculator.operate()
        # Obtiene el valor que esta en el display de la calculadora
        display = self.calculator.get_display()
        # Ejecuta el assert de la prueba
        self.assertEqual(display,"0") 
```