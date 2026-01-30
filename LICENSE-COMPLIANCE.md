# License Compliance Summary

## Overview

This document verifies that the Blender 5 fork of the 3MF Format extension complies with the GNU General Public License v2.0 (GPL-2.0-or-later) requirements of the original work.

## Original Work

- **Project:** Blender 3MF Format
- **Author:** Ghostkeeper
- **Repository:** https://github.com/Ghostkeeper/Blender3mfFormat
- **License:** GNU General Public License v2.0 or later (GPL-2.0-or-later)
- **Copyright:** 2020-2024 Ghostkeeper

## This Fork

- **Version:** 2.0.0 (Blender 5 compatible)
- **License:** GNU General Public License v2.0 or later (GPL-2.0-or-later)
- **Copyright:** 
  - 2020-2024 Ghostkeeper (original work)
  - 2026 Lee Gillie, CCP (Blender 5 fork modifications)

## GPL-2.0 Compliance Checklist

### ✅ Section 1: Copyright Notices
- [x] Original copyright notice preserved in all source files
- [x] License text included in repository ([LICENSE.md](LICENSE.md))
- [x] Copyright information in manifest ([blender_manifest.toml](blender_manifest.toml))

### ✅ Section 2(a): Modification Notices
- [x] Modified files carry notices of changes (see [CHANGELOG.md](CHANGELOG.md))
- [x] Date of changes documented (2026-01-30)
- [x] Nature of changes clearly described in documentation

### ✅ Section 2(b): License Distribution
- [x] This work is licensed under GPL-2.0-or-later (same as original)
- [x] Available at no charge to all third parties
- [x] License terms clearly stated

### ✅ Section 3: Source Code Availability
- [x] Complete source code is available
- [x] No compiled or binary-only components
- [x] All modifications are in source form

### ✅ Additional Best Practices
- [x] Clear attribution to original author (Ghostkeeper)
- [x] Link to original repository provided
- [x] Fork clearly identified as derivative work
- [x] Credits file documenting all contributors ([CREDITS.md](CREDITS.md))
- [x] Changelog documenting all changes ([CHANGELOG.md](CHANGELOG.md))

## Modifications Made

This fork maintains **100% of the original functionality** while adding:

1. **Blender 5 Compatibility**
   - New extension format with `blender_manifest.toml`
   - Updated packaging structure
   - API compatibility updates

2. **Development Tooling**
   - VS Code configuration
   - Build scripts (Python and PowerShell)
   - Development documentation

3. **Documentation Updates**
   - Installation instructions for Blender 5
   - Build process documentation
   - Clear attribution and licensing information

## Important Notes

### What This Fork Does NOT Do
- ❌ Change the license terms
- ❌ Remove attribution to the original author
- ❌ Make the software proprietary
- ❌ Add additional restrictions

### What This Fork DOES Do
- ✅ Preserve all original functionality
- ✅ Maintain GPL-2.0-or-later license
- ✅ Clearly identify as a derivative work
- ✅ Provide proper attribution
- ✅ Document all changes

## SPDX License Identifier

As specified in the manifest:
```toml
license = [
  "SPDX:GPL-2.0-or-later",
]
```

This is the same license as the original work, ensuring compatibility.

## Copyright Statements

All source files maintain the original copyright header:
```python
# Blender add-on to import and export 3MF files.
# Copyright (C) 2020 Ghostkeeper
# This add-on is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later
# version.
```

The manifest includes both original and fork copyright:
```toml
copyright = [
  "2020-2024 Ghostkeeper (original author)",
  "2026 Blender 5 Fork Contributors",
]
```

## Distribution Permissions

Under GPL-2.0-or-later, anyone may:
- ✅ Use this software for any purpose
- ✅ Study and modify the source code
- ✅ Distribute copies of the software
- ✅ Distribute modified versions

**Conditions:**
- Must distribute under the same GPL-2.0-or-later license
- Must provide source code
- Must preserve copyright notices
- Must document changes

## Conclusion

This Blender 5 fork **fully complies** with the GPL-2.0-or-later license requirements of Ghostkeeper's original work. All modifications are:

1. Properly attributed
2. Clearly documented
3. Distributed under the same license
4. Available in source form
5. Respectful of the original author's rights

---

**Last Updated:** January 30, 2026  
**Verified By:** Fork Maintainers
