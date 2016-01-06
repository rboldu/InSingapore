def change(status):
	key=self.status
	key=~key
	return key

def check():
	return status


def select(status_num):
    switcher = {
        0: switcher.get(status_num, "0"),
        1: switcher.get(status_num, "1"),
    }
    return switcher.get(status_num, "nothing")