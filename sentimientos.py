# -*- coding: utf-8 -*-
"""Sentimientos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ncZVuRTaSMNjyxD8Zxl1Jo2uRr06ENNB
"""

pip install TextBlob

from textblob import TextBlob

nombre = input("Hola, ¿Como te llamas? ")
print("Hola ",nombre, "estoy aquí para saber como te sientes hoy")
y = input("¿Cuentanos algun pensamiento que tengas?: ")
edu= TextBlob(y)
print(edu.translate(from_lang="es", to="en"))
edu2= edu.translate(from_lang="es", to="en")
x=edu2.sentiment.polarity

if x<0:
  
  print("Sentimientos:",x)
  print("Negativo 😕")
elif x==0:
  

  print("Sentimientos:",x)
  print("Neutral 🙃")
elif x>0:
  

  print("Sentimientos:",x)
  print("Positivo 😃")