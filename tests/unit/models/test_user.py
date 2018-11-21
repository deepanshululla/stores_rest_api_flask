try:
    from models.user import UserModel
    from tests.base_test import BaseTest
except ModuleNotFoundError:
    from stores_rest_api_flask.models.user import UserModel
    from stores_rest_api_flask.tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test',
                         "The name of the user after creation does not equal the constructor argument.")
        self.assertEqual(user.password, 'abcd',
                         "The password of the user after creation does not equal the constructor argument.")
