import pyscreenshot as ImageGrab
from playsound import playsound
import time
import clx.xms
import requests
import numpy as np
from datetime import datetime


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
    time.sleep(40)

    try:
        batch = client.create_batch(create)
    except (requests.exceptions.RequestException,
            clx.xms.exceptions.ApiException) as ex:
        print('Failed to communicate with XMS: %s' % str(ex))
    time.sleep(40)

true = True
while true:

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    im1=ImageGrab.grab(bbox=(2000, 135, 2020, 140))
    im2=ImageGrab.grab(bbox=(2000, 172, 2020, 176))
    #im1.show()
    #im2.show()



    colors1 = im1.convert("RGB")
    colors2 = im2.convert("RGB")
    na1 = np.array(colors1)
    na2 = np.array(colors2)


    colours1, counts1 = np.unique(na1.reshape(-1, 3), axis=0, return_counts=1)
    colours2, counts2 = np.unique(na2.reshape(-1, 3), axis=0, return_counts=1)



    len1 = len(colours1)
    i = 0
    sum1_c1 = 0
    sum1_c2 = 0
    sum1_c3 = 0

    while i < len1:

        sum1_c1 = sum1_c1 + counts1[i] * colours1[i][0]
        sum1_c2 = sum1_c2 + counts1[i] * colours1[i][1]
        sum1_c3 = sum1_c3 + counts1[i] * colours1[i][2]
        i = i +1
    sum1_c1 = sum1_c1 / len1
    sum1_c2 = sum1_c2 / len1
    sum1_c3 = sum1_c3 / len1

    print("sum1_c1: " + str(sum1_c1))
    print("sum1_c2: " + str(sum1_c2))
    print("sum1_c3: " + str(sum1_c3))

    len2 = len(colours2)
    i = 0
    sum2_c1 = 0
    sum2_c2 = 0
    sum2_c3 = 0

    while i < len2:

        sum2_c1 = sum2_c1 + counts2[i] * colours2[i][0]
        sum2_c2 = sum2_c2 + counts2[i] * colours2[i][1]
        sum2_c3 = sum2_c3 + counts2[i] * colours2[i][2]
        i = i +1
    sum2_c1 = sum2_c1 / len2
    sum2_c2 = sum2_c2 / len2
    sum2_c3 = sum2_c3 / len2

    #print("sum2_c1: " + str(sum2_c1))
    #print("sum2_c2: " + str(sum2_c2))
    #print("sum2_c3: " + str(sum2_c3))




    if (sum1_c1 > 370) & (sum1_c1 < 430) & (sum1_c2 > 370) & (sum1_c2 < 430) & (sum1_c3 > 370) & (sum1_c3<430):
        sms("P1 pt dead "+ str(current_time))
        print("1")
    #elif (sum2_c1 > 370) & (sum2_c1 < 430) & (sum2_c2 > 370) & (sum2_c2 < 430) & (sum2_c3 > 370) & (sum2_c3 < 430):
    #    sms("P2 pt dead "+ str(current_time))
    #    print("2")
    elif (sum1_c1 > 245) & (sum1_c1 < 400) & (sum1_c2 > 235) & (sum1_c2 < 260) & (sum1_c3 > 215) & (sum1_c3<235) :
        sms("WP main dead "+ str(current_time))
        print("3")
    #elif (sum2_c1 > 245) & (sum2_c1 < 400) & (sum2_c2 > 235) & (sum2_c2 < 260) & (sum2_c3 > 215) & (sum2_c3<235):
    #    sms("P2 wp main dead "+ str(current_time))
    #    print("4")
    elif (sum1_c1 > 165) & (sum1_c1 < 210) & (sum1_c2 > 70) & (sum1_c2 < 105) & (sum1_c3 > 40) & (sum1_c3 < 60):
        sms("WP main logout "+ str(current_time))
        print("5")
    #elif (sum2_c1 > 165) & (sum2_c1 < 210) & (sum2_c2 > 70) & (sum2_c2 < 105) & (sum2_c3 > 40) & (sum2_c3 < 60):
    #    sms("P2 wp main logout "+ str(current_time))
    #    print("6")


    print("PASS " + str(current_time))
    time.sleep(20)


print("cos sie stanelo")