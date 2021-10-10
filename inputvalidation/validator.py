from __future__ import annotations

import re
import os
from typing import Any, Callable, Optional, Type


if os.name == "nt":
    def clearScreen():
        os.system("cls")
else:
    def clearScreen():
        os.system("cls")

class Validator:
    def __init__(self, type: Type = str, pattern: Optional[re.Pattern] = None, preCustom: Optional[Callable] = None, postCustom: Optional[Callable] = None, clearScreen: bool = False, default: Optional[str] = None) -> None:
        self.type = type
        self.pattern = pattern
        self.preCustom = preCustom
        self.postCustom = postCustom
        self.clearScreen = clearScreen
        self.default = default

        # Compile the regex pattern if it is a string
        if self.pattern != None and type(self.pattern) == str:
            self.pattern = re.compile(self.pattern)

    def validate(self, string: str) -> bool:
        "Validates the given string using the validator's settings."

        # Calling the preCustom function on the string
        if self.preCustom != None:
            if not self.preCustom(string):
                return False

        # Matching the string with a regex pattern
        if self.pattern != None:
            if not re.match(self.pattern, string):
                return False

        # Try converting the string to self.type
        if self.type != str:
            try:
                self.convert(string)
            except ValueError:
                return False

        # Calling the postCustom function on the string
        if self.postCustom != None:
            if not self.postCustom(string):
                return False

        # If it passed all tests, it is valid
        return True

    def convert(self, string: str) -> Any:
        "Converts the given string to the validator's type."

        # If we have a default value and the string is empty
        if self.default != None and string == "":
            return self.default

        return self.type(string)

    def input(self, prompt: str = "") -> Any:
        "Keeps asking the user for input until it is valid."

        while not self.validate(inp := input(prompt)):
            if self.clearScreen:
                clearScreen()
        return self.convert(inp)
