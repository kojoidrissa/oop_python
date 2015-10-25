
class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.value = val

    def get_val(self):
        return self.value

    def increment_val(self):
        self.val = self.val +1

i = MyInteger()
i.set_val(9)
