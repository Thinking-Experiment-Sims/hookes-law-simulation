with open("/Users/vladimir.lopez/AI_Ecosystem/hookes-law-simulation/simulation.js", "r") as f:
    text = f.read()

# Add a global helper
helper = """
function getCanvasColor(darkColor, lightColor) {
    return document.body.dataset.theme === 'light' ? lightColor : darkColor;
}
"""

if "function getCanvasColor" not in text:
    text = helper + text

# Replace text colors in LabSimulation
text = text.replace("'#eef2f9'", "getCanvasColor('#eef2f9', '#123140')")
text = text.replace("'#a9b2c3'", "getCanvasColor('#a9b2c3', '#4b6570')")

# Ruler background and border
text = text.replace("'rgba(229, 204, 143, 0.05)'", "getCanvasColor('rgba(229, 204, 143, 0.05)', 'rgba(11, 95, 119, 0.05)')")
text = text.replace("'rgba(229, 204, 143, 0.3)'", "getCanvasColor('rgba(229, 204, 143, 0.3)', 'rgba(11, 95, 119, 0.3)')")

# Graph Grid and Axes
text = text.replace("'rgba(229, 204, 143, 0.1)'", "getCanvasColor('rgba(229, 204, 143, 0.1)', 'rgba(11, 95, 119, 0.1)')")
text = text.replace("'rgba(229, 204, 143, 0.4)'", "getCanvasColor('rgba(229, 204, 143, 0.4)', 'rgba(11, 95, 119, 0.4)')")

# Tab labels colors in graph
text = text.replace("'#eef2f9'", "getCanvasColor('#eef2f9', '#123140')")

# Inject MutationObserver at the end of the file to trigger redrawing on theme change
observer_code = """
    // Theme observer to redraw canvases
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            if (mutation.attributeName === 'data-theme') {
                if (lab) lab.draw();
                if (graph) graph.draw();
                if (fpSim && !fpSim.isRunning) { fpSim.draw(); fpSim.drawGraphs(); }
            }
        });
    });
    observer.observe(document.body, { attributes: true });
"""

if "MutationObserver" not in text:
    text = text.replace("    function announce(msg) {", observer_code + "\n    function announce(msg) {")

with open("/Users/vladimir.lopez/AI_Ecosystem/hookes-law-simulation/simulation.js", "w") as f:
    f.write(text)
