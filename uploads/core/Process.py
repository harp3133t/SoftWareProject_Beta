from process.logic import *

class Insurance:

    def __init__(self):
        self.kb=FolKB()
        self.kb.tell(expr("(Contract(Old) & Type(Tongwon)) ==> Pay(0,3000000,180,Free)"))
        self.kb.tell(expr("(Contract(Old) & Type(Ipwon)) ==> Pay(0,10000000,180,Free)"))

        self.kb.tell(expr("(Contract(New) & Type(Tongwon)) ==> Pay(5000,300000,365,30)"))
        self.kb.tell(expr("(Contract(New) & Type(Ipwon)) ==> Pay(0,50000000,90,Free)"))

        self.kb.tell(expr("(Contract(NewNew) & Type(Ipwon)) ==> Pay(0,50000000,90,Free)"))
        self.kb.tell(expr("(Contract(NewNew) & Type(Tongwon) & Paytype(Drug)) ==> Pay(8000,50000,365,180)"))
        self.kb.tell(expr("(Contract(NewNew) & Type(Tongwon) & Paytype(Drug) & Hospital(Small)) ==> Pay(10000,250000,365,180)"))
        self.kb.tell(expr("(Contract(NewNew) & Type(Tongwon) & Paytype(Drug) & Hospital(Middle)) ==> Pay(15000,250000,365,180)"))
        self.kb.tell(expr("(Contract(NewNew) & Type(Tongwon) & Paytype(Drug) & Hospital(Big)) ==> Pay(20000,250000,365,180)"))

    def tell(self,query):
##        kb.tell(expr("Contract(NewNew)"))
##        kb.tell(expr("Type(Tongwon)"))
##        kb.tell(expr("Paytype(Drug)"))
##        kb.tell(expr("Hospital(Small)"))
        self.kb.tell(expr(query))

    def ask(self,query):
        x=self.kb.ask(expr(query))
        return x
##

wb=Insurance()
wb.tell(expr("Contract(Old)"))
wb.tell(expr("Type(Tongwon)"))
x=wb.ask(expr("Pay(small,big,day,count)"))
print x
