# マチアプRPG — グラフィック生成プロンプト集

各アセットに **ファイル名 / 用途 / サイズ / 英語プロンプト** を載せた。
GPT-4o image / Sora / Midjourney にそのまま貼れる。

---

## 共通スタイル（全部に追記してOK）

```
NES/SFC-era pixel art, hard 1px black outline, 16-color limited palette,
no anti-aliasing, sharp pixels, transparent PNG background,
top-down JRPG style consistent with Dragon Quest 1/2,
centered subject, equal padding around edges.
```

**配色基調:** 深夜マッチングアプリ世界＝ネオン・紫・ピンク・ゴールド／勇者は青と金。

---

## キャラクター・スプライトシート（4列 × 2行 = 8フレーム）

レイアウト：

```
[front-idle] [front-walk] [back-idle]  [back-walk]
[left-idle]  [left-walk]  [right-idle] [right-walk]
```

サイズ：`384×192 px`（各セル 96×96）。

### `hero_yusha.png` — 勇者（プレイヤー）

```
24x24 hero sprite in 8 frames sprite sheet 4cols×2rows,
"yusha" — a young Japanese twenty-something in casual urban wear,
navy blue jacket open over white tee, dark blue jeans,
holds up a smartphone like a sword in his right hand,
neutral determined expression, light brown short hair,
yellow rim around phone (matching dating-app icon),
back view shows backpack with a tiny pink heart pin,
walk frames: one foot forward, slight tilt.
NES palette, sharp pixels, transparent background, no anti-aliasing.
```

---

### 通常エネミー（8フレーム：idle / walk / attack / hurt / talk1 / talk2 / surprise / dance のうち4-8）

レイアウト同上。**バトル時は idle/talk を使うので豪華に**。

#### `enemy_troll_girl.png` — トロール系女子

```
JRPG enemy sprite sheet 4×2, "Troll-kei Joshi" — overconfident hostess-type
Japanese girl in cheap luxury knockoff: pink leopard top, oversized
brand-logo handbag (fake), heavy lash extensions, contour makeup,
sneering "where are we going?" face, holds smartphone with shop-search open,
8 frames: bag-pose / pointing at shop / "I told you the store" gesture /
checking smartphone / hurt face / smug smirk / disgusted look / arm-crossed.
NES pixel art, hard outline, transparent BG.
```

#### `enemy_succubus.png` — ワンナイ系サキュバス

```
JRPG enemy sprite sheet 4×2, "One-night Succubus" —
nightlife Japanese woman, tight black mini-dress, small red horns
half-hidden in long purple hair, faint translucent demon tail,
glittery makeup, holding hotel keycard in one hand,
sultry "let's go somewhere♡" pose, lean and slim,
8 frames: hair-flip / wink / pulling-on-arm / pointing-to-door /
hurt expression / pouting / surprised / laughing.
NES pixel art, hard outline, transparent BG, neon-pink accents.
```

#### `enemy_kakou_troll.png` — 加工トロール

```
JRPG enemy sprite sheet 4×2, "Filter Troll" — Japanese girl whose face
is partially hidden behind a smartphone showing an over-filtered selfie
(impossibly perfect face on screen, real face only visible at edges = plain),
oversized cat-ear filter graphic on the phone screen,
8 frames: holding phone in front of face / lowering phone slightly /
shocked when phone is taken / angry yelling / about to call police /
"profile doesn't match" pose / hiding behind phone / running away.
NES pixel art, sickly green-yellow + neon pink ring-light glow,
hard outline, transparent BG.
```

#### `enemy_papa_katsu.png` — パパ活見習い

```
JRPG enemy sprite sheet 4×2, "Papa-katsu Beginner" — Japanese girl in
pastel pink fluffy coat over short dress, calculator in one hand,
long nail extensions, condition list written on phone in other hand,
"first-meet ¥20k, tea ¥30k" expression,
8 frames: showing price-list / pointing calculator at viewer / counting
on fingers / pouting "the other guy gave me more" / taxi-receipt held up /
checking line messages / fake-cute pose / annoyed sigh.
NES pixel art, soft pink + gold, hard outline, transparent BG.
```

#### `enemy_metal_runner.png` — 食い逃げメタル

```
JRPG enemy sprite sheet 4×2, "Eat-and-Run Metal" — a metallic-silver-skinned
version of a Japanese gal, polished chrome highlights, eyes glowing
neon-green like Dragon Quest Metal Slime,
holds a half-eaten yakiniku skewer in one hand and an empty receipt in the other,
small motion-blur lines around feet (she's fast),
8 frames: chewing / wiping-mouth / starting-to-bolt /
mid-sprint silhouette / waving-goodbye-while-running /
toilet-door-closing pose / smug peace-sign / vanished (faint outline).
NES pixel art, chrome + neon-green palette, hard outline, transparent BG,
visually echoes Metal Slime so it's instantly readable as "rare enemy".
```

