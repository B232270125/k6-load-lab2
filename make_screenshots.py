import subprocess
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
font = ImageFont.truetype(FONT, 16)

shots = {
    "run-05vu":       'grep -A 25 "TOTAL RESULTS" results/run-05vu.txt',
    "run-30vu":       'grep -A 25 "TOTAL RESULTS" results/run-30vu.txt',
    "run-100vu":      'grep -A 25 "TOTAL RESULTS" results/run-100vu.txt',
    "threshold-pass": 'grep -A 8 "THRESHOLDS" results/run-threshold-pass.txt',
    "threshold-fail": 'grep -A 8 "THRESHOLDS" results/run-threshold-fail.txt; tail -n 2 results/run-threshold-fail.txt',
    "local-fast":     'grep -A 25 "TOTAL RESULTS" results/run-local-fast.txt',
    "local-slow":     'grep -A 25 "TOTAL RESULTS" results/run-local-slow.txt',
    "stages":         'grep -A 25 "TOTAL RESULTS" results/run-stages.txt',
    "k6-version":     'cat results/k6-version.txt',
}

for name, cmd in shots.items():
    out = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
    text = f"$ {cmd}\n\n{out}"
    lines = text.splitlines()
    w = max(font.getlength(l) for l in lines) + 40
    h = len(lines) * 22 + 40
    img = Image.new("RGB", (int(w), int(h)), "#1e1e1e")
    d = ImageDraw.Draw(img)
    for i, l in enumerate(lines):
        d.text((20, 20 + i * 22), l, font=font, fill="#e6e6e6")
    img.save(f"screenshots/{name}.png")
    print("үүссэн:", name)
