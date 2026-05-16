"""
マチアプRPG スプライト前処理：チェック柄/白背景をα=0に置換し
"<元名>_clean.png" として保存する。game.html の SPRITE_FILES が
ロードする版を切り替える。

実行：
    python preprocess_sprites.py
"""
from PIL import Image
from collections import deque
import os
import glob

SOURCES = {
    "hero":   "ChatGPT Image 2026年5月16日 22_28_58 (1).png",
    "troll":  "ChatGPT Image 2026年5月16日 21_20_56 (2).png",   # ← 元の緑肌トロール
    "succ":   "ChatGPT Image 2026年5月16日 22_28_58 (3).png",
    "queen":  "ChatGPT Image 2026年5月16日 22_32_46 (1).png",
    "kakou":  "ChatGPT Image 2026年5月16日 22_32_46 (2).png",
    "papa":   "ChatGPT Image 2026年5月16日 22_32_47 (3).png",
    "metal":  "ChatGPT Image 2026年5月16日 22_32_47 (4).png",
    "ghost":  "ChatGPT Image 2026年5月16日 22_32_47 (5).png",
    "bomb":   "ChatGPT Image 2026年5月16日 22_32_47 (6).png",
    "futsuu": "ChatGPT Image 2026年5月16日 22_32_47 (7).png",
    "gal":    "ChatGPT Image 2026年5月16日 22_28_58 (2).png",   # 金髪ギャル（別用途用に保持）
}

HERE = os.path.dirname(os.path.abspath(__file__))


def color_dist(a, b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))


def clean(img: Image.Image) -> Image.Image:
    img = img.convert("RGBA")
    w, h = img.size
    px = img.load()

    # 4隅とエッジ中点から背景色を採取
    samples = [
        (0, 0), (w-1, 0), (0, h-1), (w-1, h-1),
        (w//2, 0), (w//2, h-1), (0, h//2), (w-1, h//2),
    ]
    bgs = []
    for x, y in samples:
        r, g, b, _ = px[x, y]
        bgs.append((r, g, b))

    def is_bg(r, g, b):
        # 低彩度＆明るい → checker/white
        mx = max(r, g, b)
        mn = min(r, g, b)
        if mx >= 195 and (mx - mn) <= 28:
            return True
        # 4隅サンプルに近い
        for bg in bgs:
            if color_dist((r, g, b), bg) < 30:
                return True
        return False

    # Floodfill from edges: only kill if color is bg-like
    visited = [[False]*h for _ in range(w)]
    queue = deque()
    for x in range(w):
        queue.append((x, 0))
        queue.append((x, h-1))
    for y in range(h):
        queue.append((0, y))
        queue.append((w-1, y))

    while queue:
        x, y = queue.popleft()
        if x < 0 or x >= w or y < 0 or y >= h:
            continue
        if visited[x][y]:
            continue
        r, g, b, a = px[x, y]
        if not is_bg(r, g, b):
            continue
        visited[x][y] = True
        px[x, y] = (r, g, b, 0)
        queue.append((x+1, y))
        queue.append((x-1, y))
        queue.append((x, y+1))
        queue.append((x, y-1))

    # 追加：完全に独立した「囲まれた背景セル」も一応キル（保険）
    for x in range(w):
        for y in range(h):
            if visited[x][y]:
                continue
            r, g, b, a = px[x, y]
            mx = max(r, g, b); mn = min(r, g, b)
            if mx >= 220 and (mx - mn) <= 12:
                px[x, y] = (r, g, b, 0)

    return img


def main():
    for key, fname in SOURCES.items():
        src = os.path.join(HERE, fname)
        if not os.path.exists(src):
            print(f"[skip] {key}: 元ファイルなし: {fname}")
            continue
        out_name = os.path.splitext(fname)[0] + "_clean.png"
        out = os.path.join(HERE, out_name)
        print(f"[run]  {key}: {fname}")
        img = Image.open(src)
        cleaned = clean(img)
        cleaned.save(out, "PNG")
        print(f"       → {out_name}  ({cleaned.size[0]}x{cleaned.size[1]})")
    print("Done.")


if __name__ == "__main__":
    main()
