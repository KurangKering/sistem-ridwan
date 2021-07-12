from libraries.algorithms import fcm


class FCMFactory:

	@staticmethod
	def createFCM(*args, **kwargs):
		return fcm.FCM(*args, **kwargs)