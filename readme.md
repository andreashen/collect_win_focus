# collect_win_focus
by andreashen (Eswai)
## 用来干啥？
**Win 10**的锁屏界面背景默认设置为**Windows聚焦**，它提供了许多好看的图片，为什么不把它们提取出来当壁纸呢？(OvO)

## 怎么做的？
0. **Windows聚焦**的图片放在哪里？
> 默认目录：`C:\Users\用户名\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets`
1. 直接复制出来就行吗？
> 不行。该路径下的文件默认无扩展名，且并非全是锁屏界面背景，多次更新之后会存在不同名称的相同内容的图片
2. 所以，整个流程是？
> 0. 在壁纸目录下创建一个缓存目录（或清空该缓存目录）
> 1. 复制Windows聚焦路径下的文件到缓存目录，并补上图片类型的扩展名
> 2. 保留分辨率为`1920×1080`的图片（其他图片都不是壁纸）
> 3. 将缓存下剩余图片的名称用图片的MD5码重命名
> 4. 把缓存目录下的图片复制到壁纸目录

## 怎么使用？
> python run.py \[Windows聚焦图片地址\] \[壁纸保存地址\]

或者把默认参数写在`run.py` 里。

我的做法是把上面的命令写在`update.bat`批处理文件里，放在壁纸目录下，看壁纸的时候就可以双击更新了。

Enjoy it!