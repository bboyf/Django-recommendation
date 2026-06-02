# DjangoFilm 图书推荐系统

> 基于 Django + Spark 的智能图书推荐平台

## 项目简介

DjangoFilm 是一个功能完善的图书推荐系统，基于 **Django 2.2** Web 框架和 **Apache Spark** 推荐算法构建。系统提供用户注册登录、图书浏览、搜索过滤以及个性化推荐等功能。

## 技术栈

| 技术 | 版本 | 说明 |
|------|------|------|
| Django | 2.2 | Web 框架 |
| Python | 3.5+ | 编程语言 |
| Apache Spark | 2.3 | 推荐算法引擎 |
| Redis | 5.0 | 缓存服务 |
| MySQL | - | 数据库（可选） |
| PIL | - | 图片处理 |

## 功能特性

### 核心功能

- **用户管理**：注册、登录、个人信息管理
- **图书管理**：图书信息的增删改查
- **搜索过滤**：按书名、价格、评分等条件筛选
- **智能推荐**：基于协同过滤算法的个性化图书推荐
- **数据导入**：支持 CSV 文件批量导入图书数据

### 系统模块

```
djangoFilm/
├── djangoFilm/          # Django 项目配置
├── home/               # 用户和图书模型
├── recommend/          # 推荐算法模块
├── recommdModel/       # 推荐模型数据
├── static/             # 静态资源（CSS/JS/图片）
├── templates/          # HTML 模板
└── uploads/            # 上传文件目录
```

## 快速开始

### 环境要求

- Ubuntu 16.04 或更高版本
- Python 3.5+
- Redis 5.0

### 安装依赖

```bash
pip install django==2.2
pip install redis5.0
pip install pyspark==2.3
pip install Pillow
```

### 安装 Redis

```bash
wget http://download.redis.io/releases/redis-5.0.4.tar.gz
tar xzf redis-5.0.4.tar.gz
cd redis-5.0.4
make
```

启动 Redis 服务：

```bash
src/redis-server
src/redis-cli
```

### 数据库初始化

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 导入图书数据

1. 进入系统后台 `/admin`
2. 在"上传文件"功能中选择 `uploads/GoodBooks.csv` 文件
3. 系统将自动导入图书数据

> 图书数据来源：[GoodBooks Dataset](https://github.com/moverzp/GoodBooks)

### 启动服务

```bash
python manage.py runserver
```

访问 `http://localhost:8000` 即可使用系统。

## 项目页面

### 首页
展示图书列表，支持分类筛选和搜索功能。

### 详情页
显示图书详细信息，包括封面、价格、出版社、评分和简介。

### 推荐页
基于用户行为和协同过滤算法，生成个性化图书推荐列表。

### 管理后台
`/admin` 地址进入，用于管理用户和图书数据。

## 数据模型

### user（用户）
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| name | CharField | 用户名 |
| email | EmailField | 邮箱 |
| password | CharField | 密码 |

### book（图书）
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| name | CharField | 书名 |
| price | FloatField | 价格 |
| cover | ImageField | 封面图片 |
| introduction | TextField | 简介 |
| url | URLField | 外部链接 |
| publish | CharField | 出版社 |
| rating | CharField | 评分 |

### hits（点击量）
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| userid | Integer | 用户ID |
| bookid | Integer | 图书ID |
| hitnum | Integer | 点击次数 |

## 目录结构

```
djangoFilm/
├── djangoFilm/              # Django 项目配置
│   ├── settings.py          # 项目设置
│   ├── urls.py              # URL 配置
│   └── wsgi.py              # WSGI 应用
├── home/                    # 主应用
│   ├── models.py            # 数据模型
│   ├── views.py             # 视图函数
│   └── urls.py              # URL 路由
├── recommend/               # 推荐模块
│   ├── train.py             # 模型训练
│   ├── recom.py             # 推荐算法
│   └── views.py             # 推荐视图
├── recommdModel/            # 推荐模型数据
│   └── metadata/            # 模型元数据
├── static/                  # 静态资源
│   ├── css/                 # 样式文件
│   ├── img/                 # 图片资源
│   └── js/                  # JavaScript 文件
├── templates/               # HTML 模板
│   ├── base.html            # 基础模板
│   ├── index.html           # 首页
│   ├── detail.html          # 详情页
│   ├── login.html           # 登录页
│   ├── register.html        # 注册页
│   ├── recommend.html       # 推荐页
│   └── search.html          # 搜索页
├── uploads/                 # 上传文件
│   └── GoodBooks.csv        # 图书数据
├── vip4/                    # 虚拟环境
├── manage.py                # Django 管理脚本
└── README.md                 # 项目文档
```

## 注意事项

1. **推荐模块**：该模块依赖 Spark 环境，在部分环境下可能存在兼容性问题
2. **路径配置**：确保各模块路径配置正确，特别是推荐模型数据路径
3. **数据库**：默认使用 SQLite，可根据需要切换为 MySQL

## 许可证

本项目仅供学习交流使用。

---

> 北方工业大学 · 软件开发实践课程设计作品