import unittest
import adshopcart_methods as methods

class AdShopCartAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_new_user_manipulations():
        methods.setUp()
        methods.create_new_user()
        methods.check_user_created()
        methods.check_we_login_with_new_cred()
        methods.delete_new_user()
        methods.login_with_deleted_credentials()
        methods.check_homepage()
        methods.fill_out_contact_us_form()
        methods.tearDown()
