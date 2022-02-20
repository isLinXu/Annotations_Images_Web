# Annotations_Images_Web

show your Annotations in JPEGImages | 在JPEG图像中显示注释信息



---

## 一、项目介绍

或许你手头上拿到一份数据集，这个数据集可能是网络收集的，也可能是自己标注整理的。
假设目前已经做好数据清洗等工作，你下一步就打算开始进行训练。
在正式开始之前，你也许将对于这些数据重新进行一个审查和分析，
这时候就需要将数据集中对应的图像文件和标注文件进行一个标注信息的显示，
因此，就考虑开发设计一个类似的数据集显示分析小工具。



### 1.1 项目展示

参考了一些开源的代码，也几经辗转，终于得到了还算勉强的效果。
结果如下：

#### 1.1.1 主界面

![src_1](web_src/src_1.jpg)

#### 1.1.2 实际效果

![src_2](/home/linxu/Documents/MyGithub/Annotations_Images_Web/web_src/src_2.jpg)



## 二、运行方式

### 2.1  安装要求

- django == 2.0

- opencv-python

  

### 2.2 运行

```shell
git clone https://github.com/isLinXu/Annotations_Images_Web.git
```

```shell
cd Annotations_Images_Web
```

```shell
python manage.py migrate
```

```shell
python manage.py runserver
```



