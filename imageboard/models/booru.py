from pydantic import BaseModel, Field
from typing import Optional

# id: int                                | Айди
# tag: str = Field(alias='tag_string')   | Теги
# file_size: int                         | Размер без сжатия
# sample_file_size: int                  | Размер со средним сжатием
# file_url: str                          | Без сжатия
# preview_file_url: str                  | Сильное сжатие
# sample_url: Optional[str] = None       | Среднее сжатие
# source: Optional[str] = None           | Откуда арт


class BooruModel(BaseModel):
    id: int
    rating: str
    tag: str = Field(alias="tag_string")
    file_url: str
    preview_file_url: str = Field(alias="large_file_url")
    sample_url: Optional[str] = Field(alias="large_file_url")
    source: Optional[str] = None

class GelbooruModel(BooruModel):
    tag: str = Field(alias="tags")
    sample_url: str
    preview_file_url: str = Field(alias="preview_url")
