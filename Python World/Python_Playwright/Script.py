from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Launch browser in visible mode with slow motion and maximized window
        browser = p.chromium.launch(headless=False, slow_mo=200, args=["--start-maximized"])  # slow_mo=200ms between actions

        # Create context with full screen size (simulate maximized window)
        context = browser.new_context(no_viewport=True )

        # Open a new page in this context
        page = context.new_page()

        # Go to the demo login site
        page.goto("https://www.saucedemo.com/")

        # Fill username slowly
        page.type('input[name="user-name"]', 'standard_user', delay=100)  # delay=100ms per character

        # Fill password slowly
        page.type('input[name="password"]', 'secret_sauce', delay=100)

        # Click login button
        page.click('input[name="login-button"]')

        # Wait to observe result
        page.wait_for_timeout(5000)

        # Close browser
        browser.close()

if __name__ == "__main__":
    run()
