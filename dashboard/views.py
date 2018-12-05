from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.templatetags.staticfiles import static
import qrcode
import json
import os


@login_required
def dashboard(request):
    if request.method == "POST":
        json_str = request.body.decode(encoding='UTF-8')
        json_obj = json.loads(json_str)
        uuid = json_obj['uuid']
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4,
        )
        data = uuid
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(BASE_DIR)
        img.show()
        x = (os.path.join(BASE_DIR, 'dashboard/static/qr.jpg'))
        print(x)
        img.save(x)
        response_json = {'good':True}
        return HttpResponse(json.dumps(response_json),content_type = 'application/json')
    else:
        return render(request, 'dashboard/dashboard.html')
