//Cassandre, 20210863
//Viviane, [matricule]
#include "PrimeCalculator.h"
#include <stdio.h> //c libraries
#include <stdlib.h>
#include <math.h>
#include <string.h>

//Note this compiles with g++ so should be A-OK test on yours first tho
PrimeCalculator::PrimeCalculator() = default;

int PrimeCalculator::CalculateNthPrime(int N)
{
    /*
    Why is this in C you might ask? Well...kachow!
    This is an implementation of "Sieve of Eratosthenese"
    */
    
    //Handling the cases for which N is small or < 1 or 2
    
    if (N < 1) {
        return 0;
    } else if (N == 1) {
        return 2;
    }

    long long limit; //using long longs as numbers will get too big for int (had a rlly big bug cause of that)
    if(N < 14){ //if small ~ < 100 init to 104 for the smaller numbers (also causing segfault w/out)
        limit = 104;
    }
    else{
        //"The number of primes less than N is approximately N/log N, ... A is the event 'the outcome is prime', we have that Pr[A] I/log(n)." - Fundamentals of Algorithms
        //  The probability that a randomly chosen number between 1 and n is prime is approximately N*log(N) - Wikipedia (';-;) apparently nlog(n) + n(log(log(n))) is better but idk why (also wikipedia)
        limit = static_cast<long long>(N * (log(N) + log(log(N)))); //otherwise cast to long long or segfault
        //NOTE: i put N*(log(N)+ log(log(N))) instead of N*(log(N)) because just log(N) was too small for the large benchmark  and log(N) + N slightly too big (as in not enough kachow) and wikipedia said it's the best approximation clock tests confirmed this
    }

    // Allocate and initialize the sieve
    char* sieve = (char*)malloc((limit + 1) * sizeof(char));
    if (!sieve) { //sieve == null 
        perror("malloc failed");
        return 0; // error but we return 0 anyways
    }
    memset(sieve, 1, (limit + 1) * sizeof(char)); // init to true
    sieve[0] = 0;
    sieve[1] = 0;
    int index = 0;
    for (long long i = 2; i <= limit; i++) {
        if (sieve[i]) {//if true
            index++;
            if (index == N) {
                free(sieve); // free the malloc
                return i; // Found the nth prime!
            }
            // i*i is not prime
            for (long long j = i * i; j <= limit; j += i) {
                sieve[j] = 0;
            }
        }
    }
    free(sieve); // free if error
    return 0; // error if we get here
}
