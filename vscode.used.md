# 创建Django测试项目并进行配置

VS Code提供了两种范围的设置，分别是**User**及**Workspace**.

用户级别的设置可以理解为全局设置，其中的设置对任一vscode实例都生效。

工作区级别的设置则仅针对当前项目生效，配置文件存放在项目的 .vscode 文件夹中。  
一般在项目开发中我们使用工作区级别的设置。

### 以下步骤记录了如何建立Django项目的基本目录结构。

创建项目文件夹，例如 mkdir django_demo，并切换到该文件夹  
在项目文件夹中使用virtualenv env 创建env文件夹
> 创建虚拟环境，也可不设置使用系统环境

创建 requirements.txt 文件，文件中添加以下内容
> pylint为python的静态语法检测器  
> pylint-django 是适用于django项目的语法检查其插件  
> autopep8 是代码格式化工具

```shell
django<1.10
pylint
pylint-django
autopep8
```

在 vscode 中按下 `Ctrl + Shift + P`   
输入 workspace，选择 Preferences: Open Workspace Settings，配置完成后的JSON文件如下

```json
{
  "python.pythonPath": "path-to-python",
  "python.linting.pylintPath": "pylint",
  "python.linting.pylintArgs": [
    "--load-plugins",
    "pylint_django"
  ],
  "python.formatting.autopep8Path": "autopep8"
}
```

成功配置完成后，vscode 会在状态栏中提示代码是否符合 pylint的相关规则。  
之后我们可以在此基础上继续项目开发。  