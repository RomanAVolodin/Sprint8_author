from dataclasses import dataclass


@dataclass
class UserHistoryMap:
    database = 'default'
    table = 'views'
    fields = '(id, user_id, film_id, viewed_frame)'
