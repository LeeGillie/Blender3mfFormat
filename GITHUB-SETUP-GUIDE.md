# GitHub Repository Setup Guide

## Step-by-Step: Creating Your First GitHub Repository

### 1. Create the Repository on GitHub

1. Go to https://github.com
2. Click the **+** icon in top-right → **New repository**
3. Fill in:
   - **Repository name:** `Blender3mfFormat` (or `blender-3mf-blender5`)
   - **Description:** `Blender 5 fork of 3MF import/export extension with v1.4.0 spec support`
   - **Public** (so others can use it)
   - **DON'T** initialize with README (we already have one)
   - **DON'T** add .gitignore (we already have one)
   - **DON'T** choose a license (we already have GPL-2.0)
4. Click **Create repository**

### 2. Initialize Git Locally (from this folder)

Open PowerShell in `D:\Blender\3MF-import-export\` and run:

```powershell
# Initialize git repository
git init

# Add all files (respects .gitignore)
git add .

# Make first commit
git commit -m "Initial commit: Blender 5 fork with 3MF v1.4.0 support

- Blender 5.0+ compatibility with new extension system
- 3MF v1.4.0 specification support
- Triangle sets (v1.3.0 feature) import/export
- Updated build scripts and documentation
- Community-maintained fork of Ghostkeeper's original extension"

# Connect to your GitHub repo (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/Blender3mfFormat.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Create a Release (with the .zip file)

1. Go to your repository on GitHub
2. Click **Releases** (right sidebar)
3. Click **Create a new release**
4. Fill in:
   - **Tag:** `v2.2.0`
   - **Release title:** `v2.2.0 - Blender 5 + 3MF v1.4.0 Support`
   - **Description:**
     ```markdown
     ## Blender 5 Compatible Fork
     
     This release brings full Blender 5 compatibility and 3MF v1.4.0 specification support.
     
     ### Features
     - ✅ Blender 5.0+ compatibility with new extension system
     - ✅ 3MF v1.4.0 specification support
     - ✅ Triangle sets (v1.3.0) - Import/export face groups
     - ✅ Enhanced component/assembly handling
     - ✅ Full backward compatibility with v1.2.3 files
     
     ### Installation
     1. Download `io_mesh_3mf-2.2.0.zip` below
     2. In Blender: Edit → Preferences → Extensions
     3. Click "Install from Disk"
     4. Select the downloaded .zip file
     
     ### Note
     This is a community-maintained fork with minimal support. See README for details.
     
     Original project by Ghostkeeper: https://github.com/Ghostkeeper/Blender3mfFormat
     ```
   - **Attach file:** Upload `io_mesh_3mf-2.2.0.zip`
5. Click **Publish release**

### 4. Update README with Your GitHub URL

After creating the repo, update these files locally to reference your GitHub URL:
- `README.md` - Add link to your repository
- `GHOSTKEEPER-CONTACT.md` - Fill in your repository URL

Then push the updates:
```powershell
git add .
git commit -m "Add repository URL to documentation"
git push
```

### 5. Optional: Link to Original Repository

On your GitHub repository page:
1. Click **About** (top right, settings gear icon)
2. Add website: `https://github.com/Ghostkeeper/Blender3mfFormat`
3. Add topics: `blender`, `3mf`, `3d-printing`, `blender-extension`, `import-export`

## What Files Will Be Published?

Based on `.gitignore`, these will be **included**:
- ✅ All source code (`io_mesh_3mf/`, `__init__.py`)
- ✅ Build scripts (`build.py`, `build.ps1`)
- ✅ Documentation (README, CHANGELOG, etc.)
- ✅ Triangle test files
- ✅ License and credits
- ✅ Configuration files

These will be **excluded**:
- ❌ Built .zip files (go in Releases only)
- ❌ `GHOSTKEEPER-CONTACT.md` (private)
- ❌ `REPOSITORY-STRATEGY.md` (private)
- ❌ `test/Conformance tests/` (not yours to redistribute)
- ❌ Python cache, Blender files, etc.

## Submitting to Blender Extensions (Later)

Once your GitHub repo is live:

1. Go to https://extensions.blender.org
2. Sign in with Blender ID
3. Click **Submit Extension**
4. Fill in form:
   - Upload `io_mesh_3mf-2.2.0.zip`
   - Link to GitHub repository
   - Add same description from release
   - Include maintenance status disclaimer
5. Submit for review

## Contacting Ghostkeeper

**You can do this anytime**, no rush:
1. Edit `GHOSTKEEPER-CONTACT.md` with your GitHub URL
2. Find their contact info or create an issue on their repo
3. Send the message - friendly heads-up, no pressure

## Need Help?

If you get stuck:
1. GitHub has excellent documentation: https://docs.github.com
2. The community is helpful - ask in discussions
3. Or just push and see what happens - you can't break anything! 😊

---

**Remember:** You're allowed to do this! The GPL license explicitly permits and encourages forks. You've done great work updating this for Blender 5, and sharing it helps the community.
