class AppTask:
    Deadline = None
    Id = None
    Period = None
    WCET = None

    def __init__(self, deadline, id, period, wcet):
        self.Deadline = deadline
        self.Id = id
        self.Period = period
        self.WCET = wcet
