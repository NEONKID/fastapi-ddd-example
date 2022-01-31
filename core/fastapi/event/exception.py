class InvalidEventTypeException(Exception):
    def __init__(self):
        super().__init__("Event must inherit BaseEvent")


class InvalidParameterTypeException(Exception):
    def __init__(self):
        super().__init__("Parameter must inherit BaseModel")


class EmptyContextException(Exception):
    def __init__(self):
        super().__init__("Event context is empty. check if middleware configured well")


class ParameterCountException(Exception):
    def __init__(self):
        super().__init__("Event has too many parameter")


class RequiredParameterException(Exception):
    def __init__(self, cls_name):
        super().__init__(f"`{cls_name}` event require parameter")
