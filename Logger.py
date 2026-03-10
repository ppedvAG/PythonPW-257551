def logException(exc):
	from traceback import format_exception
	with open("Log.txt", "w") as log:
		for zeile in format_exception(exc):
			log.write(zeile)