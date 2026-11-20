"""Build a tiny font holding Griffiths' script r (regular + bold).

Glyphs come from the vector paths in ScriptR.pdf / BoldR.pdf (converted to
SVG with pdftocairo). They are mapped to the Unicode code points
U+1D4C7 (𝓇 MATHEMATICAL SCRIPT SMALL R) and U+1D4FB (𝓻 ... BOLD SCRIPT SMALL R),
so plain Unicode text picks them up wherever this font is loaded (e.g. if
installed on your computer), and to plain 'r' for the site's KaTeX trick.

To regenerate (run in this folder; needs `pip install fonttools brotli`):
    pdftocairo -svg ScriptR.pdf ScriptR.svg
    pdftocairo -svg BoldR.pdf BoldR.svg
    python build_font.py
then replace the base64 string in griffiths-script-r.css with
    base64 -i GriffithsScriptR.woff2
"""
import re
import sys

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.svgLib.path import parse_path

UPM = 1000
TARGET_HEIGHT = 470   # glyph height in font units (~0.47 em, just above x-height)
SIDE_BEARING = 35

GLYPHS = {  # glyph name: (svg file, code points)
    # U+0072 ('r') is included so the site CSS can swap KaTeX's fraktur r
    # (\mathfrak{r}) for this glyph; see griffiths-script-r.css
    "u1D4C7": ("ScriptR.svg", (0x1D4C7, 0x72)),
    "u1D4FB": ("BoldR.svg", (0x1D4FB,)),
}


def svg_path(fname):
    return re.search(r'<path d="([^"]+)"', open(fname).read()).group(1)


def build(out_stem):
    charstrings, metrics, cmap = {}, {}, {}

    # .notdef and space
    for name, adv in ((".notdef", 500), ("space", 250)):
        pen = T2CharStringPen(adv, None)
        charstrings[name] = pen.getCharString()
        metrics[name] = (adv, 0)
    cmap[0x20] = "space"

    for name, (fname, cps) in GLYPHS.items():
        d = svg_path(fname)
        # measure in SVG units (y down)
        bp = BoundsPen(None)
        parse_path(d, bp)
        xmin, ymin, xmax, ymax = bp.bounds
        s = TARGET_HEIGHT / (ymax - ymin)
        # flip y, scale, and shift so the left edge sits at SIDE_BEARING
        # baseline stays at y=0 (SVG y=0 is the PDF glyph baseline)
        affine = (s, 0, 0, -s, SIDE_BEARING - xmin * s, 0)
        adv = round((xmax - xmin) * s + 2 * SIDE_BEARING)
        rec = RecordingPen()
        parse_path(d, TransformPen(rec, affine))
        pen = T2CharStringPen(adv, None)
        rec.replay(pen)
        charstrings[name] = pen.getCharString()
        metrics[name] = (adv, SIDE_BEARING)
        for cp in cps:
            cmap[cp] = name

    fb = FontBuilder(UPM, isTTF=False)
    fb.setupGlyphOrder(list(charstrings))
    fb.setupCharacterMap(cmap)
    family = "Griffiths Script R"
    fb.setupCFF(family.replace(" ", ""), {"FullName": family}, charstrings, {})
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    fb.setupNameTable({"familyName": family, "styleName": "Regular"})
    fb.setupOS2(sTypoAscender=800, sTypoDescender=-200, usWinAscent=800, usWinDescent=200)
    fb.setupPost()
    fb.save(out_stem + ".otf")
    fb.font.flavor = "woff2"
    fb.save(out_stem + ".woff2")


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "GriffithsScriptR")
