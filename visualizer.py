import matplotlib.pyplot as plt


class Visualizer:
    
    def zone_chart(self, alerts: list):
        
        counts={}
        for alert in alerts:
            label=f"{alert['pool_id']}-{alert['zone_id']}"
            counts[label] = counts.get(label, 0) + 1
            
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(counts.keys(), counts.values(), color="steelblue", edgecolor="white")
        ax.set_title("Drowning Alerts by Pool Zone")
        ax.set_xlabel("Pool — Zone")
        ax.set_ylabel("Number of Alerts")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.show() 
        
    def status_pie(self, alerts: list):
        counts = {}
        for a in alerts:
            counts[a["status"]] = counts.get(a["status"], 0) + 1
        colors = {"Rescued": "steelblue", "False_Alarm": "orange", "Missed": "tomato"}
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.pie(
            counts.values(),
            labels=counts.keys(),
            autopct="%1.1f%%",
            startangle=140,
            colors=[colors.get(k, "gray") for k in counts.keys()]
         )
        ax.set_title("Alert Status Distribution")
        plt.show()
     