# Testing Triangle Sets Compliance (v2.2.1)

## Quick Test Procedure

### Step 1: Create Multi-Material Test Model

Run in Blender to create a test cube with 3 materials:

```powershell
& "C:\Program Files\Blender Foundation\Blender 5.0\blender.exe" --background --python test/create_multimaterial_test.py
```

This creates:
- `test/multimaterial_test_v2.2.1.3mf` - Exported 3MF file
- OR `test/multimaterial_test_model.blend` - Blender file (if export operator unavailable)

**Model Details:**
- Simple 10mm cube
- 3 materials: Red, Green, Blue
- Each material assigned to 2 faces
- Should produce 3 triangle sets

### Step 2: Verify Export Compliance

Run the verification script:

```powershell
python test/verify_export.py test/multimaterial_test_v2.2.1.3mf
```

**Expected Output:**
```
✓ PASS: Triangle Sets namespace declared
  xmlns:t="http://schemas.microsoft.com/3dmanufacturing/trianglesets/2021/07"

✓ PASS: Found <t:trianglesets> in object 1
  (Correct namespace)

Triangle Set #1:
  Name: Material_Red
  ✓ Identifier: ts_0 (REQUIRED attribute present)
  References: X triangle(s)
  ✓ <t:ref index="0"/> (Correct structure)

Triangle Set #2:
  Name: Material_Green
  ✓ Identifier: ts_1 (REQUIRED attribute present)
  ...

Triangle Set #3:
  Name: Material_Blue
  ✓ Identifier: ts_2 (REQUIRED attribute present)
  ...

✓ ALL CHECKS PASSED - File is 3MF v1.4.0 compliant!
```

### Step 3: Manual XML Inspection (Optional)

Extract and view the XML:

```powershell
# Copy the .3mf file and rename to .zip
Copy-Item test/multimaterial_test_v2.2.1.3mf test/inspect.zip

# Extract
Expand-Archive test/inspect.zip -DestinationPath test/extracted -Force

# View the model XML
Get-Content test/extracted/3D/3dmodel.model
```

**Look for:**
1. `xmlns:t="http://schemas.microsoft.com/3dmanufacturing/trianglesets/2021/07"` in `<model>` tag
2. `<t:trianglesets>` (not `<trianglesets>`)
3. `<t:triangleset name="..." identifier="ts_0">` (both attributes present)
4. `<t:ref index="0"/>` (index attribute, not text content)

## Compliance Checklist

All of these should be TRUE:

- [ ] Model declares `xmlns:t` namespace
- [ ] Triangle sets use `<t:trianglesets>` not `<trianglesets>`
- [ ] Each `<t:triangleset>` has both `name` and `identifier` attributes
- [ ] Identifiers are unique (ts_0, ts_1, ts_2, etc.)
- [ ] Triangle references use `<t:ref index="N"/>` structure
- [ ] No elements in core namespace that should be in Triangle Sets namespace
- [ ] Verification script reports "ALL CHECKS PASSED"

## Alternative: Manual Test in Blender

If the automated scripts don't work:

1. **Open Blender**
2. **Create a cube** (Shift+A → Mesh → Cube)
3. **Create 3 materials**:
   - Material → New → Rename to "Red", set Base Color to red
   - Add material slot → New → Rename to "Green", set to green  
   - Add material slot → New → Rename to "Blue", set to blue
4. **Enter Edit Mode** (Tab)
5. **Select faces and assign materials**:
   - Select top/bottom faces → Assign material 0 (Red)
   - Select front/back faces → Assign material 1 (Green)
   - Select left/right faces → Assign material 2 (Blue)
6. **Export**: File → Export → 3D Manufacturing Format
7. **Run verification**: `python test/verify_export.py your_file.3mf`

## Expected Files After Testing

```
test/
├── multimaterial_test_v2.2.1.3mf   ← Exported test file
├── multimaterial_test_model.blend  ← Blender source (if created)
├── create_multimaterial_test.py    ← Generator script
├── verify_export.py                ← Verification script
└── README-TESTING.md               ← This file
```

## What Each Check Validates

### Issue #1: Namespace
- **Check:** `xmlns:t="http://schemas.microsoft.com/3dmanufacturing/trianglesets/2021/07"`
- **Requirement:** §4.1.5, Appendix C.3
- **Why:** Triangle Sets is an extension and must use its own namespace

### Issue #2: Identifier Attribute  
- **Check:** `identifier="ts_0"` present on each `<t:triangleset>`
- **Requirement:** §4.1.5.1, Appendix B.1.2 XSD
- **Why:** XSD schema defines identifier as `use="required"`

### Issue #3: Non-geometric Grouping
- **Check:** Import doesn't create random materials
- **Requirement:** §4.1.5.1
- **Why:** "do not have a specific influence on the geometrical shape"

### Issue #4: Namespace Declaration
- **Check:** Model element has `xmlns:t` attribute
- **Requirement:** §2.3.1
- **Why:** Extensions must be declared before use

### Issue #5: No Random Colors
- **Check:** Import preserves triangle sets but doesn't create materials
- **Requirement:** Not defined by spec (therefore shouldn't do it)
- **Why:** Spec doesn't define visual representation behavior

### Issue #6: Documentation
- **Check:** README and docs consistent
- **Requirement:** Blender Extensions review
- **Why:** Users need clear, accurate information

## Troubleshooting

### "blender: command not found"
Use full path:
```powershell
& "C:\Program Files\Blender Foundation\Blender 5.0\blender.exe" --background --python test/create_multimaterial_test.py
```

### "export_mesh.threemf not available"
The extension may not be loaded in background mode. Alternatives:
1. Run the script from Blender's Scripting tab (not background)
2. Manually export after running the model creation part

### Verification Script Shows Failures
If you see failures, check:
- The code changes were applied correctly
- The extension was rebuilt after changes
- You're testing the NEW exported file (v2.2.1), not an old one

### Need More Detail
Add verbose output to verify_export.py or inspect the raw XML directly

## Success Criteria

**The release is ready when:**
- ✓ Generator script creates multi-material model
- ✓ Export produces valid 3MF file
- ✓ Verification script shows "ALL CHECKS PASSED"
- ✓ Manual XML inspection confirms correct structure
- ✓ All 6 checklist items are TRUE
