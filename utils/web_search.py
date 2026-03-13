from ddgs import DDGS


def search_web(query: str) -> str:
    """Perform live web search and return summarized results."""
    try:
        results = DDGS().text(query, max_results=5)

        if not results:
            return ""

        formatted_results = []
        for item in results:
            title = item.get("title", "")
            body = item.get("body", "")
            href = item.get("href", "")

            formatted_results.append(
                f"Title: {title}\nSummary: {body}\nLink: {href}"
            )

        return "\n\n".join(formatted_results)

    except Exception as e:
        return f"Web search failed: {str(e)}"