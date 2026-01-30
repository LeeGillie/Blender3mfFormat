# Blender add-on to import and export 3MF files.
# Copyright (C) 2020 Ghostkeeper
# This add-on is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later
# version.
# This add-on is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, write to the Free
# Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# <pep8 compliant>

"""
Core 3MF import/export functionality for Blender.

This module is imported by the main extension __init__.py file.
For Blender 5, extension metadata is in blender_manifest.toml at the root.
"""

# Reload functionality for development
if "bpy" in locals():
    import importlib
    if "import_3mf" in locals():
        importlib.reload(import_3mf)
    if "export_3mf" in locals():
        importlib.reload(export_3mf)

# Re-export the operators for easy import
from .import_3mf import Import3MF
from .export_3mf import Export3MF

__all__ = ['Import3MF', 'Export3MF']
