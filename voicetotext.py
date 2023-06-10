import speech_recognition as s
from googletrans import Translator
from pprint import pprint

print("Select the Language in which you want the text :")
print("Codes:")
print("1: HINDI")
print("2: MARATHI")
print("3: GUJARATI")
print("4: TAMIL")
print("5: PUNJABI")
code=int(input("Enter your choice : "))

if code==1 :

    sr=s.Recognizer()
    translater= Translator()
    print("Say Something......")

    with s.Microphone() as m:
        audio=sr.listen(m)
        print("Did you just said:")
        query=sr.recognize_google(audio,language='en')
        print(query)
        out = translater.translate(query,dest="hi")
        print(f"{out.origin} ({out.src}) --> {out.text} ({out.dest})")

elif code==2 :
    sr=s.Recognizer()
    translater= Translator()
    print("Say Something......")

    with s.Microphone() as m:
        audio=sr.listen(m)
        print("Did you just said:")
        query=sr.recognize_google(audio,language='en')
        print(query)
        out = translater.translate(query,dest="mr")
        print(f"{out.origin} ({out.src}) --> {out.text} ({out.dest})")

elif code==3:
    sr=s.Recognizer()
    translater= Translator()
    print("Say Something......")

    with s.Microphone() as m:
        audio=sr.listen(m)
        print("Did you just said:")
        query=sr.recognize_google(audio,language='en')
        print(query)
        out = translater.translate(query,dest="gu")
        print(f"{out.origin} ({out.src}) --> {out.text} ({out.dest})")

elif code==4:
    sr=s.Recognizer()
    translater= Translator()
    print("Say Something......")

    with s.Microphone() as m:
        audio=sr.listen(m)
        print("Did you just said:")
        query=sr.recognize_google(audio,language='en')
        print(query)
        out = translater.translate(query,dest="ta")
        print(f"{out.origin} ({out.src}) --> {out.text} ({out.dest})")

elif code==5:
    sr=s.Recognizer()
    translater= Translator()
    print("Say Something......")

    with s.Microphone() as m:
        audio=sr.listen(m)
        print("Did you just said:")
        query=sr.recognize_google(audio,language='en')
        print(query)
        out = translater.translate(query,dest="pa")
        print(f"{out.origin} ({out.src}) --> {out.text} ({out.dest})")