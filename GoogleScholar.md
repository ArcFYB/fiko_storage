# 谷歌学术（Google Scholar)使用技巧

* 地址：[Google Scholar Website](https://scholar.google.com/)

- [谷歌学术（Google Scholar)使用技巧](#谷歌学术google-scholar使用技巧)
  - [Google Scholar搜索文献](#google-scholar搜索文献)
    - [1. **基本关键词搜索**](#1-基本关键词搜索)
    - [2. **使用运算符优化搜索**](#2-使用运算符优化搜索)
    - [3. **基于字段的搜索**](#3-基于字段的搜索)
    - [4. **时间范围过滤**](#4-时间范围过滤)
    - [5. **学术类型与语言筛选**](#5-学术类型与语言筛选)
    - [6. **保存和整理文献**](#6-保存和整理文献)
  - [Google Scholar搜索个人](#google-scholar搜索个人)
    - [1. **label:学术领域关键词**](#1-label学术领域关键词)


---
#### vscode-Markdown All in One插件， 可以直接生成目录， 内容和手写目录基本一样, 插件生成目录： Ctrl + Shift + P -> markdown all in one create table of contents（该方案会生成所有的标题目录，并按标题等级生成无序列表目录）自定义修改关闭插件设置中Update On Save

---
## Google Scholar搜索文献

### 1. **基本关键词搜索**
直接输入主题或关键词即可。例如：
- `remote sensing super-resolution`
- `diffusion model for image prediction`

---

### 2. **使用运算符优化搜索**
谷歌学术支持一些高级搜索运算符，可以更精准地筛选文献：
- **引号 `" "`**：用于精确匹配短语。
  - 示例：`"remote sensing super-resolution"`
- **减号 `-`**：排除不需要的关键词。
  - 示例：`diffusion model -GAN`
- **OR 与 ｜ 运算符**：查找包含任意一个关键词的文献。
  - 示例：`"super-resolution" OR "image restoration"`
  - 示例：`"super-resolution" ｜ "image restoration"`
- **AND 运算符**（默认）：查找同时包含多个关键词的文献。
  - 示例：`"remote sensing" AND "super-resolution"`

---

### 3. **基于字段的搜索**
使用特定标签限制搜索范围：
- **`author:`**：查找特定作者的论文。
  - 示例：`author:goodfellow`
- **`intitle:`**：仅在论文标题中搜索关键词。
  - 示例：`intitle:"diffusion model"`
- **`journal:`**（非官方标签，但可以在常规搜索中输入期刊名称进行尝试）。

---

### 4. **时间范围过滤**
点击搜索页面左侧的“时间选项”，可以选择：
- 最近几年（例如“2020年之后”）
- 自定义时间范围（例如“2018-2023”）

---

### 5. **学术类型与语言筛选**
- 在页面左侧栏可以设置筛选条件，如语言或文献类型（例如专利、引文等）。

---

### 6. **保存和整理文献**
- 点击文献下方的星标，可以保存到您的谷歌学术个人资料库。
- 使用 `My library` 功能管理和分类文献。

---
---
## Google Scholar搜索个人

### 1. **label:学术领域关键词**
找到某个领域的顶尖学者
- `label:remote_sensing`
多 label 场景
- `label:robotics + label:machine_learning`
多 label 场景，限制国家地区
- 示例：`label:remote_sensing + label:machine_learning + .de`


---