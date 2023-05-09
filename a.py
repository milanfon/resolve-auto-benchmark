#!/usr/bin/env python
from python_get_resolve import GetResolve
import math

def timecode_to_frames(timecode, frame_rate):
    hours, minutes, seconds, frames = map(int, timecode.split(':'))
    return ((hours * 60 * 60) + (minutes * 60) + seconds) * frame_rate + frames

resolve = GetResolve()
fusion = resolve.Fusion()
pm = resolve.GetProjectManager()
project = pm.GetCurrentProject()

timeline = project.GetCurrentTimeline()

# Get the current playhead position
current_timecode = timeline.GetCurrentTimecode()
print(current_timecode)
frame_rate = project.GetSetting("timelineFrameRate")
current_frame = timecode_to_frames(current_timecode, round(frame_rate))

# Prompt the user for the title and note
marker_title = input("Enter marker title: ")
marker_note = input("Enter marker note: ")

# Create a new marker with the specified color
marker_color = "Red"
new_marker = timeline.AddMarker(current_frame, marker_color, marker_title, marker_note, 1)