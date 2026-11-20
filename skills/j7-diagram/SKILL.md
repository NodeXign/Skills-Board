---
name: j7-diagram
description: 创建用户偏好的 Notion 黑白插画、hairline 极细线逻辑图与图文信息图。用于“我的 diagram skills”、Notion 风格图、白底细线流程图、框架图或带人物隐喻的信息图；按内容选用已安装的 Diagram Design、Hairline 与 Niyam Notionaly。
---

# J7 Diagram

个人 diagram 工具采用 Diagram Design、Lucas Marques 的 Hairline 和 Niyam Notionaly。此偏好只适用于本技能，不覆盖项目品牌或用户当次要求。

## 路由

- 流程、架构、象限、飞轮、层级、关系：读取 `../diagram-design/SKILL.md` 与相关图型参考。
- 等轴测物件、分层或爆炸线稿：静态图读取个人预设和 Diagram Design 对应图型。需要指针交互时，新作读取 `../hairline-create/SKILL.md`，从 SVG 重建读取 `../hairline-adopt/SKILL.md`。
- 人物、动作隐喻、图标或单幅插画：读取 `../niyam-notionaly-illustrations/SKILL.md` 与 style-dna。
- 图文海报、数据卡片、插画式信息图：读取 `../niyam-notionaly-infographic/SKILL.md`；结构、文字与数据用 HTML/SVG，人物插画单独生成。
- 混合内容可组合以上组件，保留清楚的阅读顺序。不要为简单任务加载全部组件。

## 已选个人视觉预设

读取 `references/personal-style.md`。这是用户选择的 Notion/hairline 方向的本地实现预设，不是上游官方风格。除非当前项目或用户另有要求，直接采用，不重复询问是否定制品牌。若直接调用原始 diagram-design，则遵循其独立品牌设置流程。

## 执行与检查

先确定核心信息与合适图型。中文内容默认中文标签；不能虚构数据。
遵循组件布局规则并按本地预设着色。文字与数据保持为真实文本，不让图片模型画整页文字。
Diagram Design 使用系统字体时生成离线 HTML + 内联 SVG；需要时导出 PNG。插画按相应技能生成；图片生成和编辑须使用可用的 image_gen 工具。
渲染后检查中文字体、箭头、间距、裁切、图片载入和数据比例；对逻辑图运行 diagram-design/scripts/self_check.py。未能渲染时明确说明，不能把结构验证说成视觉验证。
产物放在当前工作区的版本化输出目录，不写进技能目录；遵循当前会话的输出位置规则。

## 来源与维护

上游来源和安装路径见 `references/sources.json`。保留原始组件，可单独调用；更新上游后检查本地入口兼容性。不自动部署、发布或上传。
