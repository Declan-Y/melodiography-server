from midiutil import MIDIFile
import random


def generate_random_melody():
    degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
    track    = 0
    channel  = 0
    time     = 0  # In beats
    durations = [0.5, 1, 2]   # In beats
    tempo    = 150   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
    MyMIDI.addTempo(track, time, tempo)

    for i in range(10):
        duration = random.choice(durations)

        MyMIDI.addNote(track, channel,random.choice(degrees), time, duration, volume)
        time += duration


    with open("major-scale.mid", "wb") as output_file:
        return MyMIDI.writeFile(output_file)