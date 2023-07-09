class RecentCounter(object):

    def __init__(self):
        self.requests = []
        self.window_start = 0

    def ping(self, t):
        self.requests.append(t)  # Add the new request to the list

        # Remove the requests that fall outside the time range [-2999, t]
        while self.requests[self.window_start] < t - 3000:
            self.window_start += 1

        return len(self.requests) - self.window_start

