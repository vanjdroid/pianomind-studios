import wave
import math

RATE = 44100
beep = wave.open("beep.wav", "wb")
beep.setnchannels(1)
beep.setsampwidth(2)
beep.setframerate(RATE)

data = bytearray()
for i in range(int(RATE * 1)):
    angle = 2 * math.pi * 440 * (i / RATE)
    height = math.sin(angle)
    data += int(height * 20000).to_bytes(2, "little", signed=True)

beep.writeframes(data)
beep.close()

import os
os.startfile("beep.wav")
