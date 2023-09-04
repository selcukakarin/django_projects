from rest_framework.views import APIView
from rest_framework.response import Response
from pydub import AudioSegment
from faster_whisper import WhisperModel
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework import status
import os
from datetime import datetime
import pytz
from media_convert.errors import ERROR_MESSAGES


def generate_output_filename(input_filename, output_format):
    base_filename = os.path.splitext(input_filename)[0]
    tz = pytz.timezone('Europe/Istanbul')  # Türkiye saat dilimi
    current_datetime = datetime.now(tz).strftime("%Y-%m-%d_%H-%M-%S")
    return f"{base_filename}_{current_datetime}.{output_format}"


class TranscribeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        if "file" not in request.data:
            return JsonResponse({"error": "Dosya eksik. 'file' alanı gereklidir."}, status=400)

        file = request.data["file"]


        try:
            # Dosyayı geçici bir yere kaydet
            output_format = "wav"
            dst = generate_output_filename(file, output_format)
            sound = AudioSegment.from_file(file, format="mp4")
            sound.export(dst, format=output_format)

            # Whisper modelini başlat
            model = WhisperModel("tiny")
            segments, info = model.transcribe(dst)

            # Transkript sonuçlarını işle ve dön
            transcriptions = []
            for segment in segments:
                transcriptions.append({
                    "start": segment.start,
                    "end": segment.end,
                    "text": segment.text
                })

            return JsonResponse(transcriptions, status=200, safe=False)
        except Exception as e:
            error_message = ERROR_MESSAGES["transcription_error"]
            return JsonResponse({"error": error_message, "detail": str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
