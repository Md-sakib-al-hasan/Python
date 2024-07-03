class Exam:
    def __init__(self,name,atten,sub,mark):
        self.name=name
        self.atten=atten
        self.sub=sub
        self.mark=mark
    def total_sum (self,sub1,sub2,sub3):
        self.mark=sub1+sub2+sub3
    def state (self):
        if(self.mark >33):
            print("your are fass")
        else:
            print('your are fail')

sakib = Exam('sakib',False,'computer',0)
sakib.total_sum(50,2,25)
sakib.state()
tanha = Exam('tanha',False,'compute',0)
tanha.state()

    
