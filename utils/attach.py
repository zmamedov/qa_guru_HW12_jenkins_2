import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='Screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(body=log, name='Logs', attachment_type=AttachmentType.TEXT, extension='.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(body=html, name='HTML', attachment_type=AttachmentType.HTML, extension='.html')


def add_video(browser):
    pass
