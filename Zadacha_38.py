#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "Привет, меабв! ааааа вабв, ааа! Вабв, абв"
text = text.split()
text_new = []
for i in range(len(text)):
     if "абв" not in text[i]:
         text_new.append(text[i])
print(" ".join(text_new))


data = 'аф фыв ыва ываабв, ывадлойц. Оывало абвываф, длоываабв.'

data=' '.join(list(filter(lambda slovo: not 'абв' in slovo, data.split())))
print(data)