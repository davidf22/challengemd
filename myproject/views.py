import requests
from django.http import JsonResponse
from django.views import View
from datetime import datetime

class NasaApodView(View):
   

    API_URL = "https://api.nasa.gov/planetary/apod"
    API_KEY = "DEMO_KEY" 

    def get(self, request):
       
        date_str = request.GET.get("date", None)

       
        params = {"api_key": self.API_KEY}
        if date_str:
            try:
                datetime.strptime(date_str, "%Y-%m-%d")
                params["date"] = date_str
            except ValueError:
                return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

        try:
            response = requests.get(self.API_URL, params=params)
            response.raise_for_status()
            dat = response.json()

           
            required_fields = ["title", "date", "explanation", "url", "media_type"]
            if not all(field in dat for field in required_fields):
                raise KeyError("Missing or malformed data in API response.")

            
            apod_info = {
                "title": dat["title"],
                "date": dat["date"],
                "explanation": dat["explanation"][:200] + ("..." if len(dat["explanation"]) > 200 else ""),
                "image_url": dat["url"],
                "media_type": dat["media_type"]
            }

            return JsonResponse(apod_info)

        except requests.exceptions.HTTPError as http_err:
            status_code = response.status_code  # response is always defined

            if status_code == 401:
                message = "Unauthorized: Invalid or missing API key."
            elif status_code == 403:
                message = "Forbidden: You do not have permission to access this resource."
            elif status_code == 429:
                message = "Too Many Requests: API rate limit exceeded. Try again later."
            elif status_code == 500:
                message = "Internal Server Error: NASA's server encountered an error."
            else:
                message = f"HTTP error occurred: {http_err}"

            return JsonResponse({
                "error": message,
                "status_code": status_code
            }, status=status_code)


        except requests.exceptions.ConnectionError:
            return JsonResponse({"error": "Network error. NASA API unavailable."}, status=503)

        except requests.exceptions.Timeout:
            return JsonResponse({"error": "Request timed out."}, status=504)

        except KeyError as key_err:
            return JsonResponse({"error": f"Data error: {key_err}"}, status=502)

       
