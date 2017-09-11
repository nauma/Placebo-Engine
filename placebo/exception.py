class LuminaBaseException(Exception):
  pass

class LuminaMediaException(LuminaBaseException):
  pass

class SoundLoadingError(LuminaMediaException):
  def __init__(self, file_name, reason, notice=""):
    message = "Error while loading %s: %s" % (repr(file_name), ", ".join(reason))
    if notice.__str__():
      message += " (%s)" % notice.__str__()

    super().__init__(message)