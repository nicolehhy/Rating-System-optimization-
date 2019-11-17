#-*- coding: utf-8 -*-
import numpy as np
import codecs


def wilson_score(pos, total, p_z=2.):

    pos_rat = pos * 1. / total * 1.  # positive rate
    score = (pos_rat + (np.square(p_z) / (2. * total))
             - ((p_z / (2. * total)) * np.sqrt(4. * total * (1. - pos_rat) * pos_rat + np.square(p_z)))) / \
            (1. + np.square(p_z) / total)
    return score

input = open('C:\\Users\\Inke185311\\Desktop\\anchor_level.txt', 'r')
all = input.readlines()





def get_result(good_weight=1.5, showpv_weight=0.01, p_z=2., low_face_weight=80,
               chat_new_weight=0.7, follow_new_weight=1.1):

    click_weight = 0.012886181267334866
    short_weight = 0.19072705034439638
    chat_weight = 0.017523205359980466*chat_new_weight
    follow_weight = 0.6722195401618779*follow_new_weight

    date_score = {}
    date_num = {}
    for i in range(21):
        date_score[20180706+i] = []
        date_num[20180706+i] = 0
    uid_level = {}
    uid_detail = {}


    # Calculate the initial score
    for item in all:
        item = item.split("\t")
        ymd = item[0]
        uid = item[1]
        face_score = int(item[2])
        showpv = int(item[3])
        click = int(item[4])
        short = int(item[5])
        chat = int(item[6])
        follow = int(item[7])

        goodpv = (min(good_weight * click, showpv) +
                  min(good_weight * short * short_weight/click_weight, showpv) + \
                  min(good_weight * chat * chat_weight/click_weight, showpv) +
                  min(good_weight * follow * follow_weight/click_weight, showpv))/4

        if showpv >= 500 and goodpv > 0:
            score = wilson_score(goodpv*showpv_weight, showpv*showpv_weight, p_z)
        else:
            score = 0

        date_num[ymd] += 1
        date_score[ymd].append([uid, score, face_score, showpv, click, short, chat, follow])


    # Calculate the level of streamers
    for i in range(21):
        score_item = []
        low_face_score_item = []
        for item in date_score[20180706+i]:
            # if show_pv < 500，set streamers who don't look good as level 1，set others as level 2
            if item[3] < 500:
                if item[2] == 3:
                    uid_level[item[0]] = 1
                    uid_detail[item[0]] = item
                else:
                    uid_level[item[0]] = 2
                    uid_detail[item[0]] = item
             #   print item[0], item[1], uid_level[item[0]]
            # if show_pv > 500，bring streamers who don't look good back to the calculation system
            elif item[2] == 3:
                low_face_score_item.append([item[0], item[1], item])
            else:
                score_item.append([item[0], item[1], item])

        # For streamers who look good
        if score_item:
            total_num = len(score_item)
            new_item = sorted(score_item, key=lambda x: x[1])
            one_score = 0
            two_score = new_item[total_num*10/100-1][1]
            three_score = new_item[total_num*65/100-1][1]
            four_score = new_item[total_num*85/100-1][1]
            five_score = new_item[total_num*95/100-1][1]
            #print one_score, two_score, three_score, four_score, five_score

            for item in new_item:
                if item[1] > five_score:
                    uid_level[item[0]] = 5
                    uid_detail[item[0]] = item
                elif item[1] > four_score:
                    uid_level[item[0]] = 4
                    uid_detail[item[0]] = item
                elif item[1] > three_score:
                    uid_level[item[0]] = 3
                    uid_detail[item[0]] = item
                elif item[1] > two_score:
                    uid_level[item[0]] = 2
                    uid_detail[item[0]] = item
                elif item[1] >= one_score:
                    uid_level[item[0]] = 1
                    uid_detail[item[0]] = item
              #  else:
                #    print item
              #  print item[0], item[1], uid_level[item[0]]

        # For streamers who don't look good
        if low_face_score_item:

            low_total_num = len(low_face_score_item)
            low_sort_item = sorted(low_face_score_item, key=lambda x: x[1])
            low_score = low_sort_item[low_total_num*low_face_weight/100-1][1]
            for item in low_sort_item:
                if item[1] > low_score:
                    uid_level[item[0]] = 2
                    uid_detail[item[0]] = item
                else:
                    uid_level[item[0]] = 1
                    uid_detail[item[0]] = item
               # print item[0], item[1], uid_level[item[0]]


get_result()
