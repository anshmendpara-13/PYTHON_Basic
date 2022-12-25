import time
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__== '__main__':
    # speak("my name is ansh")
    # time.sleep(.005)
    # speak("my collage name is pandit deendayal energy univesity")
    speak("i am B tech student")
