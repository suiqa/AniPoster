import unittest
from imageboard.yandere import Moebooru
from imageboard.booru import Booru, Gelbooru


yandere, gelbooru = Moebooru(), Gelbooru()

class Test_Imagebooru(unittest.IsolatedAsyncioTestCase):
    async def test_yandere_get_post_byid(self):
        answer = await yandere.getByid(123456)
        self.assertEqual(answer.id, 123456)

    async def test_gelbooru_get_post_byid(self):
        answer = await gelbooru.getByid(7735812)
        self.assertEqual(answer.id, 7735812)