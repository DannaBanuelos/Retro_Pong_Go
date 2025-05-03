import pygame
pygame.init()
pygame.mixer.init()

#Canvas design
pygame.display.set_caption("Retro Pong GO!🏓")
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))

#Design & Colors
White = (255, 255, 255)
Black = (0, 0, 0)
Grey = (80, 80, 80)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Green = (0, 255, 0)
Score_font = pygame.font.SysFont("Impact", 50)
Winning_score = 5
level = 1

#Sound
SOUND_DIR = "sounds/"
bounce_sound = pygame.mixer.Sound(SOUND_DIR + "Bounce.wav")
point_sound = pygame.mixer.Sound(SOUND_DIR + "Point.wav")
winner_sound = pygame.mixer.Sound(SOUND_DIR + "Winner.wav")
final_win_sound = pygame.mixer.Sound(SOUND_DIR + "Game Final Win.wav")

class Paddle: 
    Speed = 5

    def __init__(self, x, y, width, height, color):
        self.x = self.original_x = x
        self.y = self.original_y = y 
        self.width = width
        self.height = height
        self.Speed = 5
        self.COLOR = color

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.Speed
        else:
            self.y += self.Speed

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    MAX_Speed = 10

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y 
        self.radius = radius
        self.x_speed = self.MAX_Speed
        self.y_speed = 0
        self.COLOR = White 

    def draw(self, screen):
        pygame.draw.circle(screen, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_speed = 0
        self.x_speed *= -1

    
def draw_center_line(screen):
    line_width = 10
    segment_height = 30
    gap = 20

    start_y = 100

    for y in range(start_y, height, segment_height + gap):
        pygame.draw.rect(screen, Grey, (width // 2 - line_width // 2, y, line_width, segment_height))
 

def draw(screen, paddles, ball, left_score, right_score, level):
    screen.fill(Black)

    left_score_text = Score_font.render(f"{left_score}", 1, White)
    right_score_text = Score_font.render(f"{right_score}", 1, White)
    screen.blit(left_score_text, (width//4 - left_score_text.get_width()//2, 20))
    screen.blit(right_score_text, (width * (3/4) - 
                                   right_score_text.get_width()//2, 20))

    draw_center_line(screen)

    for paddle in paddles:
        paddle.draw(screen)
    
    ball.draw(screen)

    level_text = Score_font.render(f"Level {level}", 1, Green)
    screen.blit(level_text, (width//2 - level_text.get_width()//2, 20))

    pygame.display.update()


def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= height:
        ball.y_speed *= -1
        bounce_sound.play()
    elif ball.y - ball.radius <=0:
        ball.y_speed *= -1
        bounce_sound.play()

    if ball.x_speed < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_speed *= -1
                bounce_sound.play()

                middle_y = left_paddle.y + left_paddle.height / 2
                diff_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_Speed
                y_speed = diff_in_y / reduction_factor
                ball.y_speed = -1 * y_speed

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x: 
                ball.x_speed *= -1
                bounce_sound.play()

                middle_y = right_paddle.y + right_paddle.height / 2
                diff_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_Speed
                y_speed = diff_in_y / reduction_factor
                ball.y_speed = -1 * y_speed

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.Speed >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.Speed + left_paddle.height <= height:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.Speed >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.Speed + right_paddle.height <= height:
        right_paddle.move(up=False)

def set_difficulty(level, ball, left_paddle, right_paddle):
    if level == 1:
        ball.MAX_Speed = 8
        ball.x_speed = 8
        left_paddle.Speed = right_paddle.Speed = 5
    elif level == 2:
        ball.MAX_Speed = 10
        ball.x_speed = 10
        left_paddle.Speed = right_paddle.Speed = 7
    elif level == 3:
        ball.MAX_Speed = 14
        ball.x_speed = 14
        left_paddle.Speed = right_paddle.Speed = 9


def main(): #Canvas & Paddles designs 
    FPS = 60
    restart = True 
    clock = pygame.time.Clock()
    global level

    while restart:
        level = 1
        left_score = 0
        right_score = 0
        left_consecutive_wins = 0
        right_consecutive_wins = 0

        paddle_height, paddle_width = 150, 20
        left_paddle = Paddle(10, height//2 - paddle_height//2, 
                             paddle_width, paddle_height, Red)
        right_paddle = Paddle(width - 10 - paddle_width, height//2 -
                               paddle_height//2, paddle_width, paddle_height, Blue)
        ball = Ball(width // 2, height // 2, 20)
        set_difficulty(level, ball, left_paddle, right_paddle)

        run = True
        while run:
            clock.tick(FPS)
            draw(screen, [left_paddle, right_paddle], ball, left_score, right_score, level)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    restart = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        restart = False

            keys = pygame.key.get_pressed()
            handle_paddle_movement(keys, left_paddle, right_paddle)
            ball.move()
            handle_collision(ball, left_paddle, right_paddle)

            if ball.x < 0:
                right_score += 1
                point_sound.play()
                ball.reset()
            elif ball.x > width:
                left_score += 1
                point_sound.play()
                ball.reset()

            won = False
            if left_score >= Winning_score:
                won = True
                win_text = "Player 1 WINS!"
                winner_sound.play()
                left_consecutive_wins += 1
                right_consecutive_wins = 0
                
            elif right_score >= Winning_score:
                won = True
                win_text = "Player 2 WINS!"
                winner_sound.play()
                right_consecutive_wins += 1
                left_consecutive_wins = 0
                

            if won:
                result = Score_font.render(win_text, 1, White)
                screen.blit(result, (width//2 - result.get_width()//2, height//2 - result.get_height()//2))
                pygame.display.update()
                pygame.time.delay(3000)

                if left_consecutive_wins == 2 or right_consecutive_wins == 2: #prints the results if won twice first
                    screen.fill(Black)
                    final_text = "Player 1 Wins the GAME!" if left_consecutive_wins == 2 else "Player 2 Wins the GAME!"
                    result = Score_font.render(final_text, 1, White)
                    screen.blit(result, (width//2 - result.get_width()//2, height//2 - result.get_height()//2))
                    final_win_sound.play()
                    pygame.display.update()
                    pygame.time.delay(3000)
                    run = False 
                elif level == 3: #print the results in level 3
                    screen.fill(Black)
                    final_text = "Player 1 Wins the GAME!" if left_score > right_score else "Player 2 Wins the GAME!"
                    result = Score_font.render(final_text, 1, White)
                    screen.blit(result, (width//2 - result.get_width()//2, height//2 - result.get_height()//2))
                    final_win_sound.play()
                    pygame.display.update()
                    pygame.time.delay(3000)
                    run = False
                else:
                    level += 1
                    set_difficulty(level, ball, left_paddle, right_paddle)
                    ball.reset()
                    left_paddle.reset()
                    right_paddle.reset()
                    left_score = 0
                    right_score = 0


if __name__ == "__main__":
    main() 
    pygame.quit()