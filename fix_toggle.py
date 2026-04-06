with open("/Users/vladimir.lopez/AI_Ecosystem/hookes-law-simulation/index.html", "r") as f:
    text = f.read()

text = text.replace(
    '''onclick="document.body.dataset.theme=document.body.dataset.theme==='light'?'':'light'"''',
    '''onclick="const isLight = document.body.dataset.theme === 'light'; document.body.dataset.theme = isLight ? '' : 'light'; this.textContent = isLight ? 'Light mode' : 'Dark mode';"'''
)

with open("/Users/vladimir.lopez/AI_Ecosystem/hookes-law-simulation/index.html", "w") as f:
    f.write(text)
