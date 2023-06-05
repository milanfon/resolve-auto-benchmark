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

# Scripting start
def main_script(timeline):
    timeline.SetCurrentTimecode('01:00:30:00')
    pyautogui.press('space')
    rm.waitForTimecode('01:00:40:00', timeline)
    pyautogui.press('space') 

    time.sleep(1)

    timeline.SetCurrentTimecode('01:01:17:00')
    pyautogui.press('l')
    #rm.waitForTimecode('01:01:38:35', timeline)
    time.sleep(21)
    pyautogui.press('k')

    time.sleep(2)

    pyautogui.press('home')
    timeline.SetCurrentTimecode('01:00:58:00')
    pyautogui.moveTo(115, 1260)
    pyautogui.click()
    pyautogui.moveTo(352, 1423)
    pyautogui.dragTo(3066,1393, 1, button='left')
    time.sleep(1.5)
    pyautogui.moveTo(3076, 1364)
    pyautogui.dragTo(3675, 1368, 1, button='left')
    pyautogui.moveTo(3492, 445)
    pyautogui.click()
    pyautogui.hotkey(['ctrl','a'])
    pyautogui.press('backspace')
    pyautogui.write('Tohle je testovaci text', interval=0.1)
    pyautogui.moveTo(3664, 641)
    pyautogui.doubleClick()
    pyautogui.press(['backspace','backspace'])
    pyautogui.write('160', interval=0.05)
    pyautogui.press('enter')
    timeline.SetCurrentTimecode('01:01:00:00')
    pyautogui.press('l')
    time.sleep(5)
    pyautogui.press('k')
    pyautogui.moveTo(3246, 611)
    pyautogui.scroll(-1000)
    pyautogui.moveTo(3491, 612)
    pyautogui.drag(50, 0, 0.5, button='left')
    pyautogui.moveTo(3669, 612)
    pyautogui.drag(-50, 0, 0.5, button='left')
    time.sleep(1)
    pyautogui.press('l')
    time.sleep(8)
    pyautogui.press('k')
    time.sleep(1)
    pyautogui.moveTo(3252, 1357)
    pyautogui.click()
    pyautogui.press('backspace')

    time.sleep(2)

    pyautogui.moveTo(3252, 1357)
    pyautogui.click()
    pyautogui.press('home')
    pyautogui.drag(-2600, 0, 1, button='middle')
    pyautogui.click(x=1787, y=1169)
    pyautogui.press('l')
    time.sleep(15)
    pyautogui.press('k')

    time.sleep(1)

    pyautogui.press('end')
    pyautogui.moveTo(637, 315)
    pyautogui.doubleClick()
    time.sleep(0.5)
    pyautogui.press('home')
    pyautogui.press('l')
    time.sleep(5.5)
    pyautogui.press('i')
    time.sleep(10)
    pyautogui.press(['k','o'])
    time.sleep(0.5)
    pyautogui.press('f9')
    time.sleep(0.5)
    pyautogui.click(x=1549, y=531)
    pyautogui.hotkey(['alt','x'])
    time.sleep(1)
    pyautogui.click(x=2376, y=1275)
    pyautogui.press('up')
    time.sleep(1)
    pyautogui.click(x=2100, y=2065)
    time.sleep(0.5)
    pyautogui.moveTo(893, 1940)
    pyautogui.drag(800, 0, 1, button='left')
    pyautogui.moveTo(544, 1936)
    pyautogui.drag(-350, 0, 1, button='left')
    pyautogui.moveTo(201, 1937)
    pyautogui.drag(-450,0, 1, button='left')
    pyautogui.moveTo(856, 1488)
    pyautogui.drag(80, 0, 1, button='left')
    pyautogui.moveTo(904, 2003)
    pyautogui.drag(70, 0, 0.5, button='left')
    time.sleep(1)
    pyautogui.press('l')
    time.sleep(4)
    pyautogui.press('k')
    time.sleep(1)
    pyautogui.click(x=758, y=1071, button='middle')
    time.sleep(1)
    pyautogui.click(x=1745, y=2058)
    time.sleep(0.5)
    pyautogui.press('down')
    pyautogui.moveTo(637, 315)
    pyautogui.doubleClick()
    pyautogui.press(['i','l'])
    time.sleep(10)
    pyautogui.press(['k','o'])
    pyautogui.press('f9')
    time.sleep(1)
    pyautogui.click(x=2100, y=2065)
    time.sleep(0.5)
    pyautogui.click(x=3499, y=1067, button='middle')
    time.sleep(1)
    pyautogui.click(x=1745, y=2058)
    time.sleep(0.5)
    pyautogui.press(['up', 'up', 'l'])
    time.sleep(20)
    pyautogui.press('k')
    time.sleep(1)
    pyautogui.press(['home', 'end'])
    pyautogui.moveTo(2569, 1456)
    pyautogui.dragTo(1894, 1908, 1.5)
    pyautogui.press('backspace')
    time.sleep(0.5)
    pyautogui.press('home')

while(True):
    main_script(timeline)