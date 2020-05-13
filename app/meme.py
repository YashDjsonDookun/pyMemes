import json
import random
import PIL.Image, PIL.ImageFont, PIL.ImageDraw, PIL.ImageFilter
import textwrap

with open("memes.json", encoding="utf8") as question_json:
    questions_list = json.load(question_json)
    random_question = (str(questions_list["memes"][random.randint(0,26)]).split(r": '")[1]).split("'}")[0]

meme = PIL.Image.open(f"blank_images/{random.randint(1,10)}.png")
meme = meme.filter(PIL.ImageFilter.GaussianBlur(3))
draw = PIL.ImageDraw.Draw(meme)
font = PIL.ImageFont.truetype(r"font/OperatorMono-Medium.otf",30)

meme_string = ""
lines = textwrap.wrap(random_question, 25)
for line in lines:
    meme_string += (f"{line}\n")

print(meme_string.strip())
draw.text((20,20), meme_string, font= font, fill="white", align="center")
meme.show()