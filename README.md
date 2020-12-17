# ProyectoPython

## Nos encontramos ante un proyecto desarrollado para python 3.9, para la gestión de un parking.
## Se trata de una aplicación desarrollada con tkinter en el que usamos una extensión llamada tkcalendar en este caso la versión 1.6.1.
## Utilizamos SQLAlchemy como orm dónde guardamos los datos en un fichero usando sqlite (version 1.3.20).
## He implementado también una versión de prueba en el almacenamiento de vehículo para los no abonados en el cuál se le la matricula desde una imagen.
### Este proceso no está terminado por eso solo incluye la versión de pruebas con una imagen.
### Solo acepta imagenes tomadas desde una misma perspectiva puesto que no se ha aplicado nada de machine learning.
### Las técnologías necesarias para llevar a cabo esto es el siguiente:
* Instalacion de OpenCV para python  pip install opencv-python
* Instalacion de Tesseract-OCR desde  https://github.com/UB-Mannheim/tesseract/wiki
* Instalacion de pytesseract 
* En window tendremos que definir donde encontramos tesseract-ocr agregando la linea pytesseract.pytesseract.tesseract_cmd = r'<Ruta>' tras las importaciones
  
#### ¿Qué proceso utilizamos para leer la imagen?
1. Importamos cv2 de openCV y pytesseract 
2. Agregamos la línea pytesseract.pytesseract.tesseract_cmd = r'<Ruta>' (si usamos windows)
3. Declaramos placa un array vacío que nos permitirá almacenar la imagen a la matrícula encontrada. Esto lo veremos luego.
4. Leemos la imagen usando openCV (cv2.imread('ruta'))
5. Transformamos la imagen a escala de grises utilizando cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
6. Le aplicamos blur para eliminar el ruido cv2.blur(gray,(3,3))
7. Buscamos los bordes de la imagen utilizando la funcion canny de openCV cv2.Canny(gray,150,200) y le aplicamos una dilatacion para que sean mas evidentes cv2.dilate(canny,None,iterations=1)
8. Buscamos los contornos de la matricula usando cv2.findContours
9. A continuacion dibujamos los contornos 
10. Determinamos su área y encontramos la matricula del vehículo
11. Con este proceso abriamos obtenido la placa
12. Ahora tendremos que aplicar OCR que es el reconocimiento optico de caracteres en una imagen, por ello instalamos Tesseract-OCR que usaremos a través de  pytesseract
13. Obtenemos sus caracteres y digitos en base al área obtenida anteriormente y los guardamos en placa
