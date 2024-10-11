// created: 23:44 2024/10/09 by ZXPrism
// Producer & Consumer 2

#include <format>
#include <iostream>
#include <mutex>
#include <thread>

std::condition_variable cv;
std::mutex m;

int counter = 0;
int dispatch_id = 0, finish_id = 0;

void consumer()
{
    while (1)
    {
        std::unique_lock ulock(m);

        while (counter == 0)
        {
            cv.wait(ulock);
        }

        --counter;
        ulock.unlock(); // critical!

        std::this_thread::sleep_for(std::chrono::seconds(1));
        std::cout << std::format("Finished job #{}\n", finish_id++);
    }
}

void producer()
{
    while (1)
    {
        std::unique_lock ulock(m);

        ++counter;
        std::cout << std::format("Dispatched job #{}\n", dispatch_id++);
        ulock.unlock(); // critical!
        cv.notify_all();

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
