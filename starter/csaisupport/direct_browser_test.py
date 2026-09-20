from playwright.async_api import async_playwright
from bedrock_agentcore.tools.browser_client import browser_session
import asyncio

async def main():
    async with async_playwright() as playwright:
        with browser_session("us-east-1") as client:
            ws_url, headers = client.generate_ws_headers()

            browser = await playwright.chromium.connect_over_cdp(
                ws_url,
                headers=headers
            )

            context = browser.contexts[0]
            page = context.pages[0]

            try:
                await page.goto(
                    "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html"
                )

                print("PAGE TITLE:", await page.title())
                print("PAGE URL:", page.url)

            finally:
                await page.close()
                await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
