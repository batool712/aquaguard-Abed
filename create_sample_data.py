import json
import csv

def create_pools(filepath="pools.json"):
    data = {
        "pools": [
            {
                "pool_id": "P01",
                "name": "Olympic Pool",
                "length_m": 50,
                "width_m": 25,
                "zones": [
                    {"zone_id": "Z1", "name": "Shallow End", "depth_m": 1.2, "camera": "CAM01"},
                    {"zone_id": "Z2", "name": "Middle Lane", "depth_m": 1.8, "camera": "CAM02"},
                    {"zone_id": "Z3", "name": "Deep End",    "depth_m": 2.5, "camera": "CAM03"},
                ],
            },
            {
                "pool_id": "P02",
                "name": "Training Pool",
                "length_m": 25,
                "width_m": 12,
                "zones": [
                    {"zone_id": "Z1", "name": "Entry Zone", "depth_m": 0.9, "camera": "CAM04"},
                    {"zone_id": "Z2", "name": "Main Zone",  "depth_m": 1.5, "camera": "CAM05"},
                ],
            },
            {
                "pool_id": "P03",
                "name": "Kids Pool",
                "length_m": 15,
                "width_m": 8,
                "zones": [
                    {"zone_id": "Z1", "name": "Play Zone",  "depth_m": 0.6, "camera": "CAM06"},
                ],
            },
        ]
    }
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Pools saved: {filepath}")

def create_alerts(filepath="alerts.csv"):
    rows = [
        ["alert_id", "pool_id", "zone_id", "timestamp",           "confidence", "status",      "response_time_s"],
        ["ALT001",   "P01",     "Z3",      "2026-05-15 10:12:34", "0.92",       "Rescued",     "18"             ],
        ["ALT002",   "P01",     "Z2",      "2026-05-15 11:05:21", "0.87",       "False_Alarm", "0"              ],
        ["ALT003",   "P02",     "Z2",      "2026-05-15 14:33:10", "0.95",       "Rescued",     "14"             ],
        ["ALT004",   "P01",     "Z3",      "2026-05-15 15:47:02", "0.78",       "False_Alarm", "0"              ],
        ["ALT005",   "P03",     "Z1",      "2026-05-15 16:20:55", "0.91",       "Rescued",     "22"             ],
        ["ALT006",   "P01",     "Z1",      "2026-05-16 09:08:13", "0.83",       "Rescued",     "20"             ],
        ["ALT007",   "P02",     "Z1",      "2026-05-16 10:44:38", "0.69",       "False_Alarm", "0"              ],
        ["ALT008",   "P01",     "Z3",      "2026-05-16 11:30:07", "0.96",       "Rescued",     "12"             ],
        ["ALT009",   "P02",     "Z2",      "2026-05-16 13:15:50", "0.74",       "False_Alarm", "0"              ],
        ["ALT010",   "P01",     "Z2",      "2026-05-16 14:52:29", "0.88",       "Rescued",     "16"             ],
    ]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Alerts saved: {filepath}")

if __name__ == "__main__":
    create_pools()
    create_alerts()