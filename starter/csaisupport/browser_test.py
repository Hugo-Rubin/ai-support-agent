from strands_tools.browser import AgentCoreBrowser
from strands_tools.browser.models import InitSessionAction

browser = AgentCoreBrowser(region="us-east-1")
browser._start()

browser.init_session(
    InitSessionAction(
        type="init_session",
        description="Browser navigation test",
        session_name="final-browser-test",
    )
)

page = browser.get_session_page("final-browser-test")

print("PAGE CREATED:", page is not None)
print("STARTING NAVIGATION...")

result = browser._execute_async(
    page.goto(
        "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html",
        wait_until="domcontentloaded",
        timeout=30000,
    )
)

print("NAVIGATION RESULT:", result)
print("URL:", page.url)
print("TITLE:", browser._execute_async(page.title()))
