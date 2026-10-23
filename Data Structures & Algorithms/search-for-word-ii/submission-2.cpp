struct Node{
    shared_ptr<Node> next[26];
    string word;
};

class Solution {
public:
    shared_ptr<Node> root = make_shared<Node>();
    unordered_set<string> results{};
    int row_count{};
    int column_count{};
    int matched_word_count=0;

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        // build Trie
        buildTrie(words);
        row_count = board.size();
        column_count = board[0].size();
        // iterate over elements
        for (int r = 0; r < row_count; ++r){
            for (int c = 0; c < column_count; ++c){
                char chr = board[r][c];
                int c_idx = chr - 'a';
                if (root->next[c_idx]){
                    unordered_set<int> path;
                    dfs(board, r, c, root->next[c_idx], path);
                    if (matched_word_count == words.size())
                        return return_result();
                }
            }
        }
        return return_result();
    }

    vector<string> return_result(){
        vector<string> results_vector;
        for (const auto& r: results)
            results_vector.push_back(r);
        return results_vector;
    }

    void buildTrie(vector<string>& words){
        for (const string& w: words){
            shared_ptr<Node> cursor = root;
            for (const char c: w){
                int c_idx = c - 'a';
                if (!cursor->next[c_idx]){
                    Node tmp{};
                    cursor->next[c_idx] = make_shared<Node>(tmp);
                }
                cursor = cursor->next[c_idx];
            }
            cursor->word = w;
        }
    }

    void validNeighbours(vector<pair<int,int>>& neighbours, int r, int c, unordered_set<int>& path){
        vector<pair<int,int>> steps{{-1,0},{1,0},{0,-1},{0,1}};
        for (auto& step: steps){
            int nr = r + step.first;
            int nc = c + step.second;
            if (0 <= nr && nr < row_count && 0 <= nc && nc < column_count && path.find(nr * column_count + nc) == path.end())
                neighbours.push_back({nr, nc});
        }
    }

    void dfs(vector<vector<char>>& board, int r, int c, shared_ptr<Node> cursor, unordered_set<int>& path){
        if (cursor->word != "" && results.find(cursor->word) == results.end()){
            matched_word_count += 1;
            results.insert(cursor->word);
        }

        vector<pair<int,int>> neighbours{};
        validNeighbours(neighbours, r, c, path);
        for (auto& n: neighbours){
            int nr = n.first;
            int nc = n.second;
            char n_char = board[nr][nc];
            int n_char_idx = n_char - 'a';
            if (cursor->next[n_char_idx]){
                path.insert(r * column_count + c);
                dfs(board, nr, nc, cursor->next[n_char_idx], path);
                path.erase(r * column_count + c);
            }
        }
    }
};