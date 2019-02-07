import os
import time
import hashlib
from win10toast import ToastNotifier


toaster = ToastNotifier()


def path_ui_converter(path):
    pth = str(path)
    files = os.listdir(pth)
    to_watch = []

    for file in files:
        if file[-3:] == '.ui':
            to_watch.append(file)

    hashes = []

    for file_ui in to_watch:
        hash_md5 = hashlib.md5()
        with open(file_ui, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        hashes.append((file_ui, hash_md5.hexdigest()))

    return hashes


toaster.show_toast('ui files watcher', 'Watching...', duration=10)
while True:
    x_ = path_ui_converter('.')
    time.sleep(10)
    y_ = path_ui_converter('.')

    diff = [x[0] for x in x_ if x not in set(y_)]
    if len(diff) != 0:
        # print(__str(diff) + ' file(s) changed')
        toaster.show_toast('File(s) changed', str(diff), duration=10)
        for file in diff:
            os.system('pyuic5 -x' + file + ' -o python/' + str(file)[0:-3] + '.py')

