import csv
from datetime import datetime


class AlertManager:

    def load_alerts(self, filepath: str) -> list:
        alerts = []

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    row["confidence"] = float(row["confidence"])
                    row["response_time_s"] = int(row["response_time_s"])
                    alerts.append(row)

        except FileNotFoundError:
            return []

        return alerts

    def save_alerts(self, alerts: list, filepath: str) -> None:
        fieldnames = [
            "alert_id",
            "pool_id",
            "zone_id",
            "timestamp",
            "confidence",
            "status",
            "response_time_s"
        ]

        with open(filepath, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(alerts)

        print(f"Alerts saved successfully to {filepath}")

    def get_by_zone(self, alerts: list, pool_id: str, zone_id: str) -> list:
        return [
            a for a in alerts
            if a["pool_id"] == pool_id and a["zone_id"] == zone_id
        ]

    def summary_stats(self, alerts: list) -> dict:

        if not alerts:
            return {}

        total = len(alerts)

        rescued = sum(1 for a in alerts if a["status"] == "Rescued")
        false_alarms = sum(1 for a in alerts if a["status"] == "False_Alarm")
        missed = sum(1 for a in alerts if a["status"] == "Missed")

        avg_conf = sum(a["confidence"] for a in alerts) / total

        response_times = [
            a["response_time_s"]
            for a in alerts
            if a["response_time_s"] > 0
        ]

        avg_response = (
            sum(response_times) / len(response_times)
            if response_times else 0.0
        )

        stats = {
            "total": total,
            "rescued": rescued,
            "false_alarms": false_alarms,
            "missed": missed,
            "avg_confidence": round(avg_conf, 3),
            "avg_response_time": round(avg_response, 1),
        }

        print("\n--- ALERT SUMMARY STATS ---")
        for key, value in stats.items():
            print(f"{key}: {value}")

        return stats
    

