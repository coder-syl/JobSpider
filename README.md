#  招聘信息爬虫  #

## 简介 ##

[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)]()
[![Conda](https://img.shields.io/conda/v/conda-forge/python.svg)]()

本项目为大创项目--基于大数据的行业预测与就业推荐服务，主要是抓取招聘网站的招聘数据

## 主要功能 ##
- 职位信息抓取
- 发送邮件，监控状态
- 定时任务

## 框架图 ##
![](https://i.imgur.com/wJNZwav.png)

## 使用工具  ##
- beautifulsoup4==4.5.1   gevent==1.1.2
- greenlet==0.4.10 lxml==3.6.4
- PyMySQL==0.7.9 requests==2.13.0selenium==3.4.3


## 抓取元素 ##
### 一级页面 ###
- 岗位名称 发布时间 公司名称 所在省 所在市 学历要求
- 工作经验 薪资 公司资质 公司类型 公司规模

### 二级页面 ###
- 岗位职责
- 公司介绍


## 更新日志 ##
### v0.3 (2018/4/2) ###

- 增加二级页面岗位职责的爬取

### v0.2 (2018/3/29) ###

- 封装pymysql
- 添加邮箱监控
- 优化断点续爬
- 优化代码

### v0.1 (2017/12/14) ###

- 完成iP代理池
- 完成一级页面解析
- 部分完成断点续抓



