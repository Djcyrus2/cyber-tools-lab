import requests


def scan_website(url):

    results = {

        "url": url,

        "status": None,

        "server": "Unknown",

        "headers": []

    }


    try:

        response = requests.get(
            url,
            timeout=5
        )


        results["status"] = response.status_code


        results["server"] = response.headers.get(
            "Server",
            "Unknown"
        )


        security_headers = [

            "Content-Security-Policy",

            "X-Frame-Options",

            "X-Content-Type-Options",

            "Strict-Transport-Security"

        ]


        for header in security_headers:


            if header in response.headers:

                results["headers"].append(
                    header
                )


        return results



    except Exception as e:


        results["status"] = "Failed"

        return results