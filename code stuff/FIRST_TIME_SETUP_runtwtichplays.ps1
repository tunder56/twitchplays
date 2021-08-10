conda create --name twitchplays27 python=2.7
Set-Location C:\twitchplays
conda activate twitchplays27
pip install pyautogui
pip install pynput
Set-Location $home
Set-ExecutionPolicy Unrestricted -Scope LocalMachine
try {
    & /../miniconda3/envs/twitch27/python.exe C:/twitchplays/slectgame.py
    C:\ProgramData\Miniconda3\envs\twitchplays27\python.exe  c:/twitchplays/slectgame.py
}
catch {
    Write-Host "Error occured check your file paths" -BackgroundColor Darkred
}
