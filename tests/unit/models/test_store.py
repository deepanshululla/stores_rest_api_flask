try:
    from models.store import StoreModel
    from tests.base_test import BaseTest
except ModuleNotFoundError:
    from stores_rest_api_flask.models.store import StoreModel
    from stores_rest_api_flask.tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual(store.name, 'test',
                         "The name of the store after creation does not equal the constructor argument.")
