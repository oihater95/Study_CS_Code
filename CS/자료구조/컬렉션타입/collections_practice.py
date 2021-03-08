from collections import defaultdict
# 기본 딕셔너리
pairs = {('a', 1), ('b', 2), ('c', 3)}

# 내장 딕셔너리
d1 = {}
for key, value in pairs:
    if key not in d1:
        d1[key] = []
    d1[key].append(value)
print(d1)

# defaultdict
d2 = {}
for key, value in pairs:
    d2[key].append(value)
print(d2)

# 정렬된 딕셔너리
from collections import OrderedDict
tasks = OrderedDict()
task[1000] = '백업'
task[3543] = '스캔'
task[12] = '빌드'
print(task)

# 카운터 딕셔너리
from collections import Counter
seq = [1, 2 , 3, 5, 1, 2 , 5, 5, 2, 5, 1, 4]
seq_count = Counter(seq)
print(seq_count)