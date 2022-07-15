import aiohttp

from .models.booru import BooruModel


class Booru:
    domain = "danbooru.donmai.us"
    get_url = f"https://{domain}/posts.json?limit=1&tags=rating:s"
    post_url = "/posts.json?"
    rating = ["rating:s", "rating:e"]
    tag = "tag_string"

    async def getByid(self, id_: int):
        async with aiohttp.ClientSession() as session:
            if nsfw:
                self.get_url = self.get_url.replace(self.rating[0], self.rating[1])
            async with session.get(self.get_url + " id:" + str(id)) as get:
                result = await get.json()
                return BooruModel(**result[0])

    async def getLast(self, nsfw=False, tags=""):
        async with aiohttp.ClientSession() as session:
            if nsfw:
                self.get_url = self.get_url.replace(
                    self.rating[0], self.rating[1] + " " + tags
                )
            async with session.get(self.get_url) as get:
                result = await get.json()
                return BooruModel(**result[0])

    async def getRandom(self, nsfw=False, tags=""):
        async with aiohttp.ClientSession() as session:
            if nsfw:
                self.get_url = self.get_url.replace(self.rating[0], self.rating[1])
            async with session.get(self.get_url + " order:random " + tags) as get:
                result = await get.json()
                return BooruModel(**result[0])

    async def getTagsByid(self, id):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.get_url.replace(self.rating[0], "") + "id:" + str(id)
            ) as get:
                tags = await get.json()
                tag = ""
                for tag_item in tags[0][self.tag].split():
                    tag += "#" + tag_item + " "
                return tag[:4096]
