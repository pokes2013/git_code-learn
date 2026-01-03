# web前端学习笔记

## 1、html架构

html 根标签
head 头标签
title 标题标签
body 主体标签

```html
<!DOCTYPE heml>
<html>
   <head>
    <title>01.HTML骨架</title>
	<meta charset="UTF-8">
   </head>
<body>   
html    根标签</br>
head    头标签</br>
title   标题标签</br>
body    主体标签</br>

</body>
</html>
```

### 定义网页编码

```
<meta charset="UTF-8">
```

## 2、文字及段落处理

### hr横线标签

```
<hr>
```

### br换行标签

```
<br>
```

### 注释标签

不仅可以注释内容，也可以注释代码

```
<!--内容-->
```

### 标题标签

```
<h1>内容</h1>
<h2>内容</h2>
<h3>内容</h3>
<h4>内容</h4>
<h5>内容</h5>
<h6>内容</h6>
```

### 标记位段落

```
<p>内容</p>
```

### pre标签

段落标签保持原来格式

### 正文处理

#### 文字加粗

```
<b>内容</b>
<strong>内容</strong>
```

#### 文字斜体

```
<i>内容</i>
<em>内容</em>
```

#### 文字下划线

```
<ins>内容</ins>
<u>内容</u>
```

#### 文字属性

```
<font color="red" size="5">我是红色文字</font>

color="red"  颜色
size="5"     大小
```

#### 文字删除标签

```
原价<del>100</del>  ，或者<s>100</s>
现价99
```

#### 文字上标

```
<sup>2</sup>   
```

### 显示空格

```
&nbsp;
```

显示代码的实体

```
&amp;用来显示代码的实体
```



## 3、图片及超链接

图片

```
<img src="img/xuexi01.png" title="鼠标划上去的提示文字" alt="图片加载失败后的文字" width="556px"></br>
```

超链接

```
<a href="http://www.baidu.com" target="_blank" color="#FF0000" >百度网站</a></br>

target="_blank"  在新的窗口打开
```





## 4、列表项目及表格

### 文字列表

```
		<ol>
			<li>ctrl+/ 注释代码</li>
			<li>ctrl+y 恢复撤销</li>
			<li>ctrl+x 剪切</li>
			<li>ctrl+z 撤销</li>
			<li>ctrl+c 复制</li>
			<li>ctrl+p 在当前项目查找文件</li>
			<li>ctrl+f 在当前文件查找字符串</li>
			<li>ctrl+alt+f  在当前目录查找字符串</li>
			<li>ctrl+k 格式化代码</li>
			<li>ctrl+g 跳转到某行代码</li>
			<li>ctrl+o 打开文件</li>
			<li>ctrl+alt+s 保存所有文件</li>
			<li>鼠标左键+ctrl选中多行(可进行多行修改操作)</li>
		</ol>
		
黑点样式，无需列表  	<ul>
    <ul type="disc">    实心圆，默认
    <ul type="circle">  空心圆
    <ul type="square">  实心方块

数字样式，有序列表   <ol>
    <ol type="1">   数字排序，默认
    <ol type="a">  <ol type="A">  字母排序
    <ol type="i">  <ol type="I">  罗马字母排序
```

### 表格的处理

```
<table></table>  表格
<tr></tr>   表示一行
<td></td>   表示单元格
<col>       代表一列
border="1px" 表格边框属性
cellspacing="0" 取消表格边框缝隙
align="center"  单元格对齐方式
```

#### 表格的属性

举例：

```
<h1>表格的处理</h1>
		<table border="1px" cellspacing="0">
			<col width="200px"> <!-- 第1列宽度200 -->
			<col width="200px"> <!-- 第2列宽度200 -->
			<col width="200px"> <!-- 第3列宽度200 -->
			<col width="200px"> <!-- 第4列宽度200 -->
			<col width="200px"> <!-- 第5列宽度200 -->
			<tr align="center"> <!-- 文字居中 -->
				<td></td>
				<td>初级</td>
				<td>中极</td>
				<td>高级</td>
				<td>专家</td>
			</tr>
			<tr align="center"> <!-- 文字居中 -->
				<td>标准</td>
				<td>被产品怼的说不出话</td>
				<td>跟产品互怼不相上下</td>
				<td>怼的产品没话说</td>
				<td>直接将其怼辞职</td>
			</tr>
			<tr align="center"> <!-- 文字居中 -->
				<td>用户A</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>	
			</tr>
			<tr align="center"> <!-- 文字居中 -->
				<td>用户B</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			
		</table>
```

#### 合并单元格

```
<td colspan="4"></td> <!-- 横向合并：删除其他单元格，设置其占据的单元格数量 -->
<td rowspan="5"></td> <!-- 纵向合并：先删除其他单元格，设置其占据的单元格数量 -->
```

举例：

```
<h1>表格之合并单元格</h1>
		<table border="1px" cellspacing="0">
			<col width="200px"> <!-- 第1列宽度200 -->
			<col width="200px"> <!-- 第2列宽度200 -->
			<col width="200px"> <!-- 第3列宽度200 -->
			<col width="200px"> <!-- 第4列宽度200 -->
			<col width="200px"> <!-- 第5列宽度200 -->
			<tr align="center" height="40px"> <!-- 文字居中,及行高 -->
				<td>标准</td>
				<td>初级</td>
				<td>中极</td>
				<td>高级</td>
				<td>专家</td>
			</tr>
			<tr align="center" height="40px">
				<td>用户A</td>
				<td colspan="4">横向合并</td> <!-- 横向合并：删除其他单元格，设置其占据的单元格数量 -->
			</tr>
			<tr align="center" height="40px">
				<td>用户B</td>
				<td></td>
				<td></td>
				<td></td>
				<td rowspan="5">纵向合并</td> <!-- 纵向合并：先删除其他单元格，设置其占据的单元格数量 -->
			</tr>
			<tr align="center" height="40px">
				<td>用户C</td>
				<td></td>
				<td></td>
				<td></td>
				
			</tr>
			<tr align="center" height="40px">
				<td>用户D</td>
				<td></td>
				<td></td>
				<td></td>
				
			</tr>
			<tr align="center" height="40px">
				<td>用户E</td>
				<td></td>
				<td></td>
				<td></td>
				
			</tr>
			<tr align="center" height="40px">
				<td>用户F</td>
				<td></td>
				<td></td>
				<td></td>
				
			</tr>
		</table>
```

<col width="200px"> <!-- 第1列宽度200 -->

当列比较多的时候，我们可以使用列分组

```
<col width="200px"> <!-- 第1列宽度200 -->
<col width="200px"> <!-- 第2列宽度200 -->
<col width="200px"> <!-- 第3列宽度200 -->
<col width="200px"> <!-- 第4列宽度200 -->
<col width="200px"> <!-- 第5列宽度200 -->
<col width="700px"> <!-- 第7列宽度700 -->

等价于

<colgroup span="5" width="200px">
<colgroup span="1" width="700px">
```

