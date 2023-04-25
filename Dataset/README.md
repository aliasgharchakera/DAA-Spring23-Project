## Dataset

### Groups of Instances

We have divided the instances into 7 groups; One of them is taken from [artemisa.unicauca.edu.co](http://artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/)

1.  Base Dataset (By artemisa)
2.  Very Large n (Number of items)
3.  Very Large wmax (Capacity)
4.  Very large n & wmax
5.  Very large values of vi (Profit)
6.  Very large values of wi (Weight)
7.  Very Large values of vi & wi

### Files format

In each dataset instance: 
- First line should have the optimum. 
- The next line contains space separated n and wmax 
- The n lines following them contains space separated vi and wi where i ranges from 0 to n-1.

There is a script to parse any instance, `Dataset/scripts/parse_instance.py` that just takes the filepath and returns and list of [optimum, n, wmax, V, W] <br>

Note: Only the base_group has the first line as optimum right now, all the other groups have empty first lines which should be overwritten with the optimum once I get time to run DP or any other algorithm on them to get their optimum since the input is just generated through random initialization. <br>
The line is left blank to make the parsing script run similar to instances in base_group since they have optimum on the first line.

### Generating the instances

We only had 21 examples from the dataset obtained from aforementioned source. <br>
For this purpose I have written a few scripts stored in `Dataset/scripts/` to generate the dataset according to the ranges specified in `Dataset/scripts/generate_dataset.py`.

There is also a colab file in `Dataset/` which you could run to obtain new instances if you have changed the ranges in script.

