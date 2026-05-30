import json

class PoolManager:
    def load_pools(self, filepath: str) -> list:
        try:
            with open(filepath,"r",encoding="utf-8") as file:
                data=json.load(file)
                return data["pools"]
            
        except FileNotFoundError:
            raise FileNotFoundError(f"pool file not found{filepath}")
        
    def get_pool(self, pools: list, pool_id: str) -> dict:
        for pool in pools:
            if pool["pool_id"].upper()== pool_id.upper():
              return pool
        return None   
           
    def get_zone(self ,pools:list, pool_id: str,zone_id: str)->dict:
        pool=self.get_pool(pools, pool_id)
        if not pool:
            raise ValueError("pool not found")
        
        for zone in pool["zones"]:
            if zone["zone_id"].upper()==zone_id.upper():
                return zone 
            
        return None 
    
    def display_pools(self,pools:list) -> None:
        print("Pool ID  | Name            | Size (m)    | Zones | Camera Coverage")
        print("-------- |-----------------|-------------|-------|----------------")
        
        for pool in pools:
            cameras=",".join(z['camera'] for z in pool["zones"])
            size= f"{pool['length_m']} X {pool['width_m']}"
            
            print(
                f"{pool['pool_id']:<8} | "
                f"{pool['name']:<15} | "
                f"{size:<11} | "
                f"{len(pool['zones']):<5} | "
                f"{cameras}"
                 
            )   