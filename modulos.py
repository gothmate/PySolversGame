import pygame as pg
import pandas as pd
from time import sleep


class Game:
    def __init__(self, *groups):
        super().__init__(*groups)
        # Definições dos objetos (variáveis)
        self.id_planilha = '1CRPIwP0vOf9rjTRw-TFnTzCV0vHWhoMuQuqxnCPxBxo'
        self.data_frame = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{self.id_planilha}/export?format=csv')
        self.c = 0
        self.cor_player = (255, 255, 255)
        self.amarelo = (200, 200, 0)
        self.azul = pg.image.load('button_blue.png')
        self.quest = pg.image.load('q_blue.png')
        self.logo = pg.image.load('logo.png')
        self.tela = pg.display.set_mode([800, 600])
        self.clock = pg.time.Clock()
        self.fundo = pg.image.load('bground.png')
        self.sair = pg.QUIT
        self.confirmacao = 'self.r2'
    def escolhe(self, pointer, resposta, x_pos, y_pos):
        if pointer.colliderect(resposta):
            self.sombra = pg.image.load('button_shadow.png')
            self.amarelo = pg.image.load('button_yellow.png')
            self.tela.blit(self.sombra, (x_pos - 3, y_pos - 3))
            self.tela.blit(self.amarelo, (x_pos, y_pos))

    def resposta_escolha(self):
        if not self.correta == self.confirmacao:
            self.vidas = int(self.vidas)
            self.vidas -= 1
            self.vidas = str(self.vidas)
            sleep(.5)
            self.c += 1
        else:
            self.pontos = int(self.pontos)
            self.pontos += 100
            self.pontos = str(self.pontos)
            sleep(.5)
            self.c += 1

    def mouse(self):
        self.pointer = pg.image.load('pointer.png')
        self.rect = pg.Rect(0, 0, 1, 1)
        self.vidas = '3'
        self.pontos = '0'
        self.score = pg.image.load('button_pt.png')

    def fontes(self):
        self.texto_score = pg.font.SysFont('Franklin Gothic', 40, bold=True)
        self.texto_perg = pg.font.SysFont('Franklin Gothic', 38, bold=True)
        self.texto_resp = pg.font.SysFont('Franklin Gothic', 23, bold=True)
        self.texto_final = pg.font.SysFont('Franklin Gothic', 50, bold=True)

    def frame1(self):
        global event
        pg.font.init()
        pg.init()
        pg.display.set_caption("PySolvers Quiz Game")
        self.r_a = pg.Rect(30, 300, 360, 60)
        self.r_b = pg.Rect(410, 300, 360, 60)
        self.r_c = pg.Rect(30, 400, 360, 60)
        self.r_d = pg.Rect(410, 400, 360, 60)

        self.mouse()
        self.fontes()
        while self.sair != True:
            self.correta = (f'{self.data_frame["CORRETA"][self.c]}')
            self.pergunta = (f'{self.c + 1}.{self.data_frame["PERGUNTA"][self.c]}')
            self.r1 = (f'{self.data_frame["R1"][self.c]}')
            self.r2 = (f'{self.data_frame["R2"][self.c]}')
            self.r3 = (f'{self.data_frame["R3"][self.c]}')
            self.r4 = (f'{self.data_frame["R4"][self.c]}')


            # fechar tela
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.sair = True
            # FPS
            self.clock.tick(40)
            # Background
            self.tela.blit(self.fundo, (0, 0))

            # Textos
            self.text = self.texto_perg.render(self.pergunta, 1, (self.cor_player))
            self.texto_vidas = self.texto_score.render('Vidas: ', 1, self.cor_player)
            self.pontuacao = self.texto_score.render(self.pontos, 1, (200, 200, 0))
            self.vida = self.texto_score.render(self.vidas, 1, (200, 200, 0))

            # posicionamento do texto
            self.tela.blit(self.score, (600, 30))
            self.tela.blit(self.score, (55, 30))
            self.tela.blit(self.pontuacao, (100, 45))
            self.tela.blit(self.text, (30, 150))
            self.tela.blit(self.texto_vidas, (615, 45))
            self.tela.blit(self.vida, (720, 45))

            # botões de resposta
            self.tela.blit(self.azul, (30, 300))
            self.tela.blit(self.azul, (410, 300))
            self.tela.blit(self.azul, (30, 400))
            self.tela.blit(self.azul, (410, 400))

            self.tela.blit(self.quest, (630, 480))

            # Colisões
            if self.rect.colliderect(self.r_a):
                self.escolhe(self.rect, self.r_a, 30, 300)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.correta == self.r1:
                        self.confirmacao = self.r1
                    self.resposta_escolha()

            if self.rect.colliderect(self.r_b):
                self.escolhe(self.rect, self.r_b, 410, 300)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.correta == self.r2:
                        self.confirmacao = self.r2
                    self.resposta_escolha()

            if self.rect.colliderect(self.r_c):
                self.escolhe(self.rect, self.r_c, 30, 400)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.correta == self.r3:
                        self.confirmacao = self.r3
                    self.resposta_escolha()

            if self.rect.colliderect(self.r_d):
                self.escolhe(self.rect, self.r_d, 410, 400)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.correta == self.r4:
                        self.confirmacao = self.r4
                    self.resposta_escolha()


            if self.vidas == '0':
                self.frame3()
                self.c = 0
            if self.pergunta == (f'{self.c + 1}.{self.data_frame["PERGUNTA"][10]}'):
                self.frame2()
                self.c = 0



            # respostas
            self.resp1 = self.texto_resp.render(self.r1, 1, (self.cor_player))
            self.tela.blit(self.resp1, (50, 320))
            self.resp2 = self.texto_resp.render(self.r2, 1, (self.cor_player))
            self.tela.blit(self.resp2, (430, 320))
            self.resp3 = self.texto_resp.render(self.r3, 1, (self.cor_player))
            self.tela.blit(self.resp3, (50, 420))
            self.resp4 = self.texto_resp.render(self.r4, 1, (self.cor_player))
            self.tela.blit(self.resp4, (430, 420))

            # Mouse
            pg.draw.rect(self.tela, self.cor_player, self.rect)
            (self.rect.left, self.rect.top) = pg.mouse.get_pos()
            x, y = pg.mouse.get_pos()
            self.tela.blit(self.pointer, (x, y))
            pg.mouse.set_visible(False)

            pg.display.update()
        pg.quit()

    def frame2(self):
        global event
        pg.font.init()
        pg.init()
        pg.display.set_caption("PySolvers Quiz Game")
        self.victory_line1 = 'Parabéns, você vendeu.'
        self.victory_line2 = 'Nada pode te parar!'
        self.mouse()
        self.fontes()

        self.retry = pg.Rect(340, 260, 360, 60)
        self.resultados = pg.Rect(340, 360, 360, 60)

        while self.sair != True:
            # fechar tela
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.sair = True
            # FPS
            self.clock.tick(40)

            # Textos
            self.texto_vitoria = self.texto_final.render(self.victory_line1, 1, self.cor_player)
            self.texto_vitoria2 = self.texto_final.render(self.victory_line2, 1, self.cor_player)
            self.texto_vidas = self.texto_score.render('Vidas: ', 1, self.cor_player)
            self.texto_retry = self.texto_score.render('Tentar Novamente', 1, self.cor_player)
            self.texto_resultados = self.texto_score.render('Records', 1, self.cor_player)
            self.pontuacao = self.texto_score.render(self.pontos, 1, (200, 200, 0))
            self.vida = self.texto_score.render(self.vidas, 1, (200, 200, 0))

            # Background
            self.tela.blit(self.fundo, (0, 0))

            self.tela.blit(self.score, (600, 30))
            self.tela.blit(self.score, (55, 30))
            self.tela.blit(self.pontuacao, (100, 45))
            self.tela.blit(self.texto_vidas, (615, 45))
            self.tela.blit(self.vida, (720, 45))
            self.tela.blit(self.texto_vitoria, (150, 110))
            self.tela.blit(self.texto_vitoria2, (190, 160))
            self.tela.blit(self.logo, (50, 180))
            self.tela.blit(self.azul, (340, 260))
            self.tela.blit(self.azul, (340, 360))
            self.quest_correta = pg.image.load('q_green.png')
            self.tela.blit(self.quest_correta, (630, 480))

            # colisões
            if self.rect.colliderect(self.retry):
                self.escolhe(self.rect, self.retry, 340, 260)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.pontos = '0'
                    self.vidas = '3'
                    self.c = 0
                    self.frame1()
            elif self.rect.colliderect(self.resultados):
                self.escolhe(self.rect, self.resultados, 340, 360)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.escolhe(self.rect, self.resultados, 340, 360)

            self.tela.blit(self.texto_retry, (380, 275))
            self.tela.blit(self.texto_resultados, (470, 375))

            # Mouse
            pg.draw.rect(self.tela, self.cor_player, self.rect)
            (self.rect.left, self.rect.top) = pg.mouse.get_pos()
            x, y = pg.mouse.get_pos()
            self.tela.blit(self.pointer, (x, y))
            pg.mouse.set_visible(False)

            pg.display.update()
        pg.quit()

    def frame3(self):
        global event
        pg.font.init()
        pg.init()
        pg.display.set_caption("PySolvers Quiz Game")
        self.victory_line1 = 'Infelizmente, você perdeu.'
        self.victory_line2 = 'Continue estudando e arrebente!'
        self.mouse()
        self.fontes()

        self.retry = pg.Rect(340, 260, 360, 60)
        self.resultados = pg.Rect(340, 360, 360, 60)

        while self.sair != True:
            # fechar tela
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.sair = True
            # FPS
            self.clock.tick(40)

            # Textos
            self.texto_vitoria = self.texto_final.render(self.victory_line1, 1, self.cor_player)
            self.texto_vitoria2 = self.texto_final.render(self.victory_line2, 1, self.cor_player)
            self.texto_vidas = self.texto_score.render('Vidas: ', 1, self.cor_player)
            self.texto_retry = self.texto_score.render('Tentar Novamente', 1, self.cor_player)
            self.texto_resultados = self.texto_score.render('Records', 1, self.cor_player)
            self.pontuacao = self.texto_score.render(self.pontos, 1, (200, 200, 0))
            self.vida = self.texto_score.render(self.vidas, 1, (200, 200, 0))

            # Background
            self.tela.blit(self.fundo, (0, 0))

            self.tela.blit(self.score, (600, 30))
            self.tela.blit(self.score, (55, 30))
            self.tela.blit(self.pontuacao, (100, 45))
            self.tela.blit(self.texto_vidas, (615, 45))
            self.tela.blit(self.vida, (720, 45))
            self.tela.blit(self.texto_vitoria, (150, 110))
            self.tela.blit(self.texto_vitoria2, (80, 160))
            self.tela.blit(self.logo, (50, 180))
            self.tela.blit(self.azul, (340, 260))
            self.tela.blit(self.azul, (340, 360))
            self.quest_errada = pg.image.load('q_red.png')
            self.tela.blit(self.quest_errada, (630, 480))

            # colisões
            if self.rect.colliderect(self.retry):
                self.escolhe(self.rect, self.retry, 340, 260)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.vidas = '3'
                    self.pontos = '0'
                    self.c = 0
                    self.frame1()
            elif self.rect.colliderect(self.resultados):
                self.escolhe(self.rect, self.resultados, 340, 360)
                if event.type == pg.MOUSEBUTTONDOWN:
                    # descobrir como escrever em planilha o resultado ####################################
                    self.escolhe(self.rect, self.resultados, 340, 360)

            self.tela.blit(self.texto_retry, (380, 275))
            self.tela.blit(self.texto_resultados, (470, 375))

            # Mouse
            pg.draw.rect(self.tela, self.cor_player, self.rect)
            (self.rect.left, self.rect.top) = pg.mouse.get_pos()
            x, y = pg.mouse.get_pos()
            self.tela.blit(self.pointer, (x, y))
            pg.mouse.set_visible(False)

            pg.display.update()
        pg.quit()

    def menu(self):
        global event
        pg.font.init()
        pg.init()
        pg.display.set_caption("PySolvers Quiz Game")
        self.openning1 = 'Bem vindo ao Quiz Game.'
        self.opening2 = 'Meu nome é Py15-A e vou te'
        self.opening3 = 'acompanhar nesse processo.'
        self.opening4 = 'Você tem 3 chances! Não as desperdice.'
        self.mouse()
        self.fontes()

        self.start = pg.Rect(340, 240, 360, 60)
        self.options = pg.Rect(340, 320, 360, 60)
        self.records = pg.Rect(340, 410, 360, 60)

        while self.sair != True:
            # fechar tela
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.sair = True
            # FPS
            self.clock.tick(40)

            # Textos
            self.texto_openning1 = self.texto_final.render(self.openning1, 1, self.cor_player)
            self.texto_openning2 = self.texto_final.render(self.opening2, 1, self.cor_player)
            self.texto_openning3 = self.texto_final.render(self.opening3, 1, self.cor_player)
            self.texto_openning4 = self.texto_final.render(self.opening4, 1, self.cor_player)
            self.texto_start = self.texto_score.render('Começar', 1, self.cor_player)
            self.texto_resultados = self.texto_score.render('Records', 1, self.cor_player)
            self.texto_opcoes = self.texto_score.render('Opções', 1, self.cor_player)

            # Background
            self.tela.blit(self.fundo, (0, 0))

            self.tela.blit(self.texto_openning1, (150, 30))
            self.tela.blit(self.texto_openning2, (130, 70))
            self.tela.blit(self.texto_openning3, (125, 110))
            self.tela.blit(self.texto_openning4, (10, 150))
            self.tela.blit(self.logo, (50, 210))
            self.tela.blit(self.azul, (340, 240))
            self.tela.blit(self.azul, (340, 320))
            self.tela.blit(self.azul, (340, 410))

            # colisões
            if self.rect.colliderect(self.start):
                self.escolhe(self.rect, self.start, 340, 240)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.frame1()

            elif self.rect.colliderect(self.options):
                self.escolhe(self.rect, self.options, 340, 320)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.escolhe(self.rect, self.options, 340, 320)

            elif self.rect.colliderect(self.records):
                self.escolhe(self.rect, self.records, 340, 410)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.escolhe(self.rect, self.records, 340, 410)

            self.tela.blit(self.texto_start, (455, 260))
            self.tela.blit(self.texto_opcoes, (470, 340))
            self.tela.blit(self.texto_resultados, (470, 430))

            # Mouse
            pg.draw.rect(self.tela, self.cor_player, self.rect)
            (self.rect.left, self.rect.top) = pg.mouse.get_pos()
            x, y = pg.mouse.get_pos()
            self.tela.blit(self.pointer, (x, y))
            pg.mouse.set_visible(False)

            pg.display.update()
        pg.quit()
