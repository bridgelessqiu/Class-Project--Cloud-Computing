#ifndef ALGO_H
#define ALGO_H

#include<vector>
#include<utility>
#include<string>

using namespace std;

/*
The function LearnBiTree recovers the structure of the bidirectional tree based on the estimator \hat{h}_{uv}

Input: H A vector of pairs: [("u v", \hat{h}_{uv})]
       n: size of the network

Output: A vector of paris: [(u, v)] such that vertex u should be adjacent to vertex v
*/
vector<pair<int, int>> LearnBiTree(vector<pair<string, double>> H, int n);

/*
The function LearnDegBound recovers the structure of the degree bounded graphs based on the esitmator \hat{h}_{u,S}.

Input: H

Output: A vector of paris: [(u, v)] such that vertex u should be adjacent to vertex v
*/
vector<pair<int, int>> LearnDegBound(vector<vector<pair<int*, double>>> H)

// Comparison function for the pairs in decreasing order based on the second element
bool pairComp(const pair<string, double> &a, const pair<string, double> &b)
{
       return a.second > b.second;
}

#endif