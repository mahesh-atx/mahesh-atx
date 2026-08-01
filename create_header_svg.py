import base64
import sys

image_path = r'C:\Users\Mahesh\Desktop\profile\download.jpg'
try:
    with open(image_path, 'rb') as f:
        img_data = f.read()
except FileNotFoundError:
    print(f"Error: Could not find image at {image_path}")
    sys.exit(1)

b64 = base64.b64encode(img_data).decode('utf-8')

svg = f"""<svg width="800" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="rectClip">
      <rect width="800" height="250" />
    </clipPath>
  </defs>
  
  <!-- Background Image with cropping to fit -->
  <image href="data:image/jpeg;base64,{b64}" width="800" height="450" y="-100" preserveAspectRatio="xMidYMid slice" clip-path="url(#rectClip)" />
  
  <!-- Dark overlay to ensure text is readable -->
  <rect width="800" height="250" fill="rgba(13, 17, 23, 0.65)" />

  <!-- Centered Header Text -->
  <g text-anchor="middle" font-family="Consolas, 'Courier New', monospace">
    <text x="400" y="125" font-size="48" fill="#ffffff" font-weight="bold">Mahesh ATX</text>
    <text x="400" y="165" font-size="16" fill="#c9d1d9">Building clean software one commit at a time</text>
  </g>
</svg>"""

with open('header-bg.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
print("header-bg.svg created successfully.")
