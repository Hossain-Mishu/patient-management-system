"""
Author:: hossain mishu
Date:5/3/2020
Follow:: https://github.com/Hossain-Mishu
"""
class Queue:
    '''#to initialized a queue constractor just make an instance of Queue class.'''
    #initializing constructor FUNCTION
    def __init__(self):
        self.items = []

    #METHODE for adding item in Queue
    def enqueue(self,item):
        self.items.append(item)

    #METHODE for geting item from Queue
    def dequeue(self):
        return self.items.pop(0)

    #METHODE for checking if Queue is empty.
    def is_empty(self):
        if self.items==[]:
            return True
        return False
def great():
    print('\n')
    print('\n')
    print('     '+'*******************<>*******************')
    print('     '+'*******************<>*******************')
    print('        '+'WELCOME TO PATIENTS MANAGMENT SYSTEM')
    print('     '+'*******************<>*******************')
    print('             '+'Created by HOSSAIN MISHU')
    print('     '+'*******************<>*******************')
    print('     '+'*******************<>*******************')
    print('\n')

if __name__=='__main__':
    import sys
    import time
    import pyttsx3

    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)

    def say(text):
        engine.say(text)
        engine.runAndWait()
    box = Queue()
    great()
    say('welcome to patients management system')
    say("fun on behalf creator hossain mishu...this funny system is implimenting Queue data structure...let's fun..")
    print('     '+'Press 1 to admite patients.')
    say('Press one to admite patients.')
    print('     '+'Press 2 to call patients.')
    say('Press two to call patients')
    print('     '+'Press 0 to close todays service.')
    say('Press zero to close todays service')
    print('     '+'*******************<>*******************')
    while True:
        n = int(input())
        print('     '+'*******************<>*******************')
        if n ==1:
            d = {}
            say('Enter token number')
            id = input('     '+'Enter token number:')
            say('Enter patients name')
            name = input('     '+'Enter patients name:')
            say('Enter counter number')
            counter = input('     '+'Enter counter number:')
            d['id']=id
            d['name']=name
            d['counter']=counter
            try:
                box.enqueue(d)
                print('\n')
                print('     '+'*******************<>*******************') 
                print('     '+'Successful!!..patients is admitted.')
                print('     '+'*******************<>*******************')
                print('\n')
                say('Successfull...patients is admited')
            except:
                say('Sorry!!!..cant admite now..servive is interrepted.')
        elif n == 2:
            if box.is_empty()==True:
                print('     '+'Can\'t get item from empty database.')
                say("Can\'t get item from empty database..")
                print('     '+'Add some patients first')
                say('add some patients first')
                print('     '+'*******************<>*******************')
                time.sleep(1)
            else:
                d = box.dequeue()
                print('     '+'id = {}'.format(d['id']))
                say('id...'+d['id'])
                print('     '+'name = {}'.format(d['name']))
                say('Name...'+d['name'])
                print('     '+'Please go to counter {}.'.format(d['counter']))
                say('Please go to counter...'+d['counter'])
                print('     '+'*******************<>*******************')
                print('\n')
                    
        elif n == 0:
            print('     '+'Thanks for being with us..please come again.')
            say('Thanks for being with us...please come again')
            print('     '+"you can download this funny system source code from github.")
            say("you can download this funny system source code from github.")
            print('     '+"Visit: https://github.com/Hossain-Mishu/patient-management-system")
            say("visit https://github.com/Hossain-Mishu/patient-management-system...use git clone command or download the zip file")
            say('have fun...')
            print('     '+'*******************<>*******************')
            time.sleep(2)
            sys.exit(1)

        else:
            print('     '+'Invalid number pressed...try again..')
            say('Invalid number pressed..try again')
            say('you can just chose betwen 1...2...or...0')
            time.sleep(1)
            print('     '+'*******************<>*******************')
