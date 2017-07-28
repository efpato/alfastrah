# -*- coding: utf-8 -*-

from page_object import PageObject, PageElement, PageElements
from page_object.elements import Button, Link, Textbox
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements import CheckBox, ComboBox, TextBox


class KaskoCalcPage(PageObject):
    URL = "https://www.alfastrah.ru/individuals/auto/kasko/calc/"

    city = Link(xpath="//div[@class='phones']/a")
    region = Textbox(css="input[name='REGION']")
    fancybox_close = Link(xpath=("//a[@class='fancybox-item fancybox-close'"
                                 " and @title='Закрыть']"))
    cbox_close = Button(id="cboxClose")
    more_makers = Link(xpath="//a[@href='#more-makers']")
    car_set = ComboBox(css="select#car_set")
    cost = TextBox(css="input[name='equipments_cost_cars_input']")
    equipments_100km = CheckBox(css="input[name='equipments_100km']")
    equipments_credit = CheckBox(css="input[name='equipments_credit']")
    drivers_unlimited = CheckBox(css="input[name='drivers_unlimited']")
    drivers_min_age = TextBox(css="#drivers_minimum_age")
    drivers_min_experience = TextBox(css="#drivers_minimum_experience")
    add_driver = Link(link_text="Добавить водителя")
    select_options = Button(xpath="//button[contains(text(),'Выбрать опции')]")
    risks = PageElements(css="input[name='main_risk_id']")
    at_system = ComboBox(css="select[name='at_system_model_id']")

    def _fancybox_close(self):
        try:
            self.fancybox_close.click()
            WebDriverWait(self.webdriver, 10).until_not(
                lambda d: d.find_element_by_xpath(
                    "//div[contains(@class,'fancybox-overlay')]"
                ).is_displayed(),
                "Hide fancybox timed out")
        except:
            pass

    def colorbox_close(self):
        self.cbox_close.click()
        WebDriverWait(self.webdriver, 10).until_not(
            lambda d: d.find_element_by_id("cboxOverlay").is_displayed(),
            "Hide colrbox timed out")

    def wait_preloader(self, timeout=30):
        WebDriverWait(self.webdriver, timeout).until_not(
            EC.visibility_of_element_located((By.ID, "loader")),
            "Hide preloader timed out")

    def City(self, value):
        self.city.click()
        self.region = value
        PageElement(xpath="//ul[@class='regions']/li/a[text()='%s']" %
                    value).__get__(self, self.__class__).click()
        self._fancybox_close()

    def brand(self, value):
        self.more_makers.click()
        Link(link_text=value).__get__(self, self.__class__).click()

    def model(self, value):
        Link(xpath="//input[@data-model-name='%s']" % value).__get__(
            self, self.__class__).click()
        self.wait_preloader()
        Button(xpath="//button[contains(text(),'Далее')]").__get__(
            self, self.__class__).click()
        self.wait_preloader()

    def year(self, value):
        Link(xpath="//input[@name='equipments_year' and @value='%s']" %
             value).__get__(self, self.__class__).click()
        self.wait_preloader()

    def CarSet(self):
        options = self.car_set.find_elements_by_tag_name("option")
        index = int(len(options) / 2)
        value = options[index].get_attribute("value")
        self.car_set = value
        self.wait_preloader()

    def drivers_birthday(self, i, value):
        index = i if i > 0 else ""
        TextBox(css="input[name='drivers_birthday[%s]']" % index).__set__(
            self, value)

    def drivers_experience(self, i, value):
        index = i if i > 0 else ""
        TextBox(css="input[name='drivers_experience[%s]']" % index).__set__(
            self, value)

    def range_limit(self, value):
        if not str(value):
            return

        Button(xpath="//input[@name='range_limit_id' and @data-name='%s']" %
               value).__get__(self, self.__class__).click()
        self.wait_preloader()

    def franchise(self, value):
        if not str(value):
            return

        res = PageElements(xpath="//input[@name='main_franchise']").__get__(
            self, self.__class__)
        for i, button in enumerate(res):
            if i == len(res) - 1:
                button.click()
                break
            else:
                cur_value = int(res[i].get_attribute("value"))
                next_value = int(res[i + 1].get_attribute("value"))
                if cur_value <= value < next_value:
                    button.click()
                    break
        self.wait_preloader()

    @property
    def result(self):
        try:
            programs = PageElements(
                xpath="//input[@name='kasko_program_id']").__get__(
                    self, self.__class__)

            return [(program.get_attribute("data-name"),
                     program.get_attribute("data-price"))
                    for program in programs]
        except TimeoutException:
            return []
