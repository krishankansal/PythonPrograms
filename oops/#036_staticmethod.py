class DemoStatic:    

    def m1(self):
        print("m1(self) called....")

    def m2(self):        
        print("m2(self) called....")
        self.m1()

    @staticmethod
    def m3():
        print("m3() called....")
        DemoStatic().m2()


DemoStatic.m3()