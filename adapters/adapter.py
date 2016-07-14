class AdapterMethodNotImplementedError(NotImplementedError):

    def __init__(self, message: str="An adapter method was not implemented."):
        self.message = message

    def __unicode__(self):
        return unicode(self).encode('utf-8')()

    def __str__(self):
        return self.message
