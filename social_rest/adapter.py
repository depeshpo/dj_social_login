from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        # this is hack to get access token :p
        try:
            print(sociallogin.token.token)
        except:
            print("Access token not found")
