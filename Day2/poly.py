class poly:

    def _init_(self, *x):

        self.x=list(x)

    def _add_(self, other):

        max_len=max(len(self.x), len (other.x))

        result=[0]*max_len

        for i in range(len(self.x)):

            result[max_len-len(self.x)+i]+=self.x[i]

        for i in range(len(other.x)):

            result[max_len-len(other.x)+i]+=other.x[i]

        return poly(*result)

    def _repr_(self):

        return f"poly{tuple(self.x)}"