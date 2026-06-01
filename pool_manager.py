import json

class PoolManager:

    def load_pools(self, filepath: str) -> list:

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data["pools"]

        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")