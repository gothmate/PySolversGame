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
        self.vol = 10
        self.seta_esq = pg.image.load('imagens/seta_esq_az.png')
        self.seta_dir = pg.image.load('imagens/seta_dir_az.png')
        self.circulo_vol = pg.image.load('imagens/circulo_vol.png')
        self.mute = pg.image.load('imagens/mudo.png')
        self.mute = pg.image.load('imagens/mudo.png')
        self.balloon = pg.image.load('imagens/balloon.png')
        self.azul = pg.image.load('imagens/button_blue.png')
        self.quest = pg.image.load('imagens/q_blue.png')
        self.logo = pg.image.load('imagens/logo.png')
        self.tela = pg.display.set_mode([800, 600])
        self.clock = pg.time.Clock()
        self.fundo = pg.image.load('imagens/bground.png')
        self.sair = pg.QUIT
        self.confirmacao = 'self.r2'
        self.vidas = '3'
        self.pontos = '0'

    def music(self):
        pg.mixer.init()
        pg.mixer.music.load('game.mp3')
        pg.mixer.music.play(-1)

    def escolhe(self, pointer, resposta, x_pos, y_pos):
        if pointer.colliderect(resposta):
            self.sombra = pg.image.load('imagens/button_shadow.png')
            self.amarelo = pg.image.load('imagens/button_yellow.png')
            self.tela.blit(self.sombra, (x_pos - 3, y_pos - 3))
            self.tela.blit(self.amarelo, (x_pos, y_pos))

    def escolhe_vol(self, pointer, seta, xpos, ypos):
        self.music()
        if pointer.colliderect(seta):
            self.seta_esq_am = pg.image.load('imagens/seta_esq_am.png')
            self.seta_dir_am = pg.image.load('imagens/seta_dir_am.png')
            if seta == self.rect_seta_esq:
                self.tela.blit(self.seta_esq_am, (xpos - 3, ypos - 3))
            if seta == self.rect_seta_dir:
                self.tela.blit(self.seta_dir_am, (xpos - 3, ypos - 3))
            if seta == self.rect_circle:
                self.tela.blit(self.mute, (xpos, ypos))

    def resposta_escolha(self):
        if not self.correta == self.confirmacao:
            self.vidas = int(self.vidas)
            self.vidas -= 1
            self.vidas = str(self.vidas)
            sleep(.2)
            self.c += 1
        else:
            self.pontos = int(self.pontos)
            self.pontos += 100
            self.pontos = str(self.pontos)
            sleep(.2)
            self.c += 1

    def mouse(self):
        self.pointer = pg.image.load('imagens/pointer.png')
        self.rect = pg.Rect(0, 0, 1, 1)
        self.score = pg.image.load('imagens/button_pt.png')

    def cursor(self):
        # Mouse
        pg.draw.rect(self.tela, self.cor_player, self.rect)
        (self.rect.left, self.rect.top) = pg.mouse.get_pos()
        x, y = pg.mouse.get_pos()
        self.tela.blit(self.pointer, (x, y))
        pg.mouse.set_visible(False)

    def credits(self):
        self.tela.blit(self.member_one, (345, 100))
        self.tela.blit(self.member_two, (350, 150))
        self.tela.blit(self.member_three, (365, 200))
        self.tela.blit(self.member_four, (320, 250))
        self.tela.blit(self.member_five, (340, 300))

    def setting(self):
        global event
        # fechar tela
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.sair = True
        # FPS
        self.clock.tick(40)

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
        self.c = 0
        self.mouse()
        self.fontes()
        while self.sair != True:
            self.correta = (f'{self.data_frame["CORRETA"][self.c]}')
            self.pergunta = (f'{self.c + 1}.{self.data_frame["PERGUNTA"][self.c]}')
            self.r1 = (f'{self.data_frame["R1"][self.c]}')
            self.r2 = (f'{self.data_frame["R2"][self.c]}')
            self.r3 = (f'{self.data_frame["R3"][self.c]}')
            self.r4 = (f'{self.data_frame["R4"][self.c]}')

            self.setting()

            # Background
            self.tela.blit(self.fundo, (0, 0))
            self.tela.blit(self.balloon, (0, 500))

            # Textos
            self.text = self.texto_perg.render(self.pergunta, True, (self.cor_player))
            self.texto_vidas = self.texto_score.render('Vidas: ', True, self.cor_player)
            self.pontuacao = self.texto_score.render(self.pontos, True, (200, 200, 0))
            self.vida = self.texto_score.render(self.vidas, True, (200, 200, 0))
            self.resp1 = self.texto_resp.render(self.r1, True, (self.cor_player))
            self.resp2 = self.texto_resp.render(self.r2, True, (self.cor_player))
            self.resp3 = self.texto_resp.render(self.r3, True, (self.cor_player))
            self.resp4 = self.texto_resp.render(self.r4, True, (self.cor_player))

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

            if self.pergunta == (f'{self.c + 1}.{self.data_frame["PERGUNTA"][10]}'):
                self.frame2()

            # respostas
            self.tela.blit(self.resp1, (50, 320))
            self.tela.blit(self.resp2, (430, 320))
            self.tela.blit(self.resp3, (50, 420))
            self.tela.blit(self.resp4, (430, 420))

            self.cursor()

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
            self.setting()

            # Textos
            self.texto_vitoria = self.texto_final.render(self.victory_line1, True, self.cor_player)
            self.texto_vitoria2 = self.texto_final.render(self.victory_line2, True, self.cor_player)
            self.texto_vidas = self.texto_score.render('Vidas: ', True, self.cor_player)
            self.texto_retry = self.texto_score.render('Tentar Novamente', True, self.cor_player)
            self.texto_menu = self.texto_score.render('Menu', True, self.cor_player)
            self.pontuacao = self.texto_score.render(self.pontos, True, (200, 200, 0))
            self.vida = self.texto_score.render(self.vidas, True, (200, 200, 0))

            # Background
            self.tela.blit(self.fundo, (0, 0))
            self.tela.blit(self.balloon, (0, 500))
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
            self.quest_correta = pg.image.load('imagens/q_green.png')
            self.tela.blit(self.quest_correta, (630, 480))

            # colisões
            if self.rect.colliderect(self.retry):
                self.escolhe(self.rect, self.retry, 340, 260)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.pontos = '0'
                    self.vidas = '3'
                    self.c = 0
                    sleep(.1)
                    self.frame1()
            elif self.rect.colliderect(self.resultados):
                self.escolhe(self.rect, self.resultados, 340, 360)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.menu()

            self.tela.blit(self.texto_retry, (380, 275))
            self.tela.blit(self.texto_menu, (470, 375))

            self.cursor()

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
            self.setting()

            # Textos
            self.texto_vitoria = self.texto_final.render(self.victory_line1, True, self.cor_player)
            self.texto_vitoria2 = self.texto_final.render(self.victory_line2, True, self.cor_player)
            self.texto_vidas = self.texto_score.render('Vidas: ', True, self.cor_player)
            self.texto_retry = self.texto_score.render('Tentar Novamente', True, self.cor_player)
            self.texto_menu = self.texto_score.render('Menu', True, self.cor_player)
            self.pontuacao = self.texto_score.render(self.pontos, True, (200, 200, 0))
            self.vida = self.texto_score.render(self.vidas, True, (200, 200, 0))

            # Background
            self.tela.blit(self.fundo, (0, 0))
            self.tela.blit(self.balloon, (0, 500))
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
            self.quest_errada = pg.image.load('imagens/q_red.png')
            self.tela.blit(self.quest_errada, (630, 480))

            # colisões
            if self.rect.colliderect(self.retry):
                self.escolhe(self.rect, self.retry, 340, 260)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.vidas = '3'
                    self.pontos = '0'
                    self.c = 0
                    sleep(.1)
                    self.frame1()
            elif self.rect.colliderect(self.resultados):
                self.escolhe(self.rect, self.resultados, 340, 360)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.menu()

            self.tela.blit(self.texto_retry, (380, 275))
            self.tela.blit(self.texto_menu, (470, 375))

            self.cursor()

            pg.display.update()
        pg.quit()

    def menu(self):
        global event
        pg.font.init()
        pg.init()
        pg.display.set_caption("PySolvers Quiz Game")
        self.music()
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
            self.setting()

            # Textos
            self.texto_openning1 = self.texto_final.render(self.openning1, True, self.cor_player)
            self.texto_openning2 = self.texto_final.render(self.opening2, True, self.cor_player)
            self.texto_openning3 = self.texto_final.render(self.opening3, True, self.cor_player)
            self.texto_openning4 = self.texto_final.render(self.opening4, True, self.cor_player)
            self.texto_start = self.texto_score.render('Começar', True, self.cor_player)
            self.texto_resultados = self.texto_score.render('Records', True, self.cor_player)
            self.texto_opcoes = self.texto_score.render('Opções', True, self.cor_player)

            # Background
            self.tela.blit(self.fundo, (0, 0))
            self.tela.blit(self.balloon, (0, 500))
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
                    sleep(.2)
                    self.opcoes()

            elif self.rect.colliderect(self.records):
                self.escolhe(self.rect, self.records, 340, 410)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.escolhe(self.rect, self.records, 340, 410)

            self.tela.blit(self.texto_start, (455, 260))
            self.tela.blit(self.texto_opcoes, (470, 340))
            self.tela.blit(self.texto_resultados, (470, 430))

            self.cursor()

            pg.display.update()
        pg.quit()

    def opcoes(self):
        global event
        pg.font.init()
        pg.init()
        pg.display.set_caption("PySolvers Quiz Game")
        self.mouse()
        self.fontes()
        self.creditos = pg.Rect(340, 320, 360, 60)
        self.voltar = pg.Rect(340, 410, 360, 60)
        self.rect_seta_esq = pg.Rect(450, 243, 50, 50)
        self.rect_seta_dir = pg.Rect(560, 243, 50, 50)
        self.rect_circle = pg.Rect(500, 240, 50, 50)

        while self.sair != True:
            self.setting()

            # Textos
            self.texto_title = self.texto_final.render('Opções', True, self.cor_player)
            self.texto_creditos = self.texto_score.render('Créditos', True, self.cor_player)
            self.texto_voltar = self.texto_score.render('Voltar', True, self.cor_player)
            self.texto_vol = self.texto_score.render(str(self.vol), True, self.cor_player)

            # Background
            self.tela.blit(self.fundo, (0, 0))
            self.tela.blit(self.balloon, (0, 500))
            self.tela.blit(self.texto_title, (300, 30))
            self.tela.blit(self.logo, (50, 210))
            self.tela.blit(self.circulo_vol, (500, 240))
            self.tela.blit(self.seta_esq, (450, 243))
            self.tela.blit(self.seta_dir, (560, 243))
            self.tela.blit(self.azul, (340, 320))
            self.tela.blit(self.azul, (340, 410))

            # colisões
            if self.rect.colliderect(self.rect_circle):
                self.escolhe_vol(self.rect, self.rect_circle, 500, 240)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.vol > 0:
                        self.vol = 0
                        pg.mixer.music.set_volume(self.vol)
                        sleep(0.1)

            if self.rect.colliderect(self.rect_seta_esq):
                self.escolhe_vol(self.rect, self.rect_seta_esq, 450, 243)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.vol > 0:
                        self.vol -= 1
                        pg.mixer.music.set_volume(self.vol/10)
                        sleep(0.1)

            elif self.rect.colliderect(self.rect_seta_dir):
                self.escolhe_vol(self.rect, self.rect_seta_dir, 560, 243)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.vol < 10:
                        self.vol += 1
                        pg.mixer.music.set_volume(self.vol/10)
                        sleep(0.1)

            elif self.rect.colliderect(self.creditos):
                self.escolhe(self.rect, self.creditos, 340, 320)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.mostrar_creditos()

            elif self.rect.colliderect(self.voltar):
                self.escolhe(self.rect, self.voltar, 340, 410)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.menu()

            # centraliza texto do volume
            if self.vol == 10:
                self.tela.blit(self.texto_vol, (511, 260))
            else:
                self.tela.blit(self.texto_vol, (520, 260))

            self.tela.blit(self.texto_creditos, (470, 340))
            self.tela.blit(self.texto_voltar, (470, 430))

            self.cursor()

            pg.display.update()
        pg.quit()

    def mostrar_creditos(self):
        global event
        pg.font.init()
        pg.init()
        pg.display.set_caption("PySolvers Quiz Game")
        self.mouse()
        self.fontes()

        # self.start = pg.Rect(340, 240, 360, 60)
        self.creditos = pg.Rect(340, 320, 360, 60)
        self.voltar = pg.Rect(340, 410, 360, 60)

        while self.sair != True:
            self.setting()

            # Textos
            self.prod = self.texto_final.render('Produzido por:', True, self.cor_player)
            self.member_one = self.texto_final.render('Gabriel Correia', True, self.cor_player)
            self.member_two = self.texto_final.render('Ricardo Garcês', True, self.cor_player)
            self.member_three = self.texto_final.render('Pablo Narciso', True, self.cor_player)
            self.member_four = self.texto_final.render('Eduardo Gonçalves', True, self.cor_player)
            self.member_five = self.texto_final.render('Antonio (Tonny)', True, self.cor_player)

            self.texto_voltar = self.texto_score.render('Voltar', True, self.cor_player)

            # Background
            self.tela.blit(self.fundo, (0, 0))
            self.tela.blit(self.balloon, (0, 500))
            self.tela.blit(self.prod, (250, 30))
            self.tela.blit(self.logo, (30, 90))
            self.tela.blit(self.azul, (340, 410))

            # colisões
            if self.rect.colliderect(self.voltar):
                self.escolhe(self.rect, self.voltar, 340, 410)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.menu()

            self.credits()

            self.tela.blit(self.texto_voltar, (480, 430))

            self.cursor()

            pg.display.update()
        pg.quit()
