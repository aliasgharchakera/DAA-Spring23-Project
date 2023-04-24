## Dataset

### Groups of Instances

We have divided the instances into 7 groups; One of them is taken from [[artemisa](http://artemisa.unicauca.edu.co/)](http://artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/)

1.  Base Dataset (By artemisa)
2.  Very Large n (Nummber of items)
3.  Very Large wmax (Capacity)
4.  Very large n & wmax
5.  Very large values of vi
6.  Very large values of wi
7.  Very Large values of vi & wi

### Files format

In each dataset instance, the first line is the optimum, the next line contains space separated n and wmax, after that, there are n lines with space separated vi and wi where i ranges from 1 to n. <br>

### Generating the instances

We only had 21 examples from the dataset obtained from aforementioned source. <br>
For this purpose I have written a few scripts stored in `Dataset/scripts/`

There is also a colab file in `Dataset/` which you could run to obtain new instances if you have changed the scripts.

