#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Node{
    public:
    bool is_leaf;
    int freq_sum;
    char c;
    Node* left;
    Node* right;
    Node(char c,int f){
        this->c = c;
        this->freq_sum = f;
        this->left = NULL;
        this->right = NULL;
        this->is_leaf = true;
    }

    Node(int f,Node* l=NULL,Node* r=NULL){
        this->is_leaf = false;
        this->freq_sum = f;
        this->left = l;
        this->right = r;
    }
};

void build_code_table(Node* root,string code,map<char,string>& code_table){
    if(root == NULL) return;
    if(root->is_leaf){
        code_table[root->c] = code;
        return;
    }

    build_code_table(root->left,code+'0',code_table);
    build_code_table(root->right,code+'1',code_table);
}


int main(){
    // input string
    string s;
    cout<<"Enter string To Encode:";
    cin>>s;

    // build frequency table
    map<char,int> freq;
    for(char c:s) freq[c]++;

    cout<<"Frequency Of Chars:"<<endl;
    for(auto p:freq){
        cout<<p.first<<" - "<<p.second<<endl;
    }

    // build huffman tree
    vector<Node*> nodes;
    for(auto p:freq){
        nodes.push_back(new Node(p.first,p.second));
    }
    sort(nodes.begin(),nodes.end(),[](Node* a,Node* b){return a->freq_sum < b->freq_sum;});

    while(nodes.size()>1){
        int sum = nodes[0]->freq_sum + nodes[1]->freq_sum;

        Node* parent = new Node(sum,nodes[0],nodes[1]);

        nodes.erase(nodes.begin(),nodes.begin()+2);

        nodes.push_back(parent);

        sort(nodes.begin(),nodes.end(),[](Node* a,Node* b){return a->freq_sum < b->freq_sum;});
    }

    Node* root = nodes[0];

    // build code table
    map<char,string> codes;
    string code_str = "";
    build_code_table(root,code_str,codes);

    // print code table
    cout<<"Code Table:"<<endl;
    for(auto p:codes){
        cout<<p.first<<" - "<<p.second<<endl;
    }

    // encode string
    string encoded_str = "";
    for(char c:s){
        encoded_str += codes[c];
    }

    cout<<"Encoded String:"<<endl;
    cout<<encoded_str<<endl;

    return 0;
}