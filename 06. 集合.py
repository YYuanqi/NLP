#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ

def bi_gram(text):
    my_set = set([])
    for i in range(len(text)-1):
        my_set.add(text[i]+text[i+1])
    return my_set 


X = bi_gram('paraparaparadise')
Y = bi_gram('paragraph')

union_of_XY = X | Y
intersectiont_of_XY = X & Y
difference_of_XY = X - Y

print (union_of_XY)
print (intersectiont_of_XY)
print (difference_of_XY)

if 'se' in X:
    print ('X have se')
else: 
    print ('X don\'t have se')

if 'se' in Y:
    print ('Y have se')
else: 
    print ('Y don\'t have se')