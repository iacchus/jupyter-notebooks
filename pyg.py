import pyglet

music = pyglet.media.load(r'./recording.wav')
music.play()

pyglet.app.run()
