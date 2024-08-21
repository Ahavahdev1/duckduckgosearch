from duckduckgo_search import DDGS, AsyncDDGS
import asyncio

async def main():
    # Initialize DDGS and AsyncDDGS
    ddgs = DDGS()
    async_ddgs = AsyncDDGS()

    # Get user input for search
    user_query = input("Enter your search query: ")

    # 1. AI Chat
    chat_response = ddgs.chat(user_query, model='claude-3-haiku')
    print("\n--- AI Chat Response ---")
    print(chat_response if chat_response else "No response from AI Chat.")
    print("\n")

    # 2. Text Search
    text_results = await async_ddgs.atext(user_query, max_results=5)
    print("--- Text Search Results ---")
    if text_results:
        for result in text_results:
            print(f"Title: {result['title']}")
            print(f"Link: {result['href']}")
            print(f"Snippet: {result['body']}")
            print("-" * 50)
    else:
        print("No results found.")
    print("\n")

    # 3. Instant Answers
    answer_results = ddgs.answers(user_query)
    print("--- Instant Answers ---")
    if answer_results:
        for answer in answer_results:
            print(f"Answer: {answer}")
            print("-" * 50)
    else:
        print("No instant answers found.")
    print("\n")

    # 4. Find PDF files
    pdf_results = ddgs.text(f"{user_query} filetype:pdf", max_results=10)
    print("--- PDF Search Results ---")
    if pdf_results:
        for pdf in pdf_results:
            print(f"Title: {pdf['title']}")
            print(f"Link: {pdf['href']}")
            print(f"Snippet: {pdf['body']}")
            print("-" * 50)
    else:
        print("No PDF files found.")
    print("\n")

    # 5. Search with a Proxy (using Tor Browser)
    # ddgs_with_proxy = DDGS(proxy="tb")  # "tb" is an alias for "socks5://127.0.0.1:9150"
    # results = ddgs_with_proxy.text(user_query, max_results=50)

if __name__ == "__main__":
    asyncio.run(main())
