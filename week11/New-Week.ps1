# New-Week.ps1 - Precision Starter
param(
    [Parameter(Mandatory=$true)]
    [string]$WeekName
)

$base = "C:\Users\user\Desktop\AI masterclass"
$path = Join-Path $base $WeekName

if (Test-Path $path) { 
  Write-Host "Folder exists: $path" -ForegroundColor Yellow; exit 
}

New-Item -ItemType Directory -Path $path | Out-Null
Set-Location $path

@"
.env
__pycache__/
.venv/
venv/
*.pyc
*.pyo
.DS_Store
node_modules/
.env.local
"@ | Out-File -Encoding utf8 .gitignore

"# $WeekName`n`nDay tasks for $WeekName" | Out-File -Encoding utf8 README.md

git init
git add .gitignore README.md
git commit -m "chore: precise init $WeekName with gitignore"
git branch -M main

Write-Host "DONE - $path is clean and precise" -ForegroundColor Green
Write-Host "Next: git remote add origin https://github.com/OwaaOlang/$WeekName.git" -ForegroundColor Cyan
git status
