**Python排序sort函数**
data.sort(key=lambda x: x[0])
意思就是按照这个data的x[0]项排序，在这里x就是每个interval，x[0]就是st
​
**Python规范**
不能这样定义：st = interval[0], ed = interval[1]
只能这样：
st = interval[0]
ed = interval[1]