# PianoMind Studios — Google Play kit

Everything here is a **draft for Amaya to edit**. It's your app, so the words should sound like you.

## 1. Store listing text

**App name** (17 characters)
PianoMind Studios

**Short description** (max 80 characters — this one is 77)
Piano theory games: read notes, intervals and chords, train your ear. No ads.

**Full description** (max 4,000 characters)

PianoMind Studios turns music theory practice into short games. I made it for kids and anyone who finds theory hard, and for myself to practise too.

WHAT YOU CAN PLAY
• Note Reading — name notes in treble and bass clef, from C-D-E up to double sharps
• Intervals — read the distance between two notes on the staff
• Chords — name major, minor, diminished and augmented chords, or try them by ear
• Ear Training — hear C first, then work out the mystery note (no perfect pitch needed)
• Melody Echo — listen to a short tune and play it back on the piano
• Mystery Melody — one note changes. Can you spot which?
• Boss Battle — beat four bosses with chords, tunes, intervals and rhythm
• Time Attack — how many notes can you name in 60 seconds?
• Rhythm Training, Sight Reading, Scale Explorer, Hanon exercises and a metronome

LEARN AS YOU GO
• A "Start here" path for beginners
• Step-by-step theory lessons and grade-style exercises
• When you get one wrong, a "Why?" screen explains it
• Printable homework sheets with answer keys

FOR TEACHERS
• Make a link to any game and level, and send it to your class. Students open it straight into that game with no account.

KEEP GOING
• Daily challenge, streaks, a daily practice goal, trophies and XP
• Applause: send a friend a clap (only an icon, never a message)

PRIVATE AND FREE
• No ads. Play as a guest and nothing leaves your device.
• An account is optional. It saves your progress to the cloud.
• Delete your account and all your data from inside the app.

This app helps you practise skills like those in graded music exams. It is not affiliated with, endorsed by, or using material from any exam board.

**Category:** Education · **Tags to consider:** Music, Education
**Privacy policy URL:** https://vanjdroid.github.io/pianomind-studios/privacy.html
**Contact email:** use a separate support email, not a personal one. It is shown publicly on the store page.

## 2. Pictures (in this folder)

| File | Use | Size |
|---|---|---|
| icon_512.png | App icon | 512 × 512 |
| feature_graphic.png | Feature graphic (banner) | 1024 × 500 |
| 1_home.png … 7_progress.png | Phone screenshots (need at least 2) | 1080 × 1920 |

## 3. Data safety form — draft answers

Check every answer against the form itself before submitting.

| Data | Collected? | Why | Optional? |
|---|---|---|---|
| Email address | Yes, only with an account | Account sign-in | Yes |
| Name (the name typed in the app) | Yes, only with an account | App features | Yes |
| Photos (profile picture) | Yes, only if uploaded | App features | Yes |
| App activity (scores, XP, settings) | Yes, only with an account | App features | Yes |
| Other user content (feedback text) | Yes, only if sent | Fix bugs, improve the app | Yes |
| Shared with others? | No | — | — |
| Encrypted in transit? | Yes (HTTPS) | — | — |
| Can users delete data? | Yes (in the app, or via the #delete link) | — | — |
| Ads? | No | — | — |

🤔 Firebase (Google's sign-in and database service) may collect extra technical data, like device information. Read Firebase's "data disclosure" help page and copy anything it says you must declare.

## 4. Decisions you need to make first

**A. Who is the app for?** Google has a stricter rulebook (the Families policy) for apps aimed at children.
- **Children only:** sign-in features must be approved for kids' apps. Google sign-in may not be allowed. This needs checking.
- **Mixed (kids and older people):** sign-in can stay, but must sit behind a **neutral age screen**. That's a question like "How old are you?" that doesn't hint at the "right" answer. Under-13s would then play as guests only.
- The app already works fully in guest mode, so either option is doable. Decide with a parent.

**B. The website address (domain).** The Android app proves it owns the website with a small file at the very top of the site: `/.well-known/assetlinks.json`.
- With **pianomindstudios.com**, this is easy.
- Without it, you'd need a second free GitHub site named `vanjdroid.github.io` that holds just that file, plus an empty file called `.nojekyll`. Without the proof file, the app shows a browser address bar at the top.

## 5. Steps, in order

1. Mom creates the Google Play developer account. It needs her ID, she must be 18+, and there's a US$25 one-time fee.
2. Decide A and B above.
3. Build the Android app with **PWABuilder** (pwabuilder.com) → "Package for stores" → Android. It uses Google's Bubblewrap tool. Download the package and keep the signing key file safe forever.
4. Put the `assetlinks.json` file from the package on the website (step B).
5. In Play Console, create the app, upload the pictures and text above, and fill in Data safety, Content rating and Target audience.
6. **Closed test:** add your 12+ testers. They must stay opted in for **14 days in a row**.
7. Then apply for production. Google reviews it before it goes live.
