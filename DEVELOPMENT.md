# Blender 3MF Extension - Development Guide

## Project Structure

```
3MF-import-export/
├── blender_manifest.toml    # Blender 5 extension manifest (required)
├── __init__.py               # Main entry point for the extension
├── io_mesh_3mf/              # Core functionality package
│   ├── __init__.py
│   ├── import_3mf.py        # Import operator and logic
│   ├── export_3mf.py        # Export operator and logic
│   ├── annotations.py       # 3MF annotations handling
│   ├── constants.py         # Constants and definitions
│   ├── metadata.py          # Metadata parsing/writing
│   └── unit_conversions.py  # Unit conversion utilities
├── .vscode/
│   ├── tasks.json           # VS Code build tasks
│   └── settings.json        # Python and editor settings
├── build.py                 # Python build script
├── build.ps1                # PowerShell build script
└── README.md
```

## Blender 5 Extension Format

This extension follows the new Blender 5 extension format, which uses:
- `blender_manifest.toml` instead of `bl_info`
- Structured package layout
- Proper permissions declarations
- Build exclusion patterns

## Building the Extension

### Method 1: Blender Command-Line (Recommended)
```bash
blender --command extension build
```

This creates: `io_mesh_3mf-1.0.2.zip`

### Method 2: VS Code Tasks
Press `Ctrl+Shift+B` and select:
- **Build Extension** - Standard build
- **Validate Extension** - Check without building
- **Clean Build Artifacts** - Remove .zip files

### Method 3: Build Scripts

**PowerShell:**
```powershell
.\build.ps1
```

**Python:**
```bash
python build.py
```

## VS Code Setup

### Python Environment
The `.vscode/settings.json` configures Python autocomplete for Blender's API:
```json
{
    "python.analysis.extraPaths": [
        "C:\\Program Files\\Blender Foundation\\Blender 5.0\\5.0\\scripts\\modules"
    ]
}
```

**Note:** Update this path if Blender is installed elsewhere.

### Fake bpy Module (Optional)
For better autocomplete, install the fake-bpy-module:
```bash
pip install fake-bpy-module-5.0
```

Then update `.vscode/settings.json`:
```json
{
    "python.analysis.extraPaths": [
        "path/to/site-packages"
    ]
}
```

## Testing

### Manual Testing
1. Build the extension
2. Install in Blender (Edit → Preferences → Extensions)
3. Test import: File → Import → 3D Manufacturing Format
4. Test export: File → Export → 3D Manufacturing Format

### Quick Reinstall Workflow
1. Make code changes
2. Press `Ctrl+Shift+B` to build
3. In Blender:
   - Disable the extension
   - Remove it
   - Install the new `.zip`
   - Enable it

## Manifest Configuration

The `blender_manifest.toml` file contains:
- Extension metadata (name, version, author)
- Blender version requirements
- License information
- File permissions
- Build exclusion patterns

### Key Fields:
```toml
id = "io_mesh_3mf"              # Unique identifier
version = "1.0.2"                # Semantic versioning
blender_version_min = "4.2.0"   # Minimum Blender version
type = "add-on"                  # Extension type

[permissions]
files = "Import and export 3MF mesh files"

[build]
paths_exclude_pattern = [
  "__pycache__/",
  ".*",
  "*.zip",
  "test/",
]
```

## Common Issues

### Blender Not in PATH
If `blender --command extension build` fails:
1. Add Blender to system PATH, or
2. Use the full path: `"C:\Program Files\Blender Foundation\Blender 5.0\blender.exe" --command extension build`

### Import Errors
Make sure the project structure matches:
- `__init__.py` at root imports from `io_mesh_3mf/`
- All Python files use relative imports (`.` notation)

### Extension Won't Load
1. Validate the manifest: `blender --command extension validate`
2. Check Blender console for errors
3. Ensure `blender_version_min` is correct

## Contributing

When making changes:
1. Update version in `blender_manifest.toml`
2. Test import and export functionality
3. Validate the extension builds correctly
4. Update CHANGES.md with your changes

## Resources

- [Blender Extension Documentation](https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html)
- [3MF Specification](https://3mf.io/specification/)
- [Original Repository](https://github.com/Ghostkeeper/Blender3mfFormat)
