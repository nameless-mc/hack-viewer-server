# Hack-Viewer Server

サポーターズ技育 CAMP 2022 vol9 ハッカソン作品

# ドキュメント

- [API ドキュメント](./doc/api/api.md)
- [DB ドキュメント](./doc/db/db.md)

# 技術スタック

## API サーバー

- Python
  - FastAPI
  - SQLAlchemy
- MySQL(本番環境用)
- SQLite(local, develop 環境用)

## インフラ

- Docker
  - API サーバー, WEB サーバー, DB サーバーをそれぞれ Docker で管理
