import json
import random
import PIL.Image, PIL.ImageFont, PIL.ImageDraw, PIL.ImageFilter
import textwrap
from tkinter import *
import tkinter.ttk as ttk

def generate_meme():
    try:
        with open("memes.json", encoding="utf8") as question_json:
            questions_list = json.load(question_json)
            random_question = (str(questions_list["memes"][random.randint(0,114)]).split(r": '")[1]).split("'}")[0]
        image_chosen = random.randint(1,38)
        meme = PIL.Image.open(f"blank_images/{image_chosen}.png").filter(PIL.ImageFilter.MaxFilter(1)).filter(PIL.ImageFilter.GaussianBlur(2.2))
        draw = PIL.ImageDraw.Draw(meme)
        font = PIL.ImageFont.truetype(r"font/OperatorMono-Medium.otf",23)

        meme_string = ""
        lines = textwrap.wrap(random_question, 30)
        for line in lines:
            meme_string += (f"{line}\n")

        # colors = ["white","black"]
        placements = [(30,170), (50,50), (60,175), (70,20), (100,150)]
        # draw.text(placements[random.randint(0,4)], meme_string, font= font, fill=colors[random.randint(0,1)], align="center")
        draw.text(placements[random.randint(0,4)], meme_string, font= font, fill="white", align="center")
        meme.save(f"outputs/{image_chosen}.png")
        # meme.show()
    except Exception as e:
        generate_meme()

meme_app = Tk()
meme_app.geometry("235x100")
meme_app.title("Bad App")

btn = ttk.Button(meme_app,text="GeNeRaTe MeMe!",command=generate_meme)
btn.pack()
meme_app.mainloop()

