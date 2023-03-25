import tkinter as tk
from tkinter import *
import time
import math

window = tk.Tk()
window.title("Analog Clock")
window.geometry("400x400")

def draw_clock(hour, minute, second, radius):
    canvas.create_oval(100, 100, 300, 300, outline='black', width=2)
    # Dessinez les marques de l'heure
    for i in range(12):
        angle = math.pi/6 * i
        x = math.cos(angle) * (radius - 20) + 200
        y = math.sin(angle) * (radius - 20) + 200
        canvas.create_text(x, y, text=str(i+1), font=("Arial", 12, "bold"))
    
    # Dessinez les aiguilles de l'horloge
    h_angle = (hour + minute/60) * (math.pi/6) - math.pi/2
    m_angle = (minute + second/60) * (math.pi/30) - math.pi/2
    s_angle = second * (math.pi/30) - math.pi/2
    
    # Aiguille de l'heure
    canvas.create_line(200, 200, 200 + math.cos(h_angle) * radius * 0.5, 200 + math.sin(h_angle) * radius * 0.5, width=4, fill='black')
    
    # Aiguille des minutes
    canvas.create_line(200, 200, 200 + math.cos(m_angle) * radius * 0.7, 200 + math.sin(m_angle) * radius * 0.7, width=3, fill='black')
    
    # Aiguille des secondes
    canvas.create_line(200, 200, 200 + math.cos(s_angle) * radius * 0.7, 200 + math.sin(s_angle) * radius * 0.7, width=1, fill='red')

canvas = tk.Canvas(window, bg='white', height=400, width=400)
canvas.pack()
draw_clock(0, 0, 0, 100)

while True:
  current_time = time.strftime("%I:%M:%S")
  hour, minute, second = map(int, current_time.split(":"))
  if not window.winfo_exists():
      break # sortir de la boucle si la fenêtre est fermée
  canvas.delete("all")
  draw_clock(hour, minute, second, 100)
  window.update()
  time.sleep(1)


window.mainloop()
