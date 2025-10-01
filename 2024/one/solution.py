import re
def get_total_distance(location_lists):
    l1,l2=[],[]
    for line in location_lists.splitlines():
        a,b = re.split(r'\s+', line)
        l1.append(a)
        l2.append(b)
    # l1=sorted(l1)
    # l2=sorted(l2)
    # result = 0
    # for i,j in zip(l1,l2):
    #     result += abs(int(i)-int(j))
    # return result
    hashMap = {}
    for i in l2:
        if i in hashMap:
            hashMap[i]+=1
        else:
            hashMap[i]=1
    similarity_score=0
    for i in l1:
        if i in hashMap:
            similarity_score+=int(i)*hashMap[i]
    return similarity_score



with open('input.txt', 'r') as f:
    data = f.read()

print(get_total_distance(data))
