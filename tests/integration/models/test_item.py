
try:
    from models.item import ItemModel
    from tests.base_test import BaseTest
except ModuleNotFoundError:
    from stores_rest_api_flask.models.item import ItemModel
    from stores_rest_api_flask.tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))
