import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import random
import os

a=["The notes in Treble clef spell out 'FACE' in the gaps, and in the bass clef they spell 'ACEG'!","Try looking at the piano and counting up or down the note from a note you can read!","Remember the sentence 'Eating Green Broccoli Defeats Flu' (which is true, Pebble adds) for each letter on the lines of the treble clef, and for bass clef remember 'Grizzly Bears Don't Fear Anything' (true in some cases, Pebble says)!"]
treble_names = ["c", "d", "e", "f", "g", "a", "b", "c", "d", "e", "f", "g", "a"]
bass_names   = ["e", "f", "g", "a", "b", "c", "d", "e", "f", "g", "a", "b", "c"]
heights      = [-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
score = 0
total = 5
level=input("pick easy, medium, or hard.")

if level == "easy":
    clef = input("Treble or bass? ")
for round_number in range(total):
    if level=="easy":
        spot = random.randint(1, 11)
        clef = input("Treble or bass? ")
    elif level=="medium":
        clef = random.choice(["treble", "bass"])
        spot = random.randint(0, 12)
    else:
        clef = random.choice(["treble", "bass"])
        spot = random.randint(0, 12)
    plt.figure(facecolor="#a2cafb")
    plt.gca().set_facecolor("#a2cafb")
    plt.gca().add_patch(Rectangle((-2, -3), 6, 10, color="#95b3d8", zorder=0))
    b = random.choice(a)
    
    if clef == "treble":
        names = treble_names
    else:
        names = bass_names

    
    note_name = names[spot]
    note_height = heights[spot]
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
    plt.axis("off")
    plt.xlim(-1, 3)
    plt.ylim(-2, 6)
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