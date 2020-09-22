class DeadlineMonotic():
    def __init__(self):
        pass

    def is_solution(self, c_next):
        c_next.calc_wcrt()
        for task in c_next.tasks:
            if task.wcrt > task.deadline:
                return False

        return True
