import os
os.system('cls' if os.name == 'nt' else 'clear')
print("Start Game...")
print("============[ Chuc Ban Choi Game Vui Ve ]=============")
import pygame
import random
import time
import sys

pygame.init()

screen_x = 900
screen_y = 550
screen = pygame.display.set_mode((screen_x, screen_y))

mini_game = pygame.image.load('assets/table.png')
game = mini_game.convert_alpha()

avatar = pygame.image.load('assets/avt.png')
avatar_convert = avatar.convert_alpha()

bground = pygame.image.load('assets/bg.png').convert_alpha()

pygame.display.set_caption('cổng game tài xỉu uy tín xanh chín')
def load_bg():
	background = pygame.transform.scale(bground, (900, 550))
	screen.blit(background, (0, 0))

def load_mini_game():
	loads_mini_game = pygame.transform.scale(game, (900, 550))
	screen.blit(loads_mini_game, (0, 0))

def load_profile():
	font_tnv = pygame.font.Font(None, 30)
	text_tnv = font_tnv.render("adm_chienph07", True, (255, 255, 255))
	load_img_avt = pygame.transform.scale(avatar_convert, (50, 50))
	screen.blit(load_img_avt, (0, 0))
	screen.blit(text_tnv, (60, 5))

	def load_coins():
		font_coint = pygame.font.Font(None, 25)
		text_coins = font_coint.render('3,890,567,000', True, (255, 255, 0, 0))
		screen.blit(text_coins, (60, 30))
	load_coins()

session = True
member_tai = random.randint(1, 20)
member_xiu = random.randint(1, 20)

hu_tai = random.randint(1, 3)
hu_xiu = random.randint(1, 3)

phien = 22618

time_phien = 10

clock = pygame.time.Clock()

