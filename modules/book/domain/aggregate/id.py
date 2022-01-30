from pydantic import PositiveInt

from core.snowflake import seq


class BookId(PositiveInt):
    gt = 1

    @staticmethod
    def next_id() -> 'BookId':
        return BookId(seq.__next__())
