__author__ = 'Epsirom'

from django.http import HttpResponse, Http404
import qrcode


def get_qr_code(request, qrmsg):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0
    )
    qr.add_data(qrmsg)
    qr.make(fit=True)
    img = qr.make_image()
    response = HttpResponse(mimetype='image/png')
    img.save(response, 'png')
    return response

