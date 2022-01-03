class Phone:    #class
    def call(self):     # call method
        print("Hello,How r U?")
    def message(self):  #message method
        print("It is Fahad")

class Honor:    #Honor class
    def light(self):    #light method
        print("On light")
    def musicplayer(self):  #musicplayer method
        print("On music")

#creat object and the method

p=Phone() #phone object
p.call() #call method in phone class
p.message() #call method in phone class

h=Honor()
h.light()
h.musicplayer()
