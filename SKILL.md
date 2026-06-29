---
name: ai-director
description: AI short-video director workflow for producing complete video preparation packages and pre-video image assets. Use when Codex is asked to make an AI video, short-video preparation package, Jimeng/即梦 prompt set, image-to-video asset package, storyboard prompts, lens-level asset mapping, promotional film plan, product/activity/story short film, or to turn a theme into AI-generated video assets.
---

# AI-director

## Purpose

Use this skill to turn a user theme into a complete AI short-video production preparation package, then generate the pre-video image assets needed for image-to-video tools.

Core principle:

**Prepare assets first, then direct the model. AI video is a director workflow, not a single prompt.**

## Mandatory Workflow

Run the workflow in gated stages. Stop after each important stage and wait for the user.

1. **Brief confirmation**
   - If the user did not provide enough information, ask for what is missing before planning.
   - Required minimum: theme, video goal, target audience, publishing platform, desired length, style/tone, required or forbidden information.
   - If the user gives a vague theme, propose reasonable defaults and ask for confirmation.

2. **Creative direction confirmation**
   - Output three directions: safe version, social-spread version, story version.
   - Recommend one direction and explain why.
   - Stop and ask the user to confirm, revise, or choose another direction.

3. **Storyboard confirmation**
   - Convert the confirmed direction into a storyboard.
   - For 15 seconds, prefer 2-4 shots.
   - Each shot must have one clear job.
   - Identify hard shots and simplification options.
   - Stop for confirmation.

4. **Preparation package confirmation**
   - Generate the complete preparation package documents.
   - Include the lens-level prompt and asset mapping document.
   - Stop for confirmation.

5. **Image asset generation confirmation and execution**
   - First output the image asset generation plan.
   - Only after user confirmation, call `imagegen` one asset at a time.
   - Save all final image assets into the project package, not only under `.codex/generated_images`.
   - Generate an image asset index and contact sheet.

The stage advance keyword is **“继续”**. If the user is dissatisfied at any stage, revise that stage and wait again. Do not move to the next stage until the user confirms or says “继续”.

Fast mode is allowed only when the user explicitly asks to skip confirmations. Even in fast mode, still produce lens-level prompts and asset mapping.

## Output Package

Create a project folder named from the project theme, for example:

```text
<项目名>_AI短视频制作准备包/
```

Include these documents:

```text
00_使用说明.md
01_项目Brief与创意方案.md
02_视频脚本与分镜.md
03_资产清单.md
04_镜头级提示词与资产映射表.md
05_资产分步生成提示词.md
06_视频工具导演式提示词.md
07_难镜头测试与备选方案.md
08_剪辑脚本与旁白字幕.md
09_发布版本与封面建议.md
10_图片资产生成计划.md
图片资产/
```

Read `references/output-templates.md` before writing these documents.

## Lens-Level Prompt Rule

`04_镜头级提示词与资产映射表.md` is mandatory.

If a 15-second video has three shots, output three independent shot sections:

- Shot 1: its own image-to-video prompt plus its own first-frame image and asset list.
- Shot 2: its own image-to-video prompt plus its own first-frame image and asset list.
- Shot 3: its own image-to-video prompt plus its own first-frame image and asset list.

Every shot must include:

- Shot goal
- Duration
- Shot size
- Visual content
- Action
- Camera movement
- Required first-frame image
- Required character assets
- Required product assets
- Required prop assets
- Required scene assets
- First-frame image prompt
- Image-to-video prompt
- Negative constraints
- Backup plan if generation fails

Rule: **one shot, one prompt, one asset package, one negative constraint set.**

Do not replace shot-level prompts with a whole-video prompt. A whole-video prompt may be included only as a supplement.

## Prompting And Asset Rules

Read `references/ai-video-director-method.md` for the production method.

Read `references/prompt-patterns.md` when writing:

- Image asset generation prompts
- First-frame prompts
- Image-to-video prompts
- Negative constraints
- Hard-shot test prompts

Default guidance:

- Prefer image-to-video over one-shot text-to-video for important shots.
- Do not ask AI video tools to generate large Chinese text, dates, addresses, QR codes, or brand/legal details inside the video.
- Add text in post-production unless the user explicitly asks otherwise.
- Split complex actions into shorter shots.
- Test the hardest shot before generating every asset.
- Keep character, product, scene, and color style consistent.

## Image Asset Generation

When image generation is confirmed:

1. Use the built-in `imagegen` skill/tool by default.
2. Generate one distinct asset per image prompt.
3. Save or copy final assets into:

```text
<项目包>/图片资产/
```

4. Name files with stable ordered names:

```text
01_主产品特写.png
02_主角正面半身.png
03_场景远景.png
```

5. Create `图片资产索引.md` with file name, purpose, related shot, and source prompt.
6. Run `scripts/make_contact_sheet.py` to create:

```text
contact-sheet_图片资产总览.png
```

Never leave project-bound image assets only in the default generated image folder.

## References

- `references/ai-video-director-method.md`: production method and quality rules.
- `references/output-templates.md`: required document structures.
- `references/prompt-patterns.md`: reusable prompt patterns.
- `scripts/make_contact_sheet.py`: contact-sheet utility for generated image assets.
