# Python – 如何通过多个字符替换（replace）字符串的方法

> 方式1:

```py
a = "eew \\ eawr,2 fd sa:21"
b = a.replace("\\", " ").replace(":", " ").replace(",", " ")
print(b)
```

> 方式2:

```
import re
a = "eew \\ eawr,2 fd sa:21"
b = re.sub(r"[:,\\ ]+", " ", a) # 前面是正则表达式，匹配多种字符（串）
print(b)
```

*** 
原文：https://blog.csdn.net/liuchengzimozigreat/article/details/85339372
