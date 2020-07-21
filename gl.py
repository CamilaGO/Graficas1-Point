"""
Paula Camila Gonzalez Ortega
18398
"""
from funciones_gl import Render, changecolor

posX = 250
posY = 250
width = 1000
height = 1000

bitmap = Render(width, height) #los ultimos tres son los colores son los del background

bitmap.glViewPort(posX, posY, width - 500 , height - 500)

bitmap.glClearColor(0, 0, 0)
bitmap.glclear()

bitmap.glColor(1, 0, 0) #estos colores son los que se usaran en Vertex

bitmap.glVertex(0, 0)

bitmap.finish('out.bmp')




