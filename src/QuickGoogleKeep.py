#sys.argv[1]=username
#sys.argv[2]=password
#sys.argv[3]=input

import sys
import gkeepapi
import keyring
import traceback


keep = gkeepapi.Keep()

try:
	if keyring.get_password('google-keep-token', sys.argv[1]) is None:
		success = keep.login(sys.argv[1], sys.argv[2])
		keyring.set_password('google-keep-token', sys.argv[1], keep.getMasterToken())
	else:
		keep.resume(sys.argv[1], keyring.get_password('google-keep-token', sys.argv[1]))
except:
	print("An error in QuickKeep has occurred.")

note = keep.createNote('', sys.argv[3])

keep.sync()