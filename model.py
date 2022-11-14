from manager import BaseManager
from utils import Miscellaneous


class MetaModel(type):
    manager_class = BaseManager

    def _get_manager(cls):
        return cls.manager_class(model_class=cls)

    @property
    def objects(cls):
        return cls._get_manager()


class BaseModel(metaclass=MetaModel):
    table_name = ""

    def __init__(self, **row_data):
        for field_name, value in row_data.items():
            setattr(self, field_name, value)

    def __repr__(self):
        dq = '"'
        attrs_format = ", ".join(
            [f'"{field}":{value if (str(value).isnumeric() or Miscellaneous.is_float(value)) else dq + value + dq}' for field, value in self.__dict__.items()])
        # return f"{{{self.__class__.__name__}: {{{attrs_format}}}}}"
        return f"{{{attrs_format}}}"

    @classmethod
    def get_fields(cls):
        return cls._get_manager()._get_fields()
