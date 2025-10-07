from PIL import Image, ImageDraw
img = Image.new
image = ImageDraw

white_color = (255, 255, 255)
black_color = (0, 0, 0)
l_side = 640
w_side = 80
n = 8


class Images:
    def __init__(self, size = (l_side, l_side), color = white_color):
        self.size = size
        self.color = color
        self.image = Image.new("RGB", self.size, self.color)
        self.draw = ImageDraw.Draw(self.image)

    def call(self):
        for i in range(n):
            for j in range(n):
                if (i + j) % 2 == 0:
                    fill_color = white_color
                else:
                    fill_color = black_color
                left = (i * w_side, j * w_side)
                right = ((i + 1) * w_side, (j + 1) * w_side)
                self.draw.rectangle([left, right], fill=fill_color)

    def save(self, filename):
        self.image.save(filename)
        print(f"Рисунок сохранен с именем файла: {filename}")

chess = Images()
chess.call()
chess.save("шахматная_доска.png")