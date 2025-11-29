from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GcdInputSerializer
from .utils import compute_gcd_steps




class GcdAPIView(APIView):
    """POST endpoint: принимает два числа и возвращает НОД с подробным объяснением."""

    def post(self, request):
        serializer = GcdInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"error": "Неверные данные", "details": serializer.errors},
                     status=status.HTTP_400_BAD_REQUEST
                )


        a = serializer.validated_data['a']
        b = serializer.validated_data['b']


        gcd, steps = compute_gcd_steps(a, b)


        if gcd is None:
            return Response({
                "a": a,
                "b": b,
                "gcd": None,
                "steps": steps,
                "explanation": "НОД(0,0) математически не определён."
            }, status=status.HTTP_400_BAD_REQUEST)


        explanation = (
            "Алгоритм Евклида: пока b != 0 выполняем деление a на b, "
            "заменяя (a, b) → (b, r), где r — остаток. Последнее ненулевое значение — НОД."
        )


        return Response({
            "a": a,
            "b": b,
            "gcd": gcd,
            "steps": steps,
            "explanation": explanation,
        }, status=status.HTTP_200_OK)