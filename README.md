#### Scrapy批量下载百度美女图n张/自定义文件名-流水序号命名/灵活运用ImagesPipeline
#### 疫情期间看看美女养眼，依据序号，哪一张是你的菜？
##### 1，下载结果截图:
![img1](https://github.com/ziliang-wang/baidu/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200428150737.png)
##### 2，抓包截图，每加载一次就返回一个json对象，每一次30张(参数rn)，参数pn为每次加载的起始值，step步进值为30，下载的url字段为"thumbURL"，只下载"缩略图"
![img2](https://github.com/ziliang-wang/baidu/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200428150127.png)
##### 3，ImagesPipeline代码
![img3](https://github.com/ziliang-wang/baidu/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200428144711.png)
###### a，自定义一个继承于ImagesPipeline的类，用来处理spider发过来的item并发出请求
###### b，设置一个类变量idx，做为图片的文件名，每发一个请求(每下载一张图片)，就+1，再透过meta参数传递给file_path()
###### c，file_path()的部份，使用正则替换函数re.sub()，将0.jpg中的0，替换成序号，zfill(8)为填充函数，不满8位数的部分，都填充为0
##### 主要处理的部份-每一个图片都是0.jpg，必须重命名！
![img4](https://github.com/ziliang-wang/baidu/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200428152534.png)
