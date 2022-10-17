import urllib.request
import os


def testingImage(image_url, filename):
    image_url = image_url

    filename = filename

    req = urllib.request.build_opener()
    req.addheaders = [{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}]
    urllib.request.install_opener(req)

    urllib.request.urlretrieve(image_url, filename)


def create_or_get_path(path):
    path = path
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print("success")

    else:
        print("path exit")
