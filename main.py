from googletrans import Translator

text1 = "Bună, ce faci?"
text2 = "Hello, how are you?"
text3 = "Bongiorno, come tu stai?"

##print(googletrans.LANGUAGES)

translator = Translator()
out = translator.translate("How are you?", dest = 'ro')
print(out.text)
##if text1 is None or text2 is None or text3 is None:
  ##raise ValueError("none")
#3else:
print(translator.detect(text1))
print(translator.detect(text2))
print(translator.detect(text3)) 