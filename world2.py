import math

import pygame
import random

# 初始化 Pygame
import pytmx

pygame.init()

# 设置屏幕和游戏世界的大小
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WORLD_WIDTH, WORLD_HEIGHT = 2000, 1500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Camera Example")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 定义玩家
player = pygame.Rect(400, 400, 16, 16)  # 玩家初始位置和大小
player_speed = 5

# 创建游戏对象
objects = []
for _ in range(50):  # 随机生成 50 个对象
    obj_x = random.randint(0, WORLD_WIDTH)
    obj_y = random.randint(0, WORLD_HEIGHT)
    obj_size = random.randint(10, 50)
    objects.append(pygame.Rect(obj_x, obj_y, obj_size, obj_size))

# 摄像机位置
camera_x, camera_y = 0, 0
tmx_data = pytmx.load_pygame("grass2.tmx")

def draw_map():
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)

                if tile:
                    screen.blit(tile, (x * tmx_data.tilewidth - camera_x, y * tmx_data.tileheight - camera_y))

# 更新摄像机位置
def update_camera():
    global camera_x, camera_y
    # 让摄像机跟随玩家
    camera_x = max(0, min(player.x - SCREEN_WIDTH // 2, WORLD_WIDTH - SCREEN_WIDTH))
    camera_y = max(0, min(player.y - SCREEN_HEIGHT // 2, WORLD_HEIGHT - SCREEN_HEIGHT))


# 检查某个位置是否有墙体
def check_collision(x, y):
    # 获取该位置的瓦片 ID
    dic = None
    try:
        x_pos = math.floor(x / tmx_data.tilewidth)
        y_pos = math.floor(y / tmx_data.tileheight)
        # print(x, y)
        print(x_pos, y_pos)
        dic = tmx_data.get_tile_properties(x_pos, y_pos, layer=0)
    except Exception as e:
        pass

    # print(gid)
    if dic:
        return dic['collides'] == True
    else:
        return False



# 主游戏循环
clock = pygame.time.Clock()
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取键盘输入
    keys = pygame.key.get_pressed()
    new_x, new_y = player.x, player.y

    if keys[pygame.K_UP]:
        new_y -= player_speed  # 向上移动
        if not check_collision(new_x, new_y):
            player.y = max(0, new_y - player_speed)
    if keys[pygame.K_DOWN]:
        new_y += player_speed  # 向上移动
        if not check_collision(new_x, new_y):
            player.y = min(WORLD_HEIGHT - player.height, new_y + player_speed)
    if keys[pygame.K_LEFT]:
        new_x -= player_speed  # 向左移动
        if not check_collision(new_x, new_y):
            player.x = max(0, new_x - player_speed)
    if keys[pygame.K_RIGHT]:
        new_x += player_speed  # 向左移动
        if not check_collision(new_x, new_y):
            player.x = min(WORLD_WIDTH - player.width, new_x + player_speed)

    # 更新摄像机位置
    update_camera()

    # 绘制屏幕
    screen.fill(WHITE)
    draw_map()
    # 绘制对象
    for obj in objects:
        screen_x = obj.x - camera_x
        screen_y = obj.y - camera_y
        # 只绘制在摄像机视野内的对象
        if screen_x + obj.width > 0 and screen_x < SCREEN_WIDTH and screen_y + obj.height > 0 and screen_y < SCREEN_HEIGHT:
            pygame.draw.rect(screen, BLACK, (screen_x, screen_y, obj.width, obj.height))

    # 绘制玩家
    screen_player_x = player.x - camera_x
    screen_player_y = player.y - camera_y
    pygame.draw.rect(screen, RED, (screen_player_x, screen_player_y, player.width, player.height))

    # 显示调试信息
    font = pygame.font.SysFont(None, 24)
    debug_text = f"Camera: ({camera_x}, {camera_y}) | Player: ({player.x}, {player.y})"
    text_surface = font.render(debug_text, True, BLACK)
    screen.blit(text_surface, (10, 10))

    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出 Pygame
pygame.quit()
