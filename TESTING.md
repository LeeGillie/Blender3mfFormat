# Testing Guide for 3MF Extension

This guide covers multiple approaches to test the Blender 5 3MF extension, from quick manual testing to comprehensive automated testing.

## Quick Start Testing (Recommended First)

### Method 1: Install and Test in Blender 5

**Best for:** Quick validation that the extension works

1. **Build the extension:**
   ```powershell
   # In VS Code: Press Ctrl+Shift+B
   # Or run:
   python build.py
   ```

2. **Install in Blender:**
   - Open Blender 5
   - Edit → Preferences → Extensions
   - Click dropdown arrow → Install from Disk
   - Select `io_mesh_3mf-2.0.0.zip`
   - Enable the extension

3. **Quick Test - Import:**
   - File → Import → 3D Manufacturing Format (.3mf)
   - Try importing a sample 3MF file
   - Check if objects appear in scene
   - Verify materials, scale, transformations

4. **Quick Test - Export:**
   - Create a simple mesh (cube, sphere)
   - File → Export → 3D Manufacturing Format (.3mf)
   - Save to a file
   - Re-import the file to verify round-trip works

5. **Check Blender Console:**
   - Window → Toggle System Console (Windows)
   - Look for errors or warnings

**Time: 5-10 minutes**

---

## Development Testing Workflow

### Method 2: Rapid Development Cycle

**Best for:** Making changes and testing quickly

1. **Initial Setup:**
   - Note the extension install location in Blender
   - Typical: `%APPDATA%\Blender Foundation\Blender\5.0\extensions\user_default\io_mesh_3mf\`

2. **Development Cycle:**
   ```
   Make code changes → Build → Reinstall → Test → Repeat
   ```

3. **Streamlined Reinstall:**
   ```powershell
   # Build
   python build.py
   
   # In Blender:
   # - Extensions → Click ⋮ next to 3MF Format → Remove
   # - Install from Disk → Select new .zip
   # - Enable extension
   ```

4. **Optional: Direct File Replacement** (Advanced)
   - After first install, you can directly replace Python files in:
     `%APPDATA%\Blender Foundation\Blender\5.0\extensions\user_default\io_mesh_3mf\`
   - Restart Blender or reload scripts: F3 → "Reload Scripts"
   - **Warning:** Changes will be lost if extension is reinstalled

**Time per cycle: 2-3 minutes**

---

## Comprehensive Testing

### Method 3: Test with Sample 3MF Files

**Best for:** Validating real-world compatibility

1. **Get Sample Files:**
   - **3MF Consortium Samples:** https://github.com/3MFConsortium/3mf-samples
   - **3MF Test Suites:** https://github.com/3MFConsortium/test_suites/releases
   
   ```powershell
   # Download samples
   git clone https://github.com/3MFConsortium/3mf-samples.git
   ```

2. **Test Categories:**

   **Basic Geometry:**
   - Simple cube/sphere meshes
   - Multiple objects
   - Complex meshes (high polygon count)

   **Transformations:**
   - Rotated objects
   - Scaled objects
   - Transformed assemblies

   **Materials:**
   - Single material
   - Multi-material objects
   - Color properties

   **Assemblies:**
   - Nested components
   - Multiple instances
   - Complex hierarchies

3. **Create Test Matrix:**
   ```
   | Test File          | Import | Export | Round-trip | Notes      |
   |--------------------|--------|--------|------------|------------|
   | simple_cube.3mf    | ✓      | ✓      | ✓          | OK         |
   | multi_object.3mf   | ✓      | ✓      | ✓          | OK         |
   | materials.3mf      | ✓      | ⚠      | ?          | Colors off |
   ```

**Time: 1-2 hours for comprehensive testing**

---

## Automated Testing

### Method 4: Run Python Unit Tests

**Best for:** Regression testing, CI/CD

The extension includes a test suite. However, it needs Blender's Python environment.

1. **Locate Tests:**
   ```
   d:\Blender\3MF-import-export\test\
   ```

2. **Run Tests via Blender:**
   ```powershell
   # Run all tests
   blender --background --python-expr "import sys; sys.path.append('d:/Blender/3MF-import-export'); import unittest; loader = unittest.TestLoader(); suite = loader.discover('test'); runner = unittest.TextTestRunner(verbosity=2); runner.run(suite)"
   ```

3. **Run Specific Test:**
   ```powershell
   blender --background --python d:\Blender\3MF-import-export\test\import_3mf.py
   ```

4. **VS Code Task (Optional):**
   Add to `.vscode/tasks.json`:
   ```json
   {
       "label": "Run Tests",
       "type": "shell",
       "command": "blender",
       "args": [
           "--background",
           "--python-expr",
           "import sys; sys.path.append('${workspaceFolder}'); import unittest; loader = unittest.TestLoader(); suite = loader.discover('test'); runner = unittest.TextTestRunner(verbosity=2); runner.run(suite)"
       ]
   }
   ```

**Note:** The test suite may need updates for Blender 5 API changes.

**Time: Variable (automated once set up)**

---

## Test Scenarios

### Import Testing

**1. Basic Import:**
```
Test: Import a simple cube 3MF file
Expected: Cube appears in scene at origin
Verify: 
  - Object exists in outliner
  - Correct geometry (8 vertices, 6 faces)
  - Correct scale
