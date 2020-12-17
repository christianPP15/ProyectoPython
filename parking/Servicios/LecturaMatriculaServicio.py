import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def obtenerMatricula(ruta):
  placa = []

  image = cv2.imread(ruta)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  gray = cv2.blur(gray,(3,3))
  canny = cv2.Canny(gray,150,200)
  canny = cv2.dilate(canny,None,iterations=1)

  #_,cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
  cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
  #cv2.drawContours(image,cnts,-1,(0,255,0),2)

  for c in cnts:
    area = cv2.contourArea(c)

    x,y,w,h = cv2.boundingRect(c)
    epsilon = 0.09*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)

    if len(approx)==4 and area>9000:
      #cv2.drawContours(image,[approx],0,(0,255,0),3)

      aspect_ratio = float(w)/h
      if aspect_ratio>2.4:

        placa = gray[y:y+h,x:x+w]
        text = pytesseract.image_to_string(placa,config='--psm 11')


  cv2.moveWindow('Image',45,10)
  cv2.waitKey(0)
  return text
