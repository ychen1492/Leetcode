# Hash table
[Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
In computing, a hash table (hash map) is a data structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

Ideally, the hash function will assign each key to a unique bucket, but most hash table designs employ an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. Such collisions must be accommodated in some way.

In a well-dimensioned hash table, the average cost (number of instructions) for each lookup is independent of the number of elements stored in the table. 

The idea of hashing is to distribute the entries (key/value pairs) across an array of buckets. Given a key, the algorithm computes an index that suggests where the entry can be found:

> index = f(key, array_size)

It is usually interpreted as:
> hash = hashfunc(key)
index = hash % array_size

hash here is independent from the array size to improve the speed

## Hash function
A hash function is any function that can be used to map data of arbitrary size to fixed-size values.