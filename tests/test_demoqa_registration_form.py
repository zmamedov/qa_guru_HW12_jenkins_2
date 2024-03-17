import allure
from allure_commons.types import Severity

from qa_guru_HW12_jenkins_2.pages.registration_page import RegistrationPage


@allure.title("Test of successful user's registration")
@allure.description("Filling all fields in registration form. Submit data. Check that all fields are correct.")
@allure.suite("test_demoqa_registration_form.py")
@allure.issue("https://school.qa.guru/pl/teach/control/lesson/view?id=320799527&editMode=0", "Homework12")
@allure.tag("UI")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "zmamedov")
@allure.feature("Registration of new user")
@allure.story("Successful registration")
@allure.link("https://demoqa.com/automation-practice-form", name="DemoQA Form")
def test_register_new_user():
    registration_page = RegistrationPage()

    with allure.step('Open registration form'):
        registration_page.open()

    with allure.step('Fill registration form and submit data'):
        registration_page.fill_first_name('Gercog')
        registration_page.fill_last_name('Perkins')
        registration_page.fill_user_email('Chester@mail.com')
        registration_page.click_gender_checkbox('Male')
        registration_page.fill_user_number('7890005670')
        registration_page.fill_birthday('1950', 'January', '16')
        registration_page.fill_subject('Chemistry')
        registration_page.click_hobby('Reading')
        registration_page.upload_picture('Chester-Mills.jpeg')
        registration_page.fill_current_address('Chester-Mills, Center')
        registration_page.fill_state('Haryana')
        registration_page.fill_state_city('Karnal')
        registration_page.submit()

    with allure.step('Check that submit data are correct'):
        registration_page.should_registered_user_with(
            'Gercog Perkins',
            'Chester@mail.com',
            'Male',
            '7890005670',
            '16 January,1950',
            'Chemistry',
            'Reading',
            'Chester-Mills.jpeg',
            'Chester-Mills, Center',
            'Haryana Karnal',
        )
