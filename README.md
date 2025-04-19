# Next Degital Library MCP Server

このプロジェクトは、国立国会図書館の[次世代デジタルライブラリー (NDL)](https://lab.ndl.go.jp) のAPIを利用して、書籍の検索を行うためのMCPサーバーです。
このツールを使用することでAIエージェントが書籍情報の収集・検索を行うことが可能です。

## ツール

- **search_books**
  - 資料の横断検索が可能です。
  - 入力値
    - `keyword`(string): 検索キーワード
- **search_in_book**
  - 指定した資料内の全文検索が可能です。
  - 入力値
    - `book_id`(string): 資料のPID
    - `keyword`(string): 検索キーワード
- **get_page**
  - 指定したページのデータが取得可能です。
  - 入力値
    - `book_id`(string): 資料のPID
    - `page_number`(int): ページ番号

## 前提条件

- Python 3.13以上

## 使用方法

### MCP設定

MCPの設定ファイルに以下の記述を追加してください。

```json
{
  "mcpServers": {
    "ndl": {
      "command": "/path/to/uv",
      "args": [
          "--directory",
          "/path/to/ndl-mcp",
          "run",
          "ndl.py"
      ]
    }
  }
}
```

## 注意事項

- 本ツールによって提供される資料データは自由に二次利用が可能です。
- 二次利用する際は[次世代デジタルライブラリー](https://lab.ndl.go.jp/service/tsugidigi/)の利用規約を必ずご確認いただき、規約に従ってご利用ください。
