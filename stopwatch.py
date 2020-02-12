import time

print("Press Enter key to start the stopwatch")
start=int(input(time.time()))

print("Press Enter key to stop the stopwatch")
end=int(input(time.time())

total_time=end-start
print("Elapsed time is ",total_time,"secs")