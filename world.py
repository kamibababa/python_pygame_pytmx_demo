# import random
# import pygame
# import pytmx
#
# pygame.init()
#
# # 设置窗口大小
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# WORLD_WIDTH, WORLD_HEIGHT = 1600, 1600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Pytmx Demo")
#
#
# tmx_data = pytmx.load_pygame("grass2.tmx")  # 将 'your_map.tmx' 替换为你的文件路径
# player_x = 250
# player_y = 350
# player_speed = 5  # 玩家速度
#
# # 定义颜色
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
#
# def draw_map():
#     for layer in tmx_data.visible_layers:
#         if isinstance(layer, pytmx.TiledTileLayer):
#             for x, y, gid in layer:
#                 tile = tmx_data.get_tile_image_by_gid(gid)
#
#                 if tile:
#                     screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
#
# # 创建游戏对象
# # objects = []
# # for _ in range(50):  # 随机生成 50 个对象
# #     obj_x = random.randint(0, WORLD_WIDTH)
# #     obj_y = random.randint(0, WORLD_HEIGHT)
# #     obj_size = random.randint(10, 50)
# #     objects.append(pygame.Rect(obj_x, obj_y, obj_size, obj_size))
#
# # 摄像机位置
# camera_x, camera_y = 0, 0
#
# # 更新摄像机位置
# def update_camera():
#     global camera_x, camera_y
#     # 让摄像机跟随玩家
#     camera_x = max(0, min(player_x - SCREEN_WIDTH // 2, WORLD_WIDTH - SCREEN_WIDTH))
#     camera_y = max(0, min(player_y - SCREEN_HEIGHT // 2, WORLD_HEIGHT - SCREEN_HEIGHT))
#
# # 主游戏循环
# clock = pygame.time.Clock()
# # 游戏主循环
# running = True
# while running:
#
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         # 获取键盘输入
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         player_y = max(0, player_y - player_speed)
#     if keys[pygame.K_DOWN]:
#         player_y = min(WORLD_HEIGHT - 32, player_y + player_speed)
#     if keys[pygame.K_LEFT]:
#         player_x = max(0, player_x - player_speed)
#     if keys[pygame.K_RIGHT]:
#         player_x = min(WORLD_WIDTH - 32, player_x + player_speed)
#     # 更新摄像机位置
#     update_camera()
#     # 绘制屏幕
#     screen.fill((0,0,0))
#
#     draw_map()  # 绘制地图
#     # 绘制对象
#     # for obj in objects:
#     #     screen_x = obj.x - camera_x
#     #     screen_y = obj.y - camera_y
#     #     # 只绘制在摄像机视野内的对象
#     #     if screen_x + obj.width > 0 and screen_x < SCREEN_WIDTH and screen_y + obj.height > 0 and screen_y < SCREEN_HEIGHT:
#     #         pygame.draw.rect(screen, (0, 0, 255), (screen_x, screen_y, obj.width, obj.height))
#
#     # 绘制玩家
#     screen_player_x = player_x - camera_x
#     screen_player_y = player_y - camera_y
#     # 限制玩家位置在屏幕内
#     pygame.draw.rect(screen, (255,0,0), (screen_player_x, screen_player_y, 32, 32))
#
#     # 显示调试信息
#     font = pygame.font.SysFont(None, 24)
#     debug_text = f"Camera: ({camera_x}, {camera_y}) | Player: ({player_x}, {player_y})"
#     text_surface = font.render(debug_text, True, (0,255,0))
#     screen.blit(text_surface, (10, 10))
#
#     pygame.display.flip()  # 更新显示
#     # 控制帧率
#     clock.tick(60)
#
# pygame.quit()
