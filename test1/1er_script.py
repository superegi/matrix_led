#!/usr/bin/env python
 
import max7219.led as led
import max7219.transitions as transitions
 
led.init()
 
#Mensaje en scroll de abajo a arriba
led.show_message("Hola que tal estas?", transition = transitions.up_scroll)
#Mensaje en scroll de derecha a izquierda
led.show_message("Hola que tal estas?", transition = transitions.left_scroll)
#Mensaje mostrando caracteres uno a uno
led.show_message("Hola que tal estas?", transition = transitions.simple)
 
#Apagamos todos los LEDs
led.letter(0)