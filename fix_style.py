"""Fix pycodestyle issues in test files."""
import os
import re

def fix_file(filepath):
    """Fix pycodestyle issues in a single file."""
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.split('\n')
    
    # Fix all issues line by line
    fixed_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # W291/W293: Remove trailing whitespace
        line = line.rstrip()
        
        # E226: Fix missing whitespace around * operator
        line = re.sub(r"'='\*", "'=' *", line)
        line = re.sub(r"'-'\*", "'-' *", line)
        line = re.sub(r'\*(\d+)(?!\d)', r' * \1', line)  # Fix *60, *70, etc.
        
        fixed_lines.append(line)
        i += 1
    
    content = '\n'.join(fixed_lines)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Fix all test files
files = [
    'test_trianglesets.py',
    'test/test_trianglesets.py',
    'test/generate_test_3mf.py',
    'test/verify_export.py',
    'test/create_multimaterial_test.py',
    'test/test_export_compliance.py'
]

fixed_count = 0
for f in files:
    if fix_file(f):
        print(f'Fixed: {f}')
        fixed_count += 1

print(f'\nFixed {fixed_count} files')
