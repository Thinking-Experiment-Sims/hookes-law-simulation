# Hooke's Law Simulation — README

An interactive physics lab simulation for **Hooke's Law**. Students hang masses from a virtual spring, record data, graph Force vs. Stretch, and discover the spring constant — mirroring the hands-on lab experience.

## 🔗 Live Demo

[View on GitHub Pages](https://thinkerlopez.github.io/hookes-law-simulation/)

## Two Modes

### 🔬 Lab Mode (default)
A virtual version of the Hooke's Law lab. Students:
1. Add masses in 50 g increments to a vertical spring
2. Observe the spring stretch to equilibrium (with settling animation)
3. Click "Record Data Point" to capture each trial
4. Build a Force vs. Stretch graph point-by-point
5. Toggle a best-fit line to discover the slope = spring constant k

**Features:**
- Ring stand, vertical spring, ruler, and colorful stacking masses
- Data table (8 trials) matching the lab worksheet format
- Live Force vs. Stretch scatter plot with labeled data points
- Best-fit line toggle showing slope (k) in N/m
- 🔒 **Teacher Mode**: hidden spring constant (randomized on load), adjustable via slider

### 🎮 Free Play Mode
An interactive Simple Harmonic Motion simulation. Students explore:
- Adjustable spring constant, mass, displacement, and damping
- Real-time displacement and velocity graphs
- Energy distribution bar (PE ↔ KE)
- Force arrows and position trails

## Technologies

- HTML5 Canvas for rendering
- Vanilla JavaScript (no dependencies)
- CSS3 for responsive layout
- MathJax for equation rendering

## Lab Alignment

This simulation is designed to complement the **Hooke's Law Lab** worksheet:
- **Part 1**: Predictions (Guided Exploration tab)
- **Part 2**: Equipment (virtual ring stand, masses, ruler)
- **Part 3**: Procedure (add mass → record → repeat)
- **Part 4**: Analysis (graph, best-fit line, slope)
- **Part 5**: Model building (F = kx discovery)

## Usage

Open `index.html` in any modern browser, or visit the GitHub Pages link above.

## © 2026 Vladimir Lopez | The Thinking Experiment
