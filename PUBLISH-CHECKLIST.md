# Pre-Publish Checklist

## Before Pushing to GitHub

### ✅ Files to Keep (will be published)
- [ ] Source code (`io_mesh_3mf/`)
- [ ] Build scripts (`build.py`, `build.ps1`)  
- [ ] Documentation (`README.md`, `CHANGELOG.md`, etc.)
- [ ] License files (`LICENSE.md`, `CREDITS.md`)
- [ ] Your triangle test (`test/v1.3.0 triangle test/`)
- [ ] Config files (`blender_manifest.toml`)
- [ ] `.gitignore` (updated to exclude private files)

### ❌ Files Already Excluded (via .gitignore)
- [ ] `*.zip` files (will go in GitHub Releases instead)
- [ ] `GHOSTKEEPER-CONTACT.md` (private, keep local)
- [ ] `REPOSITORY-STRATEGY.md` (private, keep local)
- [ ] `test/Conformance tests/` (not yours to redistribute)
- [ ] Build artifacts and caches

### 🔍 Double Check
- [ ] No personal email/info in any files
- [ ] All attribution to Ghostkeeper is correct
- [ ] LICENSE.md is GPL-2.0-or-later
- [ ] Version numbers are 2.2.0 everywhere
- [ ] README has maintenance status disclaimer

## Build the Release

```powershell
# Build the extension
python build.py

# Verify it created: io_mesh_3mf-2.2.0.zip
```

- [ ] Test the .zip in Blender 5 one more time
- [ ] Save the .zip somewhere safe for GitHub Release

## Create GitHub Repository

See [GITHUB-SETUP-GUIDE.md](GITHUB-SETUP-GUIDE.md) for step-by-step instructions.

- [ ] Created repository on GitHub
- [ ] Initialized git locally
- [ ] Added and committed all files
- [ ] Pushed to GitHub
- [ ] Created v2.2.0 Release with .zip file
- [ ] Updated README with repository URL

## After Publishing

### Optional: Contact Ghostkeeper
- [ ] Edit `GHOSTKEEPER-CONTACT.md` with your GitHub URL
- [ ] Send friendly notification
- [ ] No rush - can do anytime

### Optional: Submit to Blender Extensions
- [ ] Account on extensions.blender.org
- [ ] Upload `io_mesh_3mf-2.2.0.zip`
- [ ] Include maintenance disclaimer
- [ ] Link to GitHub repository

## You're Done! 🎉

Your work is now available for:
- Blender 5 users who need 3MF support
- People wanting the latest 3MF v1.4.0 features
- The 3D printing community
- Anyone who wants to fork and improve it further
