from pool_manager import PoolManager
from alert_manager import AlertManager
from visualizer import Visualizer

def main():
    POOLS_FILE  = "pools.json"
    ALERTS_FILE = "alerts.csv"

    pm  = PoolManager()
    am  = AlertManager()
    viz = Visualizer()

    # Step 1: Load data
    print("[1/5] Loading data...")
    pools  = pm.load_pools(POOLS_FILE)
    alerts = am.load_alerts(ALERTS_FILE)
    print(f"      Pools loaded  : {len(pools)}")
    print(f"      Alerts loaded : {len(alerts)}\n")

    # Step 2: Display pool configurations
    print("[2/5] Monitored pools and zones:")
    pm.display_pools(pools)

    # Step 3: Show summary statistics
    print("\n[3/5] Alert statistics:")
    stats = am.summary_stats(alerts)
    for key, value in stats.items():
        print(f"      {key:<22}: {value}")

    # Step 4: Log a new test alert
    print("\n[4/5] Logging a test alert...")
    try:
        alerts = am.log_alert(
            alerts,
            pool_id="P01",
            zone_id="Z3",
            confidence=0.94,
            status="Rescued",
            response_time_s=15
        )
        am.save_alerts(alerts, ALERTS_FILE)
    except ValueError as e:
        print(f"      Failed: {e}")

    # Step 5: Visualize
    print("\n[5/5] Displaying charts...")
    viz.zone_chart(alerts)
    viz.status_pie(alerts)

    print("\nDone!")

if __name__ == "__main__":
    main()