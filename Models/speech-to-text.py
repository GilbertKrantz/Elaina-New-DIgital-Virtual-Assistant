import speech_recognition as sr

def speech_to_text(microphone, recognizer):

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

    print("Listening...")
    with microphone as source:
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Recognized Text: ", text)

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return text

if __name__ == "__main__":

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while(True):
        speech_to_text(microphone, recognizer)