Blender 3MF Format (Blender 5 Fork)
====

> **Note:** This is a Blender 5-compatible fork of [Ghostkeeper's original Blender 3MF Format add-on](https://github.com/Ghostkeeper/Blender3mfFormat). The original add-on was designed for Blender 2.8-4.2. This fork has been updated to work with Blender 5.x using the new extension system.

## Maintenance Status

⚠️ **Community Maintained / Minimal Support**

This is a personal fork created for Blender 5 compatibility and 3MF v1.4.0 support. 
It is provided **as-is** with no guarantee of ongoing maintenance or support.

- ✅ **Works:** Blender 5.0+ with 3MF v1.4.0 specification
- ✅ **Tested:** Import/export functionality verified with triangle sets
- ⚠️ **Issues:** May not be addressed - community support only
- 💡 **Pull Requests:** Welcome but not guaranteed to be reviewed/merged
- 🍴 **Forking Encouraged:** Feel free to fork and maintain your own version

**For the original version (Blender 2.8-4.2):** See [Ghostkeeper's repository](https://github.com/Ghostkeeper/Blender3mfFormat).

This is a Blender extension that allows importing and exporting 3MF files.

3D Manufacturing Format files (.3mf) are a file format for triangular meshes intended to serve as exchange format for 3D printing applications. They can communicate not only the model, but also the intent and material of a 3D printing job from the CAD software to the CAM software (slicer). In this scenario, Blender serves as the CAD software. To that end, the aim of this extension is to make Blender a more viable alternative as CAD software for additive manufacturing.

## Requirements

- **Blender 4.2 or newer** (tested with Blender 5.0)
- This extension uses the new Blender 5 extension format with `blender_manifest.toml`

## Installation

### From Release (Recommended)
1. Download the latest release `.zip` file from the releases page
   - **For Blender 5.x:** Use this fork's releases
   - **For Blender 2.8-4.2:** Use [Ghostkeeper's original releases](https://github.com/Ghostkeeper/Blender3mfFormat/releases/latest)
2. In Blender, go to **Edit → Preferences → Extensions** (Blender 5) or **Add-ons** (Blender 4.2 and earlier)
3. Click on the **Install from Disk** button (dropdown arrow next to the install icon)
4. Navigate to and select the downloaded `.zip` file
5. The extension will appear in the list - make sure it's enabled

### Building from Source
If you want to build the extension yourself:

1. Clone this repository
2. Make sure Blender is in your system PATH, or use the build scripts:
   ```bash
   # Using Blender's command-line tool
   blender --command extension build
   
   # Or using PowerShell script
   .\build.ps1
   
   # Or using Python script
   python build.py
   ```
3. Install the generated `.zip` file in Blender as described above

### For Development (VS Code)
1. Open the project folder in VS Code
2. Use **Ctrl+Shift+B** to run the default build task
3. Tasks available:
   - **Build Extension** (default) - Creates the extension .zip file
   - **Validate Extension** - Checks the manifest and structure
   - **Clean Build Artifacts** - Removes generated .zip files

Usage
----
When this add-on is installed, a new entry will appear under the File -> Import menu called "3D Manufacturing Format". When you click that, you'll be able to select 3MF files to import into your Blender scene. A new entry will also appear under the File -> Export menu with the same name. This allows you to export your scene to a 3MF file.

![Screenshot](screenshot.png)

The following options are available when importing 3MF files:
* Scale: A scaling factor to apply to the scene after importing. All of the mesh data loaded from the 3MF files will get scaled by this factor from the origin of the coordinate system. They are not scaled individually from the centre of each mesh, but all from the coordinate origin.

The following options are available when exporting to 3MF:
* Selection only: Only export the objects that are selected. Other objects will not be included in the 3MF file.
* Scale: A scaling factor to apply to the models in the 3MF file. The models are scaled by this factor from the coordinate origin.
* Apply modifiers: Apply the modifiers to the mesh data before exporting. This embeds these modifiers permanently in the file. If this is disabled, the unmodified meshes will be saved to the 3MF file instead.
* Precision: Number of decimals to use for coordinates in the 3MF file. Greater precision will result in a larger file size.

Scripting
----
From a script, you can import a 3MF mesh by executing the following function call:

```
bpy.ops.import_mesh.threemf(filepath="/path/to/file.3mf")
```

This import function has two relevant parameters:
* `filepath`: A path to the 3MF file to import.
* `global_scale` (default `1`): A scaling factor to apply to the scene after importing. All of the mesh data loaded from the 3MF files will get scaled by this factor from the origin of the coordinate system.

You can export a 3MF mesh by executing the following function call:

```
bpy.ops.export_mesh.threemf(filepath="/path/to/file.3mf")
```

This export function has five relevant parameters:
* `filepath`: The location to store the 3MF file.
* `use_selection` (default `False`): Only export the objects that are selected. Other objects will not be included in the 3MF file.
* `global_scale` (default `1`): A scaling factor to apply to the models in the 3MF file. The models are scaled by this factor from the coordinate origin.
* `use_mesh_modifiers` (default `True`): Apply the modifiers to the mesh data before exporting. This embeds these modifiers permanently in the file. If this is disabled, the unmodified meshes will be saved to the 3MF file instead.
* `coordinate_precision` (default `4`): Number of decimals to use for coordinates in the 3MF file. Greater precision will result in a larger file size.

## Credits and License

This extension is a Blender 5 fork of Ghostkeeper's original work. See [CREDITS.md](CREDITS.md) for detailed attribution.

**License:** GNU General Public License v2.0 or later (GPL-2.0-or-later)

The original add-on was created by Ghostkeeper and is available at:
https://github.com/Ghostkeeper/Blender3mfFormat

## 3MF Specification Support

**Current Support:** [3MF Core Specification v1.4.0](https://github.com/3MFConsortium/spec_core) (February 2025) ✅

**Fully Up-to-Date!** This extension supports the latest 3MF specification including:
- ✅ **v1.4.0 Compliance** - Latest specification with enhanced clarifications
- ✅ **v1.3.0 Triangle Sets** - Full import/export of triangle groups with material assignments
- ✅ **Component/Assembly Handling** - Verified against v1.4.0 clarifications

### Supported Features (all versions):
- **Mesh Geometry:** Full import/export with automatic triangulation
- **Triangle Sets (v1.3.0):** Group triangles by material for better organization
- **Materials & Colors:** Base materials with RGB/RGBA color support
- **Components & Assemblies:** Hierarchical object structures with transformations
- **Metadata:** Scene-level and object-level metadata preservation
- **Unit Conversions:** Automatic conversion between mm, cm, inch, meter, etc.
- **Transformations:** Full 4x4 matrix support with scaling, rotation, translation
- **Build Items:** Multiple objects with independent transformations
- **Error Recovery:** Graceful handling of malformed files (continues loading valid data)

### v1.4.0 Clarifications Implemented:
- Enhanced assembly/component relationship handling
- Improved transformation validation and error reporting
- Compliant naming conventions for objects and metadata
- Better handling of complex nested hierarchies

### Specification Compliance

This add-on currently supports the full 3MF Core Specification v1.4.0. However there are a number of places where it deviates from the specification on purpose.

The 3MF specification demands that consumers of 3MF files (i.e. importing 3MF files) must fail quickly and catastrophically when anything is wrong. If a single field is wrong, the entire archive should not get loaded. This add-on has the opposite approach: If something small is wrong with the file, the rest of the file can still be loaded, but for instance without loading that particular triangle that's wrong. You'll get an incomplete file and a warning is placed in the Blender log.

The 3MF specification is also not designed to handle loading multiple 3MF files at once, or to load 3MF files into existing scenes together with other 3MF files. This add-on will try to load as much as possible, but if there are conflicts with parts of the files, it will load neither. One example is the scene metadata such as the title of the scene. If loading two files with the same title, that title is kept. However when combining files with multiple titles, no title will be loaded.

No 3MF format extensions are currently supported. That is a goal for future development.

## Want to Fork or Contribute?

🍴 **Forking is Encouraged!**

This is a community-maintained project with minimal active support. If you:
- Need features or fixes urgently
- Want to maintain an actively-supported version
- Have ideas for improvements

**Please fork this repository!** See [CONTRIBUTING-FORK.md](CONTRIBUTING-FORK.md) for details.

If you create an actively-maintained fork, let us know and we'll link to it here so users can find the best version for their needs.

## Contact Ghostkeeper (Original Author)

If you'd like to reach out to the original author about integrating these changes or discussing the fork, see [GHOSTKEEPER-CONTACT.md](GHOSTKEEPER-CONTACT.md) for a message template.
