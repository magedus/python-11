
打印出100以内的斐波那契数列，使用2种方法实现


```python
a=1
b=1
print(a,end=' ')
print(b,end=' ')
while True:
    c=a+b
    if c>100:
        break
    a=b
    b=c
    print(c,end=' ')
```

    1 1 2 3 5 8 13 21 34 55 89 


```python
a=1
b=1
print(a,end=' ')
print(b,end=' ')
for i in range(100):
    c=a+b
    if c>100:
        break
    a=b
    b=c
    print(c,end=' ')
```

    1 1 2 3 5 8 13 21 34 55 89 

搭建好pytenv环境，理解local、global、shell3种方式区别，安装部署完成jupyter并运行

搭建pyenv环境与运行jupyter此次省略；；；；
pyenv global VERSION   # 全局改变python版本 【强烈不建议使用】
pyenv shell VERSION    # 改变当前shell的python版本（在当前shell始终是生效的）
pyenv local VERSION    # 切换python版本，在当前目录及其子目录下改变python版本（这个设置在我们切换到其他目录就失效）
