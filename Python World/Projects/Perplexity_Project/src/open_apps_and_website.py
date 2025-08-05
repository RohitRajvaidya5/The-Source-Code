import subprocess


def open_app(path):
    subprocess.Popen(path)


app_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\chrome_proxy.exe"

open_app(app_path)


# Run PowerShell command to get installed programs
command = 'powershell "Get-StartApps | Select-Object Name"'
result = subprocess.run(command, capture_output=True, text=True, shell=True)

print(result.stdout)

