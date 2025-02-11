
#region Binary and Bitwise Operations
#operations
# x & y     - AND         (0b1010 & 0b1100 = 0b1000)
# x | y     - OR          (0b1010 | 0b1100 = 0b1110)
# x ^ y     - XOR         (0b1010 ^ 0b1100 = 0b0110)
# ~x        - NOT         (~0b1010 = 0b0101)
# x << y    - left shift  (0b1010 << 2 = 0b101000)
# x >> y    - right shift (0b1010 >> 2 = 0b10)

#example 1
x = 0b1010 # 10/A
y = 0b1100 # 12/C
z = x & y
print(z) # 8 = 0b1000

#example 2
nums = [1,2,3]
vals = nums
print(nums, vals)
del vals[1:2]
print(nums, vals)

def foo(x):
    global y
    y = x * x
    return y

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
    print(v)
    v = dictionary[v]
    
print(v)