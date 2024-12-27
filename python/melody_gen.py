from midiutil.MidiFile import MIDIFile

import random

# Create MIDI object
MyMIDI = MIDIFile(1)  # One track
track = 0   
time = 0
MyMIDI.addTempo(track, time, 140)  # 140 BPM

# Set channel and volume
channel = 0
volume = 100

# Minor scale notes
base_notes = [60, 63, 65, 67, 68, 70, 72]  # C minor scale
duration = 0.5  # Half beats

# Create melodic pattern
time = 0
for i in range(32):  # 16 bars
    note = random.choice(base_notes)
    # Add main note
    MyMIDI.addNote(track, channel, note, time, duration, volume)

    # Add occasional chord notes
    if random.random() > 0.5:
        MyMIDI.addNote(track, channel, note + 4, time, duration, volume - 20)

    time += duration

# Save MIDI file
with open("trap_piano.midi", "wb") as output_file:
    MyMIDI.writeFile(output_file)

# Created/Modified files during execution:
print("trap_piano.midi")