#### `enemy_ghost_decoy.png` — 当て馬ゴースト

```
JRPG enemy sprite sheet 4×2, "Decoy Ghost" — translucent Japanese girl,
visibly see-through (50% alpha), pale blue and lavender,
holds phone showing a chat thread with someone named "本命♡" (her real love),
expression: polite but absent-minded, looking past the viewer,
small floating "既読" (read receipt) icons around her head,
8 frames: looking-past-viewer / smiling-at-phone / showing-phone-screen /
shaking-head "no" / drifting-backward / waving-bye / glancing-at-watch /
fading-out.
NES pixel art, cold-blue/lavender ghostly palette, hard outline,
semi-transparent body — render outline 100% but fill at 50%.
```

#### `enemy_bomb_rock.png` — 爆弾岩おんな

```
JRPG enemy sprite sheet 4×2, "Bomb-Rock Woman" — DQ-style "bomb rock"
monster reimagined as a clingy girlfriend: cute Japanese girl with
a round bomb-shaped body (like Pokemon Voltorb but cute),
short red fuse sticking out of her head, anxious-but-smiling expression,
phone in hand constantly typing,
8 frames: sending-LINE / "5-minutes-already?" angry-glare /
demanding location share / sweet-smile facade /
flames-rising-from-fuse / about-to-explode panic /
sobbing-emotionally / hugging-tight.
NES pixel art, red+orange+black palette with cute pastel-pink dress,
hard outline, transparent BG.
```

---

## ボス（4列 × 2行、サイズ `480×240` 各セル 120×120 = 通常より大きい）

### `boss_shinigami.png` — 死神（永遠に近づけない）

```
JRPG BOSS sprite sheet 4×2, large 120x120 cells, "Shinigami — the
forever-unreachable woman" — elegant tall Japanese woman in flowing
black-and-violet dress with subtle bat-wing collar, half-veil over eyes,
calm distant smile, no horns (more "elegant grim reaper" than demon),
holds a smartphone displaying perpetual "私のこと、まだ何にも知らないでしょ" message,
seated on dark-purple velvet throne in 4 frames, standing in 4 frames,
8 poses: throne-idle / throne-smile / showing-phone-to-viewer /
gently-shaking-head "no" / standing-walking-backward (key boss move) /
faint-laugh / wiping-fake-tear / barely-visible-genuine-smile (intimacy
unlocked pose, used only when intimacy reaches 3).
NES pixel art at higher res, deep purple + black + ghost-pink palette,
hard outline, transparent BG. Mysterious and slightly sad, not menacing —
this boss is "the girl who never lets you close", not a demon.
```

---

## NPC

### `npc_futsuu_girl.png` — 普通の子（ゴール、真エンディング）

```
JRPG NPC sprite sheet 4×2, "Futsuu no Ko" — an absolutely ordinary
Japanese girl, ~25, plain pale-pink cardigan over white blouse, jeans,
medium-length brown hair, no makeup-heavy look, gentle resting face,
holds a small paper book (no phone), light freckles,
8 frames: front-idle (slight smile) / front-walk (waving) /
back-idle / back-walk / left-walk / right-walk /
talking-pose (slight head-tilt) / surprised-but-pleased.
NES pixel art, warm earth-tones + soft pink, hard outline, transparent BG.
Conveys "normal in the best sense" — no flashiness, just genuine presence.
```

---

## タイルセット（4列 × 2行、各 32×32 = 計 128×64）

### `tiles_world.png`

```
Top-down JRPG tile sheet, exactly 8 tiles laid out 4 columns × 2 rows,
each tile 32×32 pixels, seamless tileable, NES color palette,
hard 1px outline, transparent background where applicable.

Tile layout:
[0,0] Wall — dark navy "city skyscraper window" tile, neon-blue grid pattern, looks tall and impassable
[1,0] Like-Grass — dark soil with bright pink hearts scattered (the "いいね草原"), low-encounter zone
[2,0] Love-Hotel Street — magenta neon brick with subtle pink heart-shaped lights, high-encounter zone
[3,0] App Floor — solid dark-blue grid floor, the default walkable path, slightly cyan glow lines
[0,1] Castle Wall — gilded gold-and-black brick with purple velvet trim (運営本社の壁)
[1,1] Home — pixel-art small apartment building, gray with single lit window, antenna on roof emitting tiny WiFi signal
[2,1] Throne — gold throne with pink velvet cushion on a 2-step base, faint pink glow behind
[3,1] Heart-Portal — magical pink portal with a glowing white heart-with-check icon, animated suggestion (slight glow ring)

Each tile readable instantly: WALL clearly tall+dark, FLOOR clearly walkable+flat,
GRASS clearly hearts on green, HOTEL clearly neon-magenta, CASTLE clearly gold,
HOME clearly building, THRONE clearly seat, PORTAL clearly magical.
```

