import tkinter as tk

#Matrices
Sudoku_list_solved=[["9","6","5","4","2","1","7","3","8"]
                    ,["4","3","8","5","7","9","1","2","6"]
                    ,["1","2","7","6","3","8","9","4","5"]
                    ,["8","9","6","7","4","3","5","1","2"]
                    ,["7","5","4","2","1","6","3","8","9"]
                    ,["2","1","3","9","8","5","6","7","4"]
                    ,["6","8","1","3","5","4","2","9","7"]
                    ,["3","7","9","8","6","2","4","5","1"]
                    ,["5","4","2","1","9","7","8","6","3"]]
Sudoku_list_unsolved=[["9","","5","","","","","","8"]
                      ,["4","","","5","7","","1","","6"]
                      ,["","2","7","6","","","","4",""]
                      ,["","9","6","","","3","5","1","2"]
                      ,["7","","4","","1","","3","",""]
                      ,["2","1","","9","8","","","","4"]
                      ,["","8","1","","","4","","9",""]
                      ,["3","","","8","","","","5","1"]
                      ,["","","2","","","7","","6",""]]
Sudoku_list_player=[["9","","5","","","","","","8"]
                    ,["4","","","5","7","","1","","6"]
                    ,["","2","7","6","","","","4",""]
                    ,["","9","6","","","3","5","1","2"]
                    ,["7","","4","","1","","3","",""]
                    ,["2","1","","9","8","","","","4"]
                    ,["","8","1","","","4","","9",""]
                    ,["3","","","8","","","","5","1"]
                    ,["","","2","","","7","","6",""]]

#GUI
sudoku=tk.Tk()
sudoku.title("Sudoku")
sudoku.geometry("200x320")
stopwatch=tk.Label(sudoku)
stopwatch.grid(row=9,column=6,columnspan=3)
minutes=0
seconds=0

#Functions
def get():
    if len(r0_c1.get())==0:
        val=""
    else:
        val=r0_c1.get()
    Sudoku_list_unsolved[0][1]=val
    if len(r0_c3.get())==0:
        val=""
    else:
        val=r0_c3.get()
    Sudoku_list_unsolved[0][3]=val
    if len(r0_c4.get())==0:
        val=""
    else:
        val=r0_c4.get()
    Sudoku_list_unsolved[0][4]=val
    if len(r0_c5.get())==0:
        val=""
    else:
        val=r0_c5.get()
    Sudoku_list_unsolved[0][5]=val
    if len(r0_c6.get())==0:
        val=""
    else:
        val=r0_c6.get()
    Sudoku_list_unsolved[0][6]=val
    if len(r0_c7.get())==0:
        val=""
    else:
        val=r0_c7.get()
    Sudoku_list_unsolved[0][7]=val
    if len(r1_c1.get())==0:
        val=""
    else:
        val=r1_c1.get()
    Sudoku_list_unsolved[1][1]=val
    if len(r1_c2.get())==0:
        val=""
    else:
        val=r1_c2.get()
    Sudoku_list_unsolved[1][2]=val
    if len(r1_c5.get())==0:
        val=""
    else:
        val=r1_c5.get()
    Sudoku_list_unsolved[1][5]=val
    if len(r1_c7.get())==0:
        val=""
    else:
        val=r1_c7.get()
    Sudoku_list_unsolved[1][7]=val
    if len(r2_c0.get())==0:
        val=""
    else:
        val=r2_c0.get()
    Sudoku_list_unsolved[2][0]=val
    if len(r2_c4.get())==0:
        val=""
    else:
        val=r2_c4.get()
    Sudoku_list_unsolved[2][4]=val
    if len(r2_c5.get())==0:
        val=""
    else:
        val=r2_c5.get()
    Sudoku_list_unsolved[2][5]=val
    if len(r2_c6.get())==0:
        val=""
    else:
        val=r2_c6.get()
    Sudoku_list_unsolved[2][6]=val
    if len(r2_c8.get())==0:
        val=""
    else:
        val=r2_c8.get()
    Sudoku_list_unsolved[2][8]=val
    if len(r3_c0.get())==0:
        val=""
    else:
        val=r3_c0.get()
    Sudoku_list_unsolved[3][0]=val
    if len(r3_c3.get())==0:
        val=""
    else:
        val=r3_c3.get()
    Sudoku_list_unsolved[3][3]=val
    if len(r3_c4.get())==0:
        val=""
    else:
        val=r3_c4.get()
    Sudoku_list_unsolved[3][4]=val
    if len(r4_c1.get())==0:
        val=""
    else:
        val=r4_c1.get()
    Sudoku_list_unsolved[4][1]=val
    if len(r4_c3.get())==0:
        val=""
    else:
        val=r4_c3.get()
    Sudoku_list_unsolved[4][3]=val
    if len(r4_c5.get())==0:
        val=""
    else:
        val=r4_c5.get()
    Sudoku_list_unsolved[4][5]=val
    if len(r4_c7.get())==0:
        val=""
    else:
        val=r4_c7.get()
    Sudoku_list_unsolved[4][7]=val
    if len(r4_c8.get())==0:
        val=""
    else:
        val=r4_c8.get()
    Sudoku_list_unsolved[4][8]=val
    if len(r5_c2.get())==0:
        val=""
    else:
        val=r5_c2.get()
    Sudoku_list_unsolved[5][2]=val
    if len(r5_c5.get())==0:
        val=""
    else:
        val=r5_c5.get()
    Sudoku_list_unsolved[5][5]=val
    if len(r5_c6.get())==0:
        val=""
    else:
        val=r5_c6.get()
    Sudoku_list_unsolved[5][6]=val
    if len(r5_c7.get())==0:
        val=""
    else:
        val=r5_c7.get()
    Sudoku_list_unsolved[5][7]=val
    if len(r6_c0.get())==0:
        val=""
    else:
        val=r6_c0.get()
    Sudoku_list_unsolved[6][0]=val
    if len(r6_c3.get())==0:
        val=""
    else:
        val=r6_c3.get()
    Sudoku_list_unsolved[6][3]=val
    if len(r6_c4.get())==0:
        val=""
    else:
        val=r6_c4.get()
    Sudoku_list_unsolved[6][4]=val
    if len(r6_c6.get())==0:
        val=""
    else:
        val=r6_c6.get()
    Sudoku_list_unsolved[6][6]=val
    if len(r6_c8.get())==0:
        val=""
    else:
        val=r6_c8.get()
    Sudoku_list_unsolved[6][8]=val
    if len(r7_c1.get())==0:
        val=""
    else:
        val=r7_c1.get()
    Sudoku_list_unsolved[7][1]=val
    if len(r7_c2.get())==0:
        val=""
    else:
        val=r7_c2.get()
    Sudoku_list_unsolved[7][2]=val
    if len(r7_c4.get())==0:
        val=""
    else:
        val=r7_c4.get()
    Sudoku_list_unsolved[7][4]=val
    if len(r7_c5.get())==0:
        val=""
    else:
        val=r7_c5.get()
    Sudoku_list_unsolved[7][5]=val
    if len(r7_c6.get())==0:
        val=""
    else:
        val=r7_c6.get()
    Sudoku_list_unsolved[7][6]=val
    if len(r8_c0.get())==0:
        val=""
    else:
        val=r8_c0.get()
    Sudoku_list_unsolved[8][0]=val
    if len(r8_c1.get())==0:
        val=""
    else:
        val=r8_c1.get()
    Sudoku_list_unsolved[8][1]=val
    if len(r8_c3.get())==0:
        val=""
    else:
        val=r8_c3.get()
    Sudoku_list_unsolved[8][3]=val
    if len(r8_c4.get())==0:
        val=""
    else:
        val=r8_c4.get()
    Sudoku_list_unsolved[8][4]=val
    if len(r8_c6.get())==0:
        val=""
    else:
        val=r8_c6.get()
    Sudoku_list_unsolved[8][6]=val
    if len(r8_c8.get())==0:
        val=""
    else:
        val=r8_c8.get()
    Sudoku_list_unsolved[8][8]=val

def update_stopwatch():
    global minutes
    global seconds
    if seconds<59:
        seconds+=1
    elif seconds==59:
        seconds=0
        minutes+=1
    time_string="{:02d}:{:02d}".format(minutes,seconds)
    stopwatch.config(text=time_string)
    sudoku.after(1000,update_stopwatch)

def checker():
    for i in range(9):
        for j in range(9):
            if Sudoku_list_unsolved[i][j]==Sudoku_list_solved[i][j] and Sudoku_list_unsolved[i][j]!=Sudoku_list_player[i][j]:
                entry=tk.Label(sudoku,text=Sudoku_list_solved[i][j],bg="green",fg="white",width=2)
                entry.grid(row=i,column=j,padx=1,pady=1)
            elif Sudoku_list_unsolved[i][j]==Sudoku_list_solved[i][j]:
                label=tk.Label(sudoku,text=Sudoku_list_solved[i][j],bg="green",fg="white",width=2)
                label.grid(row=i,column=j,padx=1,pady=1)
    if Sudoku_list_unsolved==Sudoku_list_solved:
        game_over=tk.Label(sudoku,text="Game Over",bg="black",fg="yellow",font="bold")
        game_over.grid(row=11,column=2,rowspan=1,columnspan=5)
        minute=minutes
        second=seconds
        stopwatch=tk.Label(sudoku,text=(minute,":",second))
        stopwatch.grid(row=9,column=6,columnspan=3)
        time=tk.Label(sudoku,text=("time-",minute,":",second),bg="black",fg="yellow",font="bold")
        time.grid(row=9,column=4,rowspan=1,columnspan=5)

