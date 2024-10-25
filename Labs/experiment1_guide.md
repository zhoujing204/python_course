# 实验一 Git和Markdown基础实验指导(2学时)

## 实验目的

1. Git基础，使用Git进行版本控制
2. Markdown基础，使用Markdown进行文档编辑
3. vscode的基本使用

## 实验环境

1. Git
2. VSCode
3. VSCode插件
   - Python
   - Jupyter
   - GitLens
   - Git Graph
   - Git History
   - Markdown All in One
   - Markdown Preview Enhanced
   - Markdown PDF
   - Auto-Open Markdown Preview
   - Paste Image
   - markdownlint

## 实验内容和步骤

### 第一部分 实验环境的安装

1. 安装git，从git官网下载后直接点击可以安装：[git官网地址](https://git-scm.com/)
2. 从Github克隆课程的仓库：[课程的仓库地址](https://gitee.com/zj204/python_course)，运行git bash应用（该应用包含在git安装包内），在命令行输入下面的命令（命令运行成功后，课程仓库会默认存放在Windows的用户文件夹下）

```bash
git clone https://github.com/zhoujing204/python_course.git
```

如果你在使用`git clone`命令时遇到SSL错误，请运行下面的git命令(这里假设你的Git使用了默认安装目录，如果没有默认安装，请找到你的git的安装位置，找到`ca-bundle.crt`文件的路径，然后使用该路径进行配置，特别注意：这里的路径使用的斜杠是`/`)：

```bash
git config --global http.sslCAInfo "C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt"
```

或者运行下面的命令（不推荐，在正式的开发中这样设置会有安全隐患）:

```bash
git config --global http.sslVerify false
```

如果遇到错误：`error setting certificate file` 或者 `warning: http.sslcaInfo has multiple values`，请运行下面的命令重新指定git的安全证书(注意：这里的路径使用的斜杠是`/`)：

```bash
git config --global --unset-all http.sslCAInfo
git config --global http.sslCAInfo "C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt"
```

或者使用下面的命令编辑git配置文件，打开编辑器手动输入编辑配置信息

```bash
git config --global --edit
```

该仓库的课程材料后续会有更新，如果需要更新课程材料，可以在本地课程仓库的目录下运行下面的命令：

```bash
git pull
```

在本地的仓库内容有更新后，可以运行下面的命令，将本地仓库的内容和远程仓库的内容同步：

```bash
git push origin main
```

3. 注册Github账号或者Gitee帐号，创建一个新的仓库，例如：<https://gitee.com/zj204/python_task.git>，使用下面的命令将新建的仓库clone到本地：

```bash
git clone https://gitee.com/zj204/python_task.git
```

如果已经关联了远程仓库，显示结果如下：

```bash
origin  https://github.com/zhoujing204/python_course.git (fetch)
origin  https://github.com/zhoujing204/python_course.git (push)
```

如果还没有关联远程仓库，可以使用你创建的远程仓库的地址和下面的命令，添加你要关联的远程仓库：

```bash
git remote add gitee https://gitee.com/zj204/python_task.git
```

接下来准备好你的远程仓库账号的邮箱地址和密码，使用下面的命令下载远程仓库的内容更新本地仓库：

```bash
git pull gitee main
```

运行下面的命令，将本地仓库的内容同步到远程仓库：

```bash
git push gitee main
```

4. 安装VScode，下载地址：[Visual Studio Code](https://code.visualstudio.com/)

5. 安装下列VScode插件
   - Python
   - Jupyter
   - Git Graph
   - Git History
   - Markdown All in One
   - Markdown Preview Enhanced
   - Markdown PDF
   - Auto-Open Markdown Preview
   - Paste Image
   - markdownlint

### 第二部分 Git基础

教材《Python编程从入门到实践》P440附录D：使用Git进行版本控制，按照教材的步骤，完成Git基础的学习。

### 第三部分 learngitbranching.js.org

访问[learngitbranching.js.org](https://learngitbranching.js.org)，需要完成的实验包括三个小节：

- Main部分的Introduction Sequence

- Main部分的Ramping Up

- Remote部分第一小节Push & Pull -- Git Remotes!

![Learngitbranching.js.org](/Labs/img/2023-07-28-21-07-40.png)

上面你学习到的git命令基本上可以应付百分之九十以上的日常使用。

### 使用Git和GitHub进行团队协作

按照下面的实验步骤练习使用git和github进行团队协作：

1. 由项目组长创建一个新的Git仓库，命名为`learn-git`。

2.项目组长将项目的Git仓库链接分享给其他组员，其他组员clone到本地，例如：`git clone https://github.com/<teamleader>/learn-git.git`。

3.每个组员包括组长在进行开发前都需要将本地仓库更新，使用的命令`git pull origin master`.

4.每个组员都需要创建各自的`dev`分支并在这个分支上进行开发，使用的命令例如：`git branch -b feature1`,开发后提出`pull request`，项目组长或者项目小组成员对提交的代码要进行`code review`:

   - Github Pull Request视频教程：[B站链接](https://www.bilibili.com/video/BV16BtLegEeE)
   - Github的文档：[如何创建pull request](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

5.将`dev`分支合并到`main`分支, 在合并分支经常会遇到冲突（merge conflicts，冲突在当两个分支对同一个文件的同一个地方的修改不同时发生），处理冲突的工作流程是:

    - 项目团队成员需要进行沟通，了解冲突的来源
    - 讨论可行的解决冲突的方案，例如：
      - 保留当前分支的修改
      - 保留要合并的分支的修改
      - 最理想的方案是重写两个分支的代码并提交，在没有冲突的情况下再合并
      - 合并后再推送（push）到远程仓库

处理冲突的视频教程：[B站链接](https://www.bilibili.com/video/BV1GP2MYKErN)

### 第四部分 Markdown基础

查看[Markdown cheat-sheet](http://www.markdownguide.org/cheat-sheet)，学习Markdown的基础语法

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，使用[实验一报告模板](/Labs/experiment1_report.md)，并将其导出为 **PDF格式** 来提交。

如何将markdown文件转换为pdf格式的文件？

- 安装vscode插件Markdown PDF，安装后重启vscode，打开markdown文件，按下`Ctrl+Shift+P`，输入`Markdown PDF: Export (pdf)`，回车即可导出pdf文件。
- 使用Google Chrome浏览器，在Github网站或者Gitee网站打开你的仓库，浏览你的markdown文件，按下`Ctrl+P`，选择`打印`，选择`目标打印机`为`另存为PDF`，点击`保存`即可导出pdf文件。（这种方法可以在pdf文档中显示截图）
- 下载Yank Note 软件进行转换，[地址](https://yank-note.com/)

## 实验过程与结果的要求

记录实验过程时，注意代码需要使用markdown的代码块格式化，例如Git命令行语句应该使用下面的格式：

![Git命令](/Labs/img/2023-07-26-22-48.png)

显示效果如下：

```bash
git init
git add .
git status
git commit -m "first commit"
```

Git实验过程的记录请参考[Learning Git Branch Tutorial](https://github.com/zhoujing204/python_course/blob/main/Labs/LearningGitBranch-Tutorial.md)，请记录下每个git小实验的动机、使用的git命令、以及git命令的解释.

**注意：不要使用截图，Markdown文档转换为Pdf格式后，截图可能会无法显示。**

## Git参考资料

如果你想继续深入学习git，可以：

- 继续学习[learngitbranching.js.org](https://learngitbranching.js.org)后面的几个小节（包括Main和Remote）

- 在git使用过程中，如果遇到任何问题，例如：错误删除了某个分支、从错误的分支拉取了内容等等，请查询[git-flight-rules](https://github.com/k88hudson/git-flight-rules)

- 访问Git的官方网站，阅读官方教程[Pro Git](https://git-scm.com/book/zh/v2)
