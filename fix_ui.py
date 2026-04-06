import re

with open("/Users/vladimir.lopez/AI_Ecosystem/hookes-law-simulation/simulation.js", "r") as f:
    text = f.read()

# Replace drawRuler
ruler_pattern = re.compile(r"drawRuler\(ctx, springBottom\) \{.*?(?=    drawSpring)", re.DOTALL)
new_ruler = """drawRuler(ctx, springBottom) {
        const rulerX = this.springX + 130;
        const rulerTop = this.springTopY + this.naturalLength - 20;
        const rulerBottom = Math.min(this.H - 50, rulerTop + 450);
        const rulerWidth = 32;

        // Ruler background
        ctx.fillStyle = getCanvasColor('rgba(229, 204, 143, 0.05)', 'rgba(11, 95, 119, 0.05)');
        ctx.fillRect(rulerX, rulerTop, rulerWidth, rulerBottom - rulerTop);
        ctx.strokeStyle = getCanvasColor('rgba(229, 204, 143, 0.3)', 'rgba(11, 95, 119, 0.3)');
        ctx.lineWidth = 1.5;
        ctx.strokeRect(rulerX, rulerTop, rulerWidth, rulerBottom - rulerTop);

        const pxPerCm = this.pxPerMeter / 100;
        const startCm = Math.floor((rulerTop - this.referenceY) / pxPerCm);
        const endCm = Math.ceil((rulerBottom - this.referenceY) / pxPerCm);

        ctx.font = '10px Arial';
        ctx.textAlign = 'left';
        ctx.textBaseline = 'middle';

        for (let cm_10 = startCm * 10; cm_10 <= endCm * 10; cm_10 += 5) {
            const y = this.referenceY + (cm_10 / 10) * pxPerCm;
            if (y < rulerTop || y > rulerBottom) continue;

            let tickLen = 6;
            if (cm_10 % 10 === 0) tickLen = 12;

            ctx.strokeStyle = getCanvasColor('#a9b2c3', '#795548');
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(rulerX, y);
            ctx.lineTo(rulerX + tickLen, y);
            ctx.stroke();

            // Label every 2 cm mapping
            if (cm_10 % 20 === 0) {
                ctx.fillStyle = getCanvasColor('#a9b2c3', '#5d4037');
                const label = (cm_10 / 10).toString();
                ctx.fillText(label, rulerX + 16, y);
            }
        }

        // Zero mark highlighting
        const zeroY = this.referenceY;
        if (zeroY >= rulerTop && zeroY <= rulerBottom) {
            ctx.beginPath();
            ctx.moveTo(rulerX, zeroY);
            ctx.lineTo(rulerX + rulerWidth, zeroY);
            ctx.strokeStyle = '#ff5f7a'; 
            ctx.lineWidth = 1.5;
            ctx.stroke();
            ctx.fillStyle = '#ff5f7a'; 
            ctx.font = 'bold 11px Arial';
            ctx.fillText('0', rulerX + 16, zeroY - 8);
        }

        // Label
        ctx.save();
        ctx.translate(rulerX + rulerWidth + 14, rulerTop + (rulerBottom - rulerTop) / 2);
        ctx.rotate(Math.PI / 2);
        ctx.fillStyle = getCanvasColor('#a9b2c3', '#4b6570');
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Stretch (cm from reference)', 0, 0);
        ctx.restore();
    }

"""
text = ruler_pattern.sub(new_ruler, text)


# Replace drawReferenceLine
ref_pattern = re.compile(r"drawReferenceLine\(ctx\) \{.*?(?=    drawStretchAnnotation)", re.DOTALL)
new_ref = """drawReferenceLine(ctx) {
        ctx.save();
        ctx.strokeStyle = '#ff5f7a';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([6, 4]);
        ctx.beginPath();
        ctx.moveTo(this.springX - 35, this.referenceY);
        ctx.lineTo(this.springX + 140, this.referenceY);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#ff5f7a';
        ctx.font = 'bold 11px Arial';
        ctx.textAlign = 'left';
        ctx.fillText('x = 0 (ref)', this.springX + 45, this.referenceY - 6);
        ctx.restore();
    }

"""
text = ref_pattern.sub(new_ref, text)


# Replace drawStretchAnnotation
stretch_pattern = re.compile(r"drawStretchAnnotation\(ctx, springBottom\) \{.*?(?=    drawLabels)", re.DOTALL)
new_stretch = """drawStretchAnnotation(ctx, springBottom) {
        const currentY = springBottom + 10;
        const stretchM = (this.currentStretchPx / this.pxPerMeter) - this.hangerStretch;

        if (Math.abs(stretchM) < 0.0005) return;

        const annotX = this.springX + 45;

        ctx.save();
        ctx.strokeStyle = '#c8a24a';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 3]);

        // Vertical line from ref to current
        ctx.beginPath();
        ctx.moveTo(annotX, this.referenceY);
        ctx.lineTo(annotX, currentY);
        ctx.stroke();
        ctx.setLineDash([]);

        // Ticks
        ctx.beginPath();
        ctx.moveTo(annotX - 5, this.referenceY);
        ctx.lineTo(annotX + 5, this.referenceY);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(annotX - 5, currentY);
        ctx.lineTo(annotX + 5, currentY);
        ctx.stroke();

        // Arrow
        ctx.fillStyle = '#c8a24a';
        ctx.beginPath();
        ctx.moveTo(annotX, currentY);
        ctx.lineTo(annotX - 5, currentY - 8);
        ctx.lineTo(annotX + 5, currentY - 8);
        ctx.closePath();
        ctx.fill();

        // Label
        ctx.font = 'bold 12px Arial';
        ctx.textAlign = 'left';
        ctx.fillText(`x = ${(stretchM * 100).toFixed(1)} cm`, annotX + 12, (this.referenceY + currentY) / 2 + 4);
        ctx.font = '10px Arial';
        ctx.fillStyle = getCanvasColor('#a9b2c3', '#4b6570');
        ctx.fillText(`(${stretchM.toFixed(4)} m)`, annotX + 12, (this.referenceY + currentY) / 2 + 18);

        ctx.restore();
    }

"""
text = stretch_pattern.sub(new_stretch, text)


with open("/Users/vladimir.lopez/AI_Ecosystem/hookes-law-simulation/simulation.js", "w") as f:
    f.write(text)
