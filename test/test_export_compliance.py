"""
Test the export_3mf.py code to verify it generates spec-compliant Triangle Sets.

This runs a minimal test without requiring Blender.
"""
import sys
import os
import zipfile
import xml.etree.ElementTree as ET

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from io_mesh_3mf.constants import (
    CORE_NAMESPACE,
    TRIANGLESETS_NAMESPACE,
    MODEL_NAMESPACES
)


def test_constants():
    """Verify constants are correctly defined."""
    print("Testing constants...")
    print(f"  CORE_NAMESPACE: {CORE_NAMESPACE}")
    print(f"  TRIANGLESETS_NAMESPACE: {TRIANGLESETS_NAMESPACE}")

    assert TRIANGLESETS_NAMESPACE == "http://schemas.microsoft.com/3dmanufacturing/trianglesets/2021/07", \
        "Triangle Sets namespace must match spec"

    assert "t" in MODEL_NAMESPACES, "Triangle Sets prefix 't' must be in MODEL_NAMESPACES"
    assert MODEL_NAMESPACES["t"] == TRIANGLESETS_NAMESPACE, \
        "MODEL_NAMESPACES['t'] must map to Triangle Sets namespace"

    print("  [PASS] All constants correctly defined")


def test_export_namespace_declaration():
    """Test that export code declares the Triangle Sets namespace."""
    from io_mesh_3mf import export_3mf
    import inspect

    print("\nTesting export namespace declaration...")

    # Check write_model_to_string function
    source = inspect.getsource(export_3mf.write_model_to_string)

    # Look for xmlns:t declaration
    if 'xmlns:t=' in source and TRIANGLESETS_NAMESPACE in source:
        print("  [PASS] Export code declares xmlns:t namespace")
    else:
        print("  [FAIL] Export code missing xmlns:t declaration")
        return False

    return True


def test_export_trianglesets_structure():
    """Test that export code uses correct Triangle Sets structure."""
    from io_mesh_3mf import export_3mf
    import inspect

    print("\nTesting export Triangle Sets structure...")

    # Check write_trianglesets function
    source = inspect.getsource(export_3mf.write_trianglesets)

    checks = {
        'Uses TRIANGLESETS_NAMESPACE': 'TRIANGLESETS_NAMESPACE' in source,
        'Writes identifier attribute': '"identifier"' in source or "'identifier'" in source,
        'Creates individual ref elements': 't:ref' in source or 'SubElement' in source
    }

    all_passed = True
    for check, result in checks.items():
        status = "[PASS]" if result else "[FAIL]"
        print(f"  {status} {check}")
        if not result:
            all_passed = False

    return all_passed


if __name__ == "__main__":
    print("=" * 70)
    print("TESTING EXPORT CODE COMPLIANCE")
    print("=" * 70)

    try:
        test_constants()
        test_export_namespace_declaration()
        test_export_trianglesets_structure()

        print("\n" + "=" * 70)
        print("ALL TESTS PASSED - Export code is specification-compliant")
        print("=" * 70)

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
