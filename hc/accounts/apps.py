from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'hc.accounts'

    def ready(self):
        import hc.accounts.signals
