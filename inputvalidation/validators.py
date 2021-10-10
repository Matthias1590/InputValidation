from typing import Any, List, Optional, Type

from .validator import Validator


class MultipleChoice(Validator):
    def __init__(self, options: List[Any], type: Type = str, caseSensitive: bool = True, clearScreen: bool = False, default: Optional[str] = None) -> None:
        super().__init__(clearScreen=clearScreen, type=type, default=default)

        self.options = options
        self.type = type
        self.caseSensitive = caseSensitive

        if not self.caseSensitive:
            self.options = [str(option).lower() for option in self.options]
        if len(set(options)) != len(options):
            raise ValueError("List of options contains duplicate option(s).")

    def validate(self, string: str) -> bool:
        if not self.caseSensitive:
            string = string.lower()

        # If we have a default value and the string is empty
        if self.default != None and string == "":
            return True

        return string in self.options
