from pydantic import BaseConfig
from pydantic.fields import ModelField


class ConStr(str):
    min_length = 0
    max_length = 0

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: str, field: ModelField, config: BaseConfig):
        if not isinstance(value, str):
            raise ValueError('This value is only str')

        if not cls.min_length <= len(value) <= cls.max_length:
            raise ValueError('This value length {} ~ {}'.format(cls.min_length, cls.max_length))

        return value
