from machine import Pin, ADC
import utime

# --- Inställningar ---
# Fysiskt stift 34 är GPIO 28 (ADC kanal 2)
mic_analog = ADC(Pin(28))
mic_digital = Pin(15, Pin.IN) 

# Omvandlingsfaktor: 3.3V dividerat med maxvärdet för 16-bit (65535)
conversion_factor = 3.3 / 65535

print("Startar löpande spänningsmätning...")
print("Tips: Öppna 'Plotter' i Thonny för att se grafen!")
print("-" * 30)

try:
    while True:
        # Läs råvärdet (0-65535)
        raw_value = mic_analog.read_u16()
        #raw_value = mic_digital.value()
        
        # Räkna om till Volt
        voltage = raw_value * conversion_factor
        
        # Skriv ut värdet så att Plottern kan rita det
        # (Vi skriver ut bara siffran för att grafen ska bli ren)
        print((raw_value,))
        
        # En mycket kort paus för att inte överbelasta konsolen
        # 0.01s ger 100 mätningar i sekunden
        utime.sleep(2)

except KeyboardInterrupt:
    print("\nMätning avslutad.")