from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import json
import logging

mcp = FastMCP("ndl")

API_BASE_URL = "https://lab.ndl.go.jp"

async def make_request(url: str) -> dict[str, Any] | None:
    """Make a GET request to the NDL API."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=10.0)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
@mcp.tool()
async def search_books(keyword: str) -> dict[str, Any] | None:
    """Search for books using the NDL API."""
    url = f"{API_BASE_URL}/dl/api/book/search?keyword={keyword}"
    data = await make_request(url)

    if not data:
        return None
    
    books = []
    for book in data["list"]:
        books.append(
            f"""
Id: {book['id']}
Title: {book['title']}
Volume: {book['volume']}
Responsibility: {book['responsibility']}
Publishyear {book['publishyear']}
            """
        )

    return "\n---\n".join(books)

@mcp.tool()
async def search_in_book(book_id: str, keyword: str) -> dict[str, Any] | None:
    """Search for a keyword in a book using the NDL API."""
    url = f"{API_BASE_URL}/dl/api/page/search?f-book={book_id}&q-contents={keyword}"
    data = await make_request(url)

    if not data:
        return None

    pages = []
    for page in data["list"]:
        pages.append(
            f"""
Id: {page['id']}
PageNumber: {page['page']}
Contents: {page['contents']}
            """
        )
    
    return "\n---\n".join(pages)

@mcp.tool()
async def get_page(book_id: str, page_number: int) -> dict[str, Any] | None:
    """Get a specific page of a book using the NDL API."""
    url = f"{API_BASE_URL}/dl/api/page/{book_id}_{page_number}"
    data = await make_request(url)

    if not data and data["coordjson"] is None:
        return None
    
    logging.info(f"ContentText: {data['coordjson']}")

    coordjson = json.loads(data["coordjson"])
    content_text = "".join([item["contenttext"] for item in coordjson])

    return f"""
ContentText: {content_text}
    """
    
if __name__ == "__main__":
    mcp.run(transport='stdio')