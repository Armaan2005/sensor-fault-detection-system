import os
import json
from datetime import datetime

class MetricsUtils:

    @staticmethod
    def update_prediction_metrics(predictions):
       

        metrics_path = os.path.join(
            "artifacts", "metrics", "prediction_metrics.json"
        )

        os.makedirs(os.path.dirname(metrics_path), exist_ok=True)

        total = len(predictions)
        good = int((predictions == 1).sum())
        bad = int((predictions == 0).sum())

        metrics = {
            "total_predictions": total,
            "good_count": good,
            "bad_count": bad,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        with open(metrics_path, "w") as f:
            json.dump(metrics, f, indent=4)