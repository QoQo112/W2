# Request_01
print("Request: 01")

def calculate(min, max, step):
    sum = 0 
    while min <= max: 
        sum += min
        min += step    
    print(sum) 
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

print("-------------------------")
# Request_02
print("Request: 02")

def avg(data):
    sum = 0
    count = 0
    length = len(data["employees"])
    for i in range(0, length):
        if (data["employees"][i]["manager"]) == False:
            sum += data["employees"][i]["salary"]
            count += 1  
    print(int(sum/count))
avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) # 呼叫 avg 函式
print("-------------------------")
# Request_03
print("Request: 03")

def func(a):
    def F(b, c):
        print (a + b * c)
    return F
    

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果
print("-------------------------")

# Request_04
print("Request: 04")

def maxProduct(nums):
    result = 0 
    data = []
    length = len(nums)
    for n in range(0, length):
        for n1 in range(n+1, length):
            result = nums[n] * nums[n1]
            data.append(result)
    max = data[0]
    for n in range(1, len(data)):
        if max <= data[n]:
            max = data[n]
    print(max)   
            
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

print("-------------------------")
# Request_05
print("Request: 05")

def twoSum(nums, target):
    p = []
    length = len(nums)
    for n in range(0, length):
        for n1 in range(1, length):
            if (nums[n] + nums[n1]) == target:
                p.append(n)
                p.append(n1)
    return p

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

print("-------------------------")
# Request_06
print("Request: 06")

def maxZeros(nums):
    length = len(nums) 
    result = 0
    count = 0  
    for i in range(0, length):
        if nums[i] != 0:
            count = 0 
        else:  
            count += 1
        result = max(result, count)
    print(result)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
print("-------------------------")


