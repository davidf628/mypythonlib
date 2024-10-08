
import sys, math
sys.path.append('../mypythonlib')
import number


def test():
    test_isNumber()
    test_isInt()
    test_isFloat()

def test_isNumber():
    print(f'8 => {number.isNumber(8)}')
    print(f'10.3 => {number.isNumber(10.3)}')
    print(f'"25" => {number.isNumber("25")}')
    print(f'math.pi => {number.isNumber(math.pi)}')
    print(f'"s" => {number.isNumber("s")}')
    print(f'[1, 2] => {number.isNumber([1, 2])}')
    print(f'"*" => {number.isNumber("*")}')
    print(f'None => {number.isNumber(None)}')


def test_isInt():
    x = 13
    print(f'x == 13 => {number.isInt(x)}')
    print(f'8 => {number.isInt(8)}')
    print(f'10.3 => {number.isInt(10.3)}')
    print(f'-25 => {number.isInt(-25)}')
    print(f'0 => {number.isInt(0)}')
    print(f'11/3 => {number.isInt(11/3)}')
    print(f'20/5 => {number.isInt(20/5)}')
    print(f'math.pi => {number.isInt(math.pi)}')
    print(f'"s" => {number.isInt("s")}')
    print(f'[1, 2] => {number.isInt([1, 2])}')
    print(f'"*" => {number.isInt("*")}')
    print(f'None => {number.isInt(None)}')    

def test_isFloat():
    x = 13
    print(f'x == 13 => {number.isFloat(x)}')
    print(f'8 => {number.isFloat(8)}')
    print(f'10.3 => {number.isFloat(10.3)}')
    print(f'-25 => {number.isFloat(-25)}')
    print(f'0 => {number.isFloat(0)}')
    print(f'11/3 => {number.isFloat(11/3)}')
    print(f'20/5 => {number.isFloat(20/5)}')
    print(f'math.pi => {number.isFloat(math.pi)}')
    print(f'"s" => {number.isFloat("s")}')
    print(f'[1, 2] => {number.isFloat([1, 2])}')
    print(f'"*" => {number.isFloat("*")}')
    print(f'None => {number.isFloat(None)}')  

if __name__ == '__main__':
    test()