# Rating-System-optimization
This repository aims to conduct rating system optimization using `Wilson Score` according to business needs, so that the accuracy of the scoring system of a live broadcast platform can be higher, saving more resources for the platform to recommend more high-quality streamers to the homepage.

### Background
In the live broadcast industry, the major live-streaming platforms are more willing to recommend high-quality online streamers to the homepage of the website, thus to attract more users. But the accuracy of the old algorithm used by the project was only `80%`, which means that the `20%` of the streamers recommended by the system can hardly bring better benefits to the platform. So how to improve the accuracy of the scoring system is what the platform must do.

### Methodology
Suppose there are two videos in a live-streaming platform. One has 3 favors and 1 objection, the other has 30 favors and 10 objections. 
The approval rate of both answers is 75%. Which video should be ranked first?

* Normal situation <br>
In general, the normal approximation confidence interval for a sample is: <br>
<img src="https://github.com/nicolehhy/Rating-System-optimization-/raw/master/Normal.png" width="300" alt="Normal">

* Small sample <br>
In 1927, American mathematician Edwin Bidwell Wilson proposed a correction formula called "Wilson Confidence Interval", which solved the problem of accuracy of small samples well. <br>
The Wilson normal interval is also related to the number of samples. The smaller the sample size, the larger the confidence interval will be:
<img src="https://github.com/nicolehhy/Rating-System-optimization-/raw/master/Wilson.png" width="300" alt="Normal">

### Research with the operation department
This scoring system not only contains the favorable rate mentioned in the Wilson algorithm, we also referred to, how many times the live video is been viewed more than 1 minute, the number of clicks, how often the chats happen and the number of new followers. <br>
Due to the low accuracy of the previous scoring system, we conducted a scoring result survey within the operation department. they summarized that the weight of the clicks by their understanding should be reduced, and the weights of the other three indicators should be appropriately increased. Then, the values of the final favors number `P` was calculated by combining these four dimensions, and brought into the Wilson algorithm to obtain a more realistic evaluation for the streamers.

```python
click_weight = 0.012886181267334866
short_weight = 0.19072705034439638
chat_weight = 0.017523205359980466*chat_new_weight
follow_weight = 0.6722195401618779*follow_new_weight
```





