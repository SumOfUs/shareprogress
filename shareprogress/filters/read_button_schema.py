import valideer as V
import re

class readButtonSchema():
    def schema(self):
        return {
            # required parameters (marked with a '+' before the key name)
            "+key": V.String(min_length=1),
            "+id": "integer"
        }
