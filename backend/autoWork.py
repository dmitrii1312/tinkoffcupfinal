from dataclasses import dataclass
from datetime import datetime
import time
import TypeOfWork

@dataclass
class autoWork(TypeOfWork):
    compress: int # cтепень сжатия работ

    def set_priority(self, priority):
        if priority == "critical":
            return False, "Can't set this priority to the task of this type"
        else:
            self.priority = priority
        return True


