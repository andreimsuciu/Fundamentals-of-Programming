from Errors.errors import *

import time 

class Console(object):
    def __init__(self,__shipServicePlayer,__shipServiceAI,__gameService):
        self.__shipServicePlayer = __shipServicePlayer
        self.__gameService = __gameService
        self.__shipServiceAI = __shipServiceAI
        
    def printMenu(self):
        print('Possible commands:')
        print('1.help')
        print('2.exit')
        print('3.add x y length direction')
        print('4.remove <length>')
        print('5.start')
        
    def run(self):
        print('Welcome to Battleships!')
        self.printMenu()
        self.__shipServicePlayer.add_ship(2,3,2,'V')
        self.__shipServicePlayer.add_ship(4,4,3,'H')
        #self.__shipServicePlayer.add_ship(7,2,4,'H')
        commands={"add":self.__uiAdd,"remove":self.__uiRemove}
        while True:
            cmd=input(">>")
            params = cmd.split()
            if cmd == "exit":
                return
            elif cmd == "help":
                self.printMenu()
            elif cmd == "start":
                self.__uiStart()
            else:
                try:
                    if params[0] in commands:
                        try:
                            commands[params[0]](params[1:])
                        except ValueError:
                            print("invalid numeric value given!")
                        except RepositoryError as re:
                            print("Repository Error:")
                            print(re)
                        except ValidError as ve:
                            print("Validation Error:")
                            print(ve)
                    else:
                        print("invalid command!")

                except IndexError:
                    print("That was not a command!")
            
    def __uiAdd(self,params):
        if len(params) != 4:
            print('invalid no of params!')
            return
        if (len(self.__gameService.shipRepoPlayer)==3):
            print('You already have the 3 ships ready to go!')
            return
        x=int(params[0])
        y=int(params[1])
        x-=1
        y-=1
        length=int(params[2])
        direction=params[3]
        self.__shipServicePlayer.add_ship(x,y,length,direction)
        
    def __uiRemove(self,params):
        if len(params) != 1:
            print('invalid no of params!')
            return
        length=int(params[0])
        self.__shipServicePlayer.remove_ship(length)
    
    """
    Here starts the game
    """
    def printMenuStart(self):
        print('Possible commands:')
        print('1.help')
        print('2.exit')
        print('3.boards')
        print('4.hit <column><row>')
        print('5.')
        
    def __uiPrintBoard(self,board):
        print (" ", end="")
        for i in range(8):
            i+=64+1
            c=chr(i)
            print ("  " + c + "  ",end="")
        print ("")

        for i in range(8):
            print(str(i+1) + "  ",end="")
            for j in range(8):
                print(board[i][j],end=" |  ")
            print(' ')
            print('-----------------------------------------')
        print("")
        
    def __uiPrintBoards(self, boardPlayer,boardAI):
        print('Player board:')
        self.__uiPrintBoard(boardPlayer)
        print('AI board:')
        self.__uiPrintBoard(boardAI)
    
    def __uiAi_place_ships(self):
        length=1
        l=0
        while True:
            length+=1
            x,y,direction=self.__gameService.ai_place_ships()
            
            try:
                self.__shipServiceAI.add_ship(x,y,length,direction)
            except:
                pass
            if (len(self.__gameService.shipRepoAI) == l and l<4):
                length-=1
            else:
                l+=1
            if l>2:
                return
    
    def __uiHit(self,params):
        if len(params) != 1:
            print('invalid no of params!')
            return
        if len(params[0]) != 2:
            print('invalid coordinates!')
            return
        y=params[0][0]
        x=int(params[0][1])
        
        y=ord(y)-64
        if x>8 or x<1 or y>8 or y<1:
            print("Invalid coordinates!")
        try:
            ship=self.__gameService.player_hit(x,y)
            if ship=="D" or ship =="C" or ship =="B":
                print("Player hits!")
            elif ship=="d" or ship =="c" or ship =="b":
                print(ship+" destroyed by player!") 
            elif ship=="N":
                print("Thats a miss!")
            if self.__gameService.check_win_player():
                self.__uiWinPlayer()
            print("AI thinking... ")
            time.sleep(1.5)
            ship=self.__gameService.ai_hit()
            if ship=="D" or ship =="C" or ship =="B":
                print("AI hits!")
            elif ship=="d" or ship =="c" or ship =="b":
                print(ship+" destroyed by AI!") 
            elif ship=="N":
                print("AI misses!")
            if self.__gameService.check_win_ai():
                self.__uiWinAI()    
        except GameServiceError as gs:
            print(gs)
            return
        
    def __uiWinPlayer(self):
        print("You win! Play again? (Y/N)")
    def __uiWinAI(self):
        print("AI wins! Play again? (Y/N)")
                
                
    def __uiStart(self):
        if len(self.__gameService.shipRepoPlayer)<3:
            print('Going into battle without all ships? Are you mad?')
            return
        elif len(self.__gameService.shipRepoPlayer)>3:
            print('Smth is wrong. You shouldnt have that many ships!')
            return 
        boardPlayer=self.__gameService.hitRepoPlayer
        boardAI=self.__gameService.hitRepoAI
        
        self.__uiAi_place_ships()
        self.printMenuStart()
        print('Enemy placed its ships! Sink them!')
        
        commands={"hit":self.__uiHit}
        while True:
            cmd=input(">>")
            params = cmd.split()
            if cmd == "exit":
                return
            elif cmd == "help":
                self.printMenuStart()
            elif cmd == "boards":
                self.__uiPrintBoards(boardPlayer,boardAI)
            elif params[0] in commands:
                try:
                    commands[params[0]](params[1:])
                except ValueError:
                    print("invalid numeric value given!")
                except RepositoryError as re:
                    print("Repository Error:")
                    print(re)
                except ValidError as ve:
                    print("Validation Error:")
                    print(ve)
            else:
                print("invalid command!")