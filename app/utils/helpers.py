from utils import constants as c
from components import pages

def get_site_pages():
    return {
    c.welcome: pages.welcome_page,
    c.invalid_permissions: pages.invalid_permissions_page,
    c.home: pages.home_page,
    c.table_maker: pages.table_maker_page,
    c.table: pages.table_page,
    c.line_maker: pages.line_maker_page,
    c.line: pages.line_page
}