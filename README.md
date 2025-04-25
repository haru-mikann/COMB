# COMB - Command Optimized Manager Bot

<p>
  <!-- <a href="URL TO JUMP TO ANOTHER PAGE" target="_blank"> -->
    <img width="100%" src="https://github.com/user-attachments/assets/6d438898-2c26-4484-bbd1-61d0b8103c47" alt="COMB Banner"></a>
</p>

COMB は様々な場面でユーザーのオンラインアクティビティをサポートする Discord ボットです。
コマンド操作などのインタラクティブな方法で簡単かつ迅速に機能を利用できます。

## 概要

COMB はユーザーの様々なオンラインアクティビティを Discord 上でサポートするボットで、天気情報の取得や YouTube 動画のダウンロードなどの機能を提供します。

## システム構成

システムは主に 2 つのコンポーネントで構成されています：

1. **Discord ボット（bot/）**: Discord との連携を担当し、ユーザーからのコマンドを受け付けます
2. **API サーバー（api/）**: 一部の機能（特に YouTube ダウンロード）を処理するバックエンドサービス

両方のサービスは Docker コンテナとして実装され、docker-compose で管理されています。

## 機能

### Discord Bot 機能

- **?hello**: 挨拶を返す簡単なコマンド
- **?get_ip**: サーバーのグローバル IP アドレスを表示
- **?tokyo_weather**: 東京の天気情報を表示
- **?aichi_weather**: 愛知県の天気情報を表示
- **?yd [URL]**: YouTube の動画をダウンロードするリクエストを API サーバーに送信
- **?helpme**: 利用可能なコマンド一覧を表示

### API サーバー機能

- **/download_video**: YouTube の動画をダウンロードするエンドポイント（Discord ボットから呼び出される）
- **/tmp_video/{file_name}**: ダウンロードしたビデオファイルを提供するエンドポイント

## 技術スタック

- **言語**: Python
- **Discord ボット**: discord.py
- **API サーバー**: FastAPI
- **YouTube ダウンロード**: yt-dlp
- **コンテナ化**: Docker & Docker Compose
- **その他ライブラリ**:
  - httpx（非同期 HTTP 通信）
  - requests（HTTP 通信）
  - dotenv（環境変数管理）

## デプロイ

Docker Compose を使用して、単一のコマンドで両方のサービスをデプロイできます：

```bash
docker-compose up -d
```

API サーバーはポート 8000 で公開され、ボットサービスは Discord と通信します。

## プロジェクト構造

```
COMB/
├── api/                  # APIサーバー
│   ├── Dockerfile        # APIコンテナ構成
│   ├── index.py          # FastAPIアプリケーション
│   ├── module/
│   │   └── youtube.py    # YouTube動画ダウンロード機能
│   └── requirements.txt  # 依存関係
├── bot/                  # Discordボット
│   ├── Dockerfile        # ボットコンテナ構成
│   ├── main.py           # Discordボットのメイン処理
│   ├── module/
│   │   ├── weather.py    # 天気情報取得機能
│   │   └── ...
│   └── requirements.txt  # 依存関係
└── compose.yml           # Docker Compose設定
```
