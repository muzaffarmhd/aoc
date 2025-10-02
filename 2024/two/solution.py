import re
def get_total_distance(location_lists):
    reports = []
    count=0
    for line in location_lists.splitlines():
        lis = re.split(r'\s+', line)
        reports.append(lis)
    def check_safe(seq):
        previous = int(seq[0])
        current = int(seq[1])
        increasing = current > previous
        n=len(seq)
        safe=False
        for i in range(1,n):
            current = int(seq[i])
            if (current > previous) == increasing:
                safe=True
            else:
                safe=False
                break
            difference = abs(current-previous)
            if (difference > 0 and difference < 4):
                safe=True
            else:
                safe=False
                break
            previous=current
        return safe
    for report in reports:
        if (check_safe(report)):
            count+=1
        else:
            for i in range(0,len(report)):
                dropped_list = [report[j] for j in range(0,len(report)) if j!=i]
                if (check_safe(dropped_list)):
                    print(f'original_list: {report}, dropped list {dropped_list} safe by removing {report[i]}')
                    count+=1
                    break
    return count
            


with open('input.txt', 'r') as f:
    data = f.read()

print(get_total_distance(data))
