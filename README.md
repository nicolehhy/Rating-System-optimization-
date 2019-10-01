# Rating-System-optimization
This repository aims to conduct rating system optimization using `Wilson Score` according to business needs, so that the accuracy of the scoring system of a live broadcast platform can be higher, saving more resources for the platform to recommend more high-quality streamers to the homepage. After the optimization, the accuracy of this system was increased by `11.7%`. 

### Background
In the live broadcast industry, the major live-streaming platforms are more willing to recommend high-quality online streamers to the homepage of the website, thus to attract more users. But the accuracy of the old algorithm used by the project was only `80%`, which means that `20%` of the streamers recommended by the system can hardly bring better benefits to the platform. So how to improve the accuracy of the scoring system is what the platform must do.

### Methodology
Suppose there are two videos in a live-streaming platform. One has 3 favors and 1 objection, the other has 30 favors and 10 objections. 
The approval rate of both answers is 75%. Which video should be ranked first? This should be considered is because sometimes a new streamer who just made a live broadcast doesn't have many views or followers, we can't directly say that he or she is not good. `Wilson Score` can solved this problem well.

* Normal situation <br>
In general, the normal approximation confidence interval for a sample is: <br>
<img src="https://github.com/nicolehhy/Rating-System-optimization-/raw/master/Normal.png" width="300" alt="Normal">

* Small sample <br>
In 1927, American mathematician Edwin Bidwell Wilson proposed a correction formula called "Wilson Confidence Interval", which solved the problem of accuracy of small samples well. <br>
The Wilson normal interval is also related to the number of samples. The smaller the sample size is, the larger the confidence interval will be:
<img src="https://github.com/nicolehhy/Rating-System-optimization-/raw/master/Wilson.png" width="300" alt="Normal">

### Research with the operation department
This scoring system not only contains the favorable rate`p` mentioned in the Wilson algorithm, we also referred to how many times the live video has been viewed more than 1 minute, the number of clicks, how often the chats happen and the number of new followers. <br>

Due to the low accuracy of the previous scoring system, I conducted a scoring result survey within the operation department. According to their responds I summarized that:

* Weight on different indicators needs to be adjusted <br>
The weight of the chats during a live broadcast should be reduced, and the weight of the new followers the streamers got during the live should be appropriately increased. Because chats happen easily but getting new followers is not that easy.
```python
# chat_new_weight = 0.7 and follow_new_weight = 1.1
click_weight = 0.012886181267334866 
short_weight = 0.19072705034439638
chat_weight = 0.017523205359980466*chat_new_weight
follow_weight = 0.6722195401618779*follow_new_weight
```
* The scoring system is biased against people who don't look that good <br>
Inside the scoring system, we have a minor scoring system for looks. If the score is 1, it means a bad look. And the streamers who got score 1 will be directly rated as level 1, which is the lowest score. <br>
This is unfair to some live broadcasters who don't look good but are talented. Therefore, among these people, we rated the live broadcasters with page views less than 500 times a week as 1, and the rest of the live broadcasters will be evaluated through Wilson Score based on the four indicators. 

```python
# Calculate the ratings for steamers who don't look good
    for i in range(21):
        score_item = []
        low_face_score_item = []
        for item in date_score[20180706+i]:
            # if exposures are less than 500 times, set level as 1
            if item[3] < 500:
                if item[2] == 3:
                    uid_level[item[0]] = 1
                    uid_detail[item[0]] = item
                else:
                    uid_level[item[0]] = 2
                    uid_detail[item[0]] = item
             #   print(item[0], item[1], uid_level[item[0]])
            # if exposures are more than 500 times, rate the streamers through a specific calculation
            elif item[2] == 3:
                low_face_score_item.append([item[0], item[1], item])
            else:
                score_item.append([item[0], item[1], item])
```

```python
 # For the streamers who don't look good but got high exposures
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
               # print(item[0], item[1], uid_level[item[0]])
```

### Results
After achieving the above optimization, I conducted an offline test and found that the accuracy of the optimized algorithm increased to `91.7%`. The limitation of the project is that I only use 10,000 online streamers' information.
The problems that can be mined from it are also limited. Gievn more time, I will try to dig more problems to further improve the accuracy and save more resources for the platform. If you have any good questions or suggestions, please feel free to contact me. 

