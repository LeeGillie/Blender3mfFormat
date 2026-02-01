# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.1] - 2026-02-01

### Changed - License Upgrade
- **IMPORTANT:** Upgraded license from GPL-2.0-or-later to GPL-3.0-or-later
  - Required for Blender Extensions platform submission
  - Permitted under original license's "or later" clause
  - All patent protections and user freedoms now covered by GPL-3.0
  - See [LICENSE](LICENSE) for full text

### Fixed - 3MF Triangle Sets Specification Compliance
**CRITICAL FIXES:** Corrected Triangle Sets implementation to fully comply with 3MF Core Specification v1.4.0

#### Triangle Sets Namespace (§4.1.5, Appendix C.3)
- **Fixed:** Triangle Sets now use the correct extension namespace: `http://schemas.microsoft.com/3dmanufacturing/trianglesets/2021/07`
- **Fixed:** Triangle Sets are properly prefixed with `t:` namespace in exported files
- **Fixed:** Model element declares `xmlns:t` namespace when triangle sets are present
- **Previous Issue:** Triangle Sets incorrectly used core namespace, producing invalid 3MF files

#### Required Identifier Attribute (§4.1.5.1, Appendix B.1.2)
- **Fixed:** Triangle Sets now include required `identifier` attribute per XSD schema
- **Fixed:** Identifiers are unique within each mesh (format: `ts_0`, `ts_1`, etc.)
- **Fixed:** Both `name` and `identifier` attributes are validated on import
- **Previous Issue:** Missing identifier attribute made files non-compliant with XSD schema

#### Non-Geometric Grouping Clarification (§4.1.5.1)
- **Fixed:** Triangle Sets are now correctly treated as **non-geometric organizational groupings**
- **Fixed:** Triangle Sets no longer generate materials or affect rendering on import
- **Fixed:** Removed random color generation for triangle sets
- **Previous Issue:** Triangle Sets were incorrectly treated as defining material assignments

#### Specification-Compliant Export
- **Fixed:** Individual `<ref>` elements with `index` attribute per spec §4.1.5.2
- **Fixed:** Support for `<refrange>` elements on import per spec §4.1.5.3
- **Fixed:** Proper namespace prefixing for all triangle set elements
- **Previous Issue:** Used text content instead of index attribute; wrong namespace

### Added
- **New Documentation:** [3MF-FOR-3D-PRINTING.md](3MF-FOR-3D-PRINTING.md) - Comprehensive guide on using 3MF for multi-material 3D printing
  - Explains 3MF use cases for Bambu Lab, Prusa MMU, and other multi-material printers
  - Clarifies how Blender materials map to filament assignments
  - Workflow guide for creating multi-material prints
  - Common questions and troubleshooting

### Changed
- Updated constants to include `TRIANGLESETS_NAMESPACE` 
- Updated `TriangleSet` namedtuple: changed `pid` to `identifier` (spec compliance)
- Enhanced Triangle Sets documentation to clarify they are organizational, not geometric
- Updated all Triangle Sets comments and docstrings for accuracy

### Documentation Updates
- README.md: Added 3D printing guide link and Triangle Sets clarifications
- V1.3.0-IMPLEMENTATION.md: Corrected Triangle Sets description and implementation details
- All documentation now reflects Triangle Sets as non-geometric groupings per spec

### Technical Notes
- Triangle Sets are now fully compliant with 3MF Core Specification v1.4.0
- Files exported by v2.2.1 will validate against the official XSD schema
- For multi-material printing: **Use standard 3MF base materials, not triangle sets**
- Triangle Sets are organizational tools for CAD/CAM workflows, not material assignment

### Migration from v2.2.0
- **No action required for most users**
- If you relied on triangle set random colors: Update workflow to use explicit materials
- Exported files from v2.2.1 are now spec-compliant and will work with all conforming consumers

## [2.2.0] - 2026-01-30

### Added - 3MF v1.4.0 Specification Support
- **Full v1.4.0 Compliance:** Updated to latest 3MF Core Specification (February 2025)
- Verified component and assembly handling against v1.4.0 clarifications
- Enhanced transformation matrix parsing and validation
- Improved object reference handling and error reporting
- Compliant with v1.4.0 naming conventions and best practices

### Changed
- Updated 3MF specification support from v1.3.0 to v1.4.0
- Enhanced documentation for assembly/component relationships
- Improved error handling for malformed object references

### Technical Notes
- v1.4.0 is primarily a clarification release (no breaking changes)
- All v1.3.0 features (triangle sets) remain fully supported
- Backward compatible with v1.2.3 and v1.3.0 files
- Component/assembly code verified against v1.4.0 specification
- Transformation handling compliant with v1.4.0 clarifications

## [2.1.0] - 2026-01-30

### Added - 3MF v1.3.0 Triangle Sets Support
- **Triangle Sets (`<trianglesets>`):** Full import and export support for v1.3.0 triangle sets feature
- Import triangle sets from 3MF files and map them to Blender materials
- Export meshes with multiple materials as triangle sets in 3MF files
- Triangle sets allow grouping triangles for better material assignment and organization
- Each triangle set can have a name and property/material ID
- Automatic color generation for triangle sets without explicit materials

### Changed
- Updated 3MF specification support from v1.2.3 to v1.3.0
- Enhanced ResourceObject structure to include triangle sets
- Improved material handling to support triangle set assignments

### Technical Details
- Added `read_trianglesets()` method to parse `<trianglesets>` elements
- Added `write_trianglesets()` method to export triangle groups
- Triangle sets map to Blender material slots for seamless integration
- Compatible with existing v1.2.3 files (backward compatible)

## [2.0.0] - 2026-01-30

### Added - Blender 5 Compatibility Fork
**Fork Maintainer:** Lee Gillie, CCP
- **BREAKING:** Updated to Blender 5 extension format with `blender_manifest.toml`
- Added VS Code development environment with tasks, settings, and launch configurations
- Created build scripts: `build.py` (Python) and `build.ps1` (PowerShell)
- Added development documentation: `DEVELOPMENT.md`, `QUICKSTART.md`, `CREDITS.md`
- Added proper GPL-3.0-or-later license attribution
- Restructured root `__init__.py` to properly import from `io_mesh_3mf` package
- Updated `.gitignore` for modern development workflow

### Changed
- **BREAKING:** Minimum Blender version is now 4.2.0 (using new extension system)
- Updated all documentation for Blender 5 workflow
- Simplified `io_mesh_3mf/__init__.py` (removed duplicate bl_info)
- Updated copyright to include both original author (Ghostkeeper) and fork contributors
- Changed version from 1.0.2 to 2.0.0 to indicate major compatibility change

### Maintained from v1.0.2
- Full 3MF Core Specification v1.2.3 support (from original add-on)
- All import/export functionality from Ghostkeeper's original work
- Support for materials, metadata, annotations, and unit conversions
- "Fail gracefully" approach to malformed 3MF files

### Future Considerations
- 3MF Core Specification v1.4.0 is now available (February 2025)
- v1.3.0 added triangle sets and mirror mesh features
- v1.4.0 added clarifications on assemblies and components
- See [3MF-SPEC-UPDATES.md](3MF-SPEC-UPDATES.md) for update roadmap

### Notes
- This is a fork of Ghostkeeper's original Blender 3MF Format add-on
- Original repository: https://github.com/Ghostkeeper/Blender3mfFormat
- For Blender 2.8-4.2, use the original add-on instead

---

## Previous Versions (by Ghostkeeper)

For changelog of versions 1.0.0-1.0.2, see:
https://github.com/Ghostkeeper/Blender3mfFormat/blob/master/CHANGES.md
