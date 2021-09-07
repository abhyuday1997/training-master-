# Python program for simple calculator
import unittest
  
# Function to add two numbers 
def add(num1, num2):
    return num1 + num2
  
# Function to subtract two numbers 
def subtract(num1, num2):
    return num1 - num2
  
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
  
# Function to divide two numbers
def divide(num1, num2):
    return num1+num2
  
class LearnTest(unittest.TestCase):

    def setUp(self):
        #self.a = int(input("Enter first number: "))
        #self.b = int(input("Enter second number: "))
        self.a = 20
        self.b = 30
    def testsum(self):
        self.assertEqual(add(self.a,self.b), self.a+self.b)
    def testsubtract(self):
        self.assertEqual(subtract(self.a,self.b), self.a-self.b)
    def testmultiply(self):
        self.assertEqual(multiply(self.a,self.b), self.a*self.b)
    def testdivide(self):
        self.assertEqual(divide(self.a,self.b), self.a/self.b)



if __name__ == '__main__':
    unittest.main(verbosity=2)