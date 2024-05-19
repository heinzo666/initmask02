import os
import shutil
from git import Repo
import datetime as dt
tgl = dt.datetime.now().strftime("%y%m%d_%H%M%S")
os.chdir('../initmask')
#import shutil
#shutil.make_archive('HEINZO', 'zip', '/content/images')
full_local_path = "/content/initmask"

initt = "/content/init.png"
maskk = "/content/mask.png"
initoutputss = "/content/initmask/outputs/" + str(tgl) + "I.png"
maskoutputss = "/content/initmask/outputs/" + str(tgl) + "M.png"
shutil.copy(initt, initoutputss)
shutil.copy(maskk, maskoutputss)

#inname = "/content/initmask/outputs/init.png"
#inn = ('/content/initmask/outputs/' + str(tgl) + 'I.png')
#os.rename(inname, inn)
#maname = "/content/initmask/outputs/mask.png"
#ma = ('/content/initmask/outputs/' + str(tgl) + 'M.png')
#os.rename(maname, ma)
#backupname = "/content/training/HEINZO.zip"
#backup = ('/content/training/H' + str(tgl) + '.zip')
#os.rename(backupname, backup)


repo = Repo(full_local_path)
repo.git.add("-A")
repo.index.commit("user_fakes")

#repo = Repo(full_local_path)
origin = repo.remote(name="origin")
origin.push()


os.chdir('..')
