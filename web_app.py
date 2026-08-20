"""
🎹 Piano Mind Studios — Web App
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Game logic by Amaya
Streamlit UI wrapper = given boilerplate

Run with:  streamlit run web_app.py
"""

import streamlit as st
import random
import math
import wave
import io
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import matplotlib.image as mpimg

# ── Page setup ──
st.set_page_config(page_title="Piano Mind Studios", page_icon="🎹")

# ── Pebbles images (Amaya's character, rendered via ChatGPT) ──
def pebbles(mood, width=150):
    """Show Pebbles the dino mascot. mood = 'asking', 'thinking', or 'happy'."""
    path = os.path.join(os.path.dirname(__file__), f"pebbles_{mood}.png")
    if os.path.exists(path):
        st.image(path, width=width)


# ── Amaya's color palette ──
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700&display=swap');

    /* ── Hide Streamlit chrome (menu, footer, header bar) ── */
    #MainMenu, footer, header[data-testid="stHeader"] {
        display: none !important;
    }

    /* Baby blue sky with clouds */
    .stApp {
        background-color: #a2cafb;
        background-image:
            radial-gradient(ellipse 120px 60px at 15% 20%, rgba(255,255,255,0.7) 0%, transparent 100%),
            radial-gradient(ellipse 90px 45px at 18% 22%, rgba(255,255,255,0.5) 0%, transparent 100%),
            radial-gradient(ellipse 150px 70px at 75% 15%, rgba(255,255,255,0.6) 0%, transparent 100%),
            radial-gradient(ellipse 100px 50px at 78% 13%, rgba(255,255,255,0.4) 0%, transparent 100%),
            radial-gradient(ellipse 110px 55px at 45% 35%, rgba(255,255,255,0.5) 0%, transparent 100%),
            radial-gradient(ellipse 130px 65px at 90% 45%, rgba(255,255,255,0.5) 0%, transparent 100%);
        background-attachment: fixed;
    }

    /* ── Smooth everything ── */
    * { transition: all 0.2s ease !important; }

    /* ── Center content + comfortable width ── */
    .block-container {
        max-width: 600px !important;
        padding: 2rem 1.5rem 4rem 1.5rem !important;
    }

    /* Soft rounded font + dark text */
    .stApp, .stApp p, .stApp label, .stApp span, .stApp div {
        font-family: 'Quicksand', sans-serif !important;
        color: #1a2a3a !important;
    }
    h1, h2, h3 {
        font-family: 'Quicksand', sans-serif !important;
        color: #0f2744 !important;
    }
    h1 { font-size: 2.2rem !important; margin-bottom: 0.3rem !important; }
    .stMarkdown strong {
        color: #0f2744 !important;
    }

    /* ── Pebbles image: centered ── */
    [data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
        background: transparent !important;
    }

    /* ── Buttons: default = lilac, pill-shaped ── */
    .stButton > button {
        background: #c1c3ea !important;
        color: #2c3e50 !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.8rem 1.8rem !important;
        font-weight: 700 !important;
        font-size: 1.08rem !important;
        font-family: 'Quicksand', sans-serif !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.10) !important;
        letter-spacing: 0.3px !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 6px 18px rgba(0,0,0,0.15) !important;
        background: #e1bcd8 !important;
    }
    .stButton > button:active {
        transform: translateY(0) scale(0.98) !important;
    }

    /* Column buttons get different colors */
    [data-testid="stColumn"]:first-child .stButton > button {
        background: #a2cafb !important;
    }
    [data-testid="stColumn"]:first-child .stButton > button:hover {
        background: #c1c3ea !important;
    }
    [data-testid="stColumn"]:nth-child(2) .stButton > button {
        background: #b2ebd8 !important;
    }
    [data-testid="stColumn"]:nth-child(2) .stButton > button:hover {
        background: #a2cafb !important;
    }
    [data-testid="stColumn"]:nth-child(3) .stButton > button {
        background: #f7b0a6 !important;
    }
    [data-testid="stColumn"]:nth-child(3) .stButton > button:hover {
        background: #e1bcd8 !important;
    }

    /* ── Text input: soft pill ── */
    .stTextInput > div > div > input {
        border-radius: 20px !important;
        border: 2px solid #c1c3ea !important;
        background-color: rgba(255,255,255,0.5) !important;
        font-family: 'Quicksand', sans-serif !important;
        font-size: 1.05rem !important;
        color: #1a2a3a !important;
        padding: 0.6rem 1rem !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #a5a7d4 !important;
        background-color: rgba(255,255,255,0.75) !important;
        box-shadow: 0 0 12px rgba(193, 195, 234, 0.4) !important;
    }
    .stTextInput label {
        font-weight: 700 !important;
    }

    /* ── Staff image: transparent background ── */
    .stPlotlyChart, iframe[title="st.pyplot"] {
        background: transparent !important;
    }

    /* ── Progress bar: pastel gradient, rounded ── */
    .stProgress > div > div {
        border-radius: 10px !important;
        overflow: hidden !important;
    }
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #b2ebd8, #a2cafb, #c1c3ea, #e1bcd8) !important;
        border-radius: 10px !important;
    }

    /* ── Alert boxes: glass-card style ── */
    [data-testid="stAlert"] {
        border-radius: 18px !important;
        font-family: 'Quicksand', sans-serif !important;
        backdrop-filter: blur(8px) !important;
        border: 1px solid rgba(255,255,255,0.3) !important;
    }

    /* ── Audio player: blend in ── */
    .stAudio {
        opacity: 0.85;
        border-radius: 12px !important;
        overflow: hidden !important;
    }

    /* ── Caption text ── */
    .stCaption, [data-testid="stCaptionContainer"] {
        color: #6b7fa3 !important;
        font-size: 0.85rem !important;
    }

    /* ── Columns: even spacing ── */
    [data-testid="stHorizontalBlock"] {
        gap: 0.8rem !important;
    }

    /* ── Markdown text: comfortable line height ── */
    .stMarkdown p {
        line-height: 1.6 !important;
        font-size: 1.05rem !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Amaya's formula ──
def note_to_freq(n):
    return 440 * 2 ** (n / 12)

# ── Sound maker (given plumbing) ──
@st.cache_data
def make_sound(n1, n2, speed):
    RATE = 44100
    buf = io.BytesIO()
    wf = wave.open(buf, "wb")
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(RATE)
    data = bytearray()
    for note in [n1, n2]:
        freq = note_to_freq(note)
        for i in range(int(RATE * speed)):
            angle = 2 * math.pi * freq * (i / RATE)
            sample = int(math.sin(angle) * 20000)
            data += sample.to_bytes(2, "little", signed=True)
    wf.writeframes(data)
    wf.close()
    buf.seek(0)
    return buf.read()

# ── Staff drawer (given plumbing, Amaya's colors) ──
def draw_staff(note_height, accidental, clef):
    fig, ax = plt.subplots(figsize=(5, 4))
    fig.patch.set_alpha(0)
    ax.set_facecolor("#a2cafb")
    for line in range(5):
        ax.axhline(y=line, color="black", linewidth=2)
    if accidental == "sharp":
        ax.text(0.35, note_height + 0.15, "#",
                fontsize=40, ha="center", va="center", color="black")
    elif accidental == "flat":
        ax.text(0.35, note_height, r"$\flat$",
                fontsize=40, ha="center", va="center", color="black")
    ax.add_patch(Ellipse((1, note_height), width=0.45, height=0.9, color="black"))
    # Ledger lines
    if note_height <= -1:
        ax.plot([0.6, 1.4], [-1, -1], color="black", linewidth=2)
    if note_height <= -2:
        ax.plot([0.6, 1.4], [-2, -2], color="black", linewidth=2)
    if note_height >= 5:
        ax.plot([0.6, 1.4], [5, 5], color="black", linewidth=2)
    if note_height >= 6:
        ax.plot([0.6, 1.4], [6, 6], color="black", linewidth=2)
    ax.axis("off")
    ax.set_xlim(-1, 3)
    ax.set_ylim(-3, 7)
    ax.set_title(f"{clef.title()} Clef", fontsize=28, fontweight="bold", color="#2c5f8a")
    plt.tight_layout()
    return fig


# ═══════════════════════════════════
#  AMAYA'S GAME DATA
# ═══════════════════════════════════

EAR_TIPS = [
    "If the second note feels lighter, it's higher. If it feels heavier, it's lower!",
    "Try humming both notes back-to-back to feel which way the sound moves!",
    "Lock in the first note, then listen if the second one goes up or down!",
    "Slide your voice from note A to B — did you climb up or drop down?",
    "Brighter sounds are usually higher; deeper sounds are lower!",
    "Feel the buzz: higher notes hit your head, lower notes hit your chest!",
    "Try singing along — does your voice have to reach up or dip down?",
    "Close your eyes and imagine stairs. Did the sound go up the stairs or down?",
    "Think of a bird flying — did it fly up to the sky or swoop down?",
    "Pretend the notes are on a slide. Did you go up the ladder or down the slide?",
    "Hum the first note, then the second. Your throat knows the answer!",
    "Higher notes feel tighter, lower notes feel more relaxed. Which one was it?",
    "Imagine you're on a roller coaster. Did it go up the hill or down?",
    "Picture a bouncing ball — did it bounce UP or fall DOWN?",
    "Listen for the energy. Higher = more sparkly, lower = more rumbly!",
]

NOTE_TIPS = [
    "The notes in Treble clef spell out 'FACE' in the gaps!",
    "In bass clef the gaps spell 'ACEG' — All Cows Eat Grass!",
    "Try counting up or down from a note you already know!",
    "Treble lines: Every Green Broccoli Defeats Flu (E G B D F)!",
    "Bass lines: Grizzly Bears Don't Fear Anything (G B D F A)!",
    "Middle C sits on its own little ledger line below treble or above bass!",
    "Notes go in alphabetical order: A B C D E F G, then start over!",
    "If the note is ON a line, it's a line note. If it's BETWEEN lines, it's a space note!",
    "Sharps (#) raise a note by one tiny step. Flats (b) lower it by one tiny step!",
    "Lines and spaces go up the alphabet as you go UP the staff!",
    "The bottom line of treble clef is always E. Count up from there!",
    "The bottom line of bass clef is always G. Count up from there!",
    "If a note has a ledger line, count from the nearest staff line to figure it out!",
    "Notes that look higher on the staff sound higher on the piano!",
]

# ── Pebbles random dialogue ──
PEBBLES_YAY_EAR = [
    "Nailed it! You're on fire!",
    "Yes yes yes! That's the one!",
    "Woo-hoo! Pebbles is so proud!",
    "Correct! Your ears are superb!",
    "Ding ding ding! You heard it!",
    "Amazing! Keep that streak going!",
    "That's right! You're a natural listener!",
    "Your ears are like radar! Nice!",
    "Pebbles can't believe how good you are!",
    "You're hearing things Pebbles can't even hear!",
    "Music genius alert!",
    "Spot on! Those ears don't miss a thing!",
]
PEBBLES_YAY_NOTE = [
    "Nailed it! You're on fire!",
    "Yes yes yes! That's the one!",
    "Woo-hoo! Pebbles is so proud!",
    "Correct! Your eyes are sharp!",
    "Ding ding ding! You got it!",
    "Amazing! You really know your notes!",
    "That's right! You're a natural reader!",
    "You read that staff like a book!",
    "Pebbles can't believe how fast you got that!",
    "Note master! Nothing gets past you!",
    "You're reading music like a pro!",
    "Sharp eyes AND sharp mind!",
]
PEBBLES_RETRY_YAY = [
    "Yes! You heard it that time!",
    "There you go! Second time's the charm!",
    "See? You totally knew it!",
    "Boom! Pebbles believed in you!",
    "That's the spirit! You figured it out!",
    "Persistence pays off! Nice one!",
    "You got it on the retry — that still counts!",
]
PEBBLES_OOF = [
    "Mistakes help you learn!",
    "Don't worry, even Pebbles gets confused sometimes!",
    "Oops! But you're getting better!",
    "Not this time, but next time for sure!",
    "That's okay — every musician makes mistakes!",
    "Pebbles tripped over his tail once too. We learn!",
    "Almost! You'll get the next one!",
    "No worries — that was a tricky one!",
]
PEBBLES_PERFECT = [
    "PERFECT SCORE! You're a music legend!",
    "FLAWLESS! Pebbles is doing a happy dance!",
    "INCREDIBLE! Not a single mistake!",
    "100%! You are officially amazing!",
    "PERFECT! Pebbles is speechless! Well... almost!",
    "WOW! Full marks! You're unstoppable!",
    "Not one wrong! Pebbles needs to sit down!",
]
PEBBLES_GOOD = [
    "Great job! Keep practising!",
    "Nicely done! You're getting so good!",
    "Solid score! Pebbles is impressed!",
    "Well played! You're levelling up!",
    "Really good! A few more tries and you'll be perfect!",
    "Pebbles gives you a big thumbs up! Well... a claw up!",
    "You're on your way to being a music star!",
]
PEBBLES_MEH = [
    "Keep trying! Practice makes perfect!",
    "Every try makes you stronger!",
    "Pebbles says try again — you'll smash it!",
    "Don't give up! You're learning!",
    "Even the best musicians started somewhere!",
    "Pebbles believes in you! One more round?",
    "That's how learning works — try, try again!",
    "You're braver than you think! Go again!",
]
PEBBLES_ASK_EAR = [
    "Was note 2 higher or lower?",
    "Did that second note go up or down?",
    "Higher or lower — what do your ears say?",
    "Which way did the sound move?",
    "Up or down? You tell me!",
    "Think about it... higher or lower?",
    "Listen closely... which way did it go?",
    "Pebbles wants to know — higher or lower?",
    "Use your super ears! Up or down?",
    "Did it climb up or slide down?",
]
PEBBLES_ASK_NOTE = [
    "What note is this?",
    "Can you name this note?",
    "Hmm, which note is that?",
    "Do you know this one?",
    "What's this note called?",
    "Quick — what note do you see?",
    "Pebbles is curious — what note is it?",
    "Read that staff! What note?",
    "This one looks familiar... what is it?",
    "Name that note!",
]

# Standard range (13 entries, index 0–12)
TREBLE_NAMES = ["c","d","e","f","g","a","b","c","d","e","f","g","a"]
BASS_NAMES   = ["e","f","g","a","b","c","d","e","f","g","a","b","c"]
HEIGHTS      = [-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]

# Extended range for hard mode (17 entries, index 0–16)
TREBLE_HARD = ["a","b","c","d","e","f","g","a","b","c","d","e","f","g","a","b","c"]
BASS_HARD   = ["c","d","e","f","g","a","b","c","d","e","f","g","a","b","c","d","e"]
HEIGHTS_HARD = [-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]

# Amaya's difficulty gap lists (ear trainer)
EASY_GAPS   = [-9,-8,9,8,-7,7,10,-10]
MEDIUM_GAPS = [5,6,-6,-5,4,-4]
HARD_GAPS   = [1,2,-2,-1,3,-3]


# ═══════════════════════════════════
#  SESSION STATE
# ═══════════════════════════════════

defaults = {
    "page": "home",
    "name": "",
    "score": 0,
    "round_num": 0,
    "total": 5,
    "level": "1",
    "chosen_clef": "treble",
    # Ear trainer
    "ear_n1": 0,
    "ear_n2": 0,
    "ear_gap": 1,
    "ear_feedback": None,
    "ear_tip": "",
    # Note reader
    "note_clef": "treble",
    "note_height": 0,
    "note_accidental": "natural",
    "note_full_name": "",
    "note_feedback": None,
    "note_tip": "",
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val


# ── Navigation helper ──
def go(page):
    st.session_state.page = page
    st.rerun()


# ── Round generators (Amaya's logic, Streamlit wiring) ──
def new_ear_round():
    level = st.session_state.level
    if level == "1":
        gaps = EASY_GAPS
    elif level == "2":
        gaps = MEDIUM_GAPS
    else:
        gaps = HARD_GAPS
    n1 = random.choice(gaps)
    gap = random.choice(gaps)
    st.session_state.ear_n1 = n1
    st.session_state.ear_n2 = n1 + gap
    st.session_state.ear_gap = gap
    st.session_state.ear_feedback = None


def new_note_round():
    level = st.session_state.level
    if level == "1":
        spot = random.randint(1, 11)
        clef = st.session_state.chosen_clef
        names = TREBLE_NAMES if clef == "treble" else BASS_NAMES
        heights = HEIGHTS
        accidental = "natural"
    elif level == "2":
        spot = random.randint(0, 12)
        clef = random.choice(["treble", "bass"])
        names = TREBLE_NAMES if clef == "treble" else BASS_NAMES
        heights = HEIGHTS
        accidental = random.choice(["flat", "sharp", "natural"])
    else:
        spot = random.randint(0, 16)
        clef = random.choice(["treble", "bass"])
        names = TREBLE_HARD if clef == "treble" else BASS_HARD
        heights = HEIGHTS_HARD
        accidental = random.choice(["flat", "sharp", "natural"])

    note_name = names[spot]
    full_name = note_name
    if accidental == "sharp":
        full_name = note_name + "#"
    elif accidental == "flat":
        full_name = note_name + "b"

    st.session_state.note_clef = clef
    st.session_state.note_height = heights[spot]
    st.session_state.note_accidental = accidental
    st.session_state.note_full_name = full_name
    st.session_state.note_feedback = None


def start_game(game, level, clef="treble", rounds=10):
    st.session_state.score = 0
    st.session_state.round_num = 0
    st.session_state.total = rounds
    st.session_state.level = level
    st.session_state.chosen_clef = clef
    if game == "ear":
        new_ear_round()
        go("ear_play")
    else:
        new_note_round()
        go("note_play")


def next_round(game):
    st.session_state.round_num += 1
    if st.session_state.round_num >= st.session_state.total:
        go(f"{game}_result")
    else:
        if game == "ear":
            new_ear_round()
        else:
            new_note_round()
        go(f"{game}_play")


# ═══════════════════════════════════
#  PAGES
# ═══════════════════════════════════

page = st.session_state.page

# ── HOME ──────────────────────────
if page == "home":
    st.title("🎹 Piano Mind Studios")
    pebbles("happy")
    st.markdown("**Pebbles says:** 'Welcome! I'm Pebbles the dino, your music buddy!'")

    name = st.text_input("What is your name?", value=st.session_state.name)
    if name:
        st.session_state.name = name
        st.markdown(f"**Pebbles says:** 'Hi {name}! What do you want to play?'")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🎵 Ear Training", use_container_width=True):
                go("ear_level")
        with col2:
            if st.button("🎼 Note Reading", use_container_width=True):
                go("note_level")


# ── EAR TRAINER: LEVEL ───────────
elif page == "ear_level":
    st.title("🎵 Ear Training")
    st.markdown(f"**Pebbles says:** 'Pick your level, {st.session_state.name}!'")
    rounds = st.radio("How many rounds?", [5, 10, 15, 20], horizontal=True, index=1)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("😊 Easy", use_container_width=True):
            start_game("ear", "1", rounds=rounds)
    with col2:
        if st.button("🤔 Medium", use_container_width=True):
            start_game("ear", "2", rounds=rounds)
    with col3:
        if st.button("🔥 Hard", use_container_width=True):
            start_game("ear", "3", rounds=rounds)
    st.caption("Easy = big obvious jumps · Medium = medium jumps · Hard = tiny tricky steps")


# ── EAR TRAINER: PLAY ────────────
elif page == "ear_play":
    r = st.session_state.round_num
    total = st.session_state.total
    n1 = st.session_state.ear_n1
    n2 = st.session_state.ear_n2
    gap = st.session_state.ear_gap
    correct = "higher" if gap > 0 else "lower"
    fb = st.session_state.ear_feedback

    st.title(f"🎵 Round {r + 1} of {total}")
    st.progress((r + 1) / total)

    # Normal speed audio
    sound = make_sound(n1, n2, 0.6)
    st.audio(sound, format="audio/wav", autoplay=(fb is None))

    if fb is None:
        # ── Waiting for first answer ──
        pebbles("asking", width=130)
        st.markdown(f"**Pebbles asks:** '{random.choice(PEBBLES_ASK_EAR)}'")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬆️ Higher", use_container_width=True):
                if correct == "higher":
                    st.session_state.score += 1
                    st.session_state.ear_feedback = "correct"
                else:
                    st.session_state.ear_feedback = "wrong"
                    st.session_state.ear_tip = random.choice(EAR_TIPS)
                st.rerun()
        with col2:
            if st.button("⬇️ Lower", use_container_width=True):
                if correct == "lower":
                    st.session_state.score += 1
                    st.session_state.ear_feedback = "correct"
                else:
                    st.session_state.ear_feedback = "wrong"
                    st.session_state.ear_tip = random.choice(EAR_TIPS)
                st.rerun()

    elif fb == "correct":
        pebbles("happy")
        st.success(f"**Pebbles says:** '{random.choice(PEBBLES_YAY_EAR)}' 🌸")
        if st.button("Next ➡️", use_container_width=True):
            next_round("ear")

    elif fb == "wrong":
        # ── WHY screen: tip + slow replay + second chance ──
        pebbles("thinking")
        st.warning(f"**Pebbles says:** 'Not quite! Here's a tip: {st.session_state.ear_tip}'")
        st.markdown("**Pebbles says:** 'Here it is again, slower...'")
        slow = make_sound(n1, n2, 1.5)
        st.audio(slow, format="audio/wav")
        st.markdown("**Pebbles says:** 'Try again!'")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬆️ Higher", key="retry_h", use_container_width=True):
                if correct == "higher":
                    st.session_state.score += 0.5
                    st.session_state.ear_feedback = "retry_correct"
                else:
                    st.session_state.ear_feedback = "retry_wrong"
                st.rerun()
        with col2:
            if st.button("⬇️ Lower", key="retry_l", use_container_width=True):
                if correct == "lower":
                    st.session_state.score += 0.5
                    st.session_state.ear_feedback = "retry_correct"
                else:
                    st.session_state.ear_feedback = "retry_wrong"
                st.rerun()

    elif fb == "retry_correct":
        pebbles("happy")
        st.success(f"**Pebbles says:** '{random.choice(PEBBLES_RETRY_YAY)}' 🌸")
        if st.button("Next ➡️", use_container_width=True):
            next_round("ear")

    elif fb == "retry_wrong":
        pebbles("thinking")
        st.error(f"**Pebbles says:** 'It was {correct}. {random.choice(PEBBLES_OOF)}'")
        if st.button("Next ➡️", use_container_width=True):
            next_round("ear")


# ── EAR TRAINER: RESULTS ─────────
elif page == "ear_result":
    st.title("🎵 Results!")
    score = st.session_state.score
    total = st.session_state.total
    st.markdown(f"### You scored **{score}** out of **{total}**!")
    if score == total:
        pebbles("happy")
        st.balloons()
        st.markdown(f"**Pebbles says:** '{random.choice(PEBBLES_PERFECT)}' 🌸")
    elif score >= total * 0.6:
        pebbles("happy")
        st.markdown(f"**Pebbles says:** '{random.choice(PEBBLES_GOOD)}'")
    else:
        pebbles("thinking")
        st.markdown(f"**Pebbles says:** '{random.choice(PEBBLES_MEH)}'")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Play Again", use_container_width=True):
            go("ear_level")
    with col2:
        if st.button("🏠 Home", use_container_width=True):
            go("home")


# ── NOTE READER: LEVEL ───────────
elif page == "note_level":
    st.title("🎼 Note Reading")
    st.markdown(f"**Pebbles says:** 'Pick your level, {st.session_state.name}!'")
    rounds = st.radio("How many rounds?", [5, 10, 15, 20], horizontal=True, index=1, key="note_rounds")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("😊 Easy", use_container_width=True):
            st.session_state.total = rounds
            st.session_state.level = "1"
            go("note_clef")
    with col2:
        if st.button("🤔 Medium", use_container_width=True):
            start_game("note", "2", rounds=rounds)
    with col3:
        if st.button("🔥 Hard", use_container_width=True):
            start_game("note", "3", rounds=rounds)
    st.caption("Easy = no ledger lines, naturals · Medium = ledger lines + sharps/flats · Hard = extended range")


# ── NOTE READER: CLEF SELECT (easy only) ──
elif page == "note_clef":
    st.title("🎼 Choose Your Clef")
    st.markdown(f"**Pebbles says:** 'Which clef do you want to practise, {st.session_state.name}?'")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎵 Treble Clef", use_container_width=True):
            start_game("note", "1", "treble")
    with col2:
        if st.button("🎵 Bass Clef", use_container_width=True):
            start_game("note", "1", "bass")


# ── NOTE READER: PLAY ────────────
elif page == "note_play":
    r = st.session_state.round_num
    total = st.session_state.total
    fb = st.session_state.note_feedback

    st.title(f"🎼 Round {r + 1} of {total}")
    st.progress((r + 1) / total)

    # Draw the staff
    fig = draw_staff(
        st.session_state.note_height,
        st.session_state.note_accidental,
        st.session_state.note_clef,
    )
    st.pyplot(fig, transparent=True)
    plt.close(fig)

    if fb is None:
        # ── Waiting for answer ──
        pebbles("asking", width=130)
        st.markdown(f"**Pebbles asks:** '{random.choice(PEBBLES_ASK_NOTE)}'")
        st.caption("You can type letter names (C, D, E...) or solfège (do, re, mi...). Add # or 'sharp' for sharps, b or 'flat' for flats.")
        answer = st.text_input("Your answer:", key=f"note_ans_{r}")
        if st.button("Check ✓", use_container_width=True) and answer:
            clean = answer.lower().replace(" ", "").replace("sharp", "#").replace("flat", "b")
            # Solfège conversion
            solfege = {"do":"c","re":"d","mi":"e","fa":"f","so":"g","sol":"g","la":"a","ti":"b","si":"b"}
            base = clean.rstrip("#b") if clean.rstrip("#b") else clean
            suffix = clean[len(base):]
            if base in solfege:
                clean = solfege[base] + suffix
            if clean == st.session_state.note_full_name:
                st.session_state.score += 1
                st.session_state.note_feedback = "correct"
            else:
                st.session_state.note_feedback = "wrong"
                st.session_state.note_tip = random.choice(NOTE_TIPS)
            st.rerun()

    elif fb == "correct":
        pebbles("happy")
        st.success(f"**Pebbles says:** '{random.choice(PEBBLES_YAY_NOTE)}' 🌸")
        if st.button("Next ➡️", use_container_width=True):
            next_round("note")

    elif fb == "wrong":
        pebbles("thinking")
        full = st.session_state.note_full_name
        st.error(
            f"**Pebbles says:** 'This note is **{full}**! "
            f"Here's a tip: {st.session_state.note_tip}'"
        )
        if st.button("Next ➡️", use_container_width=True):
            next_round("note")


# ── NOTE READER: RESULTS ─────────
elif page == "note_result":
    st.title("🎼 Results!")
    score = st.session_state.score
    total = st.session_state.total
    st.markdown(f"### You scored **{score}** out of **{total}**!")
    if score == total:
        pebbles("happy")
        st.balloons()
        st.markdown(f"**Pebbles says:** '{random.choice(PEBBLES_PERFECT)}' 🌸")
    elif score >= total * 0.6:
        pebbles("happy")
        st.markdown(f"**Pebbles says:** '{random.choice(PEBBLES_GOOD)}'")
    else:
        pebbles("thinking")
        st.markdown(f"**Pebbles says:** '{random.choice(PEBBLES_MEH)}'")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Play Again", use_container_width=True):
            go("note_level")
    with col2:
        if st.button("🏠 Home", use_container_width=True):
            go("home")
