from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)  # Add the new request to the deque

        # Remove the requests that fall outside the time range [-2999, t]
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)

