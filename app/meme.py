import json
import random
import PIL.Image, PIL.ImageFont, PIL.ImageDraw, PIL.ImageFilter
import textwrap
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout

def generate_meme():
    try:
        with open("memes.json", encoding="utf8") as question_json:
            questions_list = json.load(question_json)
            random_question = (str(questions_list["memes"][random.randint(0,114)]).split(r": '")[1]).split("'}")[0]

        meme = PIL.Image.open(f"blank_images/{random.randint(1,38)}.png").filter(PIL.ImageFilter.MaxFilter(1)).filter(PIL.ImageFilter.GaussianBlur(2.2))
        draw = PIL.ImageDraw.Draw(meme)
        font = PIL.ImageFont.truetype(r"font/OperatorMono-Medium.otf",23)

        meme_string = ""
        lines = textwrap.wrap(random_question, 30)
        for line in lines:
            meme_string += (f"{line}\n")

        # colors = ["white","black"]
        placements = [(30,170), (50,50), (60,175), (70,20), (100,150)]
        print(meme_string.strip())
        # draw.text(placements[random.randint(0,4)], meme_string, font= font, fill=colors[random.randint(0,1)], align="center")
        draw.text(placements[random.randint(0,4)], meme_string, font= font, fill="white", align="center")
        meme.show()
    except Exception as e:
        generate_meme()

meme_app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Bad Meme Generator")
window.setFixedSize(235, 235)
layout = QVBoxLayout()

Button = QPushButton('GeNeRaTe MeMe')
Button.clicked.connect(generate_meme)
layout.addWidget(Button)
window.setLayout(layout)
window.show()
sys.exit(meme_app.exec_())