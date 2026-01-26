import pyttsx3

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
print("Available voices:")
for i, v in enumerate(voices):
    print(i, v.name, v.id)

engine.setProperty("voice", voices[0].id)  # force first voice
engine.setProperty("rate", 170)

engine.say("Hello, this is a test. Can you hear me?")
engine.runAndWait()