while session:
	load_bg()
	load_mini_game()
	load_profile()

	time_phien = time_phien - 1
	font_phien = pygame.font.Font(None, 200)
	text_phien = font_phien.render(f"{time_phien}", True, (255, 255, 0))
	screen.blit(text_phien, (400, 240))

	phien = phien
	font_phien = pygame.font.Font(None, 23)
	text_phien = font_phien.render(f"#{phien}", True, (255, 255, 0))
	screen.blit(text_phien, (420, 135))

	mb_tai = random.randint(1, 100)
	member_tai = member_tai + mb_tai
	font_member_tai = pygame.font.Font(None, 15)
	text_member_tai = font_member_tai.render(f"{member_tai}", True, (255, 255, 255))
	screen.blit(text_member_tai, (295, 180))

	mb_xiu = random.randint(1, 100)
	member_xiu = member_xiu + mb_xiu
	font_member_xiu = pygame.font.Font(None, 15)
	text_member_xiu = font_member_xiu.render(f"{member_xiu}", True, (255, 255, 255))
	screen.blit(text_member_xiu, (575, 180))

	ht = random.randint(1, 250)
	hu_tai = hu_tai + ht
	phu1 = random.randint(100, 999)
	font_hu_tai = pygame.font.Font(None, 40)
	text_hu_tai = font_hu_tai.render(f"{hu_tai},{phu1},000", True, (238, 201, 0, 255))
	screen.blit(text_hu_tai, (140, 296))

	ht1 = random.randint(1, 250)
	hu_xiu = hu_xiu + ht1
	phu2 = random.randint(100, 999)
	font_hu_xiu = pygame.font.Font(None, 40)
	text_hu_xiu = font_hu_xiu.render(f"{hu_xiu},{phu2},000", True, (238, 201, 0, 255))
	screen.blit(text_hu_xiu, (597, 296))


	print(f"""

(
	"Phien" : "#{phien}",
	"ThOi_gian_con_lai" : "{time_phien}",
	"So_Nguoi_Cuoc_TAI" : "{member_tai}",
	"So_Nguoi_Cuoc_XIU" : "{member_xiu}",
	"Tong_Cuoc_TAI" : "{hu_tai},{phu1},000",
	"Tong_Cuoc_XIU" : "{hu_xiu},{phu2},000",
)
""")

	time.sleep(3)

	if time_phien == 0:
		font_phien = pygame.font.Font(None, 200)
		text_phien = font_phien.render("0", True, (0, 0, 0))
		screen.blit(text_phien, (400, 240))

		dice_1 = random.randint(1, 6)
		if dice_1 == 1:
			img_dice_1 = pygame.image.load('dice/dice_1.png')
			dice1 = pygame.transform.scale(img_dice_1, (80, 80))
			screen.blit(dice1, (395, 210))
		if dice_1 == 2:
			img_dice_2 = pygame.image.load('dice/dice_2.png')
			dice2 = pygame.transform.scale(img_dice_2, (80, 80))
			screen.blit(dice2, (395, 210))
		if dice_1 == 3:
			img_dice_3 = pygame.image.load('dice/dice_3.png')
			dice3 = pygame.transform.scale(img_dice_3, (80, 80))
			screen.blit(dice3, (395, 210))
		if dice_1 == 4:
			img_dice_4 = pygame.image.load('dice/dice_4.png')
			dice4 = pygame.transform.scale(img_dice_4, (80, 80))
			screen.blit(dice4, (395, 210))
		if dice_1 == 5:
			img_dice_5 = pygame.image.load('dice/dice_5.png')
			dice5 = pygame.transform.scale(img_dice_5, (80, 80))
			screen.blit(dice5, (395, 210))
		if dice_1 == 6:
			img_dice_6 = pygame.image.load('dice/dice_6.png')
			dice6 = pygame.transform.scale(img_dice_6, (80, 80))
			screen.blit(dice6, (395, 210))

		dice_2 = random.randint(1, 6)
		if dice_2 == 1:
			img_dice_1 = pygame.image.load('dice/dice_1.png')
			dice1 = pygame.transform.scale(img_dice_1, (80, 80))
			screen.blit(dice1, (455, 296))
		if dice_2 == 2:
			img_dice_2 = pygame.image.load('dice/dice_2.png')
			dice2 = pygame.transform.scale(img_dice_2, (80, 80))
			screen.blit(dice2, (455, 296))
		if dice_2 == 3:
			img_dice_3 = pygame.image.load('dice/dice_3.png')
			dice3 = pygame.transform.scale(img_dice_3, (80, 80))
			screen.blit(dice3, (455, 296))
		if dice_2 == 4:
			img_dice_4 = pygame.image.load('dice/dice_4.png')
			dice4 = pygame.transform.scale(img_dice_4, (80, 80))
			screen.blit(dice4, (455, 296))
		if dice_2 == 5:
			img_dice_5 = pygame.image.load('dice/dice_5.png')
			dice5 = pygame.transform.scale(img_dice_5, (80, 80))
			screen.blit(dice5, (455, 296))
		if dice_2 == 6:
			img_dice_6 = pygame.image.load('dice/dice_6.png')
			dice6 = pygame.transform.scale(img_dice_6, (80, 80))
			screen.blit(dice6, (455, 296))

		dice_3 = random.randint(1, 6)
		if dice_3 == 1:
			img_dice_1 = pygame.image.load('dice/dice_1.png')
			dice1 = pygame.transform.scale(img_dice_1, (80, 80))
			screen.blit(dice1, (360, 300))
		if dice_3 == 2:
			img_dice_2 = pygame.image.load('dice/dice_2.png')
			dice2 = pygame.transform.scale(img_dice_2, (80, 80))
			screen.blit(dice2, (360, 300))
		if dice_3 == 3:
			img_dice_3 = pygame.image.load('dice/dice_3.png')
			dice3 = pygame.transform.scale(img_dice_3, (80, 80))
			screen.blit(dice3, (360, 300))
		if dice_3 == 4:
			img_dice_4 = pygame.image.load('dice/dice_4.png')
			dice4 = pygame.transform.scale(img_dice_4, (80, 80))
			screen.blit(dice4, (360, 300))
		if dice_3 == 5:
			img_dice_5 = pygame.image.load('dice/dice_5.png')
			dice5 = pygame.transform.scale(img_dice_5, (80, 80))
			screen.blit(dice5, (360, 300))
		if dice_3 == 6:
			img_dice_6 = pygame.image.load('dice/dice_6.png')
			dice6 = pygame.transform.scale(img_dice_6, (80, 80))
			screen.blit(dice6, (360, 300))

		Ket_Qua = int(dice_1 + dice_2 + dice_3)
		print(f"""
(
	"Phien" : "{phien}",
	"Ket_Qua" : "{Ket_Qua}",
	"KQ_Xuc_Xac_1" : "{dice_1}",
	"KQ_Xuc_Xac_2" : "{dice_2}",
	"KQ_Xuc_Xac_3" : "{dice_3}",
	"Member_Cuoc_TAI" : "{member_tai}",
	"Member_Cuoc_XIU" : "{member_xiu}",
	"Tong_Tien_Cuoc_TAI" : "{hu_tai},{phu1},000",
	"Tong_Tien_Cuoc_XIU" : "{hu_xiu},{phu2},000"
)
""")
		time_phien = 10
		phien = phien + 1
		hu_tai = random.randint(1, 6)
		hu_xiu = random.randint(1, 6)
		member_tai = random.randint(1, 20)
		member_xiu = random.randint(1, 20)
		time.sleep(1)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			session = False

	clock.tick(100)
	pygame.display.flip()
	pygame.display.update()
