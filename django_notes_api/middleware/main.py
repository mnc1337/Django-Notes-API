from django.shortcuts import render


class HttpErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        static_extensions = (".css", ".js", ".png", ".jpg", ".jpeg", ".svg", ".ico")
        if request.path.startswith("/static/") or request.path.endswith(
            static_extensions
        ):
            return response

        status_code = response.status_code
        if 400 <= status_code <= 599:
            error_type = "Client error" if status_code <= 499 else "Server error"

            message = response.reason_phrase

            return render(
                request,
                "error_page.html",
                {"status": status_code, "message": message, "type": error_type},
                status=status_code,
            )

        return response
