class authentication:


    def __init__(self):

        self.consumer_key ="tHW8rwAc7KSgDPpiQLFWzJ6mR"
        self.consumer_secret="mzoPBQgol2iTStMG0DQKbKVmNWBkXz0rmZaORfr3THLBgvzZX8"
        # After the step above, you will be redirected to your app's page.
        # Create an access token under the the "Your access token" section
        self.access_token="725610589565947908-hpDvo0o4CFry5kq13TjgFERaFFn2eV3"
        self.access_token_secret="hSSAec1LcgoIRlUT0XRRunlrbsUCGUxFw9jXN0ozVWzBD"

    def getconsumer_key(self):
        return self.consumer_key

    def getconsumer_secret(self):
        return self.consumer_secret
    def getaccess_token(self):
        return self.access_token
    def getaccess_token_secret(self):
        return self.access_token_secret