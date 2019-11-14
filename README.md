# cps_20191115

## 準備
### python

```
$ python --version
$ python3 --version
```

Pythonなら2.7.9以上、Python3なら3.4以上あると望ましい

基本的にpythonでもOKだが、
どうしてもpythob3が欲しい方は、↓

https://www.python.jp/install/windows/install_py3.html

### pip
brewが入ってる人は、
```
$ brew install pip
```

無い人は、
```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python get-pip.py
```

## install

準備が終了したら、

```
$ pip install -r requirements.txt
```
