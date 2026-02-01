"""
Generate a valid 3MF test file with Triangle Sets for compliance verification.

This creates a simple 3MF file directly (without Blender) to test Triangle Sets compliance.
"""

import zipfile
import os
from io import BytesIO

# 3D Model XML with Triangle Sets extension
MODEL_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" xmlns:t="http://schemas.microsoft.com/3dmanufacturing/trianglesets/2021/07">
  <resources>
    <basematerials id="1">
      <base name="Red" displaycolor="#FF0000"/>
      <base name="Green" displaycolor="#00FF00"/>
      <base name="Blue" displaycolor="#0000FF"/>
    </basematerials>
    <object id="2" name="MultiMaterialCube" type="model">
      <mesh>
        <vertices>
          <vertex x="-5" y="-5" z="0"/>
          <vertex x="5" y="-5" z="0"/>
          <vertex x="5" y="5" z="0"/>
          <vertex x="-5" y="5" z="0"/>
          <vertex x="-5" y="-5" z="10"/>
          <vertex x="5" y="-5" z="10"/>
          <vertex x="5" y="5" z="10"/>
          <vertex x="-5" y="5" z="10"/>
        </vertices>
        <triangles>
          <triangle v1="0" v2="1" v3="2" pid="1" p1="0"/>
          <triangle v1="0" v2="2" v3="3" pid="1" p1="0"/>
          <triangle v1="4" v2="6" v3="5" pid="1" p1="0"/>
          <triangle v1="4" v2="7" v3="6" pid="1" p1="0"/>
          <triangle v1="0" v2="4" v3="5" pid="1" p1="1"/>
          <triangle v1="0" v2="5" v3="1" pid="1" p1="1"/>
          <triangle v1="1" v2="5" v3="6" pid="1" p1="1"/>
          <triangle v1="1" v2="6" v3="2" pid="1" p1="1"/>
          <triangle v1="2" v2="6" v3="7" pid="1" p1="2"/>
          <triangle v1="2" v2="7" v3="3" pid="1" p1="2"/>
          <triangle v1="3" v2="7" v3="4" pid="1" p1="2"/>
          <triangle v1="3" v2="4" v3="0" pid="1" p1="2"/>
        </triangles>
        <t:trianglesets>
          <t:triangleset name="Red_Faces" identifier="ts_0">
            <t:ref index="0"/>
            <t:ref index="1"/>
          </t:triangleset>
          <t:triangleset name="Green_Faces" identifier="ts_1">
            <t:ref index="4"/>
            <t:ref index="5"/>
            <t:ref index="6"/>
            <t:ref index="7"/>
          </t:triangleset>
          <t:triangleset name="Blue_Faces" identifier="ts_2">
            <t:ref index="8"/>
            <t:ref index="9"/>
            <t:ref index="10"/>
            <t:ref index="11"/>
          </t:triangleset>
        </t:trianglesets>
      </mesh>
    </object>
  </resources>
  <build>
    <item objectid="2"/>
  </build>
</model>'''

# Content Types XML
CONTENT_TYPES_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
</Types>'''

# Relationships XML
RELS_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Target="/3D/3dmodel.model" Id="rel0" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
</Relationships>'''

def create_3mf_file(output_path):
    """Create a valid 3MF file with Triangle Sets."""
    
    # Create ZIP file
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add required files
        zf.writestr('[Content_Types].xml', CONTENT_TYPES_XML)
        zf.writestr('_rels/.rels', RELS_XML)
        zf.writestr('3D/3dmodel.model', MODEL_XML)
    
    print(f"✓ Created: {output_path}")
    print(f"  - Size: {os.path.getsize(output_path)} bytes")
    print(f"  - Contains 3 Triangle Sets with identifiers ts_0, ts_1, ts_2")
    print(f"  - Uses correct Triangle Sets namespace: xmlns:t=\"http://schemas.microsoft.com/3dmanufacturing/trianglesets/2021/07\"")
    print(f"  - Each triangle set has required 'name' and 'identifier' attributes")
    print(f"  - Triangle references use <t:ref index=\"N\"/> format")

if __name__ == "__main__":
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, "multimaterial_test_v2.2.1.3mf")
    create_3mf_file(output_file)
