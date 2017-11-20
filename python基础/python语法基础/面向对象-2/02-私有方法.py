class Msg:
    def __send_msg(self):
        print("Sending...")
        
    def send_msg(self, remain):
        if remain > 1000:
            self.__send_msg()
        else:
            print("Plz add money~")
            
m = Msg()
m.send_msg(90)
m.send_msg(2000)
