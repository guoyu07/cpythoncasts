##网站开发信息说明：
- 网站开发信息说明由zhangtianyi1234执笔，时间2013年8月
- 网站开发所用技术文档和需要install的组件在requirements.txt中，我会在后期添加补全
- linux开发环境下可以非常方便的在控制台$sudo pip install requirements.txt就可以安装所需要的组件
- 建议python django开发者使用linux系统，pyhton和django开发者使用的OS操作系统django官网上有统计，linux系统是占比绝大多数的系统


##开发说明:
- 本网站使用python语言开发，使用django框架，结合grappli，fontawesome,markdown等相应模块
- 网站资源来源于网络，网站用于python，django，uliweb,嵌入式开发,linux，github，html，css,javascript等程序开发的学习交流。开发目的不在于商业应用，开发服务于互联网学习交流，网站资源借鉴使用warpbootstrap开发的unify框架，在此一并致敬。保留开发者相应权益，使用请声明。
- contributors：
  - 感谢limodou大师不厌其烦的指点（python大牛，uliweb，ulipad原作者）https://github.com/limodou
  - asmcos  https://github.com/asmcos/
  - zhangtianyi1234 https://github.com/zhangtianyi1234/
				  
网站还有许多方面有待进一步优化，发扬github的开放精神，代码开源，欢迎高手和资深geeks贡献智慧，
可以在上面网址的github上查看并贡献代码，并进行优化

##网站待优化部分：^(@_@)^
- 网站开发像上帝造人一般，力求完美完善，但是凡人能力有限，专长有短，不完美之处在所难免.会者不难，难者不会。希望能给大家启迪，也期待高手指点不优雅的地方，技术进步就是不断曾删改查优化丰富的过程。
- 个人愚见有待优化部分如下：
  - 1,右侧小齿轮，更改页面theme style颜色样式的功能不禁完善，期待高手指点
  - 2,右侧language语言选择功能不尽完善，知道python由国际化的部分，但是知识有限没有做到，期待高手指点
  - 3,navbar导航条集中化管理，使得点击具体某个栏目下相应的选择效果在被选择条目。google搜索相应知识，通常有2中方案，js和urls动态添加，所提供的资讯个人感觉抓不着头脑，include vavigation html模板和urls动态加载在复杂化程度较高的网站上，问题多多。当然再此一并感谢国内python技术大师limodou指点的正确思路方法。我们采用了最原始，最土的方法解决，反而化繁为简，期待高手指点
  - 4,firefox可以支持fontawesome字体部分，国内使用情况较少，台湾开发者使用较多，开发水平较高，nginx网站部署以及网站样式风格和国外网站相差不多，值得学习。而在本网站中我们只是简单了解，绕道过去，并没有很好的解决，期待高手指点
  - 5,django后台使用，有grappli和xadmin的选择，页希望使用以增加网站特色，希望后台能做到完美，期待高手指点
  - 6,在django框架中搜索查询功能的实现，有待增进，期待高见
  - 7,goole map定位功能很酷，但是实现起来缺乏相应技术文档说明等资讯，期待高手指点
  - 8,随着网站文章扩展增加，各个栏目模块有待集约化管理，期待高手指点
  - 9,更多，bug，不优雅的语法，不严谨的逻辑，可以精简的程序。。。期待高手指点
  - 10,网站运营也会出现各种新需求，新问题，不是一朝一夕功夫达成，期待高手指点
	
##网站结构方面：
#项目基本结构：

├── accounts
├── exam
├── cpythoncasts
├── templates
├── static
├── README.txt
├── video.db
└── manage.py

#.templates文件夹目录：
├── account
│   ├── set_confirm_delete.html
│   ├── set.html
│   ├── set_info_list.html
│   ├── set_left.html
│   ├── set_question_form.html
│   ├── set_question_list.html
│   ├── set_video_form.html
│   └── set_video_list.html
├── index.html
├── layout.html
├── login.html
├── register.html
├── navigation.html--网站导航条模板（未使用）
├── newstudent.html--欢迎新同学部分在多个页面出现，所以以模板include方式集中化管理
├── right_sidebar.html--右侧列表部分在多个页面出现，所以以模板include方式集中化管理
├── unifyallvideos.html--所有课程视频集合
├── unifyblog.html--blog页面
├── unifyblogleft.html--blog页面，元素居左显示
├── unifycollection.html--网站开发所使用的元素特效集合
├── unifycontentpage.html--具体学习课程页面
├── unify.html--网站主页
├── unifylayout.html--网站所有页面继承的模板，include了right_siderbar,newstudent模板
├── unifylearn.html--学习分类模块
├── unifylesson.html--课程分类模块
├── unifylogin.html--用户login
├── unifymap.html--集合google map定位
├── unifypage.html--具体某个课程页面
├── unifyregister.html--用户注册页面
├── unifyteachers.html--师资介绍模块
└── unifytest.html--网站开发测试所用界面

##CSS引用方面：
  - 1.由于本网站使用了bootstrap相应比较新的架构fontawesome，在国内没有相应的cdn库支持，所以只能在CSS导入时加入国外网站链接，延迟问题不可避免
<link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.no-icons.min.css" rel="stylesheet">
<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">不可缺少，否则特效不能显示.
  - 现在问题解决，方法是本地static里面加载font字体文件夹和fontswesome.min.css,具体参见http://www.bootcss.com/p/font-awesome/
  - CSS样式和JS在开发阶段，基本是本地加载，服务器上线后，需要相应调整成百度cdn地址
  - static部分以及用户上传下载的文件，videos以及其他，需要单独集合到media目录，集中化管理	
  - 2.fontawesome在firefox浏览器上不支持，开发者解决方法有2种：
  - 一种是在nginx服务器端加入资源源支持语句，使得firefox可以支持fontawesome字体;
  - 二，开发过程中在static目录下加入font字体，导入fontawesome字体，具体做法可以google搜索“firefox不支持fontawesome”

##技术亮点分享：
  - 1,页面清新美观，使用python语言django框架开发，简单易用，各个功能模块新潮,uliweb也很优异
  - 2,fontawesome和bootsrtap特效结合，希望能给大家启迪，技术进步就是不断优化丰富的过程，国内使用情况较少是个亮点
  - 3,grappli和xadmin后台管理使用，xadmin是国人开发的框架，技术要点方便询问，可以找原作者问到死
  - 4,图片和视频特效比较好，可以让大家开发更有料
