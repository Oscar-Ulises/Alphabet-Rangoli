def print_rangoli(size):
    def range_char(start,stop):
        return (chr(n) for n in range(ord(start), ord(stop) + 1))
    
    letters = [ x for x in range_char('a','z')]
    
    sub_list = []
    for i in range(size):
        sub_list.append(letters[i])
        
    sub_list.reverse()
    base = 2*(n*(n-1)) -1
    
    reversed_list = []
    printed = []
    for j in range(len(sub_list)):
        printed.append(sub_list[j])
        if len(printed) == 1:
            print(printed[0].center( ((n+(n-1))*2)-1 ,'-'))
            reversed_list.append( printed[0].center( ((n+(n-1))*2)-1 ,'-') ) 
                      
        elif len(printed) >1:
            other = printed.copy()
            another = printed.copy()
            another.pop()
            another.reverse()
            other.extend(another)
            other = '-'.join(other)
            other = other.center( ((n+(n-1))*2)-1 ,'-')
            reversed_list.append(other)
            print(other)
                
    reversed_list.pop()
    reversed_list.reverse()
    
    for i in reversed_list:
        print(i)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
