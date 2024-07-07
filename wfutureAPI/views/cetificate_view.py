import os
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.utils.dateformat import DateFormat
from reportlab.lib.pagesizes import landscape

from wfuture import settings
from ..models.user_certificate import UserCertificate  # Correct import path if needed

def my_certificates(request):
    certificates = UserCertificate.objects.filter(volunteer=request.user.volunteer)
    return render(request, 'pages/my_certificates.html', {'certificates': certificates})

def generate_certificate(request, id):
    user_certificate = get_object_or_404(UserCertificate, id=id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{user_certificate.volunteer.name}_{user_certificate.volunteer.surname}.pdf"'

    custom_page_size = (1063, 591)
    p = canvas.Canvas(response, pagesize=custom_page_size)
    width, height = custom_page_size
    template_path = os.path.join(settings.BASE_DIR, 'wfutureAPI', 'static', 'certificates', 'certificate_template.png')
    print(f"Template path: {template_path}")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found: {template_path}")

    p.drawImage(template_path, 0, 0, width, height)
    p.setFont("Helvetica", 24)
    p.drawString(300, 350, f"Participant: {user_certificate.volunteer.name} {user_certificate.volunteer.surname}")  # Adjust the coordinates as needed
    p.drawString(300, 300, f"Participated as {user_certificate.volunteership.title}")
    completion_date = DateFormat(user_certificate.date_of_completion).format('F d, Y')
    p.drawString(300, 225, f"Date of completion: {completion_date}")
    p.showPage()
    p.save()

    return response
