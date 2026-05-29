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
                    