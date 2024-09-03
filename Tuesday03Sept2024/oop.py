class MyClass:
    def oddOrEven(num):
        if num % 2 == 0:
            print("The number which is", num, "is even")
        else:
            print("The number which is", num, "is odd")

    def findString(string, target):
        if not(isinstance(string, str)) or not(isinstance(target, str)):
            print('Variables are needs to be string')
            return
        
        if string in target:
            print("The", string, "is in", target)
        else:
            print("The", string, "is not in", target)

    def printArray(arr):
        for item in arr:
            print(item)



MyClass.printArray([9,8,8, 'sdfs','sew'])