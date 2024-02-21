# 部署应用到Platform.sh

很多同学在部署Django应用到platform.sh平台的时候遇到问题，这里书的作者可能没有对windows平台进行测试，或者有可能platform平台自己有变化，所以大家需要去查询platform.sh的官方网站的相关文档，这里是[链接地址](https://docs.platform.sh/administration/cli.html)

根据官方文档，下面是部署应用到platform.sh的具体步骤：

- 第1步：安装[scoop](https://scoop.sh/),打开Powershell(version 5.1 or later)，运行下面的命令：

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

- 第2步：对于Windows平台应该使用Scoop,打开Powershell运行下面的命令：

```powershell
scoop bucket add platformsh https://github.com/platformsh/homebrew-tap.git
scoop install platform
```

- 第3步：另外根据我的测试，还需要安装unzip， [下载地址](https://sourceforge.net/projects/gnuwin32/files/unzip/5.51-1/unzip-5.51-1.exe/download?use_mirror=nchc&download=)

- 第4步：安装unzip后，还需要将unzip命令的路径加入path环境变量：
C:\Program Files (x86)\GnuWin32\bin

- 第5步：在命令行运行platform，选择y，可以进入platform网站进行部署。
