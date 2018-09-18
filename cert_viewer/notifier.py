import logging



class Notifier(object):
    def factory():
        from . import config
        conf = config.get_config()
        notifier = conf.notifier_type
        if notifier == 'mail':
            return Mail(conf)
        if notifier == 'noop':
            return NoOp()
        assert 0, "Unrecognized notifier type: " + notifier

    factory = staticmethod(factory)


class NoOp(Notifier):
    def notify(self, recipient_email, first_name, last_name):
        logging.warning(
            'A notification would have been sent to first_name=%s,last_name=%s,email=%s, but no notifier is configured',
            first_name, last_name, recipient_email)
        return False


