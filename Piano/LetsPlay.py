#! python2

from midiutil.MidiFile import MIDIFile
import sound
import brainz
import time

original_speed = 100
# Configure a MIDI file with one track:
midi = MIDIFile(1)
midi.addTempo(0, 0, original_speed)

# Select a instrument:
program = 1
midi.addProgramChange(0, 0, 0, program)

# Generate some random notes:
duration = 1
# music = [57, 57, 57, 53, 60, 57, 53, 60, 57]
# music = [64, 63, 64, 63, 64, 59, 62, 60, 57]
# music = [56, 61, 64, 56, 61, 64, 56, 61, 64]

# music = [60, 64, 67, 72, 76, 67, 72, 76, 60, 62, 69, 74, 77, 69, 74, 77]
# music = [60, 55, 57, 59, 60, 62, 55, 55, 64, 60, 62, 64, 65, 67, 55, 55]
# music = [60, 62, 64, 65, 67, 69, 71, 72, 72, 71, 69, 67, 65, 64, 62, 60]

# music = [60,60,60,60,59,57,59,60,62,64,64,64,64,62,60,62,64,65,67,60,69,69,67,65,64,62,60,59,57,55,56,57,59,60]
# music = [60, 64, 67, 72, 76, 67, 72, 76, 60, 64, 67, 72, 76, 67, 72, 76, 60, 62, 69, 74, 77, 69, 74, 77, 60, 62, 69, 74, 77, 69, 74, 77]

### music = [76, 75, 76, 75, 76, 71, 74, 72, 69, 45, 52, 57, 60, 64, 69, 71, 40, 52, 56, 64, 68, 71, 72, 45, 52, 57, 64, 76, 75, 76, 75, 76, 71, 74, 72, 69, 45, 52, 57, 60, 64, 69, 71, 40, 52, 56, 62, 72, 71, 69, 45, 52, 57, 64, 71, 72, 74, 76]
#
music = [60, 64, 67, 72, 76, 67, 72, 76, 60, 64, 67, 72, 76, 67, 72, 76, 60, 62, 69, 74, 77, 69, 74, 77, 60, 62, 69, 74, 77, 69, 74, 77, 59, 62, 67, 74, 77, 67, 74, 77, 59, 62, 67, 74, 77, 67, 74, 77, 60, 64, 67, 72, 76, 67, 72, 76, 60, 64, 67, 72, 76, 67, 72, 76]

transpose = []
transposition = 0
for note in range(len(music)):
	key = music[note]
	key += transposition
	transpose.append(key)
music = transpose

play = []
for t in range(len(music)):
	pitch = music[t]
	play.append(pitch)
	# track, channel, pitch, time, duration, volume
	midi.addNote(0, 0, pitch, t * duration, duration, 100)
	
# Write output file:
with open('output.mid', 'w') as f:
	midi.writeFile(f)
	
# Play the result:
player = sound.MIDIPlayer('output.mid')
pla = int(1)
dur = 2
nos = [1, 2, 3]
with open('output.mid', 'w') as f:
	midi.writeFile(f)
place = sound.MIDIPlayer('output.mid')
place.play()
player.play()

# Time and Learning
wait_time = int(len(music)/(original_speed/60)) + .5
start = time.time()

performance = 1
while performance != 0:
	concert, performance = brainz.learn(play)
	
stop = time.time()
compute_time = stop - start
if compute_time > wait_time:
	compute_time = wait_time
	
time.sleep(wait_time - compute_time)

for piece in range(len(concert)):

	midi = MIDIFile(1)
	speed = 500
	if piece == len(concert) - 1:
		speed = 120
	midi.addTempo(0, 0, speed)
	
	# Select a instrument:
	program = 1
	midi.addProgramChange(0, 0, 0, program)
	
	# Generate some random notes:
	duration = 1
	for t in range(len(music)):
		piez = concert[piece]
		pitch = piez[t]
		# track, channel, pitch, time, duration, volume
		midi.addNote(0, 0, pitch, t * duration, duration, 100)
	# Write output file:
	with open('output.mid', 'w') as f:
		midi.writeFile(f)
	# Play the result:
	player = sound.MIDIPlayer('output.mid')
	pla = int(1)
	dur = 2
	nos = [1, 2, 3]
	with open('output.mid', 'w') as f:
		midi.writeFile(f)
	place = sound.MIDIPlayer('output.mid')
	place.play()
	player.play()
	time.sleep(int(len(music)/(speed/60)) + .5)

