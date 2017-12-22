Here we are going to detect eye blink of a person and keep a count of it.For this we will be learning a library called Dlib which basically has a wide range of machine learning algorithms and tools to create complex softwares but also has amazing features for computer vision and image processing.We will make use of these powerful features to study face patterns and use it to track eye blinks.

The basic idea that Dlib uses is that every face has the same features ie it will have two eyes, one nose, a lip, a jaw line and two eyebrows.So it doesn't really matter what is the origin of a person, these properties are going to be same for every face.Based on this idea, it has localized the regions of a face and put numbers to represent those regions.Below is a diagram that better explains the idea.

![Alt text](https://github.com/Souvikray/Eye-Blink-Detection/blob/master/screenhot1.png?raw=true "Optional Title")

As you can see the total numbers are between 1 to 68 with each region of a face represented by a bunch of numbers.For example 0 - 16 numbers represent the jaw line.The right eye brow is represented by numbers between 17 to 21 and so on.Based on these parameters, it is able to detect a face and perform operations on it.

Now in our case we need to detect and count the number of eye blinks.For that first we must define an eye blink so that the computer understands when is something called as an eye blink.

**EYE ASPECT RATIO**

The eye of a person is given six points which maps the entire eye.These six points are used to calculate EAR which gives a value that estimates whether a person's eye is closed or open.If a person's eye is closed, the value will be low and if it is open, the value will be high.Below is an illustration of the idea.

![Alt text](https://github.com/Souvikray/Eye-Blink-Detection/blob/master/screenshot2.png?raw=true "Optional Title")

As we can see there are two set of vertical points (P1, P5) and (P2, P4) and a horizontal point (P0, P3).Using these points we calcuate the EAR.

***EAR = ||P1 - P5|| + ||P2 - P4|| / 2 * ||P0 - P3||***

Notice that we multiply 2 in the denominator to equalize the effect of adding two set of vertical points.

Once EAR is calcualted, we can use this a thershold value and make a condition that any value less that this means the eyes are closed and greater than this means the eyes are open.Now a blink means that an eye is closed for some moment before it opens again.So we can put a further condition that if EAR is below the threshold for three consecutive frames and then the value spikes, it means a blink has taken place.Then we can keep of count of the number of blinks.

At first let is look at how Dlib identifies and assigns the numbers when a face is provided to it.Below is my original photo which I will pass to the Dlib library to identify the facial landmarks.

![Alt text](https://github.com/Souvikray/Eye-Blink-Detection/blob/master/mypic1.jpg?raw=true "Optional Title")

After Dlib highlights the facial landmarks

![Alt text](https://github.com/Souvikray/Eye-Blink-Detection/blob/master/screenshot4.png?raw=true "Optional Title")

We can see it successfully identifies the facial landmarks and highlights them.Now we shall try to detect and count eye blinks of a person in realtime.Below is a gif that implements that feature.

![Alt text](https://github.com/Souvikray/Eye-Blink-Detection/blob/master/EyeBlink.gif?raw=true "Optional Title")

We can also test it on an image.Since image is of only one frame, there will be no eye blinks.So the number of blinks should be 0.

![Alt text](https://github.com/Souvikray/Eye-Blink-Detection/blob/master/screenshot3.png?raw=true "Optional Title")




