##PageLive

在我开发[博客模板](https://github.com/leilux/leilux.github.io)的过程中。写前端页面的时候会有大量的修改，这时会频繁地重复`修改->保存->刷新浏览器`这个过程。所以修改的效果不能第一时间呈现，而且编程的流畅性也被额外的操作打断了，真的非常痛苦。所以开发了这款工具来自动执行这一过程。

pagelive会监控你指定的目录文件，如果有文件被修改，它会自动触发浏览器刷新页面。效果类似所见即所得的编辑器。如果配合双屏使用真是前端开发利器。

##安装

安装`requirements.txt`中的依赖

根据以下网址来选择与chrome对应的chromedriver

http://chromedriver.storage.googleapis.com/2.9/notes.txt


##使用

第一步：命令行下运行
```
$ pagelive path [browsers]
# path 表示要监控的目录
# browsers   表示用什么浏览器，默认为chrome
```

第二步：输入网址
