// created: 22:52 2024/10/09 by ZXPrism
// Producer & Consumer 1

#include <atomic>
#include <format>
#include <future>
#include <iostream>
#include <mutex>
#include <thread>

std::atomic<int> counter(0);
std::mutex m;

int finish_id = 0;
int dispatch_id = 0;

void consumer()
{
    while (1)
    {
        while (counter == 0)
        {
            ;
        }

        std::this_thread::sleep_for(std::chrono::seconds(2));

        m.lock();
        --counter;
        std::cout << std::format("Finished job #{}\n", finish_id++);
        m.unlock();
    }
}

void producer()
{
    while (1)
    {
        m.lock();
        ++counter;
        std::cout << std::format("Dispatched job #{}\n", dispatch_id++);
        m.unlock();

        std::this_thread::sleep_for(std::chrono::seconds(10));
    }
}

int main()
{
    std::thread thread_consumer(consumer);
    std::thread thread_producer(producer);
    thread_consumer.join();
    thread_producer.join();
    return 0;
}
