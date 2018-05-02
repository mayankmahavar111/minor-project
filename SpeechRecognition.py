import speech_recognition as sr
#import time
import pyttsx3


def speech():
    r = sr.Recognizer()
    #print(r.dynamic_energy_threshold,'\n',r.energy_threshold)
    r.dynamic_energy_threshold=False
    r.energy_threshold=400
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        print("recognising done")
    try:
        print("converting audio to text ...")
        temp= r.recognize_google(audio)

    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Could not request results; {0}".format(e)
    return temp


def textTospeech(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':

    text=speech()
    print(text)
    """
    text = "Sorry Unable to recognize any command try including" + '\n\n' + "search than sentence you want to search " + '\n' + "open than filename" + '\n' + ''

    textTospeech(text)
    """



