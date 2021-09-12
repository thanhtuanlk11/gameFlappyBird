import pygame
from random import randint
pygame.init()
screen =pygame.display.set_mode((400,600))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock() #kết hợp với lệnh clok trong vòng lặp để cho pahanf trăm CPU không tăng lên quá lớn
WHILE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
x_bird=50
y_bird=350
tube1_x=400
tube2_x=600
tube3_x=800
tuble_width=50
tube1_height=randint(100,400)
tube2_height=randint(100,400)
tube3_height=randint(100,400)
d_2tube=150 #khoảng cách 2 ống 
bird_drop_velocity=0 #vận tốc con chim ban đầu bằng 0
gravity=0.5 #trọng lực bằng 0.5
tube_velocity=2 #tốc độ các ống
score = 0
font=pygame.font.SysFont('san',20)  # thiết lập front chữ kích thước chữ
font1=pygame.font.SysFont('san',40) #thiết lập font chữ cho chữ kết thúc game 
background_img=pygame.image.load('images/background.png')
background_img=pygame.transform.scale(background_img,(400,600))
bird_img=pygame.image.load('images/bird.png')
bird_img=pygame.transform.scale(bird_img,(35,35))
tube_img=pygame.image.load('images/tube.png')
tube_op_img=pygame.image.load('images/tube_op.png')
sound=pygame.mixer.Sound('no6.wav') #nhạc  
sand_img=pygame.image.load('images/sand.png')
sand_img=pygame.transform.scale(sand_img,(400,30))
tuble1_pass=False
tuble2_pass=False
tuble3_pass=False
pausing=False
running =True
while running:
	pygame.mixer.Sound.play(sound)  
	#giới hạn nhấn 60 lần 
	clock.tick(60) 
	screen.fill(WHILE)
	#vẽ backgound xét kích thước
	screen.blit(background_img,(0,0))
	#vẽ cat
	sand = screen.blit(sand_img,(0,570))
	#vẽ chim 
	bird=screen.blit(bird_img,(x_bird,y_bird))
	#ep anh ong vaf ve ong
	tube1_img=pygame.transform.scale(tube_img,(tuble_width,tube1_height))
	tube1=screen.blit(tube1_img,(tube1_x,0))
	tube2_img=pygame.transform.scale(tube_img,(tuble_width,tube2_height))
	tube2=screen.blit(tube2_img,(tube2_x,0))
	tube3_img=pygame.transform.scale(tube_img,(tuble_width,tube3_height))
	tube3=screen.blit(tube3_img,(tube3_x,0))
	#ep anh ong va ve ong doi dien
	tube1_op_img=pygame.transform.scale(tube_op_img,(tuble_width,600-(tube1_height+d_2tube)))
	tube1_op=screen.blit(tube1_op_img,(tube1_x,tube1_height+d_2tube))
	tube2_op_img=pygame.transform.scale(tube_op_img,(tuble_width,600-(tube2_height+d_2tube)))
	tube2_op=screen.blit(tube2_op_img,(tube2_x,tube2_height+d_2tube))
	tube3_op_img=pygame.transform.scale(tube_op_img,(tuble_width,600-(tube3_height+d_2tube)))
	tube3_op=screen.blit(tube3_op_img,(tube3_x,tube3_height+d_2tube))
	#ông di chuyển sang trai
	tube1_x=tube1_x - tube_velocity
	tube2_x=tube2_x - tube_velocity
	tube3_x=tube3_x - tube_velocity
	#tạo ống mới
	if tube1_x<-tuble_width:
		tube1_x=550
		tube1_height=randint(100,400)
		tuble1_pass=False
	if tube2_x<-tuble_width:
		tube2_x=550
		tube2_height=randint(100,400)
		tuble2_pass=False
	if tube3_x<-tuble_width:
		tube3_x=550
		tube3_height=randint(100,400)
		tuble3_pass=False
	#cho chim rơi 
	y_bird=y_bird+bird_drop_velocity
	bird_drop_velocity=bird_drop_velocity+gravity
	#ghi điểm
	score_txt=font.render("Score:"+str(score),True,RED)
	screen.blit(score_txt,(5,5))
	#cộng điểm
	if tube1_x+tuble_width<=x_bird and tuble1_pass == False:
		score+=1
		tuble1_pass=True
	if tube2_x+tuble_width<=x_bird and tuble2_pass == False:
		score+=1
		tuble2_pass=True
	if tube3_x+tuble_width<=x_bird and tuble3_pass == False:
		score+=1
		tuble3_pass=True
	# Kiểm tra sự va chạm 
	tubes=[tube1,tube2,tube3,tube1_op,tube2_op,tube3_op,sand]
	for tube in tubes: #tube lập trong tubes
		if bird.colliderect(tube):  #Kiểm tra con chim với lại tube 
			pygame.mixer.pause()
			tube_velocity=0 #tốc độ ống
			bird_drop_velocity=0 #tốc độ con chim
			game_over_txt=font1.render("GameOver,Score"+str(score),True,RED)#tạo chữ 
			screen.blit(game_over_txt,(85,260)) #hiển thi
			space_txt=font.render("Press Space to continue!",True,BLUE)#tạo chữ chơi lại
			screen.blit(space_txt,(120,290)) #hiển thị
			pausing=True

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_SPACE:
				bird_drop_velocity=0
				bird_drop_velocity=bird_drop_velocity-7 # trọng lực trừ cho 7 mỗi khi nhấn nó sẽ nãy lên
				if pausing: # nhấn phím pause thì gán giá trị ban đầu để chời lại
					pygame.mixer.unpause()  
					x_bird=50
					y_bird=350
					tube1_x=400
					tube2_x=600
					tube3_x=800
					tube_velocity=2 
					score=0
					pausing=False

	pygame.display.flip()#thay đổi trên mà hình thì sẽ cập nhật
pygame.quit()#xóa dữ liệu