```

**2. Multiple Objects:**
```
Test: Import 3MF with multiple objects
Expected: All objects imported
Verify:
  - Correct object count
  - Correct names
  - Correct positions
```

**3. Transformations:**
```
Test: Import objects with transformations
Expected: Transforms applied correctly
Verify:
  - Position matches
  - Rotation matches
  - Scale matches
```

**4. Materials:**
```
Test: Import object with materials
Expected: Materials imported and assigned
Verify:
  - Material exists
  - Color correct
  - Assigned to correct faces
```

### Export Testing

**1. Basic Export:**
```
Test: Export a Blender cube
Expected: Valid 3MF file created
Verify:
  - File is valid ZIP
  - Contains 3dmodel.model
  - Contains [Content_Types].xml
  - Can be re-imported
```

**2. Selection Export:**
```
Test: Export with "Selection Only" enabled
Expected: Only selected objects exported
Verify:
  - Correct object count in file
  - Unselected objects not included
```

**3. Scale Factor:**
```
Test: Export with scale factor 10
Expected: Objects scaled in exported file
Verify:
  - Coordinates multiplied by 10
  - Re-import with scale 0.1 matches original
```

**4. Modifiers:**
```
Test: Export object with modifiers
Expected: Modifiers applied (or not, based on setting)
Verify:
  - Modifier effects included/excluded correctly
  - Geometry matches expectation
