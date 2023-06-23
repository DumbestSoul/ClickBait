import pygame, sys
from settings import *
from gen import Generator

# game class
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("ClickBait")
        self.generator = Generator(self.screen)
        self.text = pygame.font.SysFont('arial', 30)

    def run(self):

        while True:
            self.screen.fill((255, 255, 255))
            scoresurface = self.text.render(f"Score:{str(self.generator.score)}", True, (0, 0, 0))
            self.screen.blit(scoresurface, (5, 5))
            self.generator.main()   # geenrates food and checks for its generation


            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    x, y = event.pos[0], event.pos[1]
                    self.generator.clickEvent(x, y)
                
            pygame.display.update()
            self.clock.tick(FPS)


# main function
if __name__=='__main__':
    game = Game()
    game.run()