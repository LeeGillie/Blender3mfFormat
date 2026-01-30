# PowerShell build script for 3MF Blender Extension

$ExtensionId = "io_mesh_3mf"
$Version = "2.2.0"
$OutputFile = "$ExtensionId-$Version.zip"

Write-Host "Building Blender Extension: $OutputFile" -ForegroundColor Green

# Check if Blender is available
$blenderPath = "blender"
if (Get-Command $blenderPath -ErrorAction SilentlyContinue) {
    Write-Host "Using Blender command-line tool..." -ForegroundColor Cyan
    
    # Run Blender build command
    & $blenderPath --command extension build --output-filepath $OutputFile
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nBuild successful!" -ForegroundColor Green
        if (Test-Path $OutputFile) {
            $fileSize = (Get-Item $OutputFile).Length / 1KB
            Write-Host "Output file: $OutputFile ($([math]::Round($fileSize, 2)) KB)" -ForegroundColor Green
        }
    } else {
        Write-Host "`nBuild failed with exit code: $LASTEXITCODE" -ForegroundColor Red
        exit $LASTEXITCODE
    }
} else {
    Write-Host "Blender not found in PATH. Falling back to Python build script..." -ForegroundColor Yellow
    
    # Run Python build script
    python build.py
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nBuild successful!" -ForegroundColor Green
    } else {
        Write-Host "`nBuild failed!" -ForegroundColor Red
        exit $LASTEXITCODE
    }
}
