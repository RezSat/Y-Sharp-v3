import speech_recognition as sr

def get_audio():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said: "+ command + '\n')

    except sr.UnknownValueError:
        print("Error : i don't understand")
        command = get_audio()

    return command

while True:
    get_audio()
