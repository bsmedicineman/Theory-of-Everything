This is an ongoing project. Not all data here will be updated in real time. 

If there are errors, let me know.

# Atlas of Everything

An interactive 3-D map of human knowledge, shaped as **Gabriel's Horn**.

The seed — `1 = 1` — sits at the mouth of the horn. Everything else descends from it along the reciprocal profile **radius = 1/x** (the law *1/x = y/1*), so that as ideas grow more advanced they spiral inward and downward along the tail. **438 nodes** across **62 domains**, woven together by **811 connections**, span the whole arc from counting and the first social bonds to general relativity, the transformer, and the frontier.

Everything is generated from a single data core by one Python script, which emits three coordinated outputs:

| File | What it is |
|------|------------|
| `atlas.html` | A standalone, interactive WebGL explorer (open it in any browser — no install, no server). |
| `knowledge_core.json` | The shared data core: every node, edge, date, colour, and coordinate. |
| `blender_build.py` | A headless Blender script that rebuilds the same map as real 3-D geometry (emission spheres + beveled-tube edges). |

---

## What you're looking at

- **The shape.** Height marks how advanced an idea is; distance from the central axis follows the reciprocal law `1/x`. Points fan out along the golden angle, φ.
- **The seed.** The deep-violet point at the mouth is `1 = 1`, the Cosmic-Violet origin. Every lineage traces back to it.
- **The growth structure.** The bright lineage lines are the backbone — *what each idea is built from*. Following them is following the tree of knowledge down from the seed.
- **Constant threads.** Faint lines trace the universal constants (π, e, φ, *i*, *c*, ℏ, …) weaving through every field — the interconnectedness made visible.

### Two harmonic octaves

Colour follows the seven-layer note→colour map of the source material (C = red … B = violet) via the position operator **{ log₂x + log₂(15/8) }**, expressed as **two independent octaves**:

- **Time octave → node colour.** Each node is placed by its depth in time (doublings of years-before-now). The present lands on violet; reading back through history the spectrum cycles octave by octave.
- **Difficulty octave → the growth lines.** Each progression's rung is its reciprocal coordinate *x* = stage + 1, so the lineage lines are coloured by *how advanced* each step is.

Unity sits at B / cosmic violet in both.

---

## The strata

Knowledge is layered by **epistemic status**, and every node is labelled accordingly so the proven is never blurred with the speculative:

- **Proven core** — 214 established equations and the **Constants of Nature** (G, h, e, k_B, N_A, α, the Planck scale, Λ, …): mathematics, physics, chemistry, biology, computation, economics, medicine, psychology, logic, linguistics, and more.
- **Social organization & institutions** — an empirical developmental arc, from self-preservation → the family → the band → the tribe → the village → the city → the state, alongside the institutions that grow with them: ritual, the birth of art, the division of labour, trade, writing, law, money, banking, markets, science, and governance.
- **Symbolic & traditional** — sacred number and geometry, the zodiac, classical planets and elements, and esoteric systems, shown for the correspondences they draw (clearly flagged as symbolic, not empirical).
- **Philosophy** — major positions across metaphysics, epistemology, ethics, philosophy of mind, Eastern philosophy, and philosophy of religion, presented as reasoned stances with their rivals.
- **Theoretical & speculative** — mainstream frontier physics (string action, the Standard Model Lagrangian, …) **and** a self-contained speculative framework (the "Reciprocal / PRI / foam" books) that is explicitly badged as speculative and included to map its internal structure and its bridges to the established core. *Nothing in this stratum is presented as confirmed science.*

Every detail panel states which stratum a node belongs to.

---

## Features (interactive `atlas.html`)

