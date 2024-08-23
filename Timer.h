#include <chrono>

class Timer {
public:
    // std::chrono::steady_clock::time_point start_time, end_time;   
    std::chrono::system_clock::time_point start_time, end_time;  
    Timer();
    void start();
    void stop();
    double read();
};