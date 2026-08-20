import random
import winsound
import wave
import math

f = ["If the second note feels lighter, it's higher. If it feels heavier, it's lower!",
    "Try humming both notes back-to-back to feel which way the sound moves!",
    "Lock in the first note, then listen if the second one goes up or down!",
    "Slide your voice from note A to B—did you climb up or drop down?",
    "Brighter sounds are usually higher; deeper sounds are lower!",
    "Feel the buzz: higher notes hit your head, lower notes hit your chest!",
    "Try singing along—does your voice have to reach up or dip down?"]



def note_to_freq(n):
    return 440 * 2 ** (n / 12)

score = 0
total = 5
RATE = 44100
level = input("Pick easy, medium, or hard: ")
if level=="easy":
    y=[-9,-8,9,8,-7,7,10,-10]
elif level=="medium":
    y=[5,6,-6,-5,4,-4]
else:
    y = [1,2,-2,-1,3,-3]
for round_number in range(total):
    note1 = random.choice(y)
    gap = random.choice(y)
    note2 = note1 + gap

    beep = wave.open("beep.wav", "wb")
    beep.setnchannels(1)
    beep.setsampwidth(2)
    beep.setframerate(RATE)
    data = bytearray()
    for i in range(int(RATE * 0.6)):
        angle = 2 * math.pi * note_to_freq(note1) * (i / RATE)
        data += int(math.sin(angle) * 20000).to_bytes(2, "little", signed=True)
    for i in range(int(RATE * 0.6)):
        angle = 2 * math.pi * note_to_freq(note2) * (i / RATE)
        data += int(math.sin(angle) * 20000).to_bytes(2, "little", signed=True)
    beep.writeframes(data)
    beep.close()

    winsound.PlaySound("beep.wav", winsound.SND_FILENAME)

    answer = input("Pebbles asks: 'Was note 2 higher or lower?' ")

    if gap > 0:
        correct = "higher"
    else:
        correct = "lower"

    if answer.lower() == correct:
        print("Pebbles says: 'Correct! Good job!'")
        score += 1
    else:
        g = random.choice(f)
        print(f"Pebbles says: 'Not quite! But that's ok! Here is a tip: {g}'")
        print("Pebbles says: 'Here it is again, slower...'")

        beep = wave.open("beep_slow.wav", "wb")
        beep.setnchannels(1)
        beep.setsampwidth(2)
        beep.setframerate(RATE)
        data = bytearray()
        for i in range(int(RATE * 1.5)):
            angle = 2 * math.pi * note_to_freq(note1) * (i / RATE)
            data += int(math.sin(angle) * 20000).to_bytes(2, "little", signed=True)
        for i in range(int(RATE * 1.5)):
            angle = 2 * math.pi * note_to_freq(note2) * (i / RATE)
            data += int(math.sin(angle) * 20000).to_bytes(2, "little", signed=True)
        beep.writeframes(data)
        beep.close()

        winsound.PlaySound("beep_slow.wav", winsound.SND_FILENAME)

        answer2 = input("Pebbles says: 'Now try again! Is it higher or lower? Take your time. ' ")

        if answer2.lower() == correct:
            print("Pebbles says: 'Yes! You heard it that time! 🌸'")
            score += 0.5
        else:
            print(f"Pebbles says: 'It was {correct}. But that's ok, mistakes help you learn!'")

print(f"You scored {score} out of {total}!")