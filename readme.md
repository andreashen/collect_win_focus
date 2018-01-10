# collect_win_focus
**Win 10**的锁屏界面背景默认设置为**Windows聚焦**，它提供了许多好看的图片，为什么不把它们提取出来当壁纸呢？（ OvO）

## 解决思路
1. **Windows聚焦**的图片放在哪里？
> 默认路径：`C:\\Users\\[用户名]\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets`
2. 直接复制出来就行吗？
> 不行。该路径下的文件默认无扩展名，且并非全是锁屏界面背景
3. ​

## 用法
> python run.py \[Windows聚焦图片地址\] \[壁纸保存地址\] \[图片md5列表地址\]