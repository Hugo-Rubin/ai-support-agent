import asyncio
from strands_tools.browser import AgentCoreBrowser
from strands_tools.browser.models import InitSessionAction

async def main():
    browser_tool = AgentCoreBrowser(region="us-east-1")

    action = InitSessionAction(
        type="init_session",
        description="Test AgentCore Browser",
        session_name="final-browser-test"
    )

    print("Initializing browser session...")
    result = browser_tool.init_session(action)

    print("INIT RESULT:", result)

    page = browser_tool.get_session_page("final-browser-test")

    await page.goto(
        "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html"
    )

    print("PAGE TITLE:", await page.title())
    print("PAGE URL:", page.url)

asyncio.run(main())