---

## 背景（フルスクリーン 480×384 → 高解像度なら 960×768 で生成して縮小）

### `bg_title.png` — タイトル画面

```
Pixel art title screen, 16:10 aspect, "マチアプRPG" as huge red-and-gold
JRPG-style logo at the top (use the Japanese text exactly: マチアプRPG),
NO subtitle text whatsoever (do not write "普通の子未実装" or any other text),
below the logo: dramatic night Tokyo skyline silhouette with Tokyo Tower lit red on left,
above the skyline: a small pixel hero (the same hero_yusha character) standing
on top of a giant glowing smartphone like it's a magic carpet,
the phone displays a heart-with-checkmark dating-app icon,
floating pink neon hearts drift to the right of the hero,
deep purple and magenta night sky with stars,
small "恋活" "マッチ中" neon billboards on side buildings (in Japanese kanji),
decorative gold pixel-art border frame, no text in bottom 80px (we add PRESS ENTER programmatically).
NES/SFC pixel art, hard outline, no anti-aliasing.
```

### `bg_throne_room.png` — ボス背景（運営本社・玉座の間）

```
Pixel art background, 16:10, JRPG final boss throne room, NO characters,
massive pink-neon heart-with-checkmark glowing logo on the back wall
(the dating-app icon, two stories tall),
purple-velvet curtains with heart-checkmark embroidery on both sides,
glass walls reveal neon-magenta Tokyo skyline at night (Tokyo Tower visible far),
in the center: empty gold throne with red-pink cushion on a 3-step base,
pink runner carpet leading from camera to throne,
two pillar candles flanking with pink flames, two small heart-shaped potted plants,
reflective glossy purple-tile floor showing neon reflections,
NES/SFC pixel art, hard outline, no anti-aliasing,
moody and intimidating but elegant (this is the lair of 死神, not a demon queen —
keep it more "luxury Shibuya penthouse" than "Diablo hellscape").
```

---

## UI ウィンドウ（オプション、現状コード生成で十分なら不要）

### `ui_window.png`

```
NES-era JRPG dialogue and menu window assets, transparent background,
include four pieces stacked vertically:
1. Wide dialogue box: black fill, white 2px double-border, gold corner pixels, 480×80
2. Status box: same style, 220×80, blank inside
3. Command box: same style, 240×80, blank inside
4. HP/MP bars: red bar (80×8) and blue bar (80×8) with white outline, gradient inside

All four pieces must share identical border style (gold corners, white double-line).
No text inside any element (we render text programmatically).
NES pixel art, hard 1px outline, transparent PNG.
```

---

## 生成・差し替えフロー

1. プロンプトを GPT-4o / Sora / Midjourney に貼る
2. 出力PNGを **同名で** `c:/gm/マチアプRPG/` に保存
3. `game.html` 内の `SPRITE_FILES` を新ファイル名に書き換え（または既存名で上書き）
4. ブラウザリロード → 反映

### ファイル名 ↔ 現在の SPRITE_FILES キー対応

| 新ファイル名 | コード内のキー | 役割 |
|--------------|---------------|------|
| `hero_yusha.png` | `hero` | 勇者 |
| `enemy_troll_girl.png` | `troll` | トロール系女子 |
| `enemy_succubus.png` | `succ` | ワンナイ系サキュバス |
| `enemy_kakou_troll.png` | `kakou` | 加工トロール |
| `enemy_papa_katsu.png` | `papa` | パパ活見習い |
| `enemy_metal_runner.png` | （papa を tint で代用中） | 食い逃げメタル |
| `enemy_ghost_decoy.png` | （succ を tint で代用中） | 当て馬ゴースト |
| `enemy_bomb_rock.png` | （troll を tint で代用中） | 爆弾岩おんな |
| `boss_shinigami.png` | `queen` | 死神（ボス） |
| `npc_futsuu_girl.png` | （内蔵描画） | 普通の子 |
| `tiles_world.png` | `tiles` | マップタイル8種 |
| `ui_window.png` | `ui` | UI枠（任意） |
| `bg_title.png` | `title` | タイトル背景 |
| `bg_throne_room.png` | `bossbg` | ボス背景 |

新3敵（メタル/ゴースト/爆弾岩）は専用画像を作れば、`SPRITE_FILES` にキー追加 → 敵データの `sprite` を新キーに差し替えで反映できる。今は既存4枚を tint で流用中。
