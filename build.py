#!/usr/bin/env python3
"""
Build script for the 3MF Blender extension.
This script provides an alternative to using Blender's command-line build tools.
"""

import os
import sys
import zipfile
import shutil
from pathlib import Path

# Extension information
EXTENSION_ID = "io_mesh_3mf"
VERSION = "2.2.0"
OUTPUT_FILE = f"{EXTENSION_ID}-{VERSION}.zip"

# Files and directories to exclude
EXCLUDE_PATTERNS = [
    "__pycache__",
    ".git",
    ".github",
    ".vscode",
    "*.pyc",
    "*.pyo",
    "*.zip",
    "*.blend",
    "*.blend1",
    "test",
    "build.py",
    "build.ps1",
    "CHANGES.md",
    "CONTRIBUTING.md",
    "screenshot.png",
    ".gitignore",
    ".gitattributes"
]


def should_exclude(path: Path, base_path: Path) -> bool:
    """Check if a path should be excluded based on exclude patterns."""
    rel_path = path.relative_to(base_path)
    path_str = str(rel_path).replace('\\', '/')
    
    for pattern in EXCLUDE_PATTERNS:
        if pattern.startswith('*'):
            # File extension pattern
            if path.name.endswith(pattern[1:]):
                return True
        elif pattern.endswith('/'):
            # Directory pattern
            if any(part == pattern[:-1] for part in rel_path.parts):
                return True
        else:
            # Exact match
            if pattern in rel_path.parts or path.name == pattern:
                return True
    
    return False


def build_extension():
    """Build the extension ZIP file."""
    base_path = Path(__file__).parent
    output_path = base_path / OUTPUT_FILE
    
    # Remove existing build
    if output_path.exists():
        print(f"Removing existing build: {output_path}")
        output_path.unlink()
    
    print(f"Building extension: {OUTPUT_FILE}")
    print(f"Base path: {base_path}")
    
    # Create ZIP file
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add files
        for root, dirs, files in os.walk(base_path):
            root_path = Path(root)
            
            # Filter directories
            dirs[:] = [d for d in dirs if not should_exclude(root_path / d, base_path)]
            
            for file in files:
                file_path = root_path / file
                
                # Skip excluded files
                if should_exclude(file_path, base_path):
                    continue
                
                # Calculate archive name
                arcname = file_path.relative_to(base_path)
                
                print(f"  Adding: {arcname}")
                zipf.write(file_path, arcname)
    
    print(f"\n✓ Extension built successfully: {output_path}")
    print(f"  File size: {output_path.stat().st_size / 1024:.2f} KB")
    
    return output_path


if __name__ == "__main__":
    try:
        build_extension()
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Build failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
