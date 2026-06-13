# Atlas of Everything

An interactive 3-D map of human knowledge — **2,163 nodes**, **82 domains**, **2,923 connections** — grown from a single seed: `1 = 1`.

Two views. One data core.

---

## What it is

The Atlas places every idea on one of two geometric forms, both generated live from the same graph:

**Gabriel's Horn.** The seed `1 = 1` sits at the mouth. Everything descends along the reciprocal profile `radius = 1/x`, so that as ideas grow more advanced they spiral inward and downward along the tail. Stage 0 is the widest point; stage 22 is the deepest frontier. Points fan out by the golden angle.

**Fibonacci Spiral Tree.** The same graph laid upward as a branching tree. Unity at the base; every node positioned by how many edges separate it from its parents, its horizontal spread proportional to the subtree it roots. No pre-programmed form — the shape emerges entirely from the edge topology.

Switch between them with the ⌘ button. Length and width sliders reshape both views in real time.

---

## What you're looking at

### Colour

Colour follows a seven-layer note→colour map (C = red … B = violet) via the position operator `{ log₂x + log₂(15/8) }`, expressed as two independent octaves:

- **Node colour = time octave.** Depth in time (doublings of years-before-now), cycling through the spectrum. The present lands on violet; the deep past runs red. Unity is fixed at cosmic violet.
- **Edge colour = difficulty octave.** Each lineage line is coloured by the stage of the ideas it connects — how advanced the step is.

### Connections

Seven edge types are independently toggleable:

| Layer | What it shows |
|-------|---------------|
| **Lineage** | What each idea is built from — the primary derivation tree |
| **Constant threads** | π, e, φ, *i*, *c*, ℏ, k_B … weaving through every field |
| **Symbolic bridges** | Connections from the symbolic stratum into the proven core |
| **Theory links** | Derivations within the speculative framework and its bridges to known physics |
| **Philosophy** | Positions and arguments across the philosophical strata |
| **Social fabric** | Developmental arcs through institutions and culture |
| **Surface** | The Gabriel's Horn shell (translucent, toggleable) |

### Strata

Every node is labelled by epistemic status. Nothing speculative is presented as established science.

| Stratum | Count | Description |
|---------|-------|-------------|
| **Established core** | 1,939 | Proven equations across mathematics, physics, chemistry, biology, computation, economics, medicine, psychology, logic, linguistics, and more |
| **Theoretical / frontier** | 111 | Mainstream frontier physics (Standard Model, string action, …) and a self-contained speculative framework (PRI / foam) — explicitly badged |
| **Philosophy** | 39 | Major positions across metaphysics, epistemology, ethics, mind, Eastern philosophy, and religion — presented as reasoned stances with rivals |
| **Symbolic / traditional** | 53 | Sacred number and geometry, zodiac, classical planets and elements, esoteric systems — flagged as symbolic, not empirical |
| **Social / institutional** | 21 | An empirical developmental arc from self-preservation through the emergence of writing, law, money, markets, and science |

---

## Features

**Click any point** to open its detail panel: rendered equation (KaTeX), description, complexity (five-dot scale), live connection count, era, and navigation pills to every linked idea.

**Light up its full tree.** One click locks the entire derivation tree — ancestors and descendants — with everything else dimmed. Stays locked while you explore; click again to release.

**Timeline scrubber.** Replay the build of knowledge with Play, or drag the scrubber manually. Toggle **"by date"** to switch from growth order to a true historical timeline — every node carries a curated discovery year, from ~250,000 BCE (self-preservation and the first social bonds) to 2026 (frontier theory).

**Search.** Live dropdown matching name, plain text, or domain. Keyboard-navigable; click any result to fly to it.

**Build & Grow.** Pick any seed equation and watch its full descendant tree reveal itself stage by stage.

**Full orbit.** Left-drag orbits the full sphere (no clamp — look from any angle). Right-drag or shift-drag pans. Scroll zooms. Two-finger pinch on touch.

**Domain filters.** Show or hide any of the 82 domains independently.

---

## Files

| File | What it is |
|------|------------|
| `atlas.html` | Standalone WebGL explorer — open in any browser, no install, no server |
| `knowledge_core.json` | The shared data core: every node, edge, date, colour, and coordinate |
| `blender_build.py` | Headless Blender script that rebuilds the same map as real 3-D geometry |

Everything is self-contained. `atlas.html` loads Three.js (r128) and KaTeX from CDN.

---

## Quick start

```bash
# View the atlas
open atlas.html        # macOS
# or double-click, or drag into any browser

# Rebuild the 3-D model in Blender (optional)
blender --background --python blender_build.py
```

---

## Coverage

**2,163 equations and ideas** across **82 domains**, spanning:

Mathematics: Foundations · Arithmetic · Constants · Geometry · Algebra · Trigonometry · Calculus · Linear Algebra · Complex Analysis · Number Theory · Probability & Stats · Information Theory · Pure Mathematics · Advanced Geometry & Topology · Abstract Algebra · Logic & Foundations · Mathematics of Infinity

Physics: Classical Mechanics · Advanced Classical Physics · Electromagnetism · Thermodynamics · Statistical Mechanics · Relativity · Quantum Mechanics · Quantum Field Theory · High-Energy Physics · Quantum Gravity · String & M-Theory · Condensed Matter · Cosmology & Astrophysics · Constants of Nature

Natural sciences: Chemistry · Advanced Chemistry · Biology · Life Sciences · Neuroscience · Earth & Space Science

Human sciences: Finance & Economics · Economics & Finance · Game Theory · Strategy & Games · Gambling & Odds · Social Dynamics · Social Organization · Institutions & Culture · Behavioral Science · Medicine & Physiology · Psychology · Language & Linguistics · Arts & Aesthetics · Ethnomathematics · Games & Gaming Math

Logic & computation: Formal Logic · Computer Science & AI

Philosophy: Metaphysics · Epistemology · Ethics · Philosophy of Mind · Eastern Philosophy · Philosophy of Religion

Symbolic: Sacred Numbers · Sacred Geometry · Zodiac · Classical Planets · Classical Elements · Esoteric Systems · I Ching · Chakras & Subtle Body · Myth & Archetype

Speculative (flagged): Reciprocal Framework · Spacetime Foam Field · Wormholes & Travel · Harmonic Resonance · Emergent Gravity · Foam Detection · Reciprocal Applied · Geometric Psychology · Reciprocal Chemistry · Reciprocal Biology · Navigator (Travel) · The Looking Glass · PRI · Infinite Forms

**Every PRI / speculative equation is reverse-derived into the established science tree** — its lineage edges trace explicitly back through the physics, mathematics, and chemistry it modifies or borrows from, so the structural relationship between the speculative and the established is visible rather than asserted.

---

## Notes on accuracy

- Discovery dates are best-estimate "first clear formulation" years. Attribution is often contested; dates represent a faithful ordering, not precise claims.
- The symbolic and speculative strata are clearly labelled throughout and are included for their structural and connective interest, not as established science.
- Coverage is representative and curated, not exhaustive.

---

## Built with

[Three.js](https://threejs.org/) r128 · [KaTeX](https://katex.org/) · Vanilla JavaScript · Python 3 · Blender (optional)
