#include <iostream>
using namespace std;

char gameBoard[8][8] = {{'#','#','#','#','#','#','#'},{'#','#','#','#','#','#','#'},{'#','#','#','#','#','#','#'},{'#','#','#','X','*','#','#'},{'#','#','*','X','#','#','#'},{'#','#','#','#','#','#','#'},{'#','#','#','#','#','#','#'},{'#','#','#','#','#','#','#'}};
int cursor[8] = {4,4}; 

// print gameboard with starting position
// print cursors position
// update map on enter press
// validate legal moves
// update gameboard piece swithces
// switch turns

    
int main()
{
    for(int i = 0; i < 8; i++)
    {
        for(int j = 0; j < 8; j++)
        {
            if (i == cursor[0] && j == cursor[1])
            {
                cout << "@" << " ";
            }
            else
            {
                cout << gameBoard[i][j];
            }
            cout << endl;
        }
        cout << endl;
    }
    

}