import csv 
from datetime import datetime

class AlertManager:
    def load_alerts(self,filepath:str) ->list:
        alerts=[]
        try:
            with open(filepath,"r",encoding="utf-8") as file:
                reader=csv.DictReader(file)
                for row in reader:
                    row["confidence"]=float(row["confidence"])
                    row["response_time_s"]=int(row["response_time_s"])
                    alerts.append(row)
            return alerts
        except FileNotFoundError:
            return []
        
        
    def save_alerts(self,alerts:list,filepath:str) ->None:
        fieldnames=["alert_id", "pool_id", "zone_id", "timestamp", "confidence", "status", "response_time_s"] 
        with open(filepath, "w", newline="", encoding="utf-8") as file:
            writer=csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(alerts)
        print(f"Alerts saved to {filepath}")              