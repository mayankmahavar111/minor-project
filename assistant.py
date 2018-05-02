from SpeechRecognition import speech,textTospeech
from sel import search,open_url
from execute import fileopen
from reminder import reminder
from mailSystem import mailInforamtion
from image import imageCaputre


def assist():
    text = speech()
    print("You said : ", text)
    text=text.lower()
    text = text.split(" ")
    if text[0] == 'search':
        temp = ' '.join(text[1:])
        search(temp)
    elif text[0] == 'open' and "." in text[-1]:
        temp = ' '.join(text[1:])
        open_url(temp)
    elif text[0] == 'open':
        temp = ' '.join(text[1:])
        fileopen(temp)
    elif " ".join(text)  == 'set reminder':
        reminder()
    elif " ".join(text)=='send mail' :
        mailInforamtion()
    elif " ".join(text) == 'click photo':
        imageCaputre()
    else:
        text="Sorry Unable to recognize any command try including"+'\n\n'+"search than sentence you want to search "+'\n'+"open than filename"+'\n'+''
        textTospeech(text)



if __name__ == '__main__':
    assist()