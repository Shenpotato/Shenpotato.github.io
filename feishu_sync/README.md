# 飞书文档同步 Agent

这个工具可以自动将你的飞书文档同步到 Jekyll 博客项目中，转换为 Markdown 格式并保存到 `_posts/` 目录。

## 功能特性

- 自动从飞书云空间获取文档
- 将飞书文档转换为 Markdown 格式
- 自动下载并保存文档中的图片到 `img/in-post/` 目录
- 根据文档标题自动分类到对应的文件夹（ai、algorithm、backend、frontend、network、program_language、utils、web3、personal）
- 支持增量同步，只处理变更过的文档
- 支持定时同步的 agent loop 模式

## 安装步骤

1. 进入 `feishu_sync` 目录：
```bash
cd feishu_sync
```

2. 创建虚拟环境（可选但推荐）：
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 配置

1. 复制环境变量示例文件：
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，填入你的飞书应用信息：

```env
# 飞书应用配置
FEISHU_APP_ID=your_app_id_here
FEISHU_APP_SECRET=your_app_secret_here

# 飞书文档空间配置（可选）
FEISHU_ROOT_FOLDER_TOKEN=optional_root_folder_token

# 同步配置
SYNC_INTERVAL_MINUTES=60
POSTS_DIR=../_posts
IMG_DIR=../img/in-post
```

## 获取飞书应用凭证

1. 访问 [飞书开放平台](https://open.feishu.cn/)
2. 创建一个企业自建应用
3. 在「凭证与基础信息」中获取 App ID 和 App Secret
4. 在「权限管理」中添加以下权限：
   - 云文档: 获取云文档文件
   - 云文档: 读取云文档内容
   - 云空间: 获取云空间文件
   - 知识库: 查看知识空间节点信息
   - 知识库: 查看知识库名称
5. 发布应用并在企业中安装

## 给知识库文档授权

要访问知识库中的文档，你需要：

1. 打开你的知识库文档
2. 点击右上角的「...」菜单
3. 选择「...更多」→「添加文档应用」
4. 搜索并选择你创建的应用，添加为协作者

## 使用方法

### 同步单个文档（推荐先测试这个）

同步单个知识库或云文档：
```bash
python main.py --doc "https://my.feishu.cn/wiki/XDIaw78yTiNCsPkfClIcH6Q7ntc"
```

或者直接使用 token：
```bash
python main.py --doc XDIaw78yTiNCsPkfClIcH6Q7ntc
```

### 单次同步整个云空间

执行一次同步操作：
```bash
python main.py --once
```

### Agent Loop 模式

持续运行，定期同步（默认每 60 分钟）：
```bash
python main.py
```

## 文档分类规则

系统会根据文档标题自动将文档分类到对应的文件夹：

- 标题包含「AI」、「ai」或「机器学习」→ `_posts/ai/`
- 标题包含「算法」→ `_posts/algorithm/`
- 标题包含「后端」或「Backend」→ `_posts/backend/`
- 标题包含「前端」或「Frontend」→ `_posts/frontend/`
- 标题包含「网络」或「Network」→ `_posts/network/`
- 标题包含「编程」或「语言」→ `_posts/program_language/`
- 标题包含「工具」或「Utils」→ `_posts/utils/`
- 标题包含「Web3」或「web3」→ `_posts/web3/`
- 标题包含「个人」、「Personal」或「思考」→ `_posts/personal/`

## 注意事项

1. 同步的文档默认设置为 `published: false`，需要手动改为 `true` 才会在博客上显示
2. 图片会保存到 `img/in-post/YYYYMMDD-标题/` 目录下
3. 同步状态保存在 `sync_state.json` 中，用于增量同步
4. 建议先使用 `--once` 模式测试，确认无误后再使用 agent loop 模式
