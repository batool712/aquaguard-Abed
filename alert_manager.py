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
        
        
        
    def log_alert(self, alerts: list, pool_id: str, zone_id: str, confidence: float, status: str, response_time_s: int) -> list:
        if status not in ["Rescued", "False_Alarm", "Missed"]:
            raise ValueError(f"Invalid status:{status}")  
        
        if  not 0.0 <= confidence <=1.0 :
            raise ValueError("Confidence must be between 0.0 and 1.0")  
        
        new_id=f"ALT{len(alerts)+ 1:03d}" 
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        new_alert = {
        "alert_id": new_id,
        "pool_id": pool_id,
        "zone_id": zone_id,
        "timestamp": timestamp,
        "confidence": confidence,
        "status": status,
        "response_time_s": response_time_s
        }
        alerts.append(new_alert)
        
        print(f"Alert logged: {new_id} — {status} in {pool_id}/{zone_id} (confidence: {confidence:.2f}, response: {response_time_s}s)")
        return alerts
    
    def get_by_zone(self, alerts: list, pool_id: str, zone_id: str) -> list:
        if not isinstance(alerts, list):
            raise TypeError("alerts must be a list")

        filtered_alerts=[]
        for alert in alerts:
            if (alert["pool_id"].upper()==pool_id.upper() and  alert["zone_id"].upper()==zone_id.upper()):
                filtered_alerts.append(alert)

        return filtered_alerts

    def summary_stats(self, alerts: list) -> dict:
        if not alerts:
            return {}
        
        total= len(alerts)
        rescued= sum(1 for a in alerts if a["status"] == "Rescued")
        false_alarms= sum(1 for a in alerts if a["status"] == "False_Alarm")
        missed = sum(1 for a in alerts if a["status"] == "Missed")
        avg_conf = sum(a["confidence"] for a in alerts) / total
        response_times = [a["response_time_s"] for a in alerts if a["response_time_s"] > 0]
        avg_response  = sum(response_times) / len(response_times) if response_times else 0.0
        
        stats ={
        "total":        total,
        "rescued":      rescued,
        "false_alarms": false_alarms,
        "missed":       missed,
        "avg_confidence":    round(avg_conf, 3),
        "avg_response_time": round(avg_response, 1),
        }
        
        return stats 
          