class A:
    def displayA(self):
        print("WELCOME")
class B():
    def displayB(self):
        print("JI aaiya nu")
class C(A,B):
    def displayC(self):
        print("KE kaam kaar laya ")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()