- **Orbit / zoom / pan** the horn; click any point for its statement, rendered equation (KaTeX), complexity metrics, discovery date, and links.
- **Light up its full tree.** Click a node and reveal its entire derivation tree — everything it is built from, back to the seed, plus everything built on it — with the rest of the atlas dimmed. The highlight stays locked while you explore.
- **Timeline scrubber.** Replay the build with **Play**: connections draw in link-by-link as each node appears. Toggle **"by date"** to switch from *growth order* to a true **historical timeline**, watching knowledge fill in from antiquity to the present (every node carries a curated discovery date, from ~250,000 BCE to 2026).
- **Live horn shaping.** Two sliders scale the **throat radius** and the **length** from 0.1× to 10×, reshaping the horn in real time without disturbing the glow.
- **Connection layers.** Toggle the lineage backbone, constant threads, the symbolic / theoretical / philosophy / social-fabric webs, and the translucent Gabriel's-Horn surface independently.
- **Search & domain filters**, optional labels, reduced-motion support, and a starfield backdrop.

---

## Quick start

### View the atlas

Just open the file — it is fully self-contained (Three.js and KaTeX load from a CDN; no build step):

```
open atlas.html        # macOS
# or double-click atlas.html, or drag it into any browser
```

### Regenerate everything from the core

```bash
python3 generate.py
```

This rebuilds `atlas.html`, `knowledge_core.json`, and `blender_build.py` from the single data core. Requires Python 3 (standard library only).

### Build the 3-D model in Blender

```bash
blender --background --python blender_build.py
```

Produces emission-lit spheres for every node and beveled-curve tubes for every edge, coloured by the same harmonic palette as the web view.

---

## How it's organised

```
Atlas of Everything/
├── atlas.html            # interactive WebGL explorer (open this)
├── knowledge_core.json   # the shared data core (nodes, edges, dates, colours, coordinates)
├── blender_build.py      # headless Blender geometry builder
├── generate.py           # the single generator that emits all of the above
└── README.md
```

Each **node** records its name, domain, developmental stage, LaTeX and plain-text form, the constants it uses, what it derives from, a discovery year, both octave colours, and its position on the horn. Each **edge** carries a kind — lineage, constant thread, symbolic bridge, theory link, philosophical relation, or social-fabric link — which drives both its colour and its toggle layer.

---

## Domains (62)

Foundations · Arithmetic · Constants · Constants of Nature · Geometry · Algebra · Trigonometry · Calculus · Linear Algebra · Complex Analysis · Number Theory · Probability & Stats · Information Theory · Classical Mechanics · Electromagnetism · Thermodynamics · Relativity · Quantum Mechanics · Chemistry · Biology · Finance & Economics · Game Theory · Strategy & Games · Gambling & Odds · Social Dynamics · Social Organization · Institutions & Culture · Behavioral Science · Medicine & Physiology · Psychology · Formal Logic · Computer Science & AI · Earth & Space Science · Language & Linguistics · Arts & Aesthetics · Sacred Numbers · Sacred Geometry · Zodiac · Classical Planets · Classical Elements · Esoteric Systems · I Ching · Chakras & Subtle Body · Myth & Archetype · Metaphysics · Epistemology · Ethics · Philosophy of Mind · Eastern Philosophy · Philosophy of Religion · Reciprocal Framework · Spacetime Foam Field · Wormholes & Travel · Harmonic Resonance · Emergent Gravity · Foam Detection · Reciprocal Applied · Geometric Psychology · Reciprocal Chemistry · Reciprocal Biology · Navigator (Travel) · The Looking Glass

---

## Notes on accuracy

- **Discovery dates** are best-estimate "first clear formulation / emergence" years and are necessarily approximate — attribution is often debated (e.g. the Pythagorean theorem is dated by attribution even though earlier cultures used it). They are meant as a faithful ordering, not precise claims.
- **The symbolic and speculative strata are clearly labelled as such** and are included for their structure and connections, not as established science.
- Content is curated and representative, not exhaustive.

---

## Built with

[Three.js](https://threejs.org/) (r128) · [KaTeX](https://katex.org/) · vanilla JavaScript · Python 3 · Blender (optional).
