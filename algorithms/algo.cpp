#include "algo.h"
#include <sstream>
#include <algorithm>

vector<pair<int, int>> LearnBiTree(vector<pair<string, double>> H, int n)
{
    // The returned 
    vector<pair<int, int>> ET;

    // Sort all pairs of vertices based 
    sort(H.begin(), H.end(), pairComp);

    // Lable which vertices has been added (to avoid cycles)
    vector<bool> A (n, 0);

    // Vertices and the corresponding string pairs
    int u, v;
    string ps;

    for(auto p : H)
    {
        ps = p.first; // the pair
        istringstream ss(ps);

        ss>>ps;
        u = stoi(ps); // the first vertex
        ss>>ps;
        v = stoi(ps); // the second vertex

        if(!A[u] || !A[v]) // no cycle is formed
        {
           ET.push_back({u, v});
           A[u] = A[v] = true;
        }
    }

    return ET;
}

vector<pair<int, int>> LearnDegBound(vector<vector<pair<int*, double>>> H)
{
    // The returned 
    vector<pair<int, int>> ET;

    for(size_t u = 0; u < H.size(); ++u)
    {
        vector<pair<int*, double>> S_union = H[u];
        auto S_max = max_element(S_union.begin(), S_union.end(), 
        [](const auto& l, const auto& r) { return l.second < r.second; });

        for(auto v : S_max) ET.push_back({u, v});
    }

    return ET;
}