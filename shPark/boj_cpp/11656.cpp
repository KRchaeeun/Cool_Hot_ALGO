#include <iostream>
#include <map>
#include <string>

using namespace std;

class Trie {
public:
    char alphabet;
    bool isWordEnd;
    int cnt;
    map<char, Trie*> children;

    Trie(char alphabet) : alphabet(alphabet), isWordEnd(false), cnt(0) {}

    Trie() : alphabet('\0'), isWordEnd(false), cnt(0) {}
};

char results[1005];

int insert(const string& words, int idx, Trie* trie) {
    if (idx == words.length()) {
        return 0;
    }

    char alphabet = words[idx];

    int subCnt = 0;
    if (trie->children.find(alphabet) == trie->children.end()) {
        Trie* newTrie = new Trie(alphabet);
        newTrie->cnt = 1;
        subCnt = 1;
        trie->children[alphabet] = newTrie;
    }

    subCnt += insert(words, idx+1, trie->children[alphabet]);
    trie->cnt += subCnt;

    return subCnt;
}

void dfs(Trie* trie, int depth) {

    string result = "";
    for (int i=0; i<depth; i++){
        result += results[i];
    }
    cout << result << "\n";


    for (char i = 'a'; i<='z'; i++) {
        if (trie->children.find(i) != trie->children.end()) {
            Trie* child = trie->children[i];

            results[depth] = i;
            dfs(trie->children[i], depth + 1);
            results[depth] = '\0';
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    Trie* head = new Trie();
    string words;
    cin >> words;

    int len = words.length();
    
    for (int i=0; i<len; i++) {
        insert(words, i, head);
    }
    results[len] = '\0';
    dfs(head, 0);

    return 0;
}
