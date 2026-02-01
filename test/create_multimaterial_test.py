"""
Create a multi-material test model for Triangle Sets verification.

This script creates a simple cube with 3 materials assigned to different faces
and exports it as 3MF to verify Triangle Sets compliance.

Run in Blender:
    blender --background --python create_multimaterial_test.py

Or from Blender's scripting tab.
"""

import bpy
import os

# Clear existing mesh objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create a cube
bpy.ops.mesh.primitive_cube_add(size=10, location=(0, 0, 5))
cube = bpy.context.active_object
cube.name = "MultiMaterialCube"

# Create three materials
materials = []
material_colors = [
    ("Material_Red", (0.8, 0.1, 0.1, 1.0)),
    ("Material_Green", (0.1, 0.8, 0.1, 1.0)),
    ("Material_Blue", (0.1, 0.1, 0.8, 1.0))
]

for mat_name, color in material_colors:
    mat = bpy.data.materials.new(name=mat_name)
    mat.use_nodes = True
    mat.diffuse_color = color

    # Set principled BSDF base color
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = color

    materials.append(mat)
    cube.data.materials.append(mat)

# Enter edit mode and assign materials to different faces
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='OBJECT')

# Assign materials to face groups
# Red: Top and bottom (faces 0, 1)
# Green: Front and back (faces 2, 3)
# Blue: Left and right (faces 4, 5)
mesh = cube.data

for i, face in enumerate(mesh.polygons):
    if i < 2:
        face.material_index = 0  # Red
    elif i < 4:
        face.material_index = 1  # Green
    else:
        face.material_index = 2  # Blue

# Export as 3MF
output_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(output_dir, "multimaterial_test_v2.2.1.3mf")

# Make sure the export operator is available
if hasattr(bpy.ops, 'export_mesh') and hasattr(bpy.ops.export_mesh, 'threemf'):
    bpy.ops.export_mesh.threemf(
        filepath=output_file,
        use_selection=False,
        global_scale=1.0,
        use_mesh_modifiers=True,
        coordinate_precision=4
    )
    print(f"✓ Exported to: {output_file}")
    print(f"  - 3 materials assigned")
    print(f"  - Should generate 3 triangle sets with identifiers ts_0, ts_1, ts_2")
    print(f"  - Should use Triangle Sets namespace with t: prefix")
else:
    # Fallback: just save the blend file
    blend_file = os.path.join(output_dir, "multimaterial_test_model.blend")
    bpy.ops.wm.save_as_mainfile(filepath=blend_file)
    print(f"✓ Saved Blender file: {blend_file}")
    print(f"  Note: 3MF export operator not available in this context")
    print(f"  Please export manually using File -> Export -> 3D Manufacturing Format")

print("\nModel details:")
print(f"  - Object: {cube.name}")
print(f"  - Vertices: {len(mesh.vertices)}")
print(f"  - Faces: {len(mesh.polygons)}")
print(f"  - Materials: {len(cube.data.materials)}")
for i, mat in enumerate(cube.data.materials):
    print(f"    {i}: {mat.name}")
