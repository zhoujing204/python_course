# 部署应用到Platform.sh

很多同学在部署Django应用到platform.sh平台的时候遇到问题，这里书的作者可能没有对windows平台进行测试，或者有可能platform平台自己有变化，所以大家需要去查询platform.sh的官方网站，这里是[链接地址](https://docs.platform.sh/administration/cli.html)

具体步骤：

- 第一步：对于Windows平台应该选择Scoop,运行下面的命令：

```cmd
scoop bucket add platformsh https://github.com/platformsh/homebrew-tap.git
scoop install platform
```

- 第二步：另外根据我的测试，还需要安装unzip， [下载地址](https://sourceforge.net/projects/gnuwin32/files/unzip/5.51-1/unzip-5.51-1.exe/download?use_mirror=nchc&download=)

- 第三步：安装unzip后，还需要将unzip命令的路径加入path环境变量：
C:\Program Files (x86)\GnuWin32\bin

- 第四步：在命令行运行platform，选择y，可以进入platform网站进行部署。
