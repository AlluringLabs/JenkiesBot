from unittest import TestCase
from jenkiesbot.adapters import Adapter


class AdapterTest(TestCase):

    def setUp(self):
        self.adapter = Adapter()
        self.test_ctx = {'test': 'test'}

    def tearDown(self):
        self.adapter = None

    def test_set_context_sets_context_attribute(self):
        self.adapter.set_context(self.test_ctx)
        self.assertEqual(self.adapter.context, self.test_ctx)

    def test_get_context_returns_context_attribute(self):
        self.adapter.context = self.test_ctx
        self.assertEqual(self.adapter.get_context(), self.test_ctx)
