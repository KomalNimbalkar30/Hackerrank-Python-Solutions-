import re
def wrapper(f):
    def fun(l):
        pat = re.compile(r'(0|91|\+91)?(\d{5})(\d{5})')
        l = [re.sub(pat, r"+91 \2 \3", x) for x in l]
        f(l)        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


