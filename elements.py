# -*- coding: utf-8 -*-

from page_object import PageElement


class CheckBox(PageElement):
    def __set__(self, instance, value):
        if not value:
            return
        self.__get__(instance, instance.__class__)
        instance.webdriver.execute_script(
            "$(arguments[0]).attr('checked', arguments[1]).change();",
            self._locator[1], value)


class ComboBox(PageElement):
    def __set__(self, instance, value):
        if not str(value):
            return
        self.__get__(instance, instance.__class__)
        instance.webdriver.execute_script(
            "$(arguments[0]).val(arguments[1]).change();",
            self._locator[1], value)


class TextBox(PageElement):
    def __set__(self, instance, value):
        if not str(value):
            return
        self.__get__(instance, instance.__class__)
        instance.webdriver.execute_script(
            "$(arguments[0]).val(arguments[1]).blur();",
            self._locator[1], value)
