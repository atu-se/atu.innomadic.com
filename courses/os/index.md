# Introduction to Operations Systems

## Lectures

| Lecture                                             | Supplemental Video | 
|-----------------------------------------------------|-------|
| [1. Introduction](lectures/ch1.pptx)                | [UMass 1](https://youtu.be/dv4mXBsv6TI?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k) [UMass 2](https://youtu.be/Nc6KKSv_Ljc?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k)|
| [2. Operating System Structures](lectures/ch2.pptx) | [UMass 3](https://youtu.be/UxCiuctkKYo?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k)|
| [3. Processes](lectures/ch3.pptx)                   | [UMass 4](https://www.youtube.com/watch?v=SfG_BefeGT4&list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k&index=4)|
| [4. Threads and Concurrency](lectures/ch4.pptx)                      | [UMass 6b](https://youtu.be/KhjqKZr3fdM?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k&t=1633) |
| [5. CPU Scheduling](lectures/ch5.pptx)                               | [UMass 5](https://www.youtube.com/watch?v=Q_tycyhNkgA&list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k&index=5) [UMass 6a](https://youtu.be/KhjqKZr3fdM?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k)|
| [6. Synchronization Tools](lectures/ch6.pptx) | [Umass 7](https://www.youtube.com/watch?v=sYBfnDUsvrc&list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k&index=7), [Umass 8](https://www.youtube.com/watch?v=o5cXttjjBVs&list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k&index=8) |
| [7. Synchronization Example](lectures/ch7.pptx) | [Umass 9](https://www.youtube.com/watch?v=Kj8bL_L9Ah8&list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k&index=9) | 

## Assignments

1. [Process ID Manager](https://classroom.github.com/a/XHdtHa23)
2. Shell Warmup
## Updates

* Assignment 1 - Process ID Manager has been posted above.  There is one mistake in the provided code:

```    def release_process_id(self, int) -> None:```

Should have a different name for the second parameter, like:

```    def release_process_id(self, id) -> None:```

