import subprocess, sys, os

try:
    from PIL import Image
except ImportError:
    print("Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

folder = os.path.dirname(os.path.abspath(__file__))

names = []
for f in os.listdir(folder):
    if f.startswith("pebbles_") and f.endswith(".png"):
        names.append(f[:-4])

print(f"Found {len(names)} Pebbles images to fix!\n")

for name in names:
    try:
        path = os.path.join(folder, name + ".png")
        img = Image.open(path).convert("RGBA")
        pixels = img.load()
        w, h = img.size
        changed = 0
        for y in range(h):
            for x in range(w):
                r, g, b, a = pixels[x, y]
                if r > 240 and g > 240 and b > 240:
                    pixels[x, y] = (r, g, b, 0)
                    changed += 1
        img.save(path)
        print(f"  Fixed: {name} ({changed} white pixels removed)")
    except Exception as e:
        print(f"  ERROR on {name}: {e}")

print("\nAll done!")
input("\nPress Enter to close...")
