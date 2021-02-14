class triangle():
    def __init__(self, a,b,c):
        self.a= a
        self.b= b
        self.c= c

class area_triangle(triangle):
    def __init__(self,a,b,c,s):
        super().__init__(a,b,c)

    def cal_area(self):
        x=s-a
        y=s-b
        z=s-c
        f=s*x*y*z
        area=f**0.5

        return area
        



a,b,c= map(int,input('Enter 3 number').split())
s=int(input('Enter the value'))
t=area_triangle(a,b,c,s)
cal_area=t.cal_area()
print(cal_area)
