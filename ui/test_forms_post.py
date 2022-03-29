from ui.test_case_ui import TestCaseUi
from selenium.webdriver.common.by import By


class TestFormsPost(TestCaseUi):

    def test_send_form(self):
        self.driver.get(self.getTestUrl('forms/post'))

        assert self.driver.find_element(By.XPATH, '/html/body/form/p[1]/label').text == 'Customer name:'
        assert self.driver.find_element(By.XPATH, '/html/body/form/p[2]/label').text == 'Telephone:'
        assert self.driver.find_element(By.XPATH, '/html/body/form/p[3]/label').text == 'E-mail address:'

        self.driver.find_element(By.XPATH, '/html/body/form/p[1]/label/input').send_keys('Lisa')
        self.driver.find_element(By.XPATH, '/html/body/form/p[2]/label/input').send_keys('+7-(999)-999-99-99')
        self.driver.find_element(By.XPATH, '/html/body/form/p[3]/label/input').send_keys('test@test.com')

        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/legend').text == 'Pizza Size'

        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[1]/label').text == 'Small'
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[2]/label').text == 'Medium'
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[3]/label').text == 'Large'

        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[1]/label/input').is_enabled()
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[2]/label/input').is_enabled()
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[3]/label/input').is_enabled()

        self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[1]/label/input').click()
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[1]/label/input').is_selected()

        self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[2]/label/input').click()
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[2]/label/input').is_selected()

        self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[3]/label/input').click()
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[1]/p[3]/label/input').is_selected()

        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/legend').text == 'Pizza Toppings'

        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[1]').text == 'Bacon'
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[2]').text == 'Extra Cheese'
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[3]').text == 'Onion'
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[4]').text == 'Mushroom'

        self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[1]/label/input').click()
        self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[2]/label/input').click()
        self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[3]/label/input').click()
        self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[4]/label/input').click()

        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[1]/label/input').is_selected()
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[2]/label/input').is_selected()
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[3]/label/input').is_selected()
        assert self.driver.find_element(By.XPATH, '/html/body/form/fieldset[2]/p[4]/label/input').is_selected()

        assert self.driver.find_element(By.XPATH, '/html/body/form/p[4]/label').text == 'Preferred delivery time:'
        self.driver.find_element(By.XPATH, '/html/body/form/p[4]/label/input').send_keys('20:59')

        assert self.driver.find_element(By.XPATH, '/html/body/form/p[5]/label').text == 'Delivery instructions:'
        self.driver.find_element(By.XPATH, '/html/body/form/p[5]/label/textarea').send_keys('Just brink that')

        self.driver.find_element(By.XPATH, '/html/body/form/p[6]/button').click()








