import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:    # Захватываем кадр с веб-камеры
    ret, frame = cap.read()
    # Преобразуем кадр в черно-белое изображение
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Находим контуры белых объектов на изображении
    _, threshold = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)
    cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    