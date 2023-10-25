class A:
    def displayA(self):
        print("WELCOME")
class B(A):
    def displayB(self):
        print("JI aaiya nu")
class C(B):
    def displayC(self):
        print("KE kaam kaar laya ")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
