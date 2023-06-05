import pyautogui
import time
import pygetwindow as pw
from python_get_resolve import GetResolve
import platform
import subprocess
import resolve_macro_functions as rm

appleactivatewin = """
tell application "DaVinci Resolve"
    activate
end tell
"""

if platform.system() == 'Windows':
    resolve_window = pw.getWindowsWithTitle('DaVinci Resolve Studio')[0]
    if resolve_window != None:
        resolve_window.activate()
elif platform.system() == 'Darwin':
   subprocess.run(['osascript', '-e', appleactivatewin])

time.sleep(2)

resolve = GetResolve()
pm = resolve.GetProjectManager()
project = pm.GetCurrentProject()
timeline = project.GetCurrentTimeline()

print(timeline.GetCurrentTimecode())
#print(timeline.SetCurrentTimecode('01:00:30:10'))
print(timeline.SetCurrentTimecode('00:00:30:00'))

pyautogui.press('space')

rm.waitForTimecode('00:00:40:00', timeline)

pyautogui.press('space') 