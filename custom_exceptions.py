class IndexValuesException(Exception):
    def __init__(self, message, start_index, end_index):
        super().__init__(message)
        self._start_index = start_index
        self._end_index = end_index

    def start(self):
        return self._start_index

    def end(self):
        return self._end_index


class IncorrectInputException(Exception):
    def __init__(self, message, expected_type):
        super().__init__(message)
        self._expected_type = expected_type

    def expected_type(self):
        return self._expected_type
