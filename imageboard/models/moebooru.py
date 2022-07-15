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


class MoebooruModel(BaseModel):
    id: int
    rating: str
    tag: str = Field(alias="tags")
    file_size: int
    sample_file_size: int
    file_url: str
    preview_file_url: str = Field(alias="preview_url")
    sample_url: Optional[str] = None
    source: Optional[str] = None
