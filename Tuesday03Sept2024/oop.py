import os

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
    
    def makeStringToArray(string):
        string_array = []

        for char in string:
            string_array += char
        
        print(string_array)

    def countNumberOfArray(nums):
        result = 0
        for num in nums:
            result += num
        print(result)

    def createConnection(connection_name, host_id, network_id):
        host = format(host_id, ',').replace(',', '.', 3)
        network = format(network_id, ',').replace(',', '.', 3)
        print(connection_name, host, network)
    
    def runFile(file_url):
        splitedPath = file_url.split('.')
        fileExtension = splitedPath[len(splitedPath) - 1]
        if fileExtension == 'ts':
            os.system('npx ts-node ' + file_url)
        elif fileExtension == 'py':
            os.system('python3 ' + file_url)
        else:
            print('This type of file extesion is not supported!')
            


MyClass.runFile('/Users/raiwirawan/Desktop/PBO-Subject/Tuesday03Sept2024/test.py')