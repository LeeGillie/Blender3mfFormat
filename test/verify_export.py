"""
Verify exported 3MF file for Triangle Sets compliance.

Usage:
    python verify_export.py multimaterial_test_v2.2.1.3mf
"""

import zipfile
import xml.etree.ElementTree as ET
import sys
import os


def verify_3mf_compliance(filepath):
    """Verify a 3MF file meets all Triangle Sets compliance requirements."""

    if not os.path.exists(filepath):
        print(f"✗ File not found: {filepath}")
        return False

    print(f"\n{'=' * 70}")
    print(f"VERIFYING 3MF COMPLIANCE: {os.path.basename(filepath)}")
    print(f"{'=' * 70}\n")

    # Required namespaces
    CORE_NS = "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
    TS_NS = "http://schemas.microsoft.com/3dmanufacturing/trianglesets/2021/07"

    namespaces = {
        '3mf': CORE_NS,
        't': TS_NS
    }

    all_checks_passed = True

    try:
        with zipfile.ZipFile(filepath, 'r') as archive:
            # Extract and parse the model
            with archive.open('3D/3dmodel.model') as model_file:
                content = model_file.read().decode('utf-8')
                tree = ET.ElementTree(ET.fromstring(content))
                root = tree.getroot()

                print("CHECK 1: Namespace Declaration")
                print("-" * 70)

                # Check for Triangle Sets namespace declaration in raw content
                has_ts_namespace = False

                if 'xmlns:t=' in content and TS_NS in content:
                    print(f"✓ PASS: Triangle Sets namespace declared")
                    print(f"  xmlns:t=\"{TS_NS}\"")
                    has_ts_namespace = True
                else:
                    print(f"✗ FAIL: Triangle Sets namespace NOT declared")
                    print(f"  Expected: xmlns:t=\"{TS_NS}\"")
                    all_checks_passed = False

                print("\nCHECK 2: Triangle Sets Structure")
                print("-" * 70)

                # Find triangle sets
                trianglesets_found = 0
                ts_in_core_ns = 0

                # Check for incorrectly namespaced triangle sets
                for obj in root.findall('.//{' + CORE_NS + '}trianglesets'):
                    ts_in_core_ns += 1
                    print(f"✗ FAIL: Found <trianglesets> in CORE namespace (invalid!)")
                    all_checks_passed = False

                # Check for correctly namespaced triangle sets
                for obj in root.findall('.//3mf:object', namespaces):
                    obj_id = obj.get('id')

                    for ts_container in obj.findall('.//t:trianglesets', namespaces):
                        trianglesets_found += 1
                        print(f"✓ PASS: Found <t:trianglesets> in object {obj_id}")
                        print(f"  (Correct namespace: {TS_NS})")

                        print("\nCHECK 3: Triangle Set Elements")
                        print("-" * 70)

                        for idx, ts in enumerate(ts_container.findall('t:triangleset', namespaces)):
                            name = ts.get('name')
                            identifier = ts.get('identifier')

                            print(f"\nTriangle Set #{idx + 1}:")
                            print(f"  Name: {name}")

                            # Check for identifier (REQUIRED)
                            if identifier:
                                print(f"  ✓ Identifier: {identifier} (REQUIRED attribute present)")
                            else:
                                print(f"  ✗ FAIL: Missing REQUIRED identifier attribute")
                                all_checks_passed = False

                            # Check ref elements
                            refs = ts.findall('t:ref', namespaces)
                            if refs:
                                print(f"  References: {len(refs)} triangle(s)")

                                # Check structure of first ref
                                first_ref = refs[0]
                                if 'index' in first_ref.attrib:
                                    index_val = first_ref.get('index')
                                    print(f"  ✓ <t:ref index=\"{index_val}\"/> (Correct structure)")
                                else:
                                    print(f"  ✗ FAIL: <ref> missing 'index' attribute")
                                    if first_ref.text:
                                        print(f"       Found text content instead: \"{first_ref.text.strip()}\"")
                                        print(f"       (Should use index attribute, not text)")
                                    all_checks_passed = False
                            else:
                                print(f"  Warning: No triangle references found")

                if trianglesets_found == 0:
                    print("✗ FAIL: No triangle sets found with correct namespace")
                    if ts_in_core_ns > 0:
                        print("  (Triangle sets were found in CORE namespace - this is wrong)")
                    all_checks_passed = False

                print("\n" + "=" * 70)
                if all_checks_passed:
                    print("✓ ALL CHECKS PASSED - File is 3MF v1.4.0 compliant!")
                else:
                    print("✗ COMPLIANCE ISSUES FOUND - See failures above")
                print("=" * 70 + "\n")

                # Print raw XML snippet if there are issues
                if not all_checks_passed:
                    print("\nRAW XML EXCERPT (first 1000 chars):")
                    print("-" * 70)
                    print(content[:1000])
                    print("...")

                return all_checks_passed

    except Exception as e:
        print(f"✗ Error reading 3MF file: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_export.py <path_to_3mf_file>")
        print("\nExample:")
        print("  python verify_export.py multimaterial_test_v2.2.1.3mf")
        sys.exit(1)

    filepath = sys.argv[1]
    success = verify_3mf_compliance(filepath)

    sys.exit(0 if success else 1)
