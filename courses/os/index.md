# Introduction to Operations Systems

## Lectures

| Lecture                                             | Supplemental Video | 
|-----------------------------------------------------|-------|
| [1. Introduction](lectures/ch1.pptx)                | [UMass 1](https://youtu.be/dv4mXBsv6TI?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k) [UMass 2](https://youtu.be/Nc6KKSv_Ljc?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k)|
| [2. Operating System Structures](lectures/ch2.pptx) | [UMass 3](https://youtu.be/UxCiuctkKYo?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k)|
| [3. Processes](lectures/ch3.pptx)                   | [UMass 4](https://www.youtube.com/watch?v=SfG_BefeGT4&list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k&index=4)|
| [4. Threads and Concurrency](lectures/ch4.pptx)                      | [UMass 6b](https://youtu.be/KhjqKZr3fdM?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k&t=1633) |
| [5. CPU Scheduling](lectures/ch5.pptx)                               | [UMass 5](https://www.youtube.com/watch?v=Q_tycyhNkgA&list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k&index=5) [UMass 6a](https://youtu.be/KhjqKZr3fdM?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k)|

## Assignments

1. [Process ID Manager](https://classroom.github.com/a/XHdtHa23)
2. [Shell Warmup](https://classroom.github.com/a/qG_trOIZ)
3. [Shell 2](https://classroom.github.com/a/A_5bFw4I) due Sept 12

## Updates

### Week of 21-Aug

* Links
    * [Hand-made tech from Apollo 11](https://history.com/news/moon-landing-technology-inventions-computers-heat-shield-rovers)
    * [Hidden Figures Movie](https://en.wikipedia.org/wiki/Hidden_Figures)
    * [Article about early NASA "computers"](https://www.popularmechanics.com/space/rockets/a24429/hidden-figures-real-story-nasa-women-computers/)
    * [_Hidden Figures_ Movie Trailer](https://www.youtube.com/watch?v=RK8xHq6dfAo)
    * [Margaret Hamilton, Apollo Lead Software Engineer](https://qeprize.org/news/margaret-hamilton-apollos-code/)
    * [Margaret Hamilton (Video)](https://www.youtube.com/watch?v=kTn56jJW4zY)
    * [Margaret Hamilton Bio](https://en.wikipedia.org/wiki/File:Margaret_Hamilton.gif)
    * [Origin of Debugging](https://en.wikipedia.org/wiki/Debugging#Origin_of_the_term)
    * [Grace Hopper Article](https://tophat.com/blog/grace-hopper-yale-computer-science/)

![Margaret Hamilton beside Apollo guidance system software on punch-cards](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Margaret_Hamilton.gif/385px-Margaret_Hamilton.gif)

![The first computer bug](https://upload.wikimedia.org/wikipedia/commons/f/ff/First_Computer_Bug%2C_1945.jpg)

### Week 1

* Assignment 1 - Process ID Manager has been posted above.  There is one mistake in the provided code:

```    def release_process_id(self, int) -> None:```

Should have a different name for the second parameter, like:

```    def release_process_id(self, id) -> None:```

