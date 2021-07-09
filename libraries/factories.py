from libraries.algorithms import fcm


class FCMFactory:

	@staticmethod
	def createFCM():
		return fcm.FCM()