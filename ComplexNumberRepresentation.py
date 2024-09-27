"""
Create a Python class named `ComplexNumber` to represent complex numbers.

Theory:
A complex number is a number that comprises a real part and an imaginary part.
It is typically written in the form a + bi, where 'a' is the real part,
and 'b' is the imaginary part, and 'i' is the imaginary unit (√-1).

Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Comparison (==, !=)

Test Cases:
Test Case 1:
complex1 = ComplexNumber(3, 4)
complex2 = ComplexNumber(1, -2)
assert str(complex1) == "3+4i"
assert str(complex2) == "1-2i"
assert str(complex1 + complex2) == "4+2i"
assert str(complex1 - complex2) == "2+6i"
assert str(complex1 * complex2) == "11-2i"
assert str(complex1 / complex2) == "-1.0+2.5i"
assert complex1 != complex2

Test Case 2:
complex3 = ComplexNumber(-2, 5)
complex4 = ComplexNumber(2, 3)
assert str(complex3) == "-2+5i"
assert str(complex4) == "2+3i"
assert str(complex3 + complex4) == "0+8i"
assert str(complex3 - complex4) == "-4+2i"
assert str(complex3 * complex4) == "-16-1i"
assert str(complex3 / complex4) == "1.0+i"
assert complex3 != complex4
"""

class ComplexNumber:
    def __init__(self,num1,num2):
        self.real=float(num1)
        self.img=float(num2)
       

    def __str__(self) -> str:
        if self.real==0:
            return f"{self.img}j"
        elif self.img>0:
            return f"{self.real} + {self.img}j"
        else:
            return f"{self.real} - {self.img}j"
         
    def conjugate(self):
        return ComplexNumber(self.real,-1*self.img)

    def __add__(self,other):
        realNumber=self.real+other.real
        imgNumber=self.img+other.img

        ans=ComplexNumber(realNumber,imgNumber)

        return ans
    
    def __sub__(self,other):
        realNumber=self.real-other.real
        imgNumber=self.img-other.img

        ans=ComplexNumber(realNumber,imgNumber)

        return ans
    
    def __mul__(self,other):
        realNumber=self.real*other.real-self.img*other.img
        imgNumber=self.real*other.img+other.real*other.img

        ans=ComplexNumber(realNumber,imgNumber)

        return ans
    
    def __truediv__(self,other):
    
        dem=other.real**2-other.img**2
        

        ans=self*ComplexNumber(other.real/dem,(-1*other.img)/dem)

        return ans
    
    def  __eq__(self, other) -> bool:
        return (self.real==other.real) and (self.img==other.img)
    


cn1=ComplexNumber(3,4)
print(cn1)
cn2=ComplexNumber(4,8)
print(cn2)
print(cn1+cn2)
print(cn1-cn2)
print(cn1*cn2)
print(cn1/cn2)
print(cn1==cn2)


