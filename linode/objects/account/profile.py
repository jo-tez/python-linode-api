from ...errors import UnexpectedResponseError
from linode.objects import Base, Property

class Profile(Base):
    api_name = 'profile'
    api_endpoint = "/account/profile"
    id_attribute = 'username'

    properties = {
        'username': Property(identifier=True),
        'email': Property(mutable=True),
        'timezone': Property(mutable=True),
        'email_notifications': Property(mutable=True),
        'referrals': Property(),
        'ip_whitelist_enabled': Property(mutable=True),
        'lish_auth_method': Property(mutable=True),
        'authorized_keys': Property(mutable=True),
        'two_factor_auth': Property(),
    }

    def reset_password(self, password):
        """
        Resets the password of the token's user.
        """
        result = self._client.post('/account/profile/password', { "password": password })

        return result

    def enable_tfa(self):
        """
        Enables TFA for the token's user.  This requies a follow-up request
        to confirm TFA.  Returns the TFA secret that needs to be confirmed.
        """
        result = self._client.post('/account/profile/tfa-enable')

        return result['secret']

    def confirm_tfa(self, code):
        """
        Confirms TFA for an account.  Needs a TFA code generated by enable_tfa
        """
        result = self._client.post('/account/profile/tfa-enable-confirm', {
            "tfa-code": code
        })

        return True

    def disable_tfa(self):
        """
        Turns off TFA for this user's account.
        """
        result = self._client.post('/account/profile/tfa-disable')

        return True

    @property
    def grants(self):
        """
        Returns grants for the current user
        """
        from linode.objects.account import UserGrants
        resp = self._client.get(UserGrants.api_endpoint.format(username=self.username))

        grants = UserGrants(self._client, self.username)
        grants._populate(resp)
        return grants
