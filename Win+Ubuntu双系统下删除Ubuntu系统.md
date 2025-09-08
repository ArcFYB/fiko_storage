

一、删除Ubuntu系统的分区
---------------

在win10界面打开cmd，找到Ubuntu系统分区并删除

1.【win】+【R】，输入cmd；

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605084334550-997931801.png)

 2.进入[命令行](https://zhida.zhihu.com/search?content_id=210387063&content_type=Article&match_order=1&q=%E5%91%BD%E4%BB%A4%E8%A1%8C&zhida_source=entity)，输入[diskpart](https://zhida.zhihu.com/search?content_id=210387063&content_type=Article&match_order=1&q=diskpart&zhida_source=entity)

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605084451723-1512961877.png)

 3.list disk 查看系统所有磁盘

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605084547186-2044147069.png)

 4.select disk 1 打开Ubuntu系统坐在的磁盘

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605084725299-1077425006.png)

 5.list partition 查看磁盘分区

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605084817802-20489016.png)

 6：

select partition # #为Ubuntu所在的分区

→delete partition override （删除分区，这一步需要谨慎操作，不要选错分区）

→重复select partition #和delete partition override直到删除所有Ubuntu分区

（补充：删除Ubuntu‘系统’分区也同理）

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605084943365-2094379076.png)

       注意：如果在删除中提示无法删除的操作，比如:

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605085145676-724046903.png)

   提示这种无法删除，此时可以使用

### 其他替代方法

——————————————————————————————————————————————————
fiko
主要就是用这个
——————————————————————————————————————————————————

1.  使用 Windows 磁盘管理工具（GUI 操作更直观）：
    
    *   按 `Win + X` → 选择 "磁盘管理" → 右键目标分区 → "删除卷"。
        
2.  使用第三方工具（如 DiskGenius、AOMEI Partition Assistant）。
    

二、删除Ubuntu系统的启动项
----------------


——————————————————————————————————————————————————
fiko自用软件
https://www.easyuefi.com/index-us.html
——————————————————————————————————————————————————

以上删除了Ubuntu系统的分区，接下来删除其启动项。

启动项不删除可能会造成开机仍然有Ubuntu的引导但却进入不了Ubuntu系统的麻烦

1.【win】+【R】，输入cmd

2.diskpart

3.list disk

4.select disk $ $是Windows安装所在的磁盘

→list partition

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605085825757-2111996582.png)

5.select partition 1（1为win下系统类型分区所对应的分区ID）

→assign letter=P.（不要关闭界面）选择其系统分区并将其分配给一个磁盘P（任意一个不与现有磁盘冲突的就行），

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605085858473-2107431764.png)

查看此电脑，磁盘多出了一个刚刚分配的P磁盘

![](https://picx.zhimg.com/v2-b1305932c4de4eff3461dbb0a524623b_1440w.png)

 6.选择电脑磁盘P

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605090118921-2080103650.png)

 7.找到Ubuntu文件夹

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605090053118-1964864379.png)

鼠标右键，选择

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605090154181-138319539.png)

 8.进入前面的操作界面，输入remove letter=P；删除P盘即可

![](https://img2024.cnblogs.com/blog/1468187/202506/1468187-20250605090221277-511065052.png)

 9.重启电脑


——————————————————————————————————————————————————
fiko
拆除硬盘前记得先脱机
——————————————————————————————————————————————————