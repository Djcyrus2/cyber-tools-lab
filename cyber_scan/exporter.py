import csv
import os


def export_csv(results):

    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/report.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Port",
            "Status"
        ])

        for port in results:

            writer.writerow([
                port,
                "OPEN"
            ])