from playwright.sync_api import Page, expect


def test_login_page_loads(page: Page):
    # Open the login page
    page.goto("http://127.0.0.1:5500/login.html")

    # Verify that the Login heading is visible
    expect(
        page.get_by_role("heading", name="Login")
    ).to_be_visible()


def test_student_login(page: Page):
    # Open the login page
    page.goto("http://127.0.0.1:5500/login.html")

    # Enter student credentials
    page.get_by_label("username").fill("student101")
    page.get_by_label("password").fill("test-password")

    # Click the Login button
    page.get_by_role("button", name="Login").click()

    # Ve+rify successful navigation
    expect(page).to_have_url(
        "http://127.0.0.1:5500/dashboard.html"
    )

    # Verify that the student dashboard is visible
    expect(
        page.get_by_role(
            "heading",
            name="Student Dashboard"
        )
    ).to_be_visible()