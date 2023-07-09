class RecentCounter(object):

    def __init__(self):
        self.requests = []

    def ping(self, t):
        self.requests.append(t)  # Add the new request to the list

        # Remove the requests that fall outside the time range [-2999, t]
        while self.requests and self.requests[0] < t - 3000:
            self.requests.pop(0)

        return len(self.requests)
