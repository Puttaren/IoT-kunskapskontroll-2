# ---------- Test Rasberry Pi Pico W ----------
# Blink with LED - "Hello world" for IoT
from machine import Pin
led = Pin("LED", Pin.OUT)
led.value(1)
led.value(0)

