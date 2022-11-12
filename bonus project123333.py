import time

input_time = input("Input time of format hh:mm:ss: ")
hh = input_time[:2]
mm = input_time[3:3+2]
ss = input_time[6:]

def countdown(hh, mm, ss):
    t = ss + mm*60 + hh*3600
    while True:
        timer = "{:02d}:{:02d}:{:02d}".format(hh, mm, ss)
        time.sleep(1)
        # t -= 1
        # if t==0:
        #     print(timer,"hello")
        #     break
        print(timer)
        # t -= 1

        if ss == 0:
            # print(timer)
            if mm != 0:
                mm -= 1
            elif mm == 0 and hh != 0:
                hh -= 1
                mm = 59
            elif hh == 0 and mm == 0:
                # print(timer)
                break
            ss = 59
        else:
            ss -= 1
        # if mm == 0 and hh != 0:
        #     hh -= 1


        # print(timer)

    # if not t:
    #     time.sleep(1)
    #     timer = "{:02d}:{:02d}:{:02d}".format(hh,mm,ss)
    #     print(timer)
    #     exit()

# print(int(hh), int(mm), int(ss))
countdown(int(hh), int(mm), int(ss))