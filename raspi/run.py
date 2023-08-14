import time
import os
import setting
import picamera
from fractions import Fraction

# take a snapshot
# snapshot_param = "raspistill -w 1024 -h 768 -q 90 -o now.jpg"
# os.system(snapshot_param)
def take_snapshot(night_mode=False):
	with picamera.PiCamera() as camera:
		camera.resolution = (1920, 1080)
		camera.start_preview()
		if night_mode:
			camera.framerate = Fraction(1, 6)
			camera.shutter_speed = 5000000
			camera.exposure_mode = 'off'
			camera.iso = 800
			time.sleep(5)
		else:
			time.sleep(2) # wram up
		camera.capture('now.jpg')
		camera.stop_preview()


# need copy `qrsctl` to /usr/bin first
# qrstcl can be download from "http://developer.qiniu.com/docs/v6/tools/qrsctl.html"
def upload_picture(local_name, key_name):
	# login to qiniu.com
	login_param = "qrsctl login %s %s"%(setting.username, setting.password)
	os.system(login_param)

	# upload photo to qiniu.com
	upload_param = "qrsctl put %s %s %s"%(setting.bucket, key_name, local_name)
	print upload_param
	os.system(upload_param)

if __name__ == "__main__":
	current_hour = time.localtime(time.time()).tm_hour
	if current_hour > 5 and current_hour < 19:
		night_mode = False
	else:
		night_mode = True

	# night_mode = False
	take_snapshot(night_mode)

	# genreate time key
	key = time.strftime("%F_%T")

	upload_picture('now.jpg', key+'.jpg')


