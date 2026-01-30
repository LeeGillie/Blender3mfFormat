# Quick Start - Building and Installing the 3MF Extension

## 1. Build the Extension

Choose one of these methods:

### Option A: VS Code (Easiest)
1. Open this folder in VS Code
2. Press `Ctrl+Shift+B` (Windows/Linux) or `Cmd+Shift+B` (Mac)
3. Select "Build Extension"
4. Done! The .zip file is created

### Option B: PowerShell
```powershell
.\build.ps1
```

### Option C: Python
```bash
python build.py
```

### Option D: Blender Command-Line
```bash
blender --command extension build
```

## 2. Install in Blender

1. Open Blender 4.2 or newer
2. Go to **Edit → Preferences**
3. Click on **Extensions** tab
4. Click the dropdown arrow next to the install button (⏷)
5. Select **Install from Disk**
6. Navigate to and select: `io_mesh_3mf-2.0.0.zip`
7. The extension will appear in the list - ensure it's enabled (checkbox)

## 3. Use the Extension

### Import a 3MF file:
1. **File → Import → 3D Manufacturing Format (.3mf)**
2. Select your .3mf file
3. Adjust scale if needed
4. Click Import

### Export to 3MF:
1. **File → Export → 3D Manufacturing Format (.3mf)**
2. Choose destination
3. Set options:
   - Selection Only (export selected objects only)
   - Scale factor
   - Apply modifiers
   - Precision
4. Click Export

## Troubleshooting

### "Blender is not recognized..."
- Add Blender to your system PATH, or
- Use the Python build script: `python build.py`

### Extension won't enable in Blender
- Make sure you're using Blender 4.2 or newer
- Check the Blender console for error messages
- Try: `blender --command extension validate` to check for issues

### Import/Export menu items don't appear
- Disable and re-enable the extension in Preferences
- Restart Blender
- Check that the extension is actually enabled (checkbox is checked)

## Development Workflow

1. Make code changes
2. Build: Press `Ctrl+Shift+B` in VS Code
3. In Blender:
   - Extensions → Click the three dots (⋮) next to the extension
   - Remove
   - Install the new .zip
   - Enable

## Need Help?

- See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed development guide
- See [README.md](README.md) for full documentation
- Check [Blender Extension Docs](https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html)
