# Prompt Patterns

## Universal Image Style Anchor

Use a compact style anchor and adapt it to the project:

```text
真实摄影感，适合AI短视频图生视频的首帧资产，画面可信、干净、主体明确，光线自然，色彩统一，不要文字，不要logo，不要水印，避免过度商业化和过度滤镜。
```

## First-Frame Image Prompt Pattern

```text
Use case: photorealistic-natural
Asset type: image-to-video first-frame image, vertical 9:16
Primary request: <镜头首帧主题>
Scene/backdrop: <场景>
Subject: <主体>
Action state: <动作开始前或关键静止状态>
Style/medium: photorealistic short-video production still
Composition/framing: <景别和构图>
Lighting/mood: <光线和情绪>
Color palette: <主色>
Constraints: no text, no logo, no watermark, no QR code, no readable signs, keep subject clear and stable
Avoid: <项目禁忌>
```

## Product Image Prompt Pattern

```text
Use case: product-mockup
Asset type: product reference image for image-to-video, vertical 9:16
Primary request: <产品名> product hero shot
Scene/backdrop: <桌面/场景>
Subject: <产品形态、包装、材质>
Style/medium: photorealistic product photography
Composition/framing: centered product, clean negative space for later text overlay
Lighting/mood: natural, trustworthy, clear texture
Constraints: no text, no logo, no watermark, no exaggerated commercial sale style
```

## Character Reference Prompt Pattern

```text
Use case: photorealistic-natural
Asset type: character reference image for image-to-video, vertical 9:16
Primary request: <角色名><角度/状态>
Scene/backdrop: <相关场景虚化背景>
Subject: <年龄、气质、服装、姿态>
Style/medium: photorealistic lifestyle portrait
Composition/framing: <半身/全身/背影/侧面>
Lighting/mood: natural, consistent with project style
Constraints: no text, no logo, no watermark, no exaggerated pose, no unrelated props
```

## Image-To-Video Prompt Pattern

```text
让画面保持<项目统一风格>。基于首帧图，镜头<运镜>。画面中<主体>进行<简单动作>，场景为<场景>，重点表现<镜头目标>。动作自然、速度缓慢、主体保持稳定。画面保留干净区域，方便后期添加文字。不要出现文字、logo、水印、二维码。
```

## Negative Constraint Pattern

```text
不要让主体变形，不要更换人物服装，不要生成额外人物，不要出现乱码文字，不要出现logo、二维码、品牌字样，不要出现城市高楼或无关场景，不要让动作过快，不要让产品形态变化，不要过度卡通化，不要过度商业广告感。
```

## Hard-Shot Backup Pattern

For each hard shot, provide three backup routes:

1. **Static close-up**: keep the object stable and use only push-in/pull-out camera movement.
2. **Cutaway replacement**: replace complex action with atmosphere or detail shot.
3. **Post-production workaround**: generate clean footage without text or complex action, then add text, sound, and transitions in editing.
