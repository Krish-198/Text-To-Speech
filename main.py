
from gtts import gtts
import Time
from playsound import playsound
text_val = input("Enter your Text: ")
time.sleep(0.1)
language = 'en'
obj = gTTS(text=text_val, lang=language, slow=False)
obj.save("exam.mp3")
playsound("exam.mp3")
time.sleep(60)