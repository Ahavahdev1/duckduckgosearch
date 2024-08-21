from duckduckgo_search import DDGS, AsyncDDGS
import asyncio

async def main():
    # Initialize DDGS and AsyncDDGS
    ddgs = DDGS()
    async_ddgs = AsyncDDGS()

    # Get user input for search
    user_query = input("Enter your search query: ")

    # 1. AI Chat
    try:
        chat_response = ddgs.chat(user_query, model='claude-3-haiku')
        print("\n--- AI Chat Response ---")
        print(chat_response if chat_response else "No response from AI Chat.")
    except Exception as e:
        print(f"Error in AI Chat: {e}")
    print("\n")

    # 2. Text Search
    try:
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
    except Exception as e:
        print(f"Error in Text Search: {e}")
    print("\n")

    # 3. Instant Answers
    try:
        answer_results = ddgs.answers(user_query)
        print("--- Instant Answers ---")
        if answer_results:
            for answer in answer_results:
                print(f"Answer: {answer}")
                print("-" * 50)
        else:
            print("No instant answers found.")
    except Exception as e:
        print(f"Error in Instant Answers: {e}")
    print("\n")

    # 4. Find PDF files
    try:
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
    except Exception as e:
        print(f"Error in PDF Search: {e}")
    print("\n")

    # 5. Video Search
    try:
        video_results = ddgs.videos(
            keywords=user_query,
            safesearch="moderate",
            timelimit="w",
            resolution="high",
            duration="medium",
            max_results=5
        )
        print("--- Video Search Results ---")
        if video_results:
            for video in video_results:
                print(f"Title: {video['title']}")
                print(f"Link: {video['content']}")
                print(f"Description: {video['description']}")
                print(f"Duration: {video['duration']}")
                print(f"Published: {video['published']}")
                print("-" * 50)
        else:
            print("No videos found.")
    except Exception as e:
        print(f"Error in Video Search: {e}")
    print("\n")

    # 6. News Search
    try:
        news_results = ddgs.news(
            keywords=user_query,
            safesearch="moderate",
            timelimit="w",
            max_results=5
        )
        print("--- News Search Results ---")
        if news_results:
            for news in news_results:
                print(f"Title: {news['title']}")
                print(f"URL: {news['url']}")
                print(f"Date: {news['date']}")
                print(f"Source: {news['source']}")
                print(f"Body: {news['body']}")
                print("-" * 50)
        else:
            print("No news found.")
    except Exception as e:
        print(f"Error in News Search: {e}")
    print("\n")

    # 7. Map Search
    try:
        map_results = ddgs.maps(
            keywords=user_query,
            max_results=5
        )
        print("--- Map Search Results ---")
        if map_results:
            for place in map_results:
                print(f"Title: {place['title']}")
                print(f"Address: {place['address']}")
                print(f"Latitude: {place['latitude']}")
                print(f"Longitude: {place['longitude']}")
                print(f"Phone: {place['phone']}")
                print(f"URL: {place['url']}")
                print("-" * 50)
        else:
            print("No map results found.")
    except Exception as e:
        print(f"Error in Map Search: {e}")
    print("\n")

    # 8. Translate
    try:
        translation_results = ddgs.translate(
            keywords=user_query,
            to="es"  # Change the target language code as needed
        )
        print("--- Translation Results ---")
        if translation_results:
            for translation in translation_results:
                print(f"Original: {translation['original']}")
                print(f"Translated: {translation['translated']}")
                print("-" * 50)
        else:
            print("No translations found.")
    except Exception as e:
        print(f"Error in Translation: {e}")
    print("\n")

    # 9. Suggestions
    try:
        suggestions_results = ddgs.suggestions(user_query)
        print("--- Suggestions Results ---")
        if suggestions_results:
            for suggestion in suggestions_results:
                print(f"Suggestion: {suggestion['phrase']}")
                print("-" * 50)
        else:
            print("No suggestions found.")
    except Exception as e:
        print(f"Error in Suggestions: {e}")
    print("\n")

    # 10. Search with a Proxy (using Tor Browser)
    # ddgs_with_proxy = DDGS(proxy="tb")  # "tb" is an alias for "socks5://127.0.0.1:9150"
    # results = ddgs_with_proxy.text(user_query, max_results=50)

if __name__ == "__main__":
    asyncio.run(main())
