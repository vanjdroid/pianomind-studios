import random
import winsound
import wave
import math
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
def note_to_freq(n):
    return 440 * 2 ** (n / 12)

def note_reader():
    a=["The notes in Treble clef spell out 'FACE' in the gaps, and in the bass clef they spell 'ACEG'!","Try looking at the piano and counting up or down the note from a note you can read!","Remember the sentence 'Eating Green Broccoli Defeats Flu' (which is true, Pebble adds) for each letter on the lines of the treble clef, and for bass clef remember 'Grizzly Bears Don't Fear Anything' (true in some cases, Pebble says)!"]
    treble_names = ["c", "d", "e", "f", "g", "a", "b", "c", "d", "e", "f", "g", "a"]
    bass_names   = ["e", "f", "g", "a", "b", "c", "d", "e", "f", "g", "a", "b", "c"]
    heights      = [-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]    
    score = 0
    total = 5
    level=input("Pebbles says:'Now, pick the level you want to play: 1 for easy, 2 for medium, or 3 for hard!'")
    if level == "1":
        clef_pick = input("Pebbles says:'Which clef? 1 for treble, 2 for bass'")
        if clef_pick == "1":
            clef = "treble"
        else:
            clef = "bass"
    for round_number in range(total):
        if level=="1":
            spot = random.randint(1, 11)
            
        elif level=="2":
            clef = random.choice(["treble", "bass"])
            spot = random.randint(0, 12)
        else:
            clef = random.choice(["treble", "bass"])
            spot = random.randint(0, 16)
            treble_names = ["a", "b", "c", "d", "e", "f", "g", "a", "b", "c", "d", "e", "f", "g", "a", "b", "c"]
            bass_names = ["c", "d", "e", "f", "g", "a", "b", "c", "d", "e", "f", "g", "a", "b", "c", "d", "e"]
            heights = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
        plt.figure(facecolor="#a2cafb")
        plt.gca().set_facecolor("#a2cafb")
        plt.gca().add_patch(Rectangle((-2, -3), 6, 10, color="#95b3d8", zorder=0))
        b = random.choice(a)
        
        if clef == "treble":
            names = treble_names
            clef="treble"
        else:
            names = bass_names
            clef="bass"

        
        note_name = names[spot]
        note_height = heights[spot]
        if level=="1":
            accidental="natural"
        else:
            accidental = random.choice(["flat", "sharp","natural"])
        full_name = note_name
        if accidental == "sharp":
            full_name = note_name + "#"
        elif accidental == "flat":
            full_name = note_name + "b"
        
        for height in range(5):
            plt.axhline(y=height, color="black", linewidth=2)
        if accidental == "sharp":
            plt.text(0.35, note_height + 0.15, "#", fontsize=40, ha="center", va="center", color="black")   
        plt.gca().add_patch(Ellipse((1, note_height), width=0.45, height=0.9, color="black"))
        if accidental == "flat":
            plt.text(0.35, note_height, r"$\flat$", fontsize=40, ha="center", va="center", color="black")
        if note_height == -1 or note_height == 5:
            plt.plot([0.6, 1.4], [note_height, note_height], color="black", linewidth=2)
        if note_height <= -1:
            plt.plot([0.6, 1.4], [-1, -1], color="black", linewidth=2)
        if note_height <= -2:
            plt.plot([0.6, 1.4], [-2, -2], color="black", linewidth=2)
        if note_height >= 5:
            plt.plot([0.6, 1.4], [5, 5], color="black", linewidth=2)
        if note_height >= 6:
            plt.plot([0.6, 1.4], [6, 6], color="black", linewidth=2)
        plt.axis("off")
        plt.xlim(-1, 3)
        plt.ylim(-3, 7)
        plt.title(f"{clef} clef", fontname="Bauhaus 93", fontsize=40)
        plt.savefig(f"note{round_number}.png", facecolor="lightblue")
        plt.close()
        os.startfile(f"note{round_number}.png")

        answer = input(f"Pebbles asks: what note is this in {clef} clef? (type the letter) ")
        answer = answer.lower().replace(" ", "").replace("sharp", "#").replace("flat", "b")
        if answer == full_name:
            print("Pebbles says: 'Yes! 🌸'")
            score += 1
        else:
            print(f"Pebbles says: 'This note is {full_name}! It's ok to make mistakes. Here is a tip: {b}'")

    print(f"Pebbles says: 'You scored {score} out of our daily 5!'")

def ear_trainer():
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
    level=input("Pebbles says:'Now, pick the level you want to play: 1 for easy, 2 for medium, or 3 for hard!'")
    if level=="1":
        y=[-9,-8,9,8,-7,7,10,-10]
    elif level=="2":
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


playing = True
while playing:
    name=input("Welcome to PianoMind Studios! What is you name?")
    choice = input(f"Pebbles says: 'Nice name : {name}! I like it! Now {name}, what do you want to play? If you want to play the note-reading game, type 1! If you want to play the ear training game, you can type 2!'")
    if choice == "1":
        note_reader()
    elif choice=="2":
        ear_trainer()
    else:
        print("Pebbles says:'I think you meant something else! We'll play ear-trainer for now!'")
        ear_trainer()
    again = input(f"Pebbles asks:'Do you want to play again, {name}?'(type y if yes and n if no)")
    if again.lower() != "y":
        playing = False

print(f"Pebbles says: 'See you next time {name}!'")
