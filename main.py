import pyscreenshot as ImageGrab
from playsound import playsound
import time
import clx.xms
import requests


def graj():
    playsound('E:\\\Projekty\\\screen_mt\\Marsz Imperialny.mp3')
    time.sleep(35)
def sms( info ):
    client = clx.xms.Client(service_plan_id='08b660356f9948d0af4926667a877c44',
                            token='45251bf963324feea58384a33ac76e30')

    create = clx.xms.api.MtBatchTextSmsCreate()
    create.sender = '447537404817'
    create.recipients = {'48535431229'}
    create.body = 'WARRNING : ' + str(info)

    try:
        batch = client.create_batch(create)
    except (requests.exceptions.RequestException,
            clx.xms.exceptions.ApiException) as ex:
        print('Failed to communicate with XMS: %s' % str(ex))


true = True
while true:

    im1=ImageGrab.grab(bbox=(2000, 135, 2020, 140))
    im2=ImageGrab.grab(bbox=(2000, 172, 2020, 176))
    #im1.show()
    #im2.show()



    colors1 = im1.convert("RGB").getcolors()
    colors2 = im2.convert("RGB").getcolors()
    #print(colors1)
    #print(colors2)

    len1 = len(colors1)
    i = 0
    sum1 = 0
    while i < len1:
        sum1 = sum1 +sum(colors1[i][1])
        i = i + 1
    sum1 = sum1/len1

    len2 = len(colors2)
    i = 0
    sum2 = 0
    while i < len2:
        sum2 = sum2 +sum(colors2[i][1])

        i = i + 1
    sum2 = sum2/len2

    print(sum1)
    print(sum2)

    if sum1 <200:
        #sms("P1")
        #graj()
        true = False
    elif sum2 < 200:
        #sms("P2")
        #graj()
        true = False

    time.sleep(20)


print("cos sie stanelo")