# マチアプRPG

殴って勝つな、撮って通報せよ。3分完結のブラックユーモアRPG。

▶ **Play:** [https://obake0000.github.io/machiapu-rpg/game.html](https://obake0000.github.io/machiapu-rpg/game.html)

## 概要

深夜1時、勇者は寝室でスマホを開く。マッチングアプリの世界に吸い込まれ、
加工バリ盛り女子・副業勧誘ちゃん・占い狂いガール・メンヘラ依存・既婚バレ女、
そして「仲良くなったらね」を繰り返す死神に立ち向かう。
真エンドは、玉座の奥で待つ "普通の子" との定食屋デート。

## 操作

- 矢印キー / 仮想パッドで移動
- Enter（または●ボタン）で決定 / メッセージ送り
- 戦闘コマンド：💋口説く / 🍽️おごる / 📸撮って通報 / 🏃にげる
- Esc で物語シーンをスキップ

## 技術

- 単一HTMLファイル（外部依存ゼロ）
- Canvas + Web Audio 合成BGM
- ピクセルアートは preprocess_sprites.py で背景白抜き

## ファイル

- `game.html` — 本体
- `index.html` — `game.html` へのリダイレクト
- `preprocess_sprites.py` — スプライト前処理ツール
- `LP用_ゲーム概要.md` — ランディングページ用ドキュメント
- `画像生成プロンプト_物語シーン.md` — ChatGPT画像生成プロンプト集