```

### Round-trip Testing

**Critical Test:**
```
1. Create scene in Blender
2. Export to 3MF
3. Clear scene
4. Import the 3MF
5. Verify everything matches original
```

---

## Common Issues & Solutions

### Issue: Extension Won't Load
**Symptoms:** Extension doesn't appear in menu  
**Check:**
- Blender version is 4.2 or newer
- Extension is enabled in preferences
- Check Blender console for Python errors
- Verify `blender_manifest.toml` is valid

**Solution:**
```powershell
# Validate the extension
blender --command extension validate
```

### Issue: Import Fails Silently
**Symptoms:** No objects appear, no error  
**Check:**
- Blender console for warnings
- 3MF file is valid ZIP
- Contains `3D/3dmodel.model`

**Debug:**
- Add print statements to `io_mesh_3mf/import_3mf.py`
- Check return value from execute()

### Issue: Export Creates Invalid File
**Symptoms:** Exported file can't be imported  
**Check:**
- File is valid ZIP (can open with 7-Zip, WinRAR)
- Contains required files
- XML is well-formed

**Validate:**
```powershell
# Check if it's a valid ZIP
python -c "import zipfile; zipfile.ZipFile('output.3mf').testzip()"
```

### Issue: Materials Not Working
**Symptoms:** Objects import but colors are wrong  
**Note:** 
- v1.2.3 has limited material support
- Full materials require Materials Extension
- Check if source file uses extensions

---

## Testing Checklist

### Pre-Release Testing

- [ ] **Build:** Extension builds without errors
- [ ] **Validate:** `blender --command extension validate` passes
- [ ] **Install:** Extension installs in Blender 5
- [ ] **Enable:** Extension enables without errors
- [ ] **Menu:** Import/Export menu items appear
- [ ] **Import Basic:** Can import simple 3MF files
- [ ] **Export Basic:** Can export Blender objects
- [ ] **Round-trip:** Export then import matches original
- [ ] **Scale:** Scale parameter works on import/export
- [ ] **Selection:** "Selection Only" export works
- [ ] **Multi-object:** Multiple objects handled correctly
- [ ] **Console:** No Python errors in console
- [ ] **Samples:** Works with 3MF Consortium samples

### Extended Testing

- [ ] Large files (>100MB)
- [ ] Complex assemblies (>100 objects)
- [ ] High polygon meshes (>1M triangles)
- [ ] Various 3MF versions (if available)
- [ ] Error handling (malformed files)
- [ ] Performance (import/export speed)
- [ ] Memory usage (large files)

---

## Recommended Test Files

Create a `test_files/` folder with:

**1. `simple_cube.3mf`**
- Single cube
- No transformations
- No materials
- **Purpose:** Basic sanity check

**2. `multi_material.3mf`**
- Object with multiple materials
- Different colors per face group
- **Purpose:** Material handling

**3. `assembly.3mf`**
- Multiple objects
- Nested components
- Transformations
- **Purpose:** Complex scene handling

**4. `large_mesh.3mf`**
- High polygon count (>100k faces)
- **Purpose:** Performance testing

**5. `edge_cases.3mf`**
- Degenerate triangles
- Empty objects
- Special characters in names
- **Purpose:** Error handling

---

## Quick Test Script

Save as `quick_test.py`:

```python
import bpy
import os

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Test 1: Create and export
print("Test 1: Creating cube...")
bpy.ops.mesh.primitive_cube_add()
bpy.context.active_object.name = "TestCube"

export_path = os.path.expanduser("~/test_export.3mf")
print(f"Test 2: Exporting to {export_path}...")
bpy.ops.export_mesh.threemf(filepath=export_path)

# Test 2: Clear and import
print("Test 3: Clearing scene...")
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

print("Test 4: Importing...")
bpy.ops.import_mesh.threemf(filepath=export_path)

# Verify
if "TestCube" in bpy.data.objects:
    print("✓ Test PASSED: Cube successfully round-tripped")
else:
    print("✗ Test FAILED: Cube not found after import")

print(f"Objects in scene: {[obj.name for obj in bpy.data.objects]}")
```

Run in Blender:
```powershell
blender --python quick_test.py
```

---

## Recommended Testing Strategy

**For Initial Development:**
1. ✅ Manual testing in Blender 5 (Method 1)
2. ✅ Use 3-4 sample files of varying complexity
3. ✅ Test both import and export
4. ✅ Verify round-trip works

**For Each Change:**
1. ✅ Quick manual test with one file
2. ✅ Check Blender console for errors
3. ✅ Verify specific feature you changed

**Before Release:**
1. ✅ Full test suite with all sample files
2. ✅ Run automated tests (if updated for Blender 5)
3. ✅ Test on different Blender versions (4.2, 5.0, 5.1)
4. ✅ Complete testing checklist

**Time Investment:**
- Initial setup: 30 min
- Per-change testing: 5 min
- Pre-release testing: 2-3 hours

---

## Next Steps

1. **Build the extension** (5 min)
   ```powershell
   python build.py
   ```

2. **Install in Blender 5** (5 min)
   - Extensions → Install from Disk
   - Select `io_mesh_3mf-2.0.0.zip`

3. **Run quick test** (5 min)
   - Import a 3MF file
   - Export a simple object
   - Verify both work

4. **Report results**
   - Note any errors in console
   - Document any issues found
   - Create GitHub issues if needed

**Total time for first test: ~15 minutes**

Good luck! 🚀
