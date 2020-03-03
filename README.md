# Middleware
中间件 - 日常小工具

* [Python – 如何通过多个字符替换（replace）字符串的方法](doc/mul_replace.md)
* [Python – 如何通过多个字符分割（split）字符串的方法](doc/mul_split.md)

> 添加 子项目 使用说明

```py
# 自定义包(添加：中间件)
sys.path.append(os.getcwd())
from Middleware.tool import 工具类的方法名

# 添加子项目（自动下载）
git submodule add https://github.com/apachecn/Middleware.git
# 如果文件删除了，就重新下载
git submodule add --force https://github.com/apachecn/Middleware.git

git remote rename <old> <new>
git remote remove origin
git remote add origin https://github.com/apachecn/Middleware.git

# 如果要修改，或者更新，和 git remote 操作一模一样
cd Middleware/
git pull origin master
```
