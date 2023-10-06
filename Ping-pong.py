from pygame import *

clock = time.Clock()



width = 600
height = 500


# создание окна
window = display.set_mode((width, height))
back = (255, 0, 255)
window.fill(back)

speed_x = 3
speed_y = 3

game = True
finish = False  

FPS = 60






class GameSprite(sprite.Sprite):
    """
    image_file - имя файла с картинкой для спрайта
    x - координата x спрайта
    y - координата y спрайта
    speed - скорость спрайта
    size_x - размер спрайта по горизонтали
    size_y - размер спрайта по вертикали
    """

    # конструктор
    def __init__(self, image_file, x, y, speed, size_x, size_y):
        super().__init__()  # конструктор суперкласса
        self.image = transform.scale(
            image.load(image_file), (size_x, size_y)
        )  # создание внешнего вида спрайта - картинки
        self.speed = speed  # скорость
        self.rect = (
            self.image.get_rect()
        )  # прозрачная подложка спрайта - физическая модель
        self.rect.x = x
        self.rect.y = y

    # метод для отрисовки спрайта
    def reset(self):
        # отобразить картинку спрайта в тех же координатах, что и его физическая модель
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    # метод для управления игрока стрелками клавиатуры
    def update_r(self):
        # получаем словарь состояний клавиш
        keys = key.get_pressed()

        # если нажата клавиша влево и физическая модель не ушла за левую границу игры
        if keys[K_UP] and self.rect.y > 5:
            # двигаем влево
            self.rect.y -= self.speed

        # если нажата клавиша вправо и физическая модель не ушла за правую границу игры
        if keys[K_DOWN] and self.rect.y < width - 70:
            # двигаем вправо
            self.rect.y += self.speed

    # метод для стрельбы пулями
    def update_l(self):
        # получаем словарь состояний клавиш
        keys = key.get_pressed()

        # если нажата клавиша влево и физическая модель не ушла за левую границу игры
        if keys[K_w] and self.rect.y > 5:
            # двигаем влево
            self.rect.y -= self.speed

        # если нажата клавиша вправо и физическая модель не ушла за правую границу игры
        if keys[K_s] and self.rect.y < width - 70:
            # двигаем вправо
            self.rect.y += self.speed




racket1 = Player('Стенка.jpg', 30, 200, 4, 50, 150)
racket2 = Player('Стенка.jpg', 520, 200, 4, 50, 150)
ball = GameSprite('мячик-transformed.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > height - 50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)