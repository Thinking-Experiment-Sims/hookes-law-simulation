import re

with open("/Users/vladimir.lopez/AI_Ecosystem/hookes-law-simulation/simulation.js", "r") as f:
    text = f.read()

# Stand
text = text.replace("#5d4037", "#a9b2c3")
text = text.replace("#4e342e", "#c9d1df")
text = text.replace("#8d6e63", "#c8a24a")
text = text.replace("#a1887f", "#d8b767")
text = text.replace("#6d4c41", "#8b7030")
text = text.replace("#455a64", "#eef2f9")

# Ruler
text = text.replace("#fffde7", "rgba(229, 204, 143, 0.05)")
text = text.replace("#f9a825", "rgba(229, 204, 143, 0.3)")
text = text.replace("#795548", "#a9b2c3")

# Reds (Reference, Arrows)
text = text.replace("#e74c3c", "#ff5f7a")

# Spring, Annotations (Purple -> Gold)
text = text.replace("#6c5ce7", "#c8a24a")

# Hanger
text = text.replace("#78909c", "#a9b2c3")
text = text.replace("#546e7a", "#c9d1df")

# Text colors
text = text.replace("#2c3e50", "#eef2f9")
text = text.replace("#6c757d", "#a9b2c3")
text = text.replace("#adb5bd", "#a9b2c3")
text = text.replace("fillStyle = '#fff'", "fillStyle = '#eef2f9'")

# Graph Backgrounds
text = text.replace("#fafafa", "transparent")
text = text.replace("#e9ecef", "rgba(229, 204, 143, 0.1)")
text = text.replace("#495057", "rgba(229, 204, 143, 0.4)")

# Data points / Mass block (Blue -> Gold)
text = text.replace("#2fa4e7", "#c8a24a")
text = text.replace("#1a7abc", "#d8b767")
text = text.replace("#1a5276", "#8b7030")

# Energy Bar
text = text.replace("#e17055", "#ff5f7a")  # PE
text = text.replace("#00b894", "#5cbf79")  # KE

# Tabs
text = text.replace(".tab-button", ".tab-btn")

with open("/Users/vladimir.lopez/AI_Ecosystem/hookes-law-simulation/simulation.js", "w") as f:
    f.write(text)
