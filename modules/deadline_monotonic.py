class DeadlineMonotic():
    def __init__(self):
        pass

    def is_solution(self, c_next):
        c_next.calc_wcrt()
        for core in c_next.cores:
            for task in core.tasks:
                if task.wcrt > task.deadline:
                    return False

        return True
