# Contributing to Blender 3MF Format (Blender 5 Fork)

## Maintenance Status

⚠️ **This is a community-maintained fork with minimal active support.**

This fork was created to update Ghostkeeper's excellent Blender 3MF extension for Blender 5 compatibility and add 3MF v1.4.0 specification support. It is provided **as-is** for the community with no guarantee of ongoing maintenance.

## How You Can Contribute

### For Users

- **Report Issues:** While there's no guarantee of fixes, documenting problems helps others
- **Share Solutions:** If you fix something, please share via PR or discussion  
- **Help Others:** Answer questions in discussions or issues if you can
- **Test:** Try the extension and report compatibility issues

### For Developers

**Pull Requests Welcome (with caveats):**

While this fork has minimal active maintenance, quality contributions are appreciated:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/your-feature`
3. **Make your changes** with clear commit messages
4. **Test thoroughly** in Blender 5.0+
5. **Submit a PR** with a clear description

⚠️ **Important Notes:**
- PRs may not be reviewed immediately
- There's no guarantee of merge
- No obligation for the maintainer to respond
- Community members may review instead

### Want to Take Over Maintenance?

**Please do!** If you'd like to actively maintain this extension:

1. **Fork this repository**
2. **Continue development** on your fork
3. **Let the community know** via a GitHub discussion
4. **We can link** to your fork as the "actively maintained" version

This is encouraged! Open source thrives when passionate developers take ownership.

## Development Setup

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed setup instructions.

Quick start:
```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/Blender3mfFormat
cd Blender3mfFormat

# Build the extension
python build.py
# or
.\build.ps1

# Install in Blender 5.0+
# Edit → Preferences → Extensions → Install from Disk
```

## Code Standards

- **Python Style:** Follow PEP 8
- **Testing:** Test import/export with various 3MF files
- **Documentation:** Update docs for any API changes
- **Compatibility:** Maintain backward compatibility when possible
- **3MF Compliance:** Follow 3MF specification v1.4.0

## What to Contribute

### High Value Contributions

- Bug fixes for import/export issues
- Support for new 3MF extensions (Materials, Production, etc.)
- Performance improvements
- Better error handling
- Documentation improvements
- Test file additions

### Medium Value

- Code cleanup and refactoring
- UI/UX improvements  
- Additional unit tests
- Example files and tutorials

### Please Avoid

- Breaking changes without discussion
- Features outside 3MF scope
- Changes that break Blender 5 compatibility

## Testing Your Changes

1. **Manual Testing:**
   - Import various 3MF files
   - Export meshes with different features
   - Test triangle sets, materials, components
   - Verify round-trip (export → import)

2. **Test Files:**
   - Use files in `test/v1.3.0 triangle test/`
   - Try conformance suite in `test/Conformance tests/`
   - Test with real-world 3MF files

3. **Blender Versions:**
   - Test primarily on Blender 5.0+
   - Note any compatibility issues

## Documentation

When making changes, update:
- Code comments for complex logic
- README.md for user-facing features
- CHANGELOG.md for version history
- This file for process changes

## License

All contributions are licensed under **GPL-2.0-or-later**, the same as the original project.

By contributing, you agree to license your code under these terms.

## Original Project

This is a fork of [Ghostkeeper's Blender 3MF Format](https://github.com/Ghostkeeper/Blender3mfFormat).

**For Blender 2.8-4.2 support:** Please see the original repository and contribute there.

**For Blender 5+ support:** You're in the right place!

## Contact & Support

- **This Fork:** GitHub issues/discussions (community support only)
- **Original Project:** [Ghostkeeper's repository](https://github.com/Ghostkeeper/Blender3mfFormat)
- **3MF Specification:** [3MF Consortium](https://3mf.io/)

## Code of Conduct

Be respectful, constructive, and helpful. This is a volunteer project maintained by the community.

---

**Thank you for your interest!** Even small contributions help make this extension better for everyone. 🚀
