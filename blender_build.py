#!/usr/bin/env python3
"""
blender_build.py  -  rebuilds The Atlas of Everything inside Blender as real
3D geometry, reading the same knowledge_core.json the web app uses.

USAGE
  Place this file next to knowledge_core.json, then either:
    blender --background --python blender_build.py        (headless build+save)
  or open Blender, load this in the Text Editor, and press "Run Script".

It creates emission-lit spheres for every equation and beveled-curve tubes for
every lineage and constant-thread edge, grouped in an "Atlas" collection.
"""
import bpy, json, os, math, mathutils

HERE = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
CORE = json.load(open(os.path.join(HERE, "knowledge_core.json"), encoding="utf-8"))

def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16)/255.0 for i in (0, 2, 4))

# ---- fresh collection -----------------------------------------------------
for c in list(bpy.data.collections):
    if c.name == "Atlas":
        for o in list(c.objects):
            bpy.data.objects.remove(o, do_unlink=True)
        bpy.data.collections.remove(c)
atlas = bpy.data.collections.new("Atlas")
bpy.context.scene.collection.children.link(atlas)

# ---- one emission material per domain ------------------------------------
mats = {}
for d in CORE["domains"]:
    m = bpy.data.materials.new("dom_" + d["id"]); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    emi = nt.nodes.new("ShaderNodeEmission")
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    r, g, b = hex2rgb(d["color"])
    emi.inputs["Color"].default_value = (r, g, b, 1)
    emi.inputs["Strength"].default_value = 3.5
    nt.links.new(emi.outputs["Emission"], out.inputs["Surface"])
    mats[d["id"]] = m

gold = bpy.data.materials.new("seed_gold"); gold.use_nodes = True
nt = gold.node_tree; nt.nodes.clear()
emi = nt.nodes.new("ShaderNodeEmission"); out = nt.nodes.new("ShaderNodeOutputMaterial")
emi.inputs["Color"].default_value = (1.0, 0.85, 0.42, 1); emi.inputs["Strength"].default_value = 8.0
nt.links.new(emi.outputs["Emission"], out.inputs["Surface"])

# ---- node spheres ---------------------------------------------------------
SCALE = 0.05                      # shrink the matrix into a comfortable Blender scale
pos = {}
for e in CORE["equations"]:
    seed = e["id"] == "unity"
    rad = 0.9 if seed else 0.18 + math.sqrt(e["T"]) * 0.07
    bpy.ops.mesh.primitive_uv_sphere_add(radius=rad, segments=20, ring_count=12)
    ob = bpy.context.active_object
    ob.name = "eq_" + e["id"]
    p = mathutils.Vector(e["pos"]) * SCALE
    ob.location = p; pos[e["id"]] = p
    bpy.ops.object.shade_smooth()
    ob.data.materials.append(gold if seed else mats[e["domain"]])
    ob["equation"] = e["plain"]; ob["name_"] = e["name"]; ob["domain"] = e["domain"]
    ob["T"] = e["T"]; ob["O"] = e["O"]; ob["D"] = e["D"]; ob["stage"] = e["stage"]
    for c in list(ob.users_collection): c.objects.unlink(ob)
    atlas.objects.link(ob)

# ---- edge tubes (one curve object per kind) ------------------------------
def edge_curve(kind, name, color, depth):
    cu = bpy.data.curves.new(name, "CURVE"); cu.dimensions = "3D"
    cu.bevel_depth = depth; cu.resolution_u = 2
    for ed in CORE["edges"]:
        if ed["kind"] != kind: continue
        a = pos.get(ed["source"]); b = pos.get(ed["target"])
        if a is None or b is None: continue
        sp = cu.splines.new("POLY"); sp.points.add(1)
        sp.points[0].co = (a.x, a.y, a.z, 1); sp.points[1].co = (b.x, b.y, b.z, 1)
    ob = bpy.data.objects.new(name, cu)
    m = bpy.data.materials.new(name + "_mat"); m.use_nodes = True
    ntt = m.node_tree; ntt.nodes.clear()
    em = ntt.nodes.new("ShaderNodeEmission"); o2 = ntt.nodes.new("ShaderNodeOutputMaterial")
    em.inputs["Color"].default_value = (*color, 1); em.inputs["Strength"].default_value = 1.4
    ntt.links.new(em.outputs["Emission"], o2.inputs["Surface"])
    ob.data.materials.append(m)
    atlas.objects.link(ob)

edge_curve("lineage",  "lineage_threads",  (0.7, 0.74, 0.9), 0.012)
edge_curve("constant", "constant_threads", (0.56, 0.63, 0.85), 0.008)

# ---- dark world -----------------------------------------------------------
w = bpy.context.scene.world
if w and w.use_nodes:
    bg = w.node_tree.nodes.get("Background")
    if bg: bg.inputs[0].default_value = (0.02, 0.025, 0.05, 1); bg.inputs[1].default_value = 1.0

print("Atlas built in Blender: %d equations, %d edges." %
      (len(CORE["equations"]), len(CORE["edges"])))

# headless save
if bpy.app.background:
    out = os.path.join(HERE, "atlas.blend")
    bpy.ops.wm.save_as_mainfile(filepath=out)
    print("Saved", out)
