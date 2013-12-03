__author__ = 'Epsirom'

from django.http import HttpResponse, Http404
import qrcode
import Image


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
    (x, y) = img.size
    newImg = Image.new('RGBA', (x * 2, x), (255, 255, 255))
    newImg.paste(img, (x / 2, 0));
    response = HttpResponse(mimetype='image/png')
    newImg.save(response, 'png')
    return response

