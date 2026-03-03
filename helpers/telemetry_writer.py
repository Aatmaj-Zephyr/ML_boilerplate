"""File to setup a simple telemetry writer that logs metrics to a CSV file. No need to modify this file."""

import csv
import os
import time

class TelemetryWriter:
    def setup_writer(self, run_id:str, fieldnames:list, directory="./telemetry_logs"):
        os.makedirs(directory, exist_ok=True)

        self.filepath = os.path.join(directory, f"{run_id}.csv")
        file_exists = os.path.isfile(self.filepath)

        self.file = open(self.filepath, "a", newline="")
        self.writer = csv.DictWriter(
            self.file,
            fieldnames=["timestamp"] + fieldnames
        )

        if not file_exists:
            self.writer.writeheader()
            self.file.flush()

    def log(self, **metrics):
        assert self.writer is not None, "TelemetryWriter not initialized. Call setup_writer first."
        metrics["timestamp"] = time.time()
        self.writer.writerow(metrics)
        self.file.flush()

telemetry_writer = TelemetryWriter()