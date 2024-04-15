#include <iostream>
#include <cmath>
#include <vector>
#include <tuple>
using namespace std`
struct Cell {
    int x;
    int y;
};

vector<vector<int>> detected(vector<vector<int>>& area) {
    // For loop to mark  area as detected
    // for (int i = 30; i <= 200; ++i) {
    //     for (int j = 30; j <= 55; ++j) {
    //         area[i][j] = -1;
    //     }
    // }
    // Code for plotting using matplotlib can be omitted in C++

    return area;
}

double distance(int x1, int y1, int x2, int y2) {
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));
}

tuple<vector<Cell>, vector<double>> neighbour_cells(
    Cell pos,
    vector<int> playGround,
    vector<vector<int>>& area,
    vector<double> orientation_last
) {
    vector<Cell> cells;
    vector<double> orientation;

    // (-1 -1)
    if (pos.x - 1 >= playGround[0] && pos.x - 1 <= playGround[1] &&
        pos.y - 1 >= playGround[2] && pos.y - 1 <= playGround[3]) {
        if (area[pos.x - 1][pos.y - 1] != -1) {
            cells.push_back({pos.x - 1, pos.y - 1});
            orientation.push_back(fabs(orientation_last[0] - 225));
        }
    }

    // (0 -1) and other directions similarly...

    return make_tuple(cells, orientation);
}

tuple<int, int, double> neighbour_least_cost(
    vector<Cell>& cells,
    Cell pos,
    Cell goal,
    vector<double>& orientation
) {
    vector<vector<double>> cost;
    tuple<int, int, double> least = {0, 0, 100000};

    for (size_t i = 0; i < cells.size(); ++i) {
        double a = distance(cells[i].x, cells[i].y, pos.x, pos.y) +
                   distance(cells[i].x, cells[i].y, goal.x, goal.y);
        cost.push_back({cells[i].x, cells[i].y, a});
        if (get<2>(least) > cost[i][2]) {
            least = make_tuple(cells[i].x, cells[i].y, cost[i][2]);
        }
    }
    return least;
}

void main_algorithm() {
    vector<int> playGround{0, 10000, 0, 400};
    vector<vector<int>> area(playGround[1], vector<int>(playGround[3], 1));

    // Define start, orientation_last, waypoint
    // Plotting functions are omitted in C++

    for (size_t i = 0; i < waypoint.size(); ++i) {
        // Code to handle waypoint iteration
        // Code for plotting and other functionalities omitted in C++
        for (size_t j = 0; j < waypoint.size(); ++j) {
            // Code for handling movement and waypoint reached alert
        }
    }
}

int main() {
    main_algorithm();
    return 0;
}
