import mjpegtools
import PIL.Image as image

url = 'https://kelder.zeus.ugent.be/webcam/video/mjpg.cgi'

def lights_on():
    stream = mjpegtools.MjpegParser(url=url).serve()
    img = image.open(stream.output)
    return not img.getcolors()
