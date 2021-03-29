# 抓取目标姿态检测与定位数据集指南

## 前言

当你看到本文的时候，感谢你阅读了我的毕业论文或小论文，由于一些原因，训练源码就暂不公开，下面是训练数据集制作的过程和思路，数据集都是自己手动标注。

数据集主要基于康奈尔大学数据集(http://pr.cs.cornell.edu/sceneunderstanding/data/data.php) （ps：好像这个链接，我之前的链接丢失了，这个链接国内网没有打开），根据cornell的数据集，标注适合自己的数据集。

本数据集一共885幅单目标+97幅多目标图像（自增）。

大论文地址：https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFD202101&filename=1020974468.nh&v=TKup8cczmWtcTrGalfDLY9Yb0omdBmv5T1QLQ8oZxCRL1uxJNotjYH%25mmd2FcHZeSSjwO

## 03_dataset 文件夹介绍

03_dataset目录对应第三章的抓取目标检测的数据集，标注工具采用labelImg。

```c++
03_dataset
    |-------Annotation
    |-------JPEGImage
    |-------labels
```

JPEGImages 里面存放原始rgb图片，一共982幅，Annotation存放标注信息，labels存放标注框和类别信息。

```python
classes = ["shoe","glasses","boxes","stationery","books",
"toothbrushes","bottles","cups","plates","toothpaste","hats","tools","e_p","fruits",
"locks","umbrellas","cans","tape","f_c","f_p_b"]
```

类别一共有20各类型，如上所示。

百度云盘地址：

## 04_dataset文件夹介绍

04_dataset文件夹介绍对应第四章  区域姿态检测与定位的数据集 。

```c++
04_dataset
	|-------dataset
    		   |-----annotation_myself
    		   |-----annotation
    		   |-----Images
    		   |-----transform_annotation
	|-------draw_rect_tool
	|-------txt_tranform_with_angle
```

dataset文件夹包含所有的标注信息。

Images表示原图像，annotation_myself是根据cornell数据集标注工具标注，得到的所有可能的抓取点，每4行为一个抓取矩阵，每行两个值为一个坐标的x,y。**我的抓取框标注顺序与cornell的原有标注方向相反**。transform_anntation文件夹为将annotation_myself标注好的抓取矩阵，转换为抓取框坐标，带抓取角度label信息。

annotation_myself为draw_rect_tool工具标注的抓取矩阵坐标，不带角度label，通过txt_tranform_with_angle中提供的脚本，计算出抓取框的左上和又下坐标，并计算角度标签。transform_annotation经过脚本生成检测的标注信息annotation文件中。

**整理流程：**

```shell
Images -> annotation_myself -> transform_annotation -> annotation
```

详细拆解：

①

```shell
Images -> annotation_myself
```

使用draw_rect_tool文件夹下面的drawRect.m标注每幅图片所有可能的抓取框，文件夹data里面有示例，程序matlab写的，要安装matlab，运行程序。同时需要修改程序中的一些文件夹路径，怎么修改自己摸索。

```matlab
addpath('data/')c
imgDataDir = './../rgbd/';
annoDataDir = './../annotations/';
imgFiles = dir([imgDataDir  'rgb*']);
```

②

```shell
annotation_myself -> transform_annotation
```

步骤①已经生成了图片所有可能的抓取框，现在计算抓取框的左上角和右下角的坐标，以及角度。实现脚本在txt_tranform_with_angle文件夹下的tansfrom_to_angle.py脚本。只要配置好源文件夹和目标文件夹的路径就可以。

ps:角度计算可以根据自己的想法重新设计计算，不必拘泥。

③

```shell
transform_annotation -> annotation
```

将txt文件生成检测标注xml信息，自己百度找脚本。

百度云盘地址：



数据集可以根据自己需求进行扩充，自己改进。我这边仅提供最基础和最必须的工具和数据集。

时间较久，表达可能不完整与不清晰，欢迎直接各位补充和提出意见，也可邮箱zhangjinlingwin@163.com联系。

​																																							敬礼