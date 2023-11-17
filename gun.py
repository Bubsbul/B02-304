import math
import random
import pygame

kill1 = 0
kill2 = 0
hitt_2 = 0
hitt_3 = 0
change_first = 0
change_second = 0
FPS = 30
g = 3
hit = 0
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface,
                 y = 500):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x_start
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = random.choice(GAME_COLORS)

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy = self.vy - g
        if self.x - self.r >= 780:
            self.vx = -self.vx
        if self.y -self.r >= 500:
            if -4 < self.vy < 4:
                self.vy = 0
                self.y = self.r + 501
            else:
                self.vy = -self.vy / 1.7
            self.vx = self.vx / 1.2
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Ball_2:
    def __init__(self, screen: pygame.Surface, y = 500):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x_start
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = random.choice(GAME_COLORS)

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy = self.vy - 0.3 * g
        if self.x - self.r >= 780:
            self.vx = -self.vx
        if self.y -self.r >= 500:
            if -4 < self.vy < 4:
                self.vy = 0
                self.y = - self.r + 501
            else:
                self.vy = -self.vy / 1.5
            self.vx = self.vx / 1.05
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r, 5 )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = 30
        self.y = 500
        self.color = GREY
        self.r = 20
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        if hit % 2 == 0:
            new_ball = Ball(self.screen)
        else:
            new_ball = Ball_2(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10


    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((event.pos[1] - 500), (event.pos[0] - x_start))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY


    def draw(self):
        global x_start
        length = self.f2_power
        if self.an < 0:
            x = self.x + math.sin(self.an) + length * math.cos(self.an)
            y = self.y - math.cos(self.an) + length * math.sin(self.an)
        else:
            x = self.x - math.sin(self.an) - length * math.cos(self.an)
            y = self.y + math.cos(self.an) - length * math.sin(self.an)
        pygame.draw.line(surface = self.screen, color = self.color, start_pos = [self.x, self.y],
                         end_pos = [x, y], width = 10)
        pygame.draw.line(surface=self.screen, color=self.color, start_pos=[self.x - 20, 500],
                         end_pos=[self.x + 20, 500], width=10)
        pygame.draw.circle(surface = self.screen, color=self.color, center = [self.x - 20, 510], radius = 5, width = 10)
        pygame.draw.circle(surface = self.screen, color = self.color, center = [self.x + 20, 510], radius=5, width=10)
        x_start = self.x

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def move(self):
        button = pygame.key.get_pressed()
        if self.x <= 770:
            if button[pygame.K_RIGHT]:
                self.x += 3
        if self.x >= 30:
            if button[pygame.K_LEFT]:
                self.x -= 3


class Target:
    def __init__(self, c):
        self.x = random.randint(600, 700)
        self.y = random.randint(300, 500)
        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-4, 4)
        self.color = c
        self.r = random.randint(5, 50)
        self.live = 1
        self.points = 1
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.randint(600, 700)
        self.y = random.randint(300, 400)
        self.r = random.randint(2, 50)
        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-4, 4)
        self.live = 1


    def hit(self, points = 1):
        """Попадание шарика в цель."""
        self.points += points


    def draw(self):
        pygame.draw.circle(screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def move(self):
        k = 0
        self.vy += k
        self.x += self.vx
        self.y += self.vy
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.x = self.x
            self.vx = -self.vx
        if self.y + self.r >= 560 or self.y - self.r <= 0:
            self.y = self.y
            self.vy = -self.vy


class Target2:
    def __init__(self, c):
        self.x = random.randint(600, 700)
        self.y = random.randint(300, 500)
        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-4, 4)
        self.color = c
        self.r = random.randint(5, 50)
        self.live = 1
        self.points = 1
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.randint(600, 700)
        self.y = random.randint(300, 400)
        self.r = random.randint(2, 50)
        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-4, 4)
        self.live = 1


    def hit(self, points = 1):
        """Попадание шарика в цель."""
        self.points += points


    def draw(self):
        pygame.draw.circle(screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def move(self):
        k = 0.5
        self.vy += k
        self.x += self.vx
        self.y += self.vy
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.x = self.x
            self.vx = -self.vx
        if self.y + self.r >= 560 or self.y - self.r <= 0:
            self.y = self.y
            self.vy = -self.vy


class Plane:
    def __init__(self, screen):
        self.screen = screen
        self.x = 51
        self.y = 30
        self.color = BLACK
        self.r = 30

    def fire(self, event):
        global bombs
        if event:
            new_bomb = Bomb(self.screen, self.x, self.y)
            bombs.append(new_bomb)

    def move(self):
        global x_plane
        button = pygame.key.get_pressed()
        if self.x <= 765:
            if button[pygame.K_d]:
                self.x += 3
        if self.x >= 51:
            if button[pygame.K_a]:
                self.x -= 3
        x_plane = self.x

    def draw(self):
        pygame.draw.line(surface=self.screen, color = self.color, start_pos = [self.x - 30, self.y],
                         end_pos = [self.x + 30, self.y], width = 10)
        pygame.draw.line(surface = self.screen, color = self.color, start_pos = [self.x - 30, self.y],
                         end_pos = [self.x - 30, self.y - 10], width = 10)
        pygame.draw.line(surface=self.screen, color=self.color, start_pos=[self.x - 5, self.y - 10],
                         end_pos=[self.x - 50, self.y - 10], width=10)
        pygame.draw.circle(surface=self.screen, color=self.color, center=[self.x + 30, self.y], radius=5, width=10)


class Bomb:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = BLACK
        self.r = 5
        self.vy = 0
        self.live = 1
        self.points = 1

    def move(self):
        self.y += self.vy
        self.vy += 0.5
        if self.y >= 500:
            self.vy = 0
            self.y = 100000

    def hit(self, points = 1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def death(self):
        self.x = 10000
        self.y = 10000000
        self.r = random.randint(2, 50)
        self.live = 1

    def hittest(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
bombs = []


pygame.display.flip()

clock = pygame.time.Clock()
gun = Gun(screen)
plane = Plane(screen)
target_first = Target(RED)
target_second = Target(GREEN)
finished = False
gameover1 = False
gameover2 = False

while not finished:
     if not gameover1 and not gameover2:
        screen.fill(WHITE)
        gun.draw()
        gun.move()
        plane.draw()
        plane.move()
        if kill1 >= 10:
            gameover2 = True
        if kill2 >= 10:
            gameover1 = True
        target_first.move()
        target_second.move()
        target_first.draw()
        target_second.draw()
        for i in bombs:
            i.draw()
        for b in balls:
            b.draw()
        font = pygame.font.SysFont(None, 25, True, False)
        tt = 'Tank:' + str(10 - kill2)
        text = font.render(tt, True, (0, 0, 0), (255, 255, 255))
        screen.blit(text, (600, 10))

        pp = 'Plane:' + str(10 - kill1)
        font = pygame.font.SysFont(None, 25, True, False)
        text = font.render(pp, True, (0, 0, 0),(255 , 255, 255))
        screen.blit(text, (600, 30))

        pygame.display.flip()
        pygame.display.update()

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                gun.fire2_end(event)
                hit += 1
            elif event.type == pygame.MOUSEMOTION:
                gun.targetting(event)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                plane.fire(event)

        for i in bombs:
            i.move()
            if i.hittest(gun):
                kill2 += 1
        for b in balls:
            b.move()

            if b.hittest(target_first) and target_first.live:
                hitt_2 += 1
                change_first += 1
                if change_first % 2 == 0:
                    target_first = Target(RED)
                else:
                    target_first = Target2(BLUE)
                target_first.live = 0
                target_first.hit()
                target_first.new_target()
            if b.hittest(target_second) and target_second.live:
                hitt_2 += 1
                change_second += 1
                if change_second % 2 == 0:
                    target_second = Target(GREEN)
                else:
                    target_second = Target2(MAGENTA)
                target_second.live = 0
                target_second.hit()
                target_second.new_target()
            if b.hittest(plane):
                kill1 += 1
            for i in bombs:
                if b.hittest(i) and i.live:
                    i.live = 0
                    i.hit()
                    i.death()

        gun.power_up()
     elif gameover1:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 finished = True

         screen.fill(WHITE)
         f2 = pygame.font.SysFont('None', 60)
         text2 = f2.render("Plane win", False,
                           (0, 180, 130))

         screen.blit(text2, (280, 230))
         pygame.display.update()

     else:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 finished = True

         screen.fill(WHITE)
         f2 = pygame.font.SysFont('None', 60)
         text2 = f2.render("Tank win", False,
                           (0, 180, 130))

         screen.blit(text2, (280, 230))
         pygame.display.update()

pygame.quit()