# coding=UTF-8
import numpy as np
if __name__ == "__main__":
    f = open('./08_input.in', 'r')
    #f = open('inFile.txt', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line, dtype=int, sep=',')
        n=8
        jump=0
        map=[[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                map[i][j]=0
        x_move = [-2,-1,1,2,2,1,-1,-2]
        y_move = [-1,-2,-2,-1,1,2,2,1]
        inx=int(npyArray[0])
        iny=int(npyArray[1])
        tarx=int(npyArray[2])
        tary=int(npyArray[3])
        queue=[]
        #with queue.mutx:
            #queue.queue.clear()
        map[inx][iny]=1
        queue.append((inx,iny))
        while(len(queue)>0):
            (x,y)=queue.pop(0)
            for k in range(8):
                nx=x+int(x_move[k])
                ny=y+int(y_move[k])
                if(nx>=0 and nx<8 and ny >=0 and ny<8):
                    if(map[nx][ny]==0):
                        map[nx][ny]=map[x][y]+1
                        queue.append((nx,ny))
                if(nx==tarx and ny==tary):
                    print("To get from Point( "+str(inx)+" , "+str(iny)+" ) to Point( "+str(nx)+" , "+str(ny)+" ) takes "+str(map[nx][ny]-1)+" knight moves.")
                    #print("To get from Point( 4 , 2 ) to Point( 4 , 4 ) takes 2 knight moves.")
                    jump=1
                    break
            if(jump==1):
                break
    f.close()



