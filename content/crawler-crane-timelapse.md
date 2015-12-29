Title: Time Lapse LEGO Assembly, Crawler Crane
Author: Josh Wickham
Tags: Lego, timelapse, video
Date: 12/08/2015 09:00
Category: Projects
FBImageIndex: 0

Timelapse time again! This time, it's the massive [Crawler Crane (#42042)][store_link], complete with various actions!

![full_view][full_view]

This moves forward, pivots, and the crane... picker upper thingy goes up and down, and the scaffolding for the crane
also raises and lowers. It's pretty great!

I tested its lifting capabilities using a glob of 4 packs of Bucky Balls which weigh close to 1 kg and, while it bogged
down, it actually lifted them and was able to turn! The second half of the video below is sped up by 2x, so it took a
while, but it's understandable considering I'm using rechargeable batteries which just don't pack as much oomph as
alkaline ones. Also, LEGO crane. Probably not winning any lifting contests...

Enjoy!

<iframe width="420" height="315" src="https://www.youtube.com/embed/6zqOktPTsvA" frameborder="0" allowfullscreen></iframe>

Oh, and since I keep on forgetting to post it, I assemble all the images into a single video using ffmpeg:

```
ffmpeg -r 30 -pattern_type glob -i '*.jpg' -c:v copy output.avi # 30 fps in this case
```

[full_view]: {filename}/images/crane_timelapse.jpg
[store_link]: http://shop.lego.com/en-US/Crawler-Crane-42042
