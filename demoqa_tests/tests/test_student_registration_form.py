import allure
import pytest
from allure_commons.types import Severity

from demoqa_tests.model.pages.registration_page import RegistrationPage


@allure.tag("allure test #1")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Rostislav")
@allure.feature('Форма студента')
@allure.story('Заполнение формы валидными данными')
@allure.link("https://github.com", name='Testing')
@allure.title("Successful test for fill form")
def test_filling_student_registration_from(browser_manager):
    rp = RegistrationPage()

    rp.open_page()
    rp.remove_banners()
    rp.fill_first_name("Test")
    rp.fill_last_name("Sidorov")
    rp.fill_email_student("test@test.test")
    rp.choose_student_gender("Male")
    rp.fill_phone_number("8800553535")
    rp.fill_student_birthday("2005", "11", "30")
    rp.fill_subjects_of_student('computer science')
    rp.fill_hobbies_student("Sports", "Reading")
    rp.upload_picture('kapibara.png')
    rp.fill_current_address("Улица Пушкина, дом Котолушкина")
    rp.fill_current_state("NCR")
    rp.fill_current_city("Noida")
    rp.submit_button()
    rp.assert_registered_user_info(
        full_name="Test Sidorov",
        email="test@test.test",
        gender="Male",
        mobile_phone="8800553535",
        birthday="30 November,2005",
        subjects="Computer Science",
        hobbies="Sports, Reading",
        file_name="kapibara.png",
        address="Улица Пушкина, дом Котолушкина",
        state_and_city="NCR Noida"
    )