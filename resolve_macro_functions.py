import resolve_aux_functions as aux
import time

def waitForTimecode(timestamp, timeline, wait = 0.5):
    tsi = aux.timecodeToInt(timestamp)
    while aux.timecodeToInt(timeline.GetCurrentTimecode()) < tsi:
        print(aux.timecodeToInt(timeline.GetCurrentTimecode()))
        time.sleep(wait)