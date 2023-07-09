class RecentCounter(object):

    def __init__(self):
        self.requests = [0] * 10000  # Initialize a circular buffer of size 10000
        self.start = 0
        self.end = 0
        self.size = 0

    def ping(self, t):
        self.requests[self.end] = t  # Add the new request to the circular buffer
        self.end = (self.end + 1) % 10000  # Increment the end pointer
        self.size += 1

        # Remove the requests that fall outside the time range [-2999, t]
        while self.requests[self.start] < t - 3000:
            self.start = (self.start + 1) % 10000  # Increment the start pointer
            self.size -= 1

        return self.size
