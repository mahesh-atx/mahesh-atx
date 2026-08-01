import base64

with open('footer-bg.jpg', 'rb') as f:
    img_data = f.read()

b64 = base64.b64encode(img_data).decode('utf-8')

svg = f"""<svg width="800" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="rectClip">
      <rect width="800" height="250" />
    </clipPath>
  </defs>
  
  <!-- Background Image with cropping to fit -->
  <image href="data:image/jpeg;base64,{b64}" width="800" height="450" y="-115" preserveAspectRatio="xMidYMid slice" clip-path="url(#rectClip)" />
  
  <!-- Subtle dark overlay to make text readable while keeping image highly visible -->
  <rect width="800" height="250" fill="rgba(13, 17, 23, 0.55)" />

  <!-- Terminal Header -->
  <g font-family="Consolas, 'Courier New', monospace" font-size="16" fill="#58a6ff" font-weight="bold">
    <text x="30" y="45">&gt; ./execute_profile.sh</text>
  </g>

  <!-- Terminal Text -->
  <g font-family="Consolas, 'Courier New', monospace" font-size="15.5" fill="#e6edf3" font-weight="bold">
    <text x="30" y="85">Name    : Mahesh</text>
    <text x="30" y="115">Handle  : @mahesh-atx</text>
    <text x="30" y="145">Mission : "Always building something better than yesterday 🚀"</text>
    <text x="30" y="175">Focus   : [Web, Backend, Open-Source]</text>
    <text x="30" y="205">Style   : "Clean architecture, dark UI, meaningful commits"</text>
  </g>
</svg>"""

with open('about-bg.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
