from PIL import Image
import requests
import time
import threading

def time_function(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__ + " took " + str((end - start)*1000) + " ms")
        return result
    return wrapper

def cropp_image():
    image_path = '/Users/Admin/Pictures/pexels-mike-b-170811.jpg'
    image = Image.open(image_path)
    small_image = image.resize((500, 500))
    small_image.save('image.jpg')

def make_request():
    requests.get('https://python.org')

@time_function
def sync_make_request():
    for i in range(5):
        make_request()

@time_function
def async_make_request():
    t1 = threading.Thread(target=make_request)
    t2 = threading.Thread(target=make_request)
    t3 = threading.Thread(target=make_request)
    t4 = threading.Thread(target=make_request)
    t5 = threading.Thread(target=make_request)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()


@time_function
def sync_cropp_image():
    for i in range(5):
        cropp_image()

@time_function
def async_cropp_image():
    t6 = threading.Thread(target=cropp_image)
    t7 = threading.Thread(target=cropp_image)
    t8 = threading.Thread(target=cropp_image)
    t9 = threading.Thread(target=cropp_image)
    t10 = threading.Thread(target=cropp_image)

    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()


if __name__ == '__main__':
    cropp_image()
    make_request()
    sync_make_request()
    async_make_request()
    sync_cropp_image()
    async_cropp_image()

#sync_make_request took 7239.1979694366455 ms
#async_make_request took 41.22304916381836 ms
#sync_cropp_image took 1269.0331935882568 ms
#async_cropp_image took 13.976573944091797 ms
#Асинхронні процеси виконуються набагато швидше, ніж синхронні, що очікувалося, тому що
#під час виконання асинхронних процесів процеси виконуються одночасно, розподіляючи
#ресурси комп'ютера, тоді як синхронні процеси слідують один за одним.