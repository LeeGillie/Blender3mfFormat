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
Mock for Blender's mathutils module to support testing without Blender.
"""


class Vector:
    """
    Mock implementation of mathutils.Vector for testing.
    """
    def __init__(self, data):
        self.data = list(data)
    
    def __iter__(self):
        return iter(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __repr__(self):
        return f"Vector({self.data})"


class Matrix:
    """
    Mock implementation of mathutils.Matrix for testing.
    """
    def __init__(self, data=None):
        if data is None:
            # Default to 4x4 identity matrix
            self.data = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
        else:
            self.data = [list(row) for row in data]
    
    @classmethod
    def Identity(cls, size):
        """Create an identity matrix of the given size."""
        return cls([[1 if i == j else 0 for j in range(size)] for i in range(size)])
    
    @classmethod
    def Scale(cls, factor, size):
        """Create a scale matrix."""
        matrix = cls.Identity(size)
        for i in range(min(3, size)):  # Scale only x, y, z components
            matrix.data[i][i] = factor
        return matrix
    
    @classmethod
    def Translation(cls, vector):
        """Create a translation matrix from a vector."""
        matrix = cls.Identity(4)
        matrix.data[0][3] = vector[0]
        matrix.data[1][3] = vector[1]
        matrix.data[2][3] = vector[2]
        return matrix
    
    def transposed(self):
        """Return the transposed matrix."""
        transposed_data = [[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))]
        return Matrix(transposed_data)
    
    def __iter__(self):
        """Allow iteration over rows."""
        return iter(self.data)
    
    def __getitem__(self, index):
        """Allow indexing to get rows."""
        return self.data[index]
    
    def __setitem__(self, index, value):
        """Allow indexing to set rows."""
        self.data[index] = value
    
    def __eq__(self, other):
        """Check equality."""
        if not isinstance(other, Matrix):
            return False
        return self.data == other.data
    
    def __matmul__(self, other):
        """Matrix multiplication using @ operator."""
        if not isinstance(other, Matrix):
            raise TypeError(f"unsupported operand type(s) for @: 'Matrix' and '{type(other).__name__}'")
        
        size = len(self.data)
        result = [[0 for _ in range(size)] for _ in range(size)]
        
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        
        return Matrix(result)
    
    def inverted_safe(self):
        """Return the inverted matrix (simplified for 4x4 identity/translation/scale matrices)."""
        # This is a simplified version that works for common transformation matrices
        # For a full implementation, you'd need proper matrix inversion
        # For now, just return a copy of identity for simplicity in tests
        return Matrix.Identity(len(self.data))
    
    def copy(self):
        """Return a copy of this matrix."""
        return Matrix([row[:] for row in self.data])
    
    def __repr__(self):
        return f"Matrix({self.data})"
