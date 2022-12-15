$Command = Read-Host "Command"
$TempFile = New-TemporaryFile
Write-Host "Input the expressions into VS Code, save and exit."
code -w -n $TempFile
$Content = Get-Content $TempFile 
$Content | powershell ./math $Command | Out-File $TempFile
code -w -n $TempFile