'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
规律：
    字符串从左到右比较
    1.当左数 >= 右数 ，就加上当前数(左数)
    2.当左数 <  右数，就减去当前数
    3.最后一个数，无法比较，直接加上
    
    初始int_num  = 0 
    III : ---> 第一个是1 ，第二个是1 ， 就加上1 ，int_num =1
               第二个是1   第三个是1， 在加1 ,int_num =2 
               第三个是1 ，没有第四个， 直接加 ， int_num = 3 

'''
def romanToInt(s: str) -> int:
    roam_num  = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    int_num = 0
    for i in range(len(s)-1):
        if roam_num[s[i]] >= roam_num[s[i+1]]: #1
            int_num +=roam_num[s[i]]
        else:
            int_num -= roam_num[s[i]] #2

    int_num +=roam_num[s[len(s)-1]] #3

    print(int_num)

    return int_num

if __name__ == '__main__':
    s =  'MCMXCIV'
    romanToInt(s)

