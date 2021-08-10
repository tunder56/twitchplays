Set-Location C:\code\twitchplayer
conda activate twitch27
Set-Location $home

try {
    & /../miniconda3/envs/twitch27/python.exe C:/twitchplays/slectgame.py
    C:\ProgramData\Miniconda3\envs\twitchplays27\python.exe  c:/twitchplays/slectgame.py
}
catch {
    Write-Host "Error occured check your file paths and change me" -BackgroundColor Darkred
}