#Creating grid
r0_c0=tk.Label(sudoku,text=Sudoku_list_unsolved[0][0],bg="black",fg="white",width=2)
r0_c0.grid(row=0,column=0,padx=1,pady=1)
r0_c1=tk.Entry(sudoku,bg="black",fg="white",width=2)
r0_c1.grid(row=0,column=1,padx=0,pady=0)
r0_c2=tk.Label(sudoku,text=Sudoku_list_unsolved[0][2],bg="black",fg="white",width=2)
r0_c2.grid(row=0,column=2,padx=1,pady=1)
r0_c3=tk.Entry(sudoku,bg="black",fg="white",width=2)
r0_c3.grid(row=0,column=3,padx=0,pady=0)
r0_c4=tk.Entry(sudoku,bg="black",fg="white",width=2)
r0_c4.grid(row=0,column=4,padx=0,pady=0)
r0_c5=tk.Entry(sudoku,bg="black",fg="white",width=2)
r0_c5.grid(row=0,column=5,padx=0,pady=0)
r0_c6=tk.Entry(sudoku,bg="black",fg="white",width=2)
r0_c6.grid(row=0,column=6,padx=0,pady=0)
r0_c7=tk.Entry(sudoku,bg="black",fg="white",width=2)
r0_c7.grid(row=0,column=7,padx=0,pady=0)
r0_c8=tk.Label(sudoku,text=Sudoku_list_unsolved[0][8],bg="black",fg="white",width=2)
r0_c8.grid(row=0,column=8,padx=1,pady=1)
r1_c0=tk.Label(sudoku,text=Sudoku_list_unsolved[1][0],bg="black",fg="white",width=2)
r1_c0.grid(row=1,column=0,padx=1,pady=1)
r1_c1=tk.Entry(sudoku,bg="black",fg="white",width=2)
r1_c1.grid(row=1,column=1,padx=0,pady=0)
r1_c2=tk.Entry(sudoku,bg="black",fg="white",width=2)
r1_c2.grid(row=1,column=2,padx=0,pady=0)
r1_c3=tk.Label(sudoku,text=Sudoku_list_unsolved[1][3],bg="black",fg="white",width=2)
r1_c3.grid(row=1,column=3,padx=1,pady=1)
r1_c4=tk.Label(sudoku,text=Sudoku_list_unsolved[1][4],bg="black",fg="white",width=2)
r1_c4.grid(row=1,column=4,padx=1,pady=1)
r1_c5=tk.Entry(sudoku,bg="black",fg="white",width=2)
r1_c5.grid(row=1,column=5,padx=0,pady=0)
r1_c6=tk.Label(sudoku,text=Sudoku_list_unsolved[1][6],bg="black",fg="white",width=2)
r1_c6.grid(row=1,column=6,padx=1,pady=1)
r1_c7=tk.Entry(sudoku,bg="black",fg="white",width=2)
r1_c7.grid(row=1,column=7,padx=0,pady=0)
r1_c8=tk.Label(sudoku,text=Sudoku_list_unsolved[1][8],bg="black",fg="white",width=2)
r1_c8.grid(row=1,column=8,padx=1,pady=1)
r2_c0=tk.Entry(sudoku,bg="black",fg="white",width=2)
r2_c0.grid(row=2,column=0,padx=0,pady=0)
r2_c1=tk.Label(sudoku,text=Sudoku_list_unsolved[2][1],bg="black",fg="white",width=2)
r2_c1.grid(row=2,column=1,padx=1,pady=1)
r2_c2=tk.Label(sudoku,text=Sudoku_list_unsolved[2][2],bg="black",fg="white",width=2)
r2_c2.grid(row=2,column=2,padx=1,pady=1)
r2_c3=tk.Label(sudoku,text=Sudoku_list_unsolved[2][3],bg="black",fg="white",width=2)
r2_c3.grid(row=2,column=3,padx=1,pady=1)
r2_c4=tk.Entry(sudoku,bg="black",fg="white",width=2)
r2_c4.grid(row=2,column=4,padx=0,pady=0)
r2_c5=tk.Entry(sudoku,bg="black",fg="white",width=2)
r2_c5.grid(row=2,column=5,padx=0,pady=0)
r2_c6=tk.Entry(sudoku,bg="black",fg="white",width=2)
r2_c6.grid(row=2,column=6,padx=0,pady=0)
r2_c7=tk.Label(sudoku,text=Sudoku_list_unsolved[2][7],bg="black",fg="white",width=2)
r2_c7.grid(row=2,column=7,padx=1,pady=1)
r2_c8=tk.Entry(sudoku,bg="black",fg="white",width=2)
r2_c8.grid(row=2,column=8,padx=0,pady=0)
r3_c0=tk.Entry(sudoku,bg="black",fg="white",width=2)
r3_c0.grid(row=3,column=0,padx=0,pady=0)
r3_c1=tk.Label(sudoku,text=Sudoku_list_unsolved[3][1],bg="black",fg="white",width=2)
r3_c1.grid(row=3,column=1,padx=1,pady=1)
r3_c2=tk.Label(sudoku,text=Sudoku_list_unsolved[3][2],bg="black",fg="white",width=2)
r3_c2.grid(row=3,column=2,padx=1,pady=1)
r3_c3=tk.Entry(sudoku,bg="black",fg="white",width=2)
r3_c3.grid(row=3,column=3,padx=0,pady=0)
r3_c4=tk.Entry(sudoku,bg="black",fg="white",width=2)
r3_c4.grid(row=3,column=4,padx=0,pady=0)
r3_c5=tk.Label(sudoku,text=Sudoku_list_unsolved[3][5],bg="black",fg="white",width=2)
r3_c5.grid(row=3,column=5,padx=1,pady=1)
r3_c6=tk.Label(sudoku,text=Sudoku_list_unsolved[3][6],bg="black",fg="white",width=2)
r3_c6.grid(row=3,column=6,padx=1,pady=1)
r3_c7=tk.Label(sudoku,text=Sudoku_list_unsolved[3][7],bg="black",fg="white",width=2)
r3_c7.grid(row=3,column=7,padx=1,pady=1)
r3_c8=tk.Label(sudoku,text=Sudoku_list_unsolved[3][8],bg="black",fg="white",width=2)
r3_c8.grid(row=3,column=8,padx=1,pady=1)
r4_c0=tk.Label(sudoku,text=Sudoku_list_unsolved[4][0],bg="black",fg="white",width=2)
r4_c0.grid(row=4,column=0,padx=1,pady=1)
r4_c1=tk.Entry(sudoku,bg="black",fg="white",width=2)
r4_c1.grid(row=4,column=1,padx=0,pady=0)
r4_c2=tk.Label(sudoku,text=Sudoku_list_unsolved[4][2],bg="black",fg="white",width=2)
r4_c2.grid(row=4,column=2,padx=1,pady=1)
r4_c3=tk.Entry(sudoku,bg="black",fg="white",width=2)
r4_c3.grid(row=4,column=3,padx=0,pady=0)
r4_c4=tk.Label(sudoku,text=Sudoku_list_unsolved[4][4],bg="black",fg="white",width=2)
r4_c4.grid(row=4,column=4,padx=1,pady=1)
r4_c5=tk.Entry(sudoku,bg="black",fg="white",width=2)
r4_c5.grid(row=4,column=5,padx=0,pady=0)
r4_c6=tk.Label(sudoku,text=Sudoku_list_unsolved[4][6],bg="black",fg="white",width=2)
r4_c6.grid(row=4,column=6,padx=1,pady=1)
r4_c7=tk.Entry(sudoku,bg="black",fg="white",width=2)
r4_c7.grid(row=4,column=7,padx=0,pady=0)
r4_c8=tk.Entry(sudoku,bg="black",fg="white",width=2)
r4_c8.grid(row=4,column=8,padx=0,pady=0)
r5_c0=tk.Label(sudoku,text=Sudoku_list_unsolved[5][0],bg="black",fg="white",width=2)
r5_c0.grid(row=5,column=0,padx=1,pady=1)
r5_c1=tk.Label(sudoku,text=Sudoku_list_unsolved[5][1],bg="black",fg="white",width=2)
r5_c1.grid(row=5,column=1,padx=1,pady=1)
r5_c2=tk.Entry(sudoku,bg="black",fg="white",width=2)
r5_c2.grid(row=5,column=2,padx=0,pady=0)
r5_c3=tk.Label(sudoku,text=Sudoku_list_unsolved[5][3],bg="black",fg="white",width=2)
r5_c3.grid(row=5,column=3,padx=1,pady=1)
r5_c4=tk.Label(sudoku,text=Sudoku_list_unsolved[5][4],bg="black",fg="white",width=2)
r5_c4.grid(row=5,column=4,padx=1,pady=1)
r5_c5=tk.Entry(sudoku,bg="black",fg="white",width=2)
r5_c5.grid(row=5,column=5,padx=0,pady=0)
r5_c6=tk.Entry(sudoku,bg="black",fg="white",width=2)
r5_c6.grid(row=5,column=6,padx=0,pady=0)
r5_c7=tk.Entry(sudoku,bg="black",fg="white",width=2)
r5_c7.grid(row=5,column=7,padx=0,pady=0)
r5_c8=tk.Label(sudoku,text=Sudoku_list_unsolved[5][8],bg="black",fg="white",width=2)
r5_c8.grid(row=5,column=8,padx=1,pady=1)
r6_c0=tk.Entry(sudoku,bg="black",fg="white",width=2)
r6_c0.grid(row=6,column=0,padx=0,pady=0)
r6_c1=tk.Label(sudoku,text=Sudoku_list_unsolved[6][1],bg="black",fg="white",width=2)
r6_c1.grid(row=6,column=1,padx=1,pady=1)
r6_c2=tk.Label(sudoku,text=Sudoku_list_unsolved[6][2],bg="black",fg="white",width=2)
r6_c2.grid(row=6,column=2,padx=1,pady=1)
r6_c3=tk.Entry(sudoku,bg="black",fg="white",width=2)
r6_c3.grid(row=6,column=3,padx=0,pady=0)
r6_c4=tk.Entry(sudoku,bg="black",fg="white",width=2)
r6_c4.grid(row=6,column=4,padx=0,pady=0)
r6_c5=tk.Label(sudoku,text=Sudoku_list_unsolved[6][5],bg="black",fg="white",width=2)
r6_c5.grid(row=6,column=5,padx=1,pady=1)
r6_c6=tk.Entry(sudoku,bg="black",fg="white",width=2)
r6_c6.grid(row=6,column=6,padx=0,pady=0)
r6_c7=tk.Label(sudoku,text=Sudoku_list_unsolved[6][7],bg="black",fg="white",width=2)
r6_c7.grid(row=6,column=7,padx=1,pady=1)
r6_c8=tk.Entry(sudoku,bg="black",fg="white",width=2)
r6_c8.grid(row=6,column=8,padx=0,pady=0)
r7_c0=tk.Label(sudoku,text=Sudoku_list_unsolved[7][0],bg="black",fg="white",width=2)
r7_c0.grid(row=7,column=0,padx=1,pady=1)
r7_c1=tk.Entry(sudoku,bg="black",fg="white",width=2)
r7_c1.grid(row=7,column=1,padx=0,pady=0)
r7_c2=tk.Entry(sudoku,bg="black",fg="white",width=2)
r7_c2.grid(row=7,column=2,padx=0,pady=0)
r7_c3=tk.Label(sudoku,text=Sudoku_list_unsolved[7][3],bg="black",fg="white",width=2)
r7_c3.grid(row=7,column=3,padx=1,pady=1)
r7_c4=tk.Entry(sudoku,bg="black",fg="white",width=2)
r7_c4.grid(row=7,column=4,padx=0,pady=0)
r7_c5=tk.Entry(sudoku,bg="black",fg="white",width=2)
r7_c5.grid(row=7,column=5,padx=0,pady=0)
r7_c6=tk.Entry(sudoku,bg="black",fg="white",width=2)
r7_c6.grid(row=7,column=6,padx=0,pady=0)
r7_c7=tk.Label(sudoku,text=Sudoku_list_unsolved[7][7],bg="black",fg="white",width=2)
r7_c7.grid(row=7,column=7,padx=1,pady=1)
r7_c8=tk.Label(sudoku,text=Sudoku_list_unsolved[7][8],bg="black",fg="white",width=2)
r7_c8.grid(row=7,column=8,padx=1,pady=1)
r8_c0=tk.Entry(sudoku,bg="black",fg="white",width=2)
r8_c0.grid(row=8,column=0,padx=0,pady=0)
r8_c1=tk.Entry(sudoku,bg="black",fg="white",width=2)
r8_c1.grid(row=8,column=1,padx=0,pady=0)
r8_c2=tk.Label(sudoku,text=Sudoku_list_unsolved[8][2],bg="black",fg="white",width=2)
r8_c2.grid(row=8,column=2,padx=1,pady=1)
r8_c3=tk.Entry(sudoku,bg="black",fg="white",width=2)
r8_c3.grid(row=8,column=3,padx=0,pady=0)
r8_c4=tk.Entry(sudoku,bg="black",fg="white",width=2)
r8_c4.grid(row=8,column=4,padx=0,pady=0)
r8_c5=tk.Label(sudoku,text=Sudoku_list_unsolved[8][5],bg="black",fg="white",width=2)
r8_c5.grid(row=8,column=5,padx=1,pady=1)
r8_c6=tk.Entry(sudoku,bg="black",fg="white",width=2)
r8_c6.grid(row=8,column=6,padx=0,pady=0)
r8_c7=tk.Label(sudoku,text=Sudoku_list_unsolved[8][7],bg="black",fg="white",width=2)
r8_c7.grid(row=8,column=7,padx=1,pady=1)
r8_c8=tk.Entry(sudoku,bg="black",fg="white",width=2)
r8_c8.grid(row=8,column=8,padx=0,pady=0)

#Buttons
save=tk.Button(sudoku,text="Save",command=get)
check=tk.Button(sudoku,text="Check",command=checker)
save.grid(row=9,column=0,columnspan=2)
check.grid(row=10,column=0,columnspan=2)
update_stopwatch()
sudoku.mainloop()
