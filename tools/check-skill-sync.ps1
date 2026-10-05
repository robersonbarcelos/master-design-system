# Verifica divergência entre skills do repositório (fonte canônica) e a pasta pessoal (~/.claude/skills).
# Rodar sempre que suspeitar de desatualização, ou periodicamente no início de sessão.
#
# Uso: pwsh -File check-skill-sync.ps1
#
# Skills convertidas em junção (carousel-writer-sms, production-orchestrator-sms, copy-qa-sms,
# narrative-framework-sms, hook-writer-sms, caption-writer-sms, social-media-context-sms)
# nunca aparecem como divergentes aqui — são o mesmo arquivo fisicamente, verificado à parte.

$repoRoot = "C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\skills"
$globalRoot = "C:\Users\Pichau\.claude\skills"

$repoSkills = Get-ChildItem -Path $repoRoot -Recurse -Filter "SKILL.md" -File

$identical = 0
$different = 0
$missing = 0
$junctions = 0

foreach ($repoFile in $repoSkills) {
    $skillName = $repoFile.Directory.Name
    $globalDir = Join-Path $globalRoot $skillName
    $globalFile = Join-Path $globalDir "SKILL.md"

    if (-not (Test-Path $globalDir)) {
        Write-Host "[AUSENTE NA PASTA PESSOAL] $skillName" -ForegroundColor DarkGray
        $missing++
        continue
    }

    $dirItem = Get-Item $globalDir -Force
    if ($dirItem.LinkType -eq "Junction") {
        $junctions++
        continue
    }

    if (-not (Test-Path $globalFile)) {
        Write-Host "[PASTA EXISTE, SKILL.md AUSENTE] $skillName" -ForegroundColor Yellow
        continue
    }

    $repoContent = Get-Content $repoFile.FullName -Raw
    $globalContent = Get-Content $globalFile -Raw

    if ($repoContent -eq $globalContent) {
        $identical++
    } else {
        Write-Host "[DIVERGENTE] $skillName" -ForegroundColor Red
        Write-Host "  repo:   $($repoFile.FullName)"
        Write-Host "  pessoal: $globalFile"
        $different++
    }
}

Write-Host ""
Write-Host "===== RESUMO =====" -ForegroundColor Cyan
Write-Host "Junções (sempre sincronizadas): $junctions" -ForegroundColor Green
Write-Host "Idênticas (cópias soltas, ok por ora): $identical" -ForegroundColor Green
Write-Host "Divergentes (precisa sincronizar): $different" -ForegroundColor $(if ($different -gt 0) { "Red" } else { "Green" })
Write-Host "Ausentes na pasta pessoal: $missing" -ForegroundColor DarkGray

if ($different -gt 0) {
    Write-Host ""
    Write-Host "Para corrigir uma divergência pontual:" -ForegroundColor Yellow
    Write-Host '  cp "<repo>\SKILL.md" "<pessoal>\SKILL.md"'
    Write-Host ""
    Write-Host "Para eliminar o risco de vez numa skill (recomendado):" -ForegroundColor Yellow
    Write-Host '  Remove-Item -Path "<pessoal>" -Recurse -Force'
    Write-Host '  New-Item -ItemType Junction -Path "<pessoal>" -Target "<repo>"'
}
