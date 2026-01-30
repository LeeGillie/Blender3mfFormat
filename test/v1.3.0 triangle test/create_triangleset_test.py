"""
Creates a simple 3MF file with v1.3.0 triangle sets feature.
This is a test file to verify how the extension handles triangle sets.
"""

import zipfile
import os

# Define the output file
output_file = "cube_with_trianglesets_v1.3.0.3mf"
output_path = os.path.join(os.path.dirname(__file__), output_file)

# Create the 3MF archive
with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    
    # 1. [Content_Types].xml
    content_types = '''<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
</Types>'''
    zipf.writestr('[Content_Types].xml', content_types)
    
    # 2. _rels/.rels
    rels = '''<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Target="/3D/3dmodel.model" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel" Id="rel-1"/>
</Relationships>'''
    zipf.writestr('_rels/.rels', rels)
    
    # 3. 3D/3dmodel.model with triangle sets (v1.3.0 feature)
    model = '''<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">
    <metadata name="Application">Blender 3MF Test File Generator</metadata>
    <metadata name="Title">Cube with Triangle Sets (v1.3.0)</metadata>
    
    <resources>
        <!-- Define a simple cube mesh -->
        <object id="1" name="Cube_with_TriangleSets" type="model">
            <mesh>
                <vertices>
                    <!-- Simple cube vertices -->
                    <vertex x="0.000000" y="0.000000" z="0.000000"/>
                    <vertex x="10.000000" y="0.000000" z="0.000000"/>
                    <vertex x="10.000000" y="10.000000" z="0.000000"/>
                    <vertex x="0.000000" y="10.000000" z="0.000000"/>
                    <vertex x="0.000000" y="0.000000" z="10.000000"/>
                    <vertex x="10.000000" y="0.000000" z="10.000000"/>
                    <vertex x="10.000000" y="10.000000" z="10.000000"/>
                    <vertex x="0.000000" y="10.000000" z="10.000000"/>
                </vertices>
                <triangles>
                    <!-- Bottom face (z=0) -->
                    <triangle v1="0" v2="2" v3="1"/>
                    <triangle v1="0" v2="3" v3="2"/>
                    
                    <!-- Top face (z=10) -->
                    <triangle v1="4" v2="5" v3="6"/>
                    <triangle v1="4" v2="6" v3="7"/>
                    
                    <!-- Front face (y=0) -->
                    <triangle v1="0" v2="1" v3="5"/>
                    <triangle v1="0" v2="5" v3="4"/>
                    
                    <!-- Back face (y=10) -->
                    <triangle v1="2" v2="3" v3="7"/>
                    <triangle v1="2" v2="7" v3="6"/>
                    
                    <!-- Left face (x=0) -->
                    <triangle v1="0" v2="4" v3="7"/>
                    <triangle v1="0" v2="7" v3="3"/>
                    
                    <!-- Right face (x=10) -->
                    <triangle v1="1" v2="2" v3="6"/>
                    <triangle v1="1" v2="6" v3="5"/>
                </triangles>
                
                <!-- Triangle Sets - v1.3.0 Feature -->
                <!-- Group triangles by face for different materials/properties -->
                <trianglesets>
                    <!-- Bottom and Top faces grouped together -->
                    <triangleset name="HorizontalFaces">
                        <ref>0 1 2 3</ref>
                    </triangleset>
                    
                    <!-- Front and Back faces -->
                    <triangleset name="FrontBackFaces">
                        <ref>4 5 6 7</ref>
                    </triangleset>
                    
                    <!-- Left and Right faces -->
                    <triangleset name="SideFaces">
                        <ref>8 9 10 11</ref>
                    </triangleset>
                </trianglesets>
            </mesh>
        </object>
    </resources>
    
    <build>
        <item objectid="1"/>
    </build>
</model>'''
    zipf.writestr('3D/3dmodel.model', model)

print(f"Created: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")
print("\nThis file contains:")
print("- A simple 10mm cube")
print("- Triangle sets grouping faces:")
print("  * HorizontalFaces: top and bottom")
print("  * FrontBackFaces: front and back")
print("  * SideFaces: left and right")
print("\nExpected behavior:")
print("- Should import geometry correctly")
print("- Triangle set grouping may be ignored (not yet implemented)")
print("- Should not crash (fail gracefully)")
