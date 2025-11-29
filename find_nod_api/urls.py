from django.urls import path
from .views import GcdAPIView


urlpatterns = [
    path('gcd/', GcdAPIView.as_view(), name='find_nod_api_gcd'),
]

# ---
# Example POST request (curl):
# curl -X POST http://127.0.0.1:8000/api/gcd/ \
#      -H "Content-Type: application/json" \
#      -d '{"a": 48, "b": 18}'


# Example JSON response:
# {
#   "a": 48,
#   "b": 18,
#   "gcd": 6,
#   "steps": [
#       "Начинаем: a = 48, b = 18",
#       "48 = 18 * 2 + 12",
#       "18 = 12 * 1 + 6",
#       "12 = 6 * 2 + 0",
#       "Найдено: НОД = 6"
#   ],
#   "explanation": "Алгоритм Евклида: ..."
# }