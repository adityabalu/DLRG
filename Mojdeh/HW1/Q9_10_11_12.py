class robot:
    def __init__(self):
        self.curPos = [0,0]
        self.curDir = [1,0]
        self.curTime = 0.0
        self.speed = 0.5

    def wait(self, time):
        self.curTime += time;

    def move_forward(self, time):
        self.curPos = [self.curPos[0]+ self.curDir[0] * 0.5*time,self.curPos[1] + self.curDir[1] * 0.5*time];

    def rotate_right(self):
        if self.curDir == [1,0]:
            self.curDir = [0,-1]
        elif self.curDir == [-1,0]:
            self.curDir = [0,1]
        elif self.curDir == [0,1]:
            self.curDir = [1,0]
        elif self.curDir == [0,-1]:
            self.curDir = [-1,0]

    def rotate_left(self):
        if self.curDir == [1,0]:
            self.curDir = [0,1]
        elif self.curDir == [-1,0]:
            self.curDir = [0,-1]
        elif self.curDir == [0,1]:
            self.curDir = [-1,0]
        elif self.curDir == [0,-1]:
            self.curDir = [1,0]

    def __repr__(self) -> str:
        return str(self.curPos)+ str(self.curDir) + str(self.curTime);


def move_square(side_length):
    r = robot()
    while(1):
        n = input("continueY/N")
        if(n == 'Y'):
            r.move_forward(1)
            if r.curPos == [0,side_length] or r.curPos == [side_length,0] or r.curPos == [0,0] or r.curPos == [side_length,side_length]:
                r.rotate_left;                        
        if(n == 'N'):
            print(repr(r));
            break;    


if __name__ == '__main__':
    move_square(1);    

