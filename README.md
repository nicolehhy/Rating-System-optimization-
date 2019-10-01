# Rating-System-optimization
This repository aims to conduct rating system optimization using `Wilson Score` according to business needs, so that the accuracy of the scoring system of a live broadcast platform can be higher, saving more resources for the platform to recommend more high-quality streamers to the homepage.

### Background
In the live broadcast industry, the major live-streaming platforms are more willing to recommend high-quality online streamers to the homepage of the website, thus to attract more users. But the accuracy of the old algorithm used by the project was only `80%`, which means that the `20%` of the streamers recommended by the system can hardly bring better benefits to the platform. So how to improve the accuracy of the scoring system is what the platform must do.

### Methodology
Suppose there are two videos in a live-streaming platform. One has 3 favors and 1 objection, the other has 30 favors and 10 objections. 
The approval rate of both answers is 75%. Which video should be ranked first?

* Normal situation
In general, the normal approximation confidence interval for a sample is: <br>
<img src="https://github.com/nicolehhy/Rating-System-optimization-/raw/master/Normal.png" width="300" alt="Normal">
* Small sample
In 1927, American mathematician Edwin Bidwell Wilson proposed a correction formula called "Wilson Confidence Interval", which solved the problem of accuracy of small samples well.
The Wilson normal interval is also related to the number of samples. The smaller the sample size, the larger the confidence interval will be:
<img src="https://github.com/nicolehhy/Rating-System-optimization-/raw/master/Wilson.png" width="300" alt="Normal">

### Research with the operation department





