#include "Timer.h"
// #include <chrono>

Timer::Timer(){
    
}

void Timer::start(){
    // start_time = std::chrono::high_resolution_clock::now();
    start_time = std::chrono::system_clock::now();
}
void Timer::stop(){
    // end_time = std::chrono::high_resolution_clock::now();
    end_time = std::chrono::system_clock::now();
}
double Timer::read(){
    std::chrono::duration<double> duration = end_time - start_time;
    return duration.count();
}
