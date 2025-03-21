from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from .forms import CodeKoraaForm, ParticipantForm
from .models import Code_Koraa, Participant
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.http import  request, HttpResponse, JsonResponse
import random

def test(request):
    try:
        if request.method == "POST":
            form = CodeKoraaForm(request.POST)  # Create form instance with POST data
            if form.is_valid():  # Validate the form
                  d = Code_Koraa()
                  d.amount = form.cleaned_data['amount']
                  d.number_part = form.cleaned_data['number_part']
                  d.date_deb = form.cleaned_data['date_deb']
                  d = form.save(commit=False)
                  d.date_fin = d.date_deb + relativedelta(months=d.number_part)
                  d.montant_part = d.amount / d.number_part
                  d.save()  # Save to database
                  instance = form.save()  # This will automatically handle 'hex_code' and other fields
                  hex_code = instance.hex_code  # Retrieve the generated hex_code

                  request.session['hc'] = hex_code
                  request.session['NUMBR'] = d.number_part
                  email = request.GET.get('email')
                  email_address = email
                  subject = "كود القرعة دارت"
                  #body = hex_code + "مرحبا بك هذا رمز قرعتك يمكنك استعماله لمراجعتها : "
                  body = f"""
                    مرحبا بك هذا رمز قرعتك يمكنك استعماله لمراجعتها :
                    "127.0.0.1:8000/consultation_sk?hex_code={hex_code}" target="_blank">{hex_code}
                  """

                  send_mail(subject=subject, message=body, from_email="rabeedevinfo@gmail.com", recipient_list=[email_address])
                  # Create a mailto link with the parameters
                  mailto_link = f"mailto:{email_address}?subject={subject}&body={body}"
                  return render(request, 'validation.html', {'B': f' تم انشاء القرعة بنجاح وهذا رمزها: {hex_code}'})

                 # Render the form  # Return success message
            else:
                return render(request, 'validation.html', {'C': 'Des informations correctes sont requises.'})  # Return error message
        else:
            form = CodeKoraaForm()  # Create an empty form instance

        return render(request, 'success.html', {'form': form})  # Render the form
    except : return HttpResponse("<h1><p>مشكل اتصال الشبكة لديك<p></h1>")
def tofirstpage(request):
    return render(request, 'Firstpage.html', {'msg': 'مرحبا أدخل بريدك الالكتروني لحفظ كود القرعة(دارت)أو أنك ستكون مظطرا لحفظه<br>. ستحتاجه لاعادة رؤية مميزات القرعة في وقت لاحق'})


def addparticipant(request):
    k = request.session.get('hc', None)
    n = int(request.session.get('NUMBR', 0))  # تحويل `n` إلى عدد صحيح

    if not k:
        return HttpResponse("Error: Missing session data", status=400)

    try:
        k_obj = Code_Koraa.objects.get(hex_code=k)
    except Code_Koraa.DoesNotExist:
        return HttpResponse("Error: Code_Koraa not found", status=400)

    c = Participant.objects.filter(code_koraa=k_obj).count()

    if c >= n:  # التحقق من الحد الأقصى لعدد المشاركين
        return redirect(f'/consultation?hex_code={k}')

    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.code_koraa = k_obj  # تعيين الكود الصحيح
            participant.save()

            # تحديث عدد المشاركين
            c += 1
            if c >= n:
                return redirect(f'/consultation?hex_code={k}')
        else:
            return render(request, 'validation.html', {'C': 'Des informations correctes sont requises.'})
    else:
        form = ParticipantForm()

    return render(request, 'participant.html', {'form': form})  # عرض النموذج عند `GET`


def consultation(request):
    # Fetch Code_Koraa objects and prefetch related participants
    hex_code_value = request.GET.get('hex_code')

    if hex_code_value:
        # Apply the prefetch_related on the filtered queryset
        code_koraa_objects = Code_Koraa.objects.prefetch_related('participants').filter(hex_code=hex_code_value)
    else:
        # If no hex_code is provided, show all objects with prefetching
        code_koraa_objects = Code_Koraa.objects.none()
    # Pass the data to the template
    return render(request, 'consultation.html', {
        'code_koraa_objects': code_koraa_objects,
        's': hex_code_value
    })


def tombola(request, hex_code):
    """
    This view updates the 'order' field in the Participant model by assigning
    a random number from 1 to the total number of participants with the same code_koraa.
    """
    hex_code_value = request.GET.get('hex_code')
    # Get the corresponding Code_Koraa object
    code_koraa = Code_Koraa.objects.filter(hex_code=hex_code).first()
    if not code_koraa:
        return JsonResponse({"error": "Code_Koraa not found"}, status=404)

    # Get all Participants linked to this Code_Koraa
    participants = list(Participant.objects.filter(code_koraa=code_koraa))

    if not participants:
        return JsonResponse({"error": "No participants found"}, status=404)

    # Shuffle the list and assign random orders
    random.shuffle(participants)

    for index, participant in enumerate(participants, start=1):
        participant.order = index

    # Bulk update to save changes in one query
    Participant.objects.bulk_update(participants, ["order"])
    #return JsonResponse({"message": "Fin tombola"})
    return redirect(f'/consultation_sk?hex_code={code_koraa}')



def waitting(request):
    return render(request, "waitting.html")
def consultation1(request):
    # Fetch Code_Koraa objects and prefetch related participants
    hex_code_value = request.GET.get('hex_code')

    if hex_code_value:
        # Apply the prefetch_related on the filtered queryset
        code_koraa_objects = Code_Koraa.objects.prefetch_related('participants').filter(hex_code=hex_code_value)
    else:
        # If no hex_code is provided, show all objects with prefetching
        code_koraa_objects = Code_Koraa.objects.none()
    # Pass the data to the template
    return render(request, 'consultation_sk.html', {
        'code_koraa_objects': code_koraa_objects,
        's': hex_code_value
    })











