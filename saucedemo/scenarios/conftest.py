import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="Firefox",
        help="my option: Chrome or Firefox",
        choices=("Chrome", "Firefox"),
    )

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")