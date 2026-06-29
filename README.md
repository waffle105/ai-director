# AI Director / AI短视频导演

## 中文

AI Director 是一个面向 AI 短视频制作的 Codex skill。它把“写一个视频提示词”升级为完整的导演工作流：先确认创意方向，再拆分分镜，准备首帧图、角色、产品、场景和道具资产，最后输出可用于即梦、Runway、可灵等图生视频工具的镜头级提示词。

### 适合场景

- AI 短视频策划与制作准备
- 即梦/图生视频提示词设计
- 产品宣传片、活动宣传片、故事短片
- 镜头级 storyboard、资产清单和首帧图规划
- 把一个主题拆成可执行的视频制作包

### 核心能力

- 分阶段确认 brief、创意方向、分镜和制作包
- 为每个镜头输出独立的图生视频提示词
- 规划首帧图、角色资产、产品资产、道具资产和场景资产
- 生成视频制作准备包、剪辑脚本、发布建议和封面建议
- 支持图片资产索引和 contact sheet 管理

### 使用方式

把本仓库作为一个 Codex skill 安装或复制到你的 Codex skills 目录，然后在 Codex 中说：

```text
Use $ai-director 帮我为这个主题做一个 AI 短视频制作准备包：……
```

## English

AI Director is a Codex skill for AI short-video production planning. Instead of producing a single generic video prompt, it guides the work like a director: confirm the creative direction, break the idea into shots, plan first-frame images and production assets, and produce shot-level prompts for image-to-video tools.

### Best For

- AI short-video planning and production packages
- Jimeng / image-to-video prompt design
- Product promos, event promos, and story-driven short films
- Storyboards, asset maps, and first-frame planning
- Turning a rough theme into an executable video production package

### What It Does

- Confirms brief, creative direction, storyboard, and package in stages
- Writes one independent prompt per shot
- Maps character, product, prop, and scene assets to each shot
- Produces production docs, editing scripts, publishing variants, and cover ideas
- Helps organize generated image assets and contact sheets

### Usage

Install or copy this repository into your Codex skills directory, then ask Codex:

```text
Use $ai-director create an AI short-video production package for this theme: ...
```

## License

MIT
