import aiohttp

from .models.booru import BooruModel, GelbooruModel


class Booru:
    domain = "danbooru.donmai.us"
    get_url = f"https://{domain}/posts.json?limit=1&tags="
    post_url = "/posts.json?"
    rating = ["rating:s", "rating:e"]
    tag = "tag_string"

    async def getByid(self, id_: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.get_url + "id:" + str(id_)) as get:
                result = await get.json()
                return BooruModel(**result[0])

    async def getLast(self, tags=""):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.get_url) as get:
                result = await get.json()
                return BooruModel(**result[0])

    async def getRandom(self, nsfw=False, tags=""):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.get_url + " order:random " + tags) as get:
                result = await get.json()
                return BooruModel(**result[0])

    async def getTagsByid(self, id):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.get_url.replace(self.rating[0], "") + "id:" + str(id)) as get:
                tags = await get.json()
                tag = "".join("#" + tag_item + " " for tag_item in tags[0][self.tag].split())
                return tag[:4096]

class Gelbooru(Booru):
    domain = "gelbooru.com"
    get_url = f"https://{domain}/index.php?page=dapi&s=post&q=index&json=1&limit=1&id="
    tag = "tags"

    async def getByid(self, id_: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.get_url + str(id_)) as get:
                result = await get.json()
                return GelbooruModel(**result["post"][0]) if "post" in result else None