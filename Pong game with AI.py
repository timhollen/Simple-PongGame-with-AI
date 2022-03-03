import tkinter

root = tkinter.Tk()
root.resizable(height=0, width=0)

# This loop creates the background
for row in range(12):
    for column in range(20):
        board = tkinter.Label(root)
        if column == 0:
            board.config(bg='white')
        elif column == 19:
            board.config(bg='white')
        else:
            board.config(bg='black')
        board.config(height=3, width=8)
        board.grid(row=row, column=column)

# Making the player, ball and the AI
player = tkinter.Label(root)
player.config(bg='blue', height=6, width=2)

AI = tkinter.Label(root)
AI.config(bg='red', height=6, width=2)

ball = tkinter.Label(root)
ball.config(bg='blue', height=1, width=3)

game_started = False
speed_multiplier = 2
ball_x = -1
ball_y = 3

game_over = False


def MainGameloop():
    global game_started, ball_x, speed_multiplier, ball_y, game_over
    if not game_over:
        root.after(10, MainGameloop)
    if not game_started:
        ball.place(x=(root.winfo_width() / 2), y=(root.winfo_height() / 2))
        player.place(x=root.winfo_width() - 1150, y=(root.winfo_height() / 2) - 20)
        AI.place(x=root.winfo_width() - 120, y=(root.winfo_height() / 2) - 20)
        game_started = True

    if int(ball.place_info()['y']) >= root.winfo_height() - 100:
        ball_y = 3
        ball.place(x=int(ball.place_info()['x']) + ball_x * speed_multiplier, y=int(ball.place_info()['y']) - ball_y)

    elif int(ball.place_info()['y']) <= 0:
        ball_y = -3
        ball.place(x=int(ball.place_info()['x']) + ball_x * speed_multiplier, y=int(ball.place_info()['y']) - ball_y)

    else:
        ball.place(x=int(ball.place_info()['x']) + ball_x * speed_multiplier, y=int(ball.place_info()['y']) - ball_y)

    if int(ball.place_info()['x']) >= root.winfo_width() - 50:
        game_over = True

    elif int(ball.place_info()['x']) <= root.winfo_width() - 1200:
        game_over = True

    AI.place(x=int(AI.place_info()['x']), y=int(ball.place_info()['y']) - ball_y)

    if abs(int(ball.place_info()['x']) - int(AI.place_info()['x'])) < 20:
        if int(ball.place_info()['y']) - int(AI.place_info()['y']) < 20:
            ball_x -= 2
            speed_multiplier += 0.2
    if abs(int(ball.place_info()['x']) - int(player.place_info()['x'])) < 20:
        if int(ball.place_info()['y']) - int(player.place_info()['y']) <= 20:
            ball_x += 2
            speed_multiplier += 0.2


def MoveUp(event):
    global speed_multiplier
    if int(player.place_info()['y']) <= 0:
        player.place(x=int(player.place_info()['x']), y=int(player.place_info()['y']))

    else:
        player.place(x=int(player.place_info()['x']), y=int(player.place_info()['y']) - 5 * speed_multiplier)


def MoveDown(event):
    global speed_multiplier
    if int(player.place_info()['y']) >= root.winfo_height() - 100:
        player.place(x=int(player.place_info()['x']), y=int(player.place_info()['y']))
    else:
        player.place(x=int(player.place_info()['x']), y=int(player.place_info()['y']) + 5 * speed_multiplier)


root.bind('<w>', MoveUp)
root.bind('<s>', MoveDown)
root.after(5, MainGameloop)
root.mainloop()
