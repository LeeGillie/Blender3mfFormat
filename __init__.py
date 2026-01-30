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
Import and export 3MF files in Blender.

This is the main entry point for the Blender 5 extension.
For Blender 5, extensions use blender_manifest.toml instead of bl_info.
"""

# Reload functionality for development
if "bpy" in locals():
    import importlib
    if "import_3mf" in locals():
        importlib.reload(import_3mf)
    if "export_3mf" in locals():
        importlib.reload(export_3mf)

import bpy
import bpy.utils
import bpy.types

from .io_mesh_3mf.import_3mf import Import3MF
from .io_mesh_3mf.export_3mf import Export3MF


def menu_import(self, context):
    """
    Calls the 3MF import operator from the menu item.
    """
    self.layout.operator(Import3MF.bl_idname, text="3D Manufacturing Format (.3mf)")


def menu_export(self, context):
    """
    Calls the 3MF export operator from the menu item.
    """
    self.layout.operator(Export3MF.bl_idname, text="3D Manufacturing Format (.3mf)")


classes = (
    Import3MF,
    Export3MF
)


def register():
    """Register all classes and menu items."""
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.TOPBAR_MT_file_import.append(menu_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_export)


def unregister():
    """Unregister all classes and menu items."""
    bpy.types.TOPBAR_MT_file_import.remove(menu_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_export)
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


# Allow the add-on to be ran directly without installation
if __name__ == "__main__":
    register()
