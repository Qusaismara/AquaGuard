import json

class PoolManager:

    def load_pools(self, filepath: str) -> list:

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data["pools"]

        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
    def get_pool(self, pools: list, pool_id: str) -> dict:

     for pool in pools:
        if pool["pool_id"].upper() == pool_id.upper():
            return pool
     return None

def get_zone(self, pools: list, pool_id: str, zone_id: str) -> dict:

    pool = self.get_pool(pools, pool_id)

    if pool is None:
        raise ValueError("Pool not found")

    for zone in pool["zones"]:
        if zone["zone_id"].upper() == zone_id.upper():
            return zone

    return None    