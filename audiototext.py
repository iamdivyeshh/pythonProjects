import speech_recognition as sr

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Not Understand.")

sptext()