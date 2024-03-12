> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/y22y22y/article/details/120339331)

1. 首先在Ubuntu上安装openssh-server

```
sudo apt install openssh-server
```

安装好以后，ssh server应该已经开始运行了，可以用下面的命令检查ssh server的状态

```
systemctl status sshd
```

![](https://img-blog.csdnimg.cn/20210918172147408.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAeTIyeTIyeQ==,size_20,color_FFFFFF,t_70,g_se,x_16) 

 如图，可以看到状态是active(running）

另外，需要的时候，还可以利用systemctl命令打开(start)/关闭(stop)/重启(restart)ssh server，例如下面的命令就可以用来重启ssh server服务

```
sudo systemctl restart ssh
```

2. 利用Ubuntu自带的ufw 修改防火墙状态

首先开启防火墙

```
sudo ufw enable
```

打开传输ssh的端口（默认22） 

```
sudo ufw allow ssh
```

设置ssh server开机启动 

```
sudo systemctl enable ssh
```

3.现在就可以用 ssh username@IP远程连接电脑了

查询IP地址

```
ip a
```

这里的192.168.1.112即为电脑IP![](https://img-blog.csdnimg.cn/20210920223247777.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAeTIyeTIyeQ==,size_20,color_FFFFFF,t_70,g_se,x_16)

所以ssh连接这台电脑的命令为⬇️

```
ssh linuxconfig@192.168.1.112
```

4.到上一步为止，其实已经可以实现连接功能了，但是为了安全着想，最好将ssh的端口从默认的22改为另一个大于1024的数字

编辑ssh server配置文件

```
sudo vim /etc/ssh/sshd_config
```

```


1.  Port 2222   #设置ssh的端口号
2.  PermitRootLogin yes   # 可以root远程登录


```

打开设定的ssh端口

```
sudo ufw allow 2222/tcp
```

 重启ssh server

```
sudo systemctl restart ssh
```

现在，可以连接你的电脑了

```
ssh -p 2222 linuxconfig@192.168.1.112
```