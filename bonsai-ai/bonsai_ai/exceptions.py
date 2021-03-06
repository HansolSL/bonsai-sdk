class BonsaiClientError(Exception):
    """
    Generic wrapper for exceptions originating in client implementations
    """
    def __init__(self, msg, e):
        super(BonsaiClientError, self).__init__("{}: {}".format(msg, repr(e)))
        self.original_exception = e


class SimulateError(BonsaiClientError):
    def __init__(self, e):
        super(SimulateError, self).__init__("Error in simulate", e)


class EpisodeStartError(BonsaiClientError):
    def __init__(self, e):
        super(EpisodeStartError, self).__init__("Error in episode_start", e)


class EpisodeFinishError(BonsaiClientError):
    def __init__(self, e):
        super(EpisodeFinishError, self).__init__("Error in episode_finish", e)


class AuthenticationError(BonsaiClientError):
    def __init__(self, e):
        super(AuthenticationError, self).__init__("Error authenticating user",
                                                  e)

class RetryTimeoutError(Exception):
    pass


class BonsaiServerError(Exception):
    pass


class SimStateError(Exception):
    pass


class UsageError(Exception):
    pass
