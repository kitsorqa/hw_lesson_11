import allure
from selene import browser, have, by, command
from demoqa_tests.model import resource


class RegistrationPage:

    @allure.step("Открытие страницы с формой")
    def open_page(self):
        browser.open('/automation-practice-form')

    @allure.step("Удаление рекламных баннеров")
    def remove_banners(self):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    @allure.step("Ввод имени")
    def fill_first_name(self, first_name):
        browser.element("#firstName").type(first_name)

    @allure.step("Ввод фамилии")
    def fill_last_name(self, last_nane):
        browser.element("#lastName").type(last_nane)

    @allure.step("Ввод email")
    def fill_email_student(self, email):
        browser.element("#userEmail").type(email)

    @allure.step("Выбор гендера")
    def choose_student_gender(self, value):
        browser.element(by.text(value)).perform(command.js.click())

    @allure.step("Ввод мобильного телефона")
    def fill_phone_number(self, number):
        browser.element("#userNumber").type(number)

    @allure.step("Заполнение даты рождения")
    def fill_student_birthday(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element('.react-datepicker__month-select').click().element(f'option[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click().element(f"option[value='{year}']").click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    @allure.step("Ввод предметов учебной программы")
    def fill_subjects_of_student(self, *args):
        for word in args:
            browser.element('#subjectsInput').type(word.title()).press_enter()

    @allure.step("Нажатие кнопки submit")
    def submit_button(self):
        browser.element('#submit').click()

    @allure.step("Ввод хобби")
    def fill_hobbies_student(self, *args):
        for arg in args:
            browser.element(by.text(arg)).click()

    @allure.step("Загрузка картинки")
    def upload_picture(self, filename):
        browser.element('#uploadPicture').set_value(resource.file_path(filename))

    @allure.step("Ввод адреса")
    def fill_current_address(self, *args):
        browser.element('#currentAddress').type(*args)
        browser.execute_script('window.scrollBy(0, 400);')

    @allure.step("Выбор региона")
    def fill_current_state(self, state):
        browser.element('#state').click().element(by.text(state)).click()

    @allure.step("Выбор города")
    def fill_current_city(self, city):
        browser.element('#city').click().element(by.text(city)).click()

    @allure.step("Проверка формы на соответствие данным")
    def assert_registered_user_info(self, full_name, email, gender, mobile_phone, birthday, subjects, hobbies,
                                    file_name, address, state_and_city):
        browser.element(".table").all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_phone,
                birthday,
                subjects,
                hobbies,
                file_name,
                address,
                state_and_city
            )
        )
