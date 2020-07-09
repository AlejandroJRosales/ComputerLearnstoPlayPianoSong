from midiutil.MidiFile import MIDIFile
import pygame
import brains


def create_midi(music, speed=150, program=1, duration=1):
	# Configure a MIDI file with one track:
	midi = MIDIFile(1)
	midi.addTempo(0, 0, speed)

	midi.addProgramChange(0, 0, 0, program)

	play = []
	for t in range(len(music)):
		pitch = music[t]
		play.append(pitch)
		# track, channel, pitch, time, duration, volume
		if t == len(music) - 1:
			midi.addNote(0, 0, pitch, t * duration, 3, 100)
		else:
			midi.addNote(0, 0, pitch, t * duration, duration, 100)

	# Write output file:
	with open('output.mid', 'wb') as f:
		midi.writeFile(f)


def play_music():
	try:
		music_file = 'output.mid'
		freq = 44100  # audio CD quality
		bitsize = -16  # unsigned 16 bit
		channels = 2  # 1 is mono, 2 is stereo
		buffer = 1024  # number of samples
		pygame.mixer.init(freq, bitsize, channels, buffer)

		# optional volume 0 to 1.0
		pygame.mixer.music.set_volume(1)

		clock = pygame.time.Clock()
		try:
			pygame.mixer.music.load(music_file)
		except pygame.error:
			print("File not found")
			return
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy():
			# check if playback has finished
			clock.tick(30)

	except KeyboardInterrupt:
		# if user hits Ctrl/C then exit
		# (works only in console mode)
		pygame.mixer.music.fadeout(1000)
		pygame.mixer.music.stop()
		raise SystemExit


# Different songs starting from easy to difficult to learn

# music = [56, 57, 58]

# music = [57, 57, 57, 53, 60, 57, 53, 60, 57]
# music = [64, 63, 64, 63, 64, 59, 62, 60, 57]
# music = [56, 61, 64, 56, 61, 64, 56, 61, 64]

# music = [60, 64, 67, 72, 76, 67, 72, 76, 60, 62, 69, 74, 77, 69, 74, 77]
# music = [60, 55, 57, 59, 60, 62, 55, 55, 64, 60, 62, 64, 65, 67, 55, 55]
# music = [60, 62, 64, 65, 67, 69, 71, 72, 72, 71, 69, 67, 65, 64, 62, 60]

# music = [60,60,60,60,59,57,59,60,62,64,64,64,64,62,60,62,64,65,67,60,69,69,67,65,64,62,60,59,57,55,56,57,59,60]
### music = [60, 64, 67, 72, 76, 67, 72, 76, 60, 64, 67, 72, 76, 67, 72, 76, 60, 62, 69, 74, 77, 69, 74, 77, 60, 62, 69, 74, 77, 69, 74, 77]

music = [76, 75, 76, 75, 76, 71, 74, 72, 69, 45, 52, 57, 60, 64, 69, 71, 40, 52, 56, 64, 68, 71, 72, 45, 52, 57, 64, 76, 75, 76, 75, 76, 71, 74, 72, 69, 45, 52, 57, 60, 64, 69, 71, 40, 52, 56, 62, 72, 71, 69, 45, 52, 57, 64, 71, 72, 74, 76]
# music = [60, 64, 67, 72, 76, 67, 72, 76, 60, 64, 67, 72, 76, 67, 72, 76, 60, 62, 69, 74, 77, 69, 74, 77, 60, 62, 69, 74, 77, 69, 74, 77, 59, 62, 67, 74, 77, 67, 74, 77, 59, 62, 67, 74, 77, 67, 74, 77, 60, 64, 67, 72, 76, 67, 72, 76, 60, 64, 67, 72, 76, 67, 72, 76]

create_midi(music)
play_music()

ai_output = brains.learn(music)

for song_number, piece in enumerate(ai_output):
	print(f'Try #{song_number}')
	if song_number == len(ai_output) - 1:
		create_midi(piece)
	else:
		create_midi(piece, speed=375)
	play_music()
