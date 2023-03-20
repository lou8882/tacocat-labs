from utils import constants as c
from utils import pages

def get_site_pages():
    return {
    c.welcome: pages.welcome_page,
    c.invalid_permissions: pages.invalid_permissions_page,
    c.home: pages.home_page,
    c.table: pages.table_page
}