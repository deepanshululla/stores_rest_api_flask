try:
    from models.store import StoreModel
    from models.item import ItemModel
    from tests.base_test import BaseTest
except ModuleNotFoundError:
    from stores_rest_api_flask.models.store import StoreModel
    from stores_rest_api_flask.models.item import ItemModel
    from stores_rest_api_flask.tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store(self):
        store = StoreModel('test')
        self.assertListEqual(store.items.all(), [],
                             "The store's items length was not 0 even though no items were added.")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(
                StoreModel.find_by_name('test'),
                "Found an store with name 'test' before save_to_db")

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'),
                                 "Did not find an store with name 'test' after save_to_db")

            store.delete_from_db()

            self.assertIsNone(
                StoreModel.find_by_name('test'),
                "Found an store with name 'test' after delete_from_db")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)
            # store doesn't need the item,but item needs the store
            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')

    def test_store_json(self):
        store = StoreModel('test')
        expected = {
            'name': 'test',
            'items': []
        }

        self.assertEqual(
            expected,
            store.json(),
            "The JSON export of the store is incorrect. Received {}, expected {}.".format(store.json(), expected))
