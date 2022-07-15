import aiohttp
from .models.moebooru import MoebooruModel


class Moebooru:
    domain = "yande.re"
    get_url = f"https://{domain}/post.json?tags="
    post_url = "/post.json?"
    rating = ["rating:s", "rating:e"]
    tag = "tags"

    async def getLast(self, tags=""):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.get_url + f" {tags}") as get:
                result = await get.json()
                return MoebooruModel(**result[0])

    async def getByid(self, id_: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.get_url + "id:" + str(id_)) as get:
                result = await get.json()
                return MoebooruModel(**result[0]) if result != [] else False

    async def getRandom(self, tags=""):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.get_url + "order:random " + tags) as get:
                result = await get.json()
                return MoebooruModel(**result[0])

    async def getTagsByid(self, id):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.get_url + "id:" + str(id)) as get:
                tags = await get.json()
                tag = "".join(
                    "#" + tag_item + " " for tag_item in tags[0][self.tag].split()
                )
                return tag[:4096]
