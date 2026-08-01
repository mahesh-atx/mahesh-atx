svg = f"""<svg width="800" height="250" xmlns="http://www.w3.org/2000/svg">
  <!-- Transparent background by default -->

  <!-- Centered Header Text -->
  <g text-anchor="middle" font-family="Consolas, 'Courier New', monospace">
    <text x="400" y="80" font-size="54" fill="#ffffff" font-weight="bold">Mahesh ATX</text>
    
    <text x="400" y="130" font-size="18" fill="#58a6ff">&gt; Full-Stack Developer | Open Source Enthusiast</text>
    
    <text x="400" y="165" font-size="16" fill="#c9d1d9">"Building clean software one commit at a time"</text>
    
    <text x="400" y="195" font-size="14" fill="#8b949e">Web • Backend • Architecture • Dark UI</text>
  </g>
</svg>"""

with open('header-bg.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
print("header-bg.svg created successfully.")
