import cv2
import time

webcam = cv2.VideoCapture(0) #connectou

if webcam.isOpened(): # se entru a webcam
    validacao, frame = webcam.read() # passa os dados da função webcam para as variaveis validação é frame

    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("Video", frame)
        key = cv2.waitKey(5)
        if key == 27: #ESC
            break
    cv2.imwrite("Foto.png", frame) # salva o frame

webcam.release()
cv2.destroyAllWindows() #destroi a janela
        
    