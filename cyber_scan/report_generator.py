from datetime import datetime
import os


def generate_html_report(
    target,
    results,
    filename="reports/report.html"
):

    os.makedirs(
        "reports",
        exist_ok=True
    )


    html = f"""
<!DOCTYPE html>
<html>

<head>

<title>
Cyber Tools Lab Report
</title>

<style>

body {{
    font-family: Arial;
    margin: 40px;
}}

table {{
    border-collapse: collapse;
    width: 100%;
}}

th, td {{
    border: 1px solid black;
    padding: 10px;
}}

th {{
    background-color: #ddd;
}}

</style>

</head>


<body>


<h1>
Cyber Tools Lab Security Report
</h1>


<p>
Target: {target}
</p>


<p>
Generated: {datetime.now()}
</p>



<table>

<tr>

<th>
Port
</th>

<th>
Service
</th>

<th>
Risk
</th>

<th>
Banner
</th>

</tr>

"""


    for item in results:

        html += f"""

<tr>

<td>
{item['port']}
</td>


<td>
{item['service']}
</td>


<td>
{item['risk']}
</td>


<td>
{item['banner']}
</td>


</tr>

"""


    html += """

</table>


</body>

</html>

"""


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            html
        )


    return